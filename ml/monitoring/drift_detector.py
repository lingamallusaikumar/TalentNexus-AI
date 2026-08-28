import numpy as np
import logging

logger = logging.getLogger(__name__)

class ModelDriftDetector:
    """
    Monitors candidate score distributions and calculates Population Stability Index (PSI)
    to detect dataset drift and model degradation over time.
    """

    @classmethod
    def calculate_psi(cls, expected_distribution: list[float], actual_distribution: list[float], num_buckets: int = 10) -> float:
        """
        Calculates Population Stability Index (PSI) between baseline scores and new inference scores.
        PSI < 0.1: No significant change.
        0.1 <= PSI < 0.2: Moderate drift.
        PSI >= 0.2: Significant drift detected, model retraining recommended.
        """
        if not expected_distribution or not actual_distribution:
            return 0.0
            
        expected = np.array(expected_distribution)
        actual = np.array(actual_distribution)
        
        # Define bin edges from 0 to 100
        bins = np.linspace(0, 100, num_buckets + 1)
        
        # Calculate frequencies
        expected_counts, _ = np.histogram(expected, bins=bins)
        actual_counts, _ = np.histogram(actual, bins=bins)
        
        # Convert to percentages with small epsilon to prevent div-by-zero
        eps = 1e-4
        expected_pct = (expected_counts / len(expected)) + eps
        actual_pct = (actual_counts / len(actual)) + eps
        
        # Normalize
        expected_pct /= np.sum(expected_pct)
        actual_pct /= np.sum(actual_pct)
        
        # Calculate PSI formula: sum((Actual% - Expected%) * ln(Actual% / Expected%))
        psi_value = np.sum((actual_pct - expected_pct) * np.log(actual_pct / expected_pct))
        
        return float(round(psi_value, 4))

    @classmethod
    def evaluate_drift_alert(cls, model_name: str, baseline_scores: list[float], recent_scores: list[float]) -> dict:
        psi = cls.calculate_psi(baseline_scores, recent_scores)
        
        if psi >= 0.2:
            alert_level = 'CRITICAL'
            action = 'Model retraining and prompt weight re-calibration required.'
        elif psi >= 0.1:
            alert_level = 'WARNING'
            action = 'Monitor incoming score distributions closely.'
        else:
            alert_level = 'HEALTHY'
            action = 'Model performance and distribution are stable.'
            
        return {
            "model_name": model_name,
            "psi_score": psi,
            "alert_level": alert_level,
            "recommended_action": action,
            "baseline_count": len(baseline_scores),
            "recent_inference_count": len(recent_scores)
        }
