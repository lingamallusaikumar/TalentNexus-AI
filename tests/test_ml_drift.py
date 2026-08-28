import pytest
from ml.monitoring.drift_detector import ModelDriftDetector

def test_model_drift_psi_calculation():
    # 1. Test identical distributions (PSI should be ~0)
    baseline = [85.0, 90.0, 75.0, 80.0, 65.0, 95.0, 70.0, 88.0] * 10
    recent = [85.0, 90.0, 75.0, 80.0, 65.0, 95.0, 70.0, 88.0] * 10
    
    psi = ModelDriftDetector.calculate_psi(baseline, recent)
    assert psi < 0.05

    # 2. Test significant drift (Shift in scores from high to low)
    drifted_recent = [30.0, 35.0, 40.0, 25.0, 45.0, 38.0, 42.0] * 10
    eval_result = ModelDriftDetector.evaluate_drift_alert("CandidateMatchScorer", baseline, drifted_recent)
    assert eval_result['alert_level'] in ['WARNING', 'CRITICAL']
    assert eval_result['psi_score'] > 0.1
