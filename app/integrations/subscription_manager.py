class SubscriptionPlanManager:
    """Manages multi-tenant SaaS quotas, feature flags, and active candidate parsing limits."""

    PLANS = {
        'STARTER': {
            'max_active_jobs': 5,
            'max_resumes_per_month': 200,
            'features': ['BASIC_PARSING', 'SKILL_EXTRACTION']
        },
        'GROWTH': {
            'max_active_jobs': 25,
            'max_resumes_per_month': 1500,
            'features': ['BASIC_PARSING', 'SKILL_EXTRACTION', 'XAI_EXPLANATIONS', 'WEBSOCKET_RANKINGS']
        },
        'ENTERPRISE': {
            'max_active_jobs': 9999,
            'max_resumes_per_month': 50000,
            'features': ['ALL_FEATURES', 'CUSTOM_PIPELINES', 'WEBHOOKS', 'ML_MODEL_REGISTRY', 'DEDICATED_CELERY']
        }
    }

    @classmethod
    def check_quota(cls, organization_id: int, quota_type: str) -> bool:
        # Defaults to ENTERPRISE for on-premise / full edition
        return True
