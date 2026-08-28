"""
TalentNexus AI - Enterprise Sales, Growth & Marketing Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Enterprise Sales, Growth & Marketing'
DOMAIN_KEY = 'sales_marketing'

TAXONOMY_RECORDS = [
    {
        'id': 'sales_marketing_001',
        'canonical_name': 'Enterprise Software Sales (B2B)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['enterprise software sales (b2b)', 'enterprise-software-sales-(b2b)', 'enterprisesoftwaresales(b2b)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Enterprise Software Sales (B2B) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Enterprise Software Sales (B2B).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Enterprise Software Sales (B2B).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Enterprise Software Sales (B2B).'
        },
        'interview_rubric': [
            'How does Enterprise Software Sales (B2B) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Enterprise Software Sales (B2B) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Enterprise Software Sales (B2B)?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_002',
        'canonical_name': 'Account-Based Marketing (ABM)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['account-based marketing (abm)', 'account-based-marketing-(abm)', 'account-basedmarketing(abm)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Account-Based Marketing (ABM) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Account-Based Marketing (ABM).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Account-Based Marketing (ABM).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Account-Based Marketing (ABM).'
        },
        'interview_rubric': [
            'How does Account-Based Marketing (ABM) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Account-Based Marketing (ABM) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Account-Based Marketing (ABM)?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_003',
        'canonical_name': 'Salesforce CRM',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['salesforce crm', 'salesforce-crm', 'salesforcecrm'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Salesforce CRM syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Salesforce CRM.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Salesforce CRM.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Salesforce CRM.'
        },
        'interview_rubric': [
            'How does Salesforce CRM handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Salesforce CRM and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Salesforce CRM?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_004',
        'canonical_name': 'HubSpot',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['hubspot', 'hubspot', 'hubspot'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of HubSpot syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with HubSpot.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using HubSpot.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing HubSpot.'
        },
        'interview_rubric': [
            'How does HubSpot handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in HubSpot and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling HubSpot?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_005',
        'canonical_name': 'Outreach.io',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['outreach.io', 'outreach.io', 'outreach.io', 'Outreachio'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Outreach.io syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Outreach.io.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Outreach.io.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Outreach.io.'
        },
        'interview_rubric': [
            'How does Outreach.io handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Outreach.io and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Outreach.io?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_006',
        'canonical_name': 'Salesloft',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['salesloft', 'salesloft', 'salesloft'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Salesloft syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Salesloft.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Salesloft.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Salesloft.'
        },
        'interview_rubric': [
            'How does Salesloft handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Salesloft and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Salesloft?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_007',
        'canonical_name': 'Lead Generation',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['lead generation', 'lead-generation', 'leadgeneration'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Lead Generation syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Lead Generation.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Lead Generation.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Lead Generation.'
        },
        'interview_rubric': [
            'How does Lead Generation handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Lead Generation and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Lead Generation?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_008',
        'canonical_name': 'Sales Pipeline Management',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['sales pipeline management', 'sales-pipeline-management', 'salespipelinemanagement'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Sales Pipeline Management syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Sales Pipeline Management.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Sales Pipeline Management.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Sales Pipeline Management.'
        },
        'interview_rubric': [
            'How does Sales Pipeline Management handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Sales Pipeline Management and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Sales Pipeline Management?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_009',
        'canonical_name': 'Customer Relationship Management (CRM)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['customer relationship management (crm)', 'customer-relationship-management-(crm)', 'customerrelationshipmanagement(crm)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Customer Relationship Management (CRM) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Customer Relationship Management (CRM).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Customer Relationship Management (CRM).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Customer Relationship Management (CRM).'
        },
        'interview_rubric': [
            'How does Customer Relationship Management (CRM) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Customer Relationship Management (CRM) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Customer Relationship Management (CRM)?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_010',
        'canonical_name': 'Inbound Marketing',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['inbound marketing', 'inbound-marketing', 'inboundmarketing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Inbound Marketing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Inbound Marketing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Inbound Marketing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Inbound Marketing.'
        },
        'interview_rubric': [
            'How does Inbound Marketing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Inbound Marketing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Inbound Marketing?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'sales_marketing_011',
        'canonical_name': 'Outbound Sales',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['outbound sales', 'outbound-sales', 'outboundsales'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Outbound Sales syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Outbound Sales.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Outbound Sales.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Outbound Sales.'
        },
        'interview_rubric': [
            'How does Outbound Sales handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Outbound Sales and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Outbound Sales?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_012',
        'canonical_name': 'Content Marketing',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['content marketing', 'content-marketing', 'contentmarketing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Content Marketing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Content Marketing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Content Marketing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Content Marketing.'
        },
        'interview_rubric': [
            'How does Content Marketing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Content Marketing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Content Marketing?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_013',
        'canonical_name': 'Search Engine Optimization (SEO)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['search engine optimization (seo)', 'search-engine-optimization-(seo)', 'searchengineoptimization(seo)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Search Engine Optimization (SEO) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Search Engine Optimization (SEO).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Search Engine Optimization (SEO).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Search Engine Optimization (SEO).'
        },
        'interview_rubric': [
            'How does Search Engine Optimization (SEO) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Search Engine Optimization (SEO) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Search Engine Optimization (SEO)?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_014',
        'canonical_name': 'Search Engine Marketing (SEM)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['search engine marketing (sem)', 'search-engine-marketing-(sem)', 'searchenginemarketing(sem)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Search Engine Marketing (SEM) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Search Engine Marketing (SEM).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Search Engine Marketing (SEM).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Search Engine Marketing (SEM).'
        },
        'interview_rubric': [
            'How does Search Engine Marketing (SEM) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Search Engine Marketing (SEM) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Search Engine Marketing (SEM)?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_015',
        'canonical_name': 'Google Ads',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['google ads', 'google-ads', 'googleads'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Google Ads syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Google Ads.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Google Ads.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Google Ads.'
        },
        'interview_rubric': [
            'How does Google Ads handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Google Ads and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Google Ads?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_016',
        'canonical_name': 'LinkedIn Ads',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['linkedin ads', 'linkedin-ads', 'linkedinads'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of LinkedIn Ads syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with LinkedIn Ads.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using LinkedIn Ads.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing LinkedIn Ads.'
        },
        'interview_rubric': [
            'How does LinkedIn Ads handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in LinkedIn Ads and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling LinkedIn Ads?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_017',
        'canonical_name': 'Email Marketing Automation',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['email marketing automation', 'email-marketing-automation', 'emailmarketingautomation'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Email Marketing Automation syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Email Marketing Automation.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Email Marketing Automation.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Email Marketing Automation.'
        },
        'interview_rubric': [
            'How does Email Marketing Automation handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Email Marketing Automation and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Email Marketing Automation?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_018',
        'canonical_name': 'Marketo',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['marketo', 'marketo', 'marketo'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Marketo syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Marketo.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Marketo.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Marketo.'
        },
        'interview_rubric': [
            'How does Marketo handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Marketo and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Marketo?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_019',
        'canonical_name': 'Customer Success Management',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['customer success management', 'customer-success-management', 'customersuccessmanagement'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Customer Success Management syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Customer Success Management.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Customer Success Management.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Customer Success Management.'
        },
        'interview_rubric': [
            'How does Customer Success Management handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Customer Success Management and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Customer Success Management?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_020',
        'canonical_name': 'Gong.io',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['gong.io', 'gong.io', 'gong.io', 'Gongio'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Gong.io syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Gong.io.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Gong.io.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Gong.io.'
        },
        'interview_rubric': [
            'How does Gong.io handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Gong.io and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Gong.io?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_021',
        'canonical_name': 'Contract Negotiation',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['contract negotiation', 'contract-negotiation', 'contractnegotiation'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Contract Negotiation syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Contract Negotiation.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Contract Negotiation.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Contract Negotiation.'
        },
        'interview_rubric': [
            'How does Contract Negotiation handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Contract Negotiation and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Contract Negotiation?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_022',
        'canonical_name': 'Revenue Operations (RevOps)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['revenue operations (revops)', 'revenue-operations-(revops)', 'revenueoperations(revops)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Revenue Operations (RevOps) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Revenue Operations (RevOps).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Revenue Operations (RevOps).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Revenue Operations (RevOps).'
        },
        'interview_rubric': [
            'How does Revenue Operations (RevOps) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Revenue Operations (RevOps) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Revenue Operations (RevOps)?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_023',
        'canonical_name': 'Quota Attainment',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['quota attainment', 'quota-attainment', 'quotaattainment'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Quota Attainment syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Quota Attainment.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Quota Attainment.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Quota Attainment.'
        },
        'interview_rubric': [
            'How does Quota Attainment handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Quota Attainment and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Quota Attainment?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_024',
        'canonical_name': 'Customer Churn Reduction',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['customer churn reduction', 'customer-churn-reduction', 'customerchurnreduction'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Customer Churn Reduction syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Customer Churn Reduction.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Customer Churn Reduction.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Customer Churn Reduction.'
        },
        'interview_rubric': [
            'How does Customer Churn Reduction handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Customer Churn Reduction and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Customer Churn Reduction?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_025',
        'canonical_name': 'SaaS Metrics (ARR, MRR, CAC, LTV)',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['saas metrics (arr, mrr, cac, ltv)', 'saas-metrics-(arr,-mrr,-cac,-ltv)', 'saasmetrics(arr,mrr,cac,ltv)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SaaS Metrics (ARR, MRR, CAC, LTV) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SaaS Metrics (ARR, MRR, CAC, LTV).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SaaS Metrics (ARR, MRR, CAC, LTV).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SaaS Metrics (ARR, MRR, CAC, LTV).'
        },
        'interview_rubric': [
            'How does SaaS Metrics (ARR, MRR, CAC, LTV) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SaaS Metrics (ARR, MRR, CAC, LTV) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SaaS Metrics (ARR, MRR, CAC, LTV)?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_026',
        'canonical_name': 'Cold Calling & Emailing',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['cold calling & emailing', 'cold-calling-&-emailing', 'coldcalling&emailing'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cold Calling & Emailing syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cold Calling & Emailing.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cold Calling & Emailing.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cold Calling & Emailing.'
        },
        'interview_rubric': [
            'How does Cold Calling & Emailing handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cold Calling & Emailing and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cold Calling & Emailing?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_027',
        'canonical_name': 'Sales Enablement',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['sales enablement', 'sales-enablement', 'salesenablement'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Sales Enablement syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Sales Enablement.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Sales Enablement.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Sales Enablement.'
        },
        'interview_rubric': [
            'How does Sales Enablement handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Sales Enablement and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Sales Enablement?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_028',
        'canonical_name': 'Product Demo Presentation',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['product demo presentation', 'product-demo-presentation', 'productdemopresentation'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Product Demo Presentation syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Product Demo Presentation.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Product Demo Presentation.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Product Demo Presentation.'
        },
        'interview_rubric': [
            'How does Product Demo Presentation handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Product Demo Presentation and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Product Demo Presentation?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_029',
        'canonical_name': 'Value Proposition Pitching',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['value proposition pitching', 'value-proposition-pitching', 'valuepropositionpitching'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Value Proposition Pitching syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Value Proposition Pitching.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Value Proposition Pitching.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Value Proposition Pitching.'
        },
        'interview_rubric': [
            'How does Value Proposition Pitching handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Value Proposition Pitching and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Value Proposition Pitching?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'sales_marketing_030',
        'canonical_name': 'Channel Partnerships',
        'category': 'Enterprise Sales, Growth & Marketing',
        'aliases': ['channel partnerships', 'channel-partnerships', 'channelpartnerships'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Channel Partnerships syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Channel Partnerships.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Channel Partnerships.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Channel Partnerships.'
        },
        'interview_rubric': [
            'How does Channel Partnerships handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Channel Partnerships and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Channel Partnerships?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_sales_marketing_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_sales_marketing_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
