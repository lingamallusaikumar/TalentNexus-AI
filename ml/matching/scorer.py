from ml.matching.embedder import SemanticEmbedder

class CandidateMatchingEngine:
    """Enterprise multi-factor candidate scoring and Explainable AI (XAI) engine."""

    @classmethod
    def calculate_match(cls, candidate, job, scoring_profile=None) -> dict:
        embedder = SemanticEmbedder.get_instance()
        
        # 1. Required Skills Match Score (0 - 100)
        reqs = job.requirements
        candidate_skill_map = {s.skill_name.lower(): s for s in candidate.skills}
        
        matched_required = []
        missing_required = []
        matched_preferred = []
        
        total_req_weight = 0.0
        earned_req_weight = 0.0
        
        if reqs:
            for r in reqs:
                w = r.weight or 1.0
                total_req_weight += w
                if r.skill_name.lower() in candidate_skill_map:
                    earned_req_weight += w
                    if r.is_required:
                        matched_required.append(r.skill_name)
                    else:
                        matched_preferred.append(r.skill_name)
                else:
                    if r.is_required:
                        missing_required.append(r.skill_name)
                        
            skills_score = (earned_req_weight / total_req_weight) * 100.0 if total_req_weight > 0 else 75.0
        else:
            skills_score = 75.0

        # 2. Semantic Embedding Similarity Score (0 - 100)
        semantic_score = 50.0
        resume_text = candidate.summary or ""
        if candidate.resumes and candidate.resumes[0].raw_text:
            resume_text = candidate.resumes[0].raw_text[:2000]
            
        if resume_text and job.description:
            sim = embedder.calculate_similarity(resume_text, job.description[:2000])
            sim = max(0.0, sim)
            semantic_score = sim * 100.0

        # 3. Experience Score (0 - 100)
        cand_exp = candidate.years_of_experience or 0.0
        # Calculate target job experience requirement
        target_exp = max([r.min_years_experience for r in reqs] + [3.0])
        exp_score = min(100.0, (cand_exp / target_exp) * 100.0) if target_exp > 0 else 80.0

        # 4. Project Score (0 - 100)
        project_count = len(candidate.projects)
        project_score = min(100.0, (project_count / 3.0) * 100.0) if project_count > 0 else 50.0

        # 5. Education Score (0 - 100)
        education_score = 60.0
        if candidate.educations:
            deg_lower = " ".join([e.degree.lower() for e in candidate.educations if e.degree])
            if 'phd' in deg_lower or 'doctor' in deg_lower:
                education_score = 100.0
            elif 'master' in deg_lower or 'mba' in deg_lower or 'ms' in deg_lower:
                education_score = 90.0
            elif 'bachelor' in deg_lower or 'bs' in deg_lower or 'b.tech' in deg_lower:
                education_score = 80.0
            else:
                education_score = 70.0

        # 6. Certifications Score (0 - 100)
        cert_count = len(candidate.certifications)
        cert_score = min(100.0, cert_count * 50.0)

        # 7. Location & Remote Compatibility Score (0 - 100)
        location_score = 100.0 if job.is_remote else (
            95.0 if candidate.location and job.location and candidate.location.lower() in job.location.lower() else 60.0
        )

        # 8. Preferences Score (0 - 100)
        preference_score = 85.0

        # Configurable Weights
        w_skills = scoring_profile.weight_required_skills if scoring_profile else 0.30
        w_sem = scoring_profile.weight_semantic_similarity if scoring_profile else 0.20
        w_exp = scoring_profile.weight_experience if scoring_profile else 0.15
        w_proj = scoring_profile.weight_projects if scoring_profile else 0.10
        w_edu = scoring_profile.weight_education if scoring_profile else 0.10
        w_cert = scoring_profile.weight_certifications if scoring_profile else 0.05
        w_loc = scoring_profile.weight_location if scoring_profile else 0.05
        w_pref = scoring_profile.weight_preferences if scoring_profile else 0.05

        overall_score = (
            (skills_score * w_skills) +
            (semantic_score * w_sem) +
            (exp_score * w_exp) +
            (project_score * w_proj) +
            (education_score * w_edu) +
            (cert_score * w_cert) +
            (location_score * w_loc) +
            (preference_score * w_pref)
        )
        overall_score = round(max(0.0, min(100.0, overall_score)), 1)

        # Recommendation
        if overall_score >= 80.0:
            recommendation = 'SHORTLIST'
        elif overall_score >= 60.0:
            recommendation = 'REVIEW'
        else:
            recommendation = 'REJECT'

        # Explainable AI report
        strengths = []
        weaknesses = []
        
        if len(matched_required) > 0:
            strengths.append(f"Matches {len(matched_required)} required skills: {', '.join(matched_required)}.")
        if semantic_score >= 70.0:
            strengths.append(f"Strong semantic domain match with job responsibilities ({round(semantic_score, 1)}%).")
        if cand_exp >= target_exp:
            strengths.append(f"Exceeds experience requirements ({cand_exp} yrs vs {target_exp} yrs required).")
            
        if len(missing_required) > 0:
            weaknesses.append(f"Missing mandatory skills: {', '.join(missing_required)}.")
        if cand_exp < target_exp:
            weaknesses.append(f"Years of experience ({cand_exp} yrs) is below required target ({target_exp} yrs).")

        explanation = {
            "overall_score": overall_score,
            "recommendation": recommendation,
            "sub_scores": {
                "skills_score": round(skills_score, 1),
                "semantic_similarity_score": round(semantic_score, 1),
                "experience_score": round(exp_score, 1),
                "projects_score": round(project_score, 1),
                "education_score": round(education_score, 1),
                "certifications_score": round(cert_score, 1),
                "location_score": round(location_score, 1),
                "preferences_score": round(preference_score, 1)
            },
            "strengths": strengths,
            "weaknesses": weaknesses,
            "matched_skills": matched_required + matched_preferred,
            "missing_skills": missing_required
        }

        return {
            "overall_score": overall_score,
            "recommendation": recommendation,
            "sub_scores": explanation["sub_scores"],
            "explanation": explanation
        }
