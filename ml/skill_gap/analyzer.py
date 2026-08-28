class SkillGapAnalyzer:
    """
    Compares candidate profile against target job requirements, highlighting missing skills,
    importance, and generating a recommended learning path.
    """

    @classmethod
    def analyze_skill_gap(cls, candidate, job) -> dict:
        reqs = job.requirements
        candidate_skills = {s.skill_name.lower(): s for s in candidate.skills}
        
        matched_skills = []
        missing_mandatory_skills = []
        missing_preferred_skills = []
        
        for r in reqs:
            if r.skill_name.lower() in candidate_skills:
                cand_skill = candidate_skills[r.skill_name.lower()]
                matched_skills.append({
                    "skill_name": r.skill_name,
                    "is_required": r.is_required,
                    "candidate_years": cand_skill.years_of_experience,
                    "required_years": r.min_years_experience
                })
            else:
                item = {
                    "skill_name": r.skill_name,
                    "weight": r.weight or 1.0,
                    "required_years": r.min_years_experience
                }
                if r.is_required:
                    missing_mandatory_skills.append(item)
                else:
                    missing_preferred_skills.append(item)
                    
        # Sort missing by weight
        missing_mandatory_skills.sort(key=lambda x: x['weight'], reverse=True)

        # Generate recommended learning path
        learning_path = []
        for s in missing_mandatory_skills:
            learning_path.append({
                "skill": s['skill_name'],
                "priority": "HIGH",
                "estimated_study_weeks": 2 if s['required_years'] <= 2 else 4,
                "recommended_action": f"Gain hands-on proficiency in {s['skill_name']} through practical project implementation."
            })
            
        for s in missing_preferred_skills:
            learning_path.append({
                "skill": s['skill_name'],
                "priority": "MEDIUM",
                "estimated_study_weeks": 1,
                "recommended_action": f"Familiarize with {s['skill_name']} core concepts."
            })

        return {
            "matched_skills": matched_skills,
            "missing_mandatory_skills": missing_mandatory_skills,
            "missing_preferred_skills": missing_preferred_skills,
            "gap_summary": {
                "matched_count": len(matched_skills),
                "missing_count": len(missing_mandatory_skills) + len(missing_preferred_skills),
                "readiness_percentage": round((len(matched_skills) / len(reqs)) * 100.0, 1) if reqs else 100.0
            },
            "learning_path": learning_path
        }
