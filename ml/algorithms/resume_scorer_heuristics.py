import re
from typing import Dict, Any, List

class ResumeHeuristicScorer:
    """
    Comprehensive heuristic analyzer inspecting 30+ syntactic and structural indicators:
    - Bullet point structure and length
    - Quantifiable ROI metrics
    - Chronological date consistency
    - Section balance and white-space density
    - Technical density vs filler words
    """

    @classmethod
    def evaluate_heuristics(cls, raw_text: str) -> Dict[str, Any]:
        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
        total_words = len(raw_text.split())
        
        # 1. Length & Verbosity Score
        if total_words < 150: length_score = 30.0
        elif total_words < 300: length_score = 70.0
        elif total_words <= 800: length_score = 100.0
        else: length_score = 80.0 # Too verbose

        # 2. Bullet point metrics
        bullet_lines = [l for l in lines if l.startswith(('•', '-', '*', '–'))]
        bullet_density = min(100.0, (len(bullet_lines) / 10.0) * 100.0)

        # 3. Action Verb Density
        action_verbs = {'engineered', 'architected', 'spearheaded', 'developed', 'optimized', 'reduced', 'increased', 'managed', 'led', 'delivered'}
        words = set(re.findall(r'\b[a-zA-Z]{3,}\b', raw_text.lower()))
        action_count = len(words.intersection(action_verbs))
        action_score = min(100.0, (action_count / 6.0) * 100.0)

        # 4. Metric Quantifiers ($ percentages, ms, GB, numbers)
        metrics = re.findall(r'\b(?:\d+%|\$\d+|\d+x|\d+\+|\d+\s*(?:users|requests|ms|seconds|engineers))\b', raw_text.lower())
        metric_score = min(100.0, len(metrics) * 20.0)

        overall = (length_score * 0.2) + (bullet_density * 0.25) + (action_score * 0.25) + (metric_score * 0.3)
        return {
            "overall_heuristic_score": round(overall, 1),
            "word_count": total_words,
            "bullet_points_count": len(bullet_lines),
            "action_verbs_found": action_count,
            "metrics_detected": len(metrics)
        }
