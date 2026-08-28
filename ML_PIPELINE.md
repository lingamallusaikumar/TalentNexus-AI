# TalentNexus AI — Machine Learning Pipeline

## 1. Pipeline Architecture

```
[Resume Upload (PDF/DOCX/TXT/Scanned)]
                │
                ▼
     [OCR & Text Extraction]
                │
                ▼
    [Section Header Detection]
 (Summary, Skills, Exp, Edu, Proj)
                │
                ▼
   [Skill Normalization Engine]
    (Alias Mapping & Taxonomy)
                │
                ▼
   [Resume Quality Analyzer]
  (Completeness, Metrics, Verbs)
                │
                ▼
  [Sentence Transformer Embedder]
   ('all-MiniLM-L6-v2' Dense Vectors)
                │
                ▼
   [Multi-Factor Matching Engine]
(Skills 30%, Semantic 20%, Exp 15%...)
                │
                ▼
   [Explainable AI (XAI) Output]
(Strengths, Weaknesses, Recommendation)
```

## 2. Quality Analysis Metrics
The `ResumeQualityAnalyzer` computes five distinct vectors:
- **Completeness (25%)**: Valid email, phone, professional links, executive summary.
- **Section Structure (20%)**: Distinct presence of Skills, Experience, Education.
- **Impact & Action Verbs (20%)**: Density of achievement verbs (*Engineered, Scaled, Architected*).
- **Quantifiable Metrics (15%)**: Statistical indicators (*% growth, $ savings, ms latency*).
- **Skill Clarity (20%)**: Detection of standard modern technologies.

## 3. Explainable AI (XAI) Engine
Every score generates a machine-readable JSON structure explaining the exact mathematical derivation of the final recommendation:
- Specific mandatory skills missing vs matched.
- Semantic domain correlation percentage.
- Experience deficiency or surplus metrics.
- Recruiter override logging for model auditing.
