def analyze_resume_quality(resume_text):
    """
    Analyze the overall quality and completeness
    of the resume.
    """

    text_lower = resume_text.lower()

    checks = {
        "Contact Information": any(
            keyword in text_lower
            for keyword in ["email", "phone", "linkedin", "github"]
        ),

        "Education": any(
            keyword in text_lower
            for keyword in [
                "education",
                "b.tech",
                "bachelor",
                "degree",
                "university",
                "college"
            ]
        ),

        "Skills": any(
            keyword in text_lower
            for keyword in [
                "skills",
                "technical skills",
                "programming"
            ]
        ),

        "Projects": any(
            keyword in text_lower
            for keyword in [
                "projects",
                "project experience"
            ]
        ),

        "Experience": any(
            keyword in text_lower
            for keyword in [
                "experience",
                "internship",
                "intern"
            ]
        ),

        "Certifications": any(
            keyword in text_lower
            for keyword in [
                "certification",
                "certifications",
                "certificate"
            ]
        )
    }

    completed = sum(checks.values())
    total = len(checks)

    score = round(
        (completed / total) * 100,
        2
    )

    return score, checks