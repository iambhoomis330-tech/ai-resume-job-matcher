def find_missing_skills(resume_skills, job_skills):
    """Find skills required by the job but missing from the resume."""

    resume_set = {skill.lower() for skill in resume_skills}
    missing = []

    for skill in job_skills:
        if skill.lower() not in resume_set:
            missing.append(skill)

    return sorted(missing)


def find_matching_skills(resume_skills, job_skills):
    """Find skills present in both resume and job description."""

    resume_set = {skill.lower() for skill in resume_skills}

    matching = []

    for skill in job_skills:
        if skill.lower() in resume_set:
            matching.append(skill)

    return sorted(matching)


def generate_recommendations(missing_skills):
    """Generate resume improvement recommendations."""

    recommendations = []

    if missing_skills:
        recommendations.append(
            "Consider adding relevant missing skills to your resume "
            "if you genuinely have experience with them."
        )

        for skill in missing_skills[:5]:
            recommendations.append(
                f"Highlight projects or experience related to {skill}."
            )
    else:
        recommendations.append(
            "Your resume contains the main skills identified in the job description."
        )

    return recommendations

if __name__ == "__main__":
    resume_skills = [
        "Python",
        "Pandas",
        "NumPy",
        "SQL"
    ]

    job_skills = [
        "Python",
        "Pandas",
        "NumPy",
        "SQL",
        "Machine Learning",
        "Power BI"
    ]

    matching = find_matching_skills(
        resume_skills,
        job_skills
    )

    missing = find_missing_skills(
        resume_skills,
        job_skills
    )

    recommendations = generate_recommendations(
        missing
    )

    print("Matching Skills:")
    print(matching)

    print("\nMissing Skills:")
    print(missing)

    print("\nRecommendations:")

    for recommendation in recommendations:
        print("-", recommendation)