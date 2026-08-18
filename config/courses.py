"""
Course Recommendations Configuration
=====================================
Contains curated course data, video resources, and helper functions
for role-specific learning recommendations.
"""

# Courses organized by category
COURSES_BY_CATEGORY = {
    "Data Science": [
        {"name": "IBM Data Science Professional Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/ibm-data-science"},
        {"name": "Data Science Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/jhu-data-science"},
        {"name": "Python for Data Science and AI", "platform": "Coursera", "url": "https://www.coursera.org/learn/python-for-applied-data-science-ai"},
        {"name": "Machine Learning by Andrew Ng", "platform": "Coursera", "url": "https://www.coursera.org/learn/machine-learning"},
        {"name": "Data Analysis with Python", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/"},
    ],
    "Web Development": [
        {"name": "The Web Developer Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-web-developer-bootcamp/"},
        {"name": "Full Stack Open", "platform": "University of Helsinki", "url": "https://fullstackopen.com/en/"},
        {"name": "Meta Front-End Developer", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer"},
        {"name": "React - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"},
        {"name": "CS50's Web Programming", "platform": "Harvard/edX", "url": "https://cs50.harvard.edu/web/"},
    ],
    "Android Development": [
        {"name": "Android Basics with Compose", "platform": "Google", "url": "https://developer.android.com/courses/android-basics-compose/course"},
        {"name": "Kotlin for Android Developers", "platform": "Udacity", "url": "https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012"},
        {"name": "The Complete Android Developer Course", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-android-n-developer-course/"},
    ],
    "iOS Development": [
        {"name": "iOS & Swift - The Complete iOS App Development", "platform": "Udemy", "url": "https://www.udemy.com/course/ios-13-app-development-bootcamp/"},
        {"name": "Developing iOS Apps with SwiftUI", "platform": "Stanford", "url": "https://cs193p.sites.stanford.edu/"},
        {"name": "Meta iOS Developer", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/meta-ios-developer"},
    ],
    "Machine Learning": [
        {"name": "Machine Learning Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/machine-learning-introduction"},
        {"name": "Deep Learning Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/deep-learning"},
        {"name": "Fast.ai Practical Deep Learning", "platform": "fast.ai", "url": "https://course.fast.ai/"},
        {"name": "TensorFlow Developer Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice"},
    ],
    "Cyber Security": [
        {"name": "Google Cybersecurity Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-cybersecurity"},
        {"name": "CompTIA Security+", "platform": "CompTIA", "url": "https://www.comptia.org/certifications/security"},
        {"name": "Introduction to Cyber Security", "platform": "Coursera", "url": "https://www.coursera.org/specializations/intro-cyber-security"},
    ],
    "Cloud Computing": [
        {"name": "AWS Cloud Practitioner Essentials", "platform": "AWS", "url": "https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/"},
        {"name": "Google Cloud Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/gcp-fundamentals"},
        {"name": "Azure Fundamentals", "platform": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/training/paths/az-900-describe-cloud-concepts/"},
    ],
    "DevOps": [
        {"name": "DevOps Engineering on AWS", "platform": "Coursera", "url": "https://www.coursera.org/specializations/aws-devops"},
        {"name": "Docker & Kubernetes: The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/"},
        {"name": "CI/CD with Jenkins", "platform": "Udemy", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero/"},
    ],
    "UI/UX Design": [
        {"name": "Google UX Design Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
        {"name": "UI/UX Design Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/ui-ux-design"},
        {"name": "Figma UI UX Design Essentials", "platform": "Udemy", "url": "https://www.udemy.com/course/figma-ux-ui-design-user-experience-tutorial-course/"},
    ],
    "Project Management": [
        {"name": "Google Project Management Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-project-management"},
        {"name": "PMP Certification Training", "platform": "Udemy", "url": "https://www.udemy.com/course/pmp-certification-exam-prep-course-pmbok-6th-edition/"},
    ],
    "Digital Marketing": [
        {"name": "Google Digital Marketing Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce"},
        {"name": "Meta Social Media Marketing", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/facebook-social-media-marketing"},
        {"name": "SEO Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/seo"},
    ],
    "General": [
        {"name": "CS50: Introduction to Computer Science", "platform": "Harvard/edX", "url": "https://cs50.harvard.edu/x/"},
        {"name": "Python for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python"},
        {"name": "Git & GitHub Crash Course", "platform": "Udemy", "url": "https://www.udemy.com/course/git-and-github-crash-course/"},
    ],
}

# Resume improvement videos
RESUME_VIDEOS = [
    {"title": "How to Write a Professional Resume", "url": "https://www.youtube.com/watch?v=Tt08KmFfIYQ"},
    {"title": "Resume Tips That Got Me Interviews at Google", "url": "https://www.youtube.com/watch?v=BYUy1yvjHxE"},
    {"title": "ATS Resume Tips - Beat the Bots", "url": "https://www.youtube.com/watch?v=J-4Fv8nq1iA"},
    {"title": "Common Resume Mistakes to Avoid", "url": "https://www.youtube.com/watch?v=dQ7Q8ZdnuN0"},
    {"title": "How to Write a Strong Resume Summary", "url": "https://www.youtube.com/watch?v=KFaugkGVeNQ"},
    {"title": "Resume Format Guide 2024", "url": "https://www.youtube.com/watch?v=y8YH0Qbu5h4"},
]

# Interview preparation videos
INTERVIEW_VIDEOS = [
    {"title": "How to Ace a Job Interview", "url": "https://www.youtube.com/watch?v=HG68Ymazo18"},
    {"title": "Top Interview Tips: Common Questions", "url": "https://www.youtube.com/watch?v=1mHjMNZZvFo"},
    {"title": "STAR Method for Behavioral Questions", "url": "https://www.youtube.com/watch?v=WSbN-0swDgM"},
    {"title": "Technical Interview Preparation", "url": "https://www.youtube.com/watch?v=09_LlHjoEiY"},
    {"title": "Body Language Tips for Interviews", "url": "https://www.youtube.com/watch?v=PCWVi5pAa30"},
    {"title": "Salary Negotiation Tactics", "url": "https://www.youtube.com/watch?v=u9BoG1n1948"},
]

# Mapping of job roles to course categories
ROLE_TO_CATEGORY = {
    # Tech roles
    "Software Developer": "Web Development",
    "Software Engineer": "Web Development",
    "Full Stack Developer": "Web Development",
    "Frontend Developer": "Web Development",
    "Backend Developer": "Web Development",
    "Web Developer": "Web Development",
    "Data Scientist": "Data Science",
    "Data Analyst": "Data Science",
    "Data Engineer": "Data Science",
    "Machine Learning Engineer": "Machine Learning",
    "AI Engineer": "Machine Learning",
    "Deep Learning Engineer": "Machine Learning",
    "NLP Engineer": "Machine Learning",
    "Android Developer": "Android Development",
    "iOS Developer": "iOS Development",
    "Mobile Developer": "Android Development",
    "DevOps Engineer": "DevOps",
    "Cloud Engineer": "Cloud Computing",
    "Cloud Architect": "Cloud Computing",
    "Cyber Security Analyst": "Cyber Security",
    "Security Engineer": "Cyber Security",
    "Penetration Tester": "Cyber Security",
    "UI/UX Designer": "UI/UX Design",
    "Product Designer": "UI/UX Design",
    "QA Engineer": "General",
    "Database Administrator": "General",
    "System Administrator": "DevOps",
    # Non-tech roles
    "Project Manager": "Project Management",
    "Product Manager": "Project Management",
    "Scrum Master": "Project Management",
    "Digital Marketer": "Digital Marketing",
    "SEO Specialist": "Digital Marketing",
    "Content Writer": "Digital Marketing",
    "Business Analyst": "Data Science",
    "HR Manager": "General",
    "Sales Manager": "General",
    "Financial Analyst": "Data Science",
}


def get_category_for_role(role):
    """
    Get the course category for a specific job role.
    
    Parameters
    ----------
    role : str
        The job role/title
        
    Returns
    -------
    str : Course category name
    """
    # Direct lookup
    if role in ROLE_TO_CATEGORY:
        return ROLE_TO_CATEGORY[role]
    
    # Fuzzy match: check if role contains any keyword
    role_lower = role.lower()
    keyword_map = {
        "data": "Data Science",
        "machine learning": "Machine Learning",
        "ml": "Machine Learning",
        "ai": "Machine Learning",
        "web": "Web Development",
        "frontend": "Web Development",
        "front-end": "Web Development",
        "backend": "Web Development",
        "back-end": "Web Development",
        "full stack": "Web Development",
        "fullstack": "Web Development",
        "android": "Android Development",
        "ios": "iOS Development",
        "swift": "iOS Development",
        "devops": "DevOps",
        "cloud": "Cloud Computing",
        "aws": "Cloud Computing",
        "azure": "Cloud Computing",
        "security": "Cyber Security",
        "cyber": "Cyber Security",
        "design": "UI/UX Design",
        "ux": "UI/UX Design",
        "ui": "UI/UX Design",
        "project": "Project Management",
        "product": "Project Management",
        "marketing": "Digital Marketing",
        "seo": "Digital Marketing",
    }
    
    for keyword, category in keyword_map.items():
        if keyword in role_lower:
            return category
    
    return "General"


def get_courses_for_role(role):
    """
    Get recommended courses for a specific job role.
    
    Parameters
    ----------
    role : str
        The job role/title
        
    Returns
    -------
    list : List of course dictionaries
    """
    category = get_category_for_role(role)
    return COURSES_BY_CATEGORY.get(category, COURSES_BY_CATEGORY["General"])
