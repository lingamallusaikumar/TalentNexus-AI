from marshmallow import Schema, fields

class RecruitmentFunnelSchema(Schema):
    active_jobs = fields.Integer()
    total_applications = fields.Integer()
    funnel_by_stage = fields.Dict()
    upcoming_interviews = fields.Integer()
    shortlist_rate_percentage = fields.Float()

class RecruiterPerformanceSchema(Schema):
    recruiter_id = fields.Integer()
    recruiter_name = fields.String()
    screened_count = fields.Integer()
    interviews_scheduled = fields.Integer()
    offers_extended = fields.Integer()
    hires_completed = fields.Integer()
    avg_time_to_screen_hours = fields.Float()

class SkillDemandAnalyticsSchema(Schema):
    skill_name = fields.String()
    category = fields.String()
    job_count = fields.Integer()
    candidate_supply_count = fields.Integer()
    demand_supply_ratio = fields.Float()
