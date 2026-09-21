import pandas as pd


def load_job_roles():
    """Load predefined job roles and their required skills."""

    return pd.read_csv("data/job_roles.csv")


def recommend_roles(resume_skills, top_n=3):
    """
    Recommend job roles based on the percentage
    of required skills found in the resume.
    """

    roles_df = load_job_roles()

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    results = []

    for _, row in roles_df.iterrows():

        required_skills = [
            skill.strip()
            for skill in row["skills"].split(",")
        ]

        matching_skills = [
            skill
            for skill in required_skills
            if skill.lower() in resume_set
        ]

        if required_skills:
            score = (
                len(matching_skills)
                / len(required_skills)
            ) * 100
        else:
            score = 0

        results.append({
            "role": row["role"],
            "score": round(score, 2),
            "matching_skills": matching_skills
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_n]