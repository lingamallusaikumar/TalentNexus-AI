"""
TalentNexus AI - Frontend Web & Mobile Comprehensive Domain Taxonomy
Defines skills, seniority criteria, interview evaluation rubrics, and relational weights.
"""

DOMAIN_NAME = 'Frontend Web & Mobile'
DOMAIN_KEY = 'frontend'

TAXONOMY_RECORDS = [
    {
        'id': 'frontend_001',
        'canonical_name': 'JavaScript',
        'category': 'Frontend Web & Mobile',
        'aliases': ['javascript', 'javascript', 'javascript'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of JavaScript syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with JavaScript.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using JavaScript.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing JavaScript.'
        },
        'interview_rubric': [
            'How does JavaScript handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in JavaScript and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling JavaScript?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_002',
        'canonical_name': 'TypeScript',
        'category': 'Frontend Web & Mobile',
        'aliases': ['typescript', 'typescript', 'typescript'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of TypeScript syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with TypeScript.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using TypeScript.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing TypeScript.'
        },
        'interview_rubric': [
            'How does TypeScript handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in TypeScript and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling TypeScript?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_003',
        'canonical_name': 'React',
        'category': 'Frontend Web & Mobile',
        'aliases': ['react', 'react', 'react'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of React syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with React.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using React.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing React.'
        },
        'interview_rubric': [
            'How does React handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in React and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling React?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_004',
        'canonical_name': 'Next.js',
        'category': 'Frontend Web & Mobile',
        'aliases': ['next.js', 'next.js', 'next.js', 'Nextjs'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Next.js syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Next.js.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Next.js.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Next.js.'
        },
        'interview_rubric': [
            'How does Next.js handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Next.js and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Next.js?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_005',
        'canonical_name': 'Vue.js',
        'category': 'Frontend Web & Mobile',
        'aliases': ['vue.js', 'vue.js', 'vue.js', 'Vuejs'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Vue.js syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Vue.js.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Vue.js.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Vue.js.'
        },
        'interview_rubric': [
            'How does Vue.js handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Vue.js and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Vue.js?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_006',
        'canonical_name': 'Nuxt.js',
        'category': 'Frontend Web & Mobile',
        'aliases': ['nuxt.js', 'nuxt.js', 'nuxt.js', 'Nuxtjs'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Nuxt.js syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Nuxt.js.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Nuxt.js.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Nuxt.js.'
        },
        'interview_rubric': [
            'How does Nuxt.js handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Nuxt.js and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Nuxt.js?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_007',
        'canonical_name': 'Angular',
        'category': 'Frontend Web & Mobile',
        'aliases': ['angular', 'angular', 'angular'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Angular syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Angular.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Angular.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Angular.'
        },
        'interview_rubric': [
            'How does Angular handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Angular and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Angular?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_008',
        'canonical_name': 'Svelte',
        'category': 'Frontend Web & Mobile',
        'aliases': ['svelte', 'svelte', 'svelte'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Svelte syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Svelte.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Svelte.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Svelte.'
        },
        'interview_rubric': [
            'How does Svelte handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Svelte and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Svelte?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_009',
        'canonical_name': 'HTML5',
        'category': 'Frontend Web & Mobile',
        'aliases': ['html5', 'html5', 'html5'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of HTML5 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with HTML5.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using HTML5.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing HTML5.'
        },
        'interview_rubric': [
            'How does HTML5 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in HTML5 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling HTML5?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_010',
        'canonical_name': 'CSS3',
        'category': 'Frontend Web & Mobile',
        'aliases': ['css3', 'css3', 'css3'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of CSS3 syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with CSS3.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using CSS3.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing CSS3.'
        },
        'interview_rubric': [
            'How does CSS3 handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in CSS3 and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling CSS3?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': True
    },
    {
        'id': 'frontend_011',
        'canonical_name': 'Sass/SCSS',
        'category': 'Frontend Web & Mobile',
        'aliases': ['sass/scss', 'sass/scss', 'sass/scss'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Sass/SCSS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Sass/SCSS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Sass/SCSS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Sass/SCSS.'
        },
        'interview_rubric': [
            'How does Sass/SCSS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Sass/SCSS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Sass/SCSS?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_012',
        'canonical_name': 'Tailwind CSS',
        'category': 'Frontend Web & Mobile',
        'aliases': ['tailwind css', 'tailwind-css', 'tailwindcss'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Tailwind CSS syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Tailwind CSS.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Tailwind CSS.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Tailwind CSS.'
        },
        'interview_rubric': [
            'How does Tailwind CSS handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Tailwind CSS and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Tailwind CSS?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_013',
        'canonical_name': 'Bootstrap',
        'category': 'Frontend Web & Mobile',
        'aliases': ['bootstrap', 'bootstrap', 'bootstrap'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Bootstrap syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Bootstrap.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Bootstrap.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Bootstrap.'
        },
        'interview_rubric': [
            'How does Bootstrap handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Bootstrap and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Bootstrap?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_014',
        'canonical_name': 'Redux',
        'category': 'Frontend Web & Mobile',
        'aliases': ['redux', 'redux', 'redux'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Redux syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Redux.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Redux.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Redux.'
        },
        'interview_rubric': [
            'How does Redux handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Redux and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Redux?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_015',
        'canonical_name': 'Zustand',
        'category': 'Frontend Web & Mobile',
        'aliases': ['zustand', 'zustand', 'zustand'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Zustand syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Zustand.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Zustand.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Zustand.'
        },
        'interview_rubric': [
            'How does Zustand handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Zustand and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Zustand?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_016',
        'canonical_name': 'Vuex',
        'category': 'Frontend Web & Mobile',
        'aliases': ['vuex', 'vuex', 'vuex'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Vuex syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Vuex.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Vuex.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Vuex.'
        },
        'interview_rubric': [
            'How does Vuex handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Vuex and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Vuex?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_017',
        'canonical_name': 'React Native',
        'category': 'Frontend Web & Mobile',
        'aliases': ['react native', 'react-native', 'reactnative'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of React Native syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with React Native.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using React Native.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing React Native.'
        },
        'interview_rubric': [
            'How does React Native handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in React Native and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling React Native?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_018',
        'canonical_name': 'Flutter',
        'category': 'Frontend Web & Mobile',
        'aliases': ['flutter', 'flutter', 'flutter'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Flutter syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Flutter.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Flutter.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Flutter.'
        },
        'interview_rubric': [
            'How does Flutter handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Flutter and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Flutter?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_019',
        'canonical_name': 'iOS Development',
        'category': 'Frontend Web & Mobile',
        'aliases': ['ios development', 'ios-development', 'iosdevelopment'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of iOS Development syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with iOS Development.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using iOS Development.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing iOS Development.'
        },
        'interview_rubric': [
            'How does iOS Development handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in iOS Development and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling iOS Development?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_020',
        'canonical_name': 'Swift',
        'category': 'Frontend Web & Mobile',
        'aliases': ['swift', 'swift', 'swift'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Swift syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Swift.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Swift.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Swift.'
        },
        'interview_rubric': [
            'How does Swift handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Swift and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Swift?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_021',
        'canonical_name': 'SwiftUI',
        'category': 'Frontend Web & Mobile',
        'aliases': ['swiftui', 'swiftui', 'swiftui'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SwiftUI syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SwiftUI.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SwiftUI.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SwiftUI.'
        },
        'interview_rubric': [
            'How does SwiftUI handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SwiftUI and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SwiftUI?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_022',
        'canonical_name': 'Android Development',
        'category': 'Frontend Web & Mobile',
        'aliases': ['android development', 'android-development', 'androiddevelopment'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Android Development syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Android Development.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Android Development.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Android Development.'
        },
        'interview_rubric': [
            'How does Android Development handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Android Development and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Android Development?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_023',
        'canonical_name': 'Kotlin',
        'category': 'Frontend Web & Mobile',
        'aliases': ['kotlin', 'kotlin', 'kotlin'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Kotlin syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Kotlin.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Kotlin.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Kotlin.'
        },
        'interview_rubric': [
            'How does Kotlin handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Kotlin and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Kotlin?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_024',
        'canonical_name': 'Jetpack Compose',
        'category': 'Frontend Web & Mobile',
        'aliases': ['jetpack compose', 'jetpack-compose', 'jetpackcompose'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Jetpack Compose syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Jetpack Compose.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Jetpack Compose.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Jetpack Compose.'
        },
        'interview_rubric': [
            'How does Jetpack Compose handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Jetpack Compose and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Jetpack Compose?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_025',
        'canonical_name': 'Webpack',
        'category': 'Frontend Web & Mobile',
        'aliases': ['webpack', 'webpack', 'webpack'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Webpack syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Webpack.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Webpack.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Webpack.'
        },
        'interview_rubric': [
            'How does Webpack handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Webpack and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Webpack?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_026',
        'canonical_name': 'Vite',
        'category': 'Frontend Web & Mobile',
        'aliases': ['vite', 'vite', 'vite'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Vite syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Vite.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Vite.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Vite.'
        },
        'interview_rubric': [
            'How does Vite handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Vite and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Vite?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_027',
        'canonical_name': 'ESBuild',
        'category': 'Frontend Web & Mobile',
        'aliases': ['esbuild', 'esbuild', 'esbuild'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of ESBuild syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with ESBuild.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using ESBuild.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing ESBuild.'
        },
        'interview_rubric': [
            'How does ESBuild handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in ESBuild and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling ESBuild?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_028',
        'canonical_name': 'Jest',
        'category': 'Frontend Web & Mobile',
        'aliases': ['jest', 'jest', 'jest'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Jest syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Jest.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Jest.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Jest.'
        },
        'interview_rubric': [
            'How does Jest handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Jest and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Jest?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_029',
        'canonical_name': 'Cypress',
        'category': 'Frontend Web & Mobile',
        'aliases': ['cypress', 'cypress', 'cypress'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Cypress syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Cypress.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Cypress.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Cypress.'
        },
        'interview_rubric': [
            'How does Cypress handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Cypress and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Cypress?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_030',
        'canonical_name': 'Playwright',
        'category': 'Frontend Web & Mobile',
        'aliases': ['playwright', 'playwright', 'playwright'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Playwright syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Playwright.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Playwright.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Playwright.'
        },
        'interview_rubric': [
            'How does Playwright handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Playwright and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Playwright?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_031',
        'canonical_name': 'WebAssembly',
        'category': 'Frontend Web & Mobile',
        'aliases': ['webassembly', 'webassembly', 'webassembly'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of WebAssembly syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with WebAssembly.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using WebAssembly.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing WebAssembly.'
        },
        'interview_rubric': [
            'How does WebAssembly handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in WebAssembly and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling WebAssembly?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_032',
        'canonical_name': 'PWA',
        'category': 'Frontend Web & Mobile',
        'aliases': ['pwa', 'pwa', 'pwa'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of PWA syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with PWA.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using PWA.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing PWA.'
        },
        'interview_rubric': [
            'How does PWA handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in PWA and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling PWA?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_033',
        'canonical_name': 'UI/UX Design',
        'category': 'Frontend Web & Mobile',
        'aliases': ['ui/ux design', 'ui/ux-design', 'ui/uxdesign'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of UI/UX Design syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with UI/UX Design.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using UI/UX Design.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing UI/UX Design.'
        },
        'interview_rubric': [
            'How does UI/UX Design handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in UI/UX Design and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling UI/UX Design?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_034',
        'canonical_name': 'Figma',
        'category': 'Frontend Web & Mobile',
        'aliases': ['figma', 'figma', 'figma'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Figma syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Figma.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Figma.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Figma.'
        },
        'interview_rubric': [
            'How does Figma handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Figma and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Figma?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_035',
        'canonical_name': 'Storybook',
        'category': 'Frontend Web & Mobile',
        'aliases': ['storybook', 'storybook', 'storybook'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Storybook syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Storybook.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Storybook.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Storybook.'
        },
        'interview_rubric': [
            'How does Storybook handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Storybook and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Storybook?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_036',
        'canonical_name': 'Accessibility (a11y)',
        'category': 'Frontend Web & Mobile',
        'aliases': ['accessibility (a11y)', 'accessibility-(a11y)', 'accessibility(a11y)'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Accessibility (a11y) syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Accessibility (a11y).',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Accessibility (a11y).',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Accessibility (a11y).'
        },
        'interview_rubric': [
            'How does Accessibility (a11y) handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Accessibility (a11y) and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Accessibility (a11y)?'
        ],
        'market_importance_weight': 1.2,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_037',
        'canonical_name': 'SEO Optimization',
        'category': 'Frontend Web & Mobile',
        'aliases': ['seo optimization', 'seo-optimization', 'seooptimization'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of SEO Optimization syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with SEO Optimization.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using SEO Optimization.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing SEO Optimization.'
        },
        'interview_rubric': [
            'How does SEO Optimization handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in SEO Optimization and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling SEO Optimization?'
        ],
        'market_importance_weight': 1.3,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_038',
        'canonical_name': 'Responsive Design',
        'category': 'Frontend Web & Mobile',
        'aliases': ['responsive design', 'responsive-design', 'responsivedesign'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Responsive Design syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Responsive Design.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Responsive Design.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Responsive Design.'
        },
        'interview_rubric': [
            'How does Responsive Design handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Responsive Design and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Responsive Design?'
        ],
        'market_importance_weight': 1.4,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_039',
        'canonical_name': 'WebGL',
        'category': 'Frontend Web & Mobile',
        'aliases': ['webgl', 'webgl', 'webgl'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of WebGL syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with WebGL.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using WebGL.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing WebGL.'
        },
        'interview_rubric': [
            'How does WebGL handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in WebGL and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling WebGL?'
        ],
        'market_importance_weight': 1.5,
        'is_critical_skill': False
    },
    {
        'id': 'frontend_040',
        'canonical_name': 'Three.js',
        'category': 'Frontend Web & Mobile',
        'aliases': ['three.js', 'three.js', 'three.js', 'Threejs'],
        'seniority_benchmarks': {
            'junior': 'Demonstrates fundamental understanding of Three.js syntax and standard libraries.',
            'mid_level': 'Builds production features, troubleshoots performance issues, and implements best practices with Three.js.',
            'senior': 'Architects high-availability systems, mentors team members, and drives architectural standards using Three.js.',
            'lead_staff': 'Defines company-wide technical direction, evaluates core tradeoffs, and scales distributed deployments utilizing Three.js.'
        },
        'interview_rubric': [
            'How does Three.js handle memory management and concurrency under load?',
            'Describe a challenging production bug you debugged in Three.js and how you resolved it.',
            'What are the core design patterns and architectural anti-patterns when scaling Three.js?'
        ],
        'market_importance_weight': 1.1,
        'is_critical_skill': False
    },
]


def get_frontend_skill_map() -> dict:
    return {item['canonical_name']: item for item in TAXONOMY_RECORDS}

def get_frontend_aliases_lookup() -> dict:
    lookup = {}
    for item in TAXONOMY_RECORDS:
        for alias in item['aliases']:
            lookup[alias.lower()] = item['canonical_name']
    return lookup
