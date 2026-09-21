import streamlit as st
import pandas as pd

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from resume_analyzer import analyze_resume_quality
from role_recommender import recommend_roles
from job_matcher import (
    calculate_match_score,
    calculate_skill_match,
    get_match_level
)
from recommender import (
    find_matching_skills,
    find_missing_skills,
    generate_recommendations
)


st.set_page_config(
    page_title="AI Resume Analyzer & Job Matcher",
    page_icon="📄",
    layout="wide"
)


st.title("🤖 AI Resume Analyzer & Job Matcher")

st.caption(
    "Analyze your resume, match it with job descriptions, "
    "identify skill gaps, and discover suitable career roles."
)

st.write(
    "Upload your resume and enter a job description to analyze "
    "your skills and calculate your job match."
)

# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

st.subheader("📄 Upload Your Resume")

uploaded_resume = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)


# --------------------------------------------------
# Job Description
# --------------------------------------------------

st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=250,
    placeholder="Paste the complete job description..."
)


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------
if st.button("🔄 Reset"):
    st.rerun()

if st.button("🚀 Analyze Resume", type="primary"):

    if uploaded_resume is None:
        st.warning("Please upload a resume.")

    elif not job_description.strip():
        st.warning(
            "Please enter a job description."
        )

    elif len(job_description.strip()) < 100:
        st.warning(
            "The job description is too short. "
            "Please provide the complete job description "
            "for a more accurate match."
        )

    else:

        try:
            # Extract resume text
            resume_text = extract_resume_text(
                uploaded_resume
            )
            if len(resume_text.strip()) < 100:
                st.error(
                    "The uploaded resume contains too little readable text. "
                    "Please upload a valid PDF or DOCX resume."
                )
                st.stop()
            resume_quality_score, resume_checks = analyze_resume_quality(
                resume_text
            )
            if not resume_text:
                st.error(
                    "Could not extract text from the resume."
                )
                st.stop()

            # Extract skills
            resume_skills = extract_skills(
                resume_text
            )

            job_skills = extract_skills(
                job_description
            )
            # --------------------------------------------------
            # Job Role Recommendations
            # --------------------------------------------------

            recommended_roles = recommend_roles(
                resume_skills,
                top_n=3
            )
            # Calculate match score
            match_score = calculate_match_score(
                resume_text,
                job_description,
                resume_skills,
                job_skills
            )

            match_level = get_match_level(
                match_score
            )

            # Skill analysis
            matching_skills = find_matching_skills(
                resume_skills,
                job_skills
            )

            missing_skills = find_missing_skills(
                resume_skills,
                job_skills
            )
            # --------------------------------------------------
            # Job Skills
            # --------------------------------------------------

            st.subheader("💼 Skills Required by Job")

            if job_skills:

                st.write(
                    " • ".join(job_skills)
                )

                st.info(
                    f"{len(job_skills)} relevant skills detected "
                    "from the job description."
                )

                st.subheader("🔥 Top Skills for This Job")

                for skill in job_skills:

                    if skill in matching_skills:
                        st.success(
                            f"✅ {skill} — Present in resume"
                        )
                    else:
                        st.warning(
                            f"⚠️ {skill} — Missing from resume"
                        )

            recommendations = generate_recommendations(
                missing_skills
            )

            # --------------------------------------------------
            # Results
            # --------------------------------------------------

            st.divider()

            st.subheader("📊 Resume Analysis")
            st.caption(
                "AI-powered analysis of resume quality, job compatibility, "
                "skills, and career opportunities."
            )

            skill_match_score = calculate_skill_match(
                resume_skills,
                job_skills
            )

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric(
                    "Overall Match",
                    f"{match_score}%"
                )

            with col2:
                st.metric(
                    "Match Level",
                    match_level
                )

            with col3:
                st.metric(
                    "Skill Match",
                    f"{skill_match_score}%"
                )

            with col4:
                st.metric(
                    "Skills Detected",
                    len(resume_skills)
                )

            with col5:
                st.metric(
                    "Resume Quality",
                    f"{resume_quality_score}%"
                )
            st.subheader("📈 Match Score Overview")

            st.caption(
                "Overall compatibility between your resume and the job description."
            )

            st.progress(
                min(match_score / 100, 1.0)
            )

            st.write(
                f"Your resume matches approximately "
                f"**{match_score}%** of the job requirements."
            )
            st.subheader("🎯 Skill Match Overview")

            st.progress(
                min(skill_match_score / 100, 1.0)
            )

            st.write(
                f"You match **{skill_match_score}%** of the "
                f"skills identified in the job description."
            )

            st.subheader("📄 Resume Quality Overview")

            st.progress(
                min(resume_quality_score / 100, 1.0)
            )

            st.write(
                f"Your resume quality score is "
                f"**{resume_quality_score}%** based on "
                "the presence of important resume sections."
            )

            if resume_quality_score >= 85:
                st.success(
                    "🌟 Your resume contains most of the important sections."
                )

            elif resume_quality_score >= 65:
                st.info(
                    "👍 Your resume has a good structure, but "
                    "some sections could be improved."
                )

            else:
                st.warning(
                    "⚠️ Your resume is missing several important sections. "
                    "Consider improving its structure."
                )
            # --------------------------------------------------
            # Matching Skills
            # --------------------------------------------------

            st.subheader("✅ Matching Skills")

            if matching_skills:
                skill_text = " • ".join(
                    f"**{skill}**"
                    for skill in matching_skills
                )

                st.markdown(skill_text)

                st.success(
                    f"{len(matching_skills)} skills match the job description."
                )

            else:
                st.info(
                    "No matching skills detected."
                )

            # --------------------------------------------------
            # Missing Skills
            # --------------------------------------------------

            st.subheader("⚠️ Missing Skills")

            if missing_skills:

                for skill in missing_skills:
                    st.warning(
                        f"⚠️ {skill}"
                    )

                st.info(
                    f"{len(missing_skills)} skills from the job "
                    "description were not detected in your resume."
                )

            else:
                st.success(
                    "🎉 No major missing skills detected."
                )
            # --------------------------------------------------
            # Skill Comparison
            # --------------------------------------------------

            st.subheader("📊 Skill Comparison")

            matching_count = len(matching_skills)
            missing_count = len(missing_skills)

            skill_chart_data = pd.DataFrame(
                {
                    "Skill Type": [
                        "Matching Skills",
                        "Missing Skills"
                    ],
                    "Count": [
                        matching_count,
                        missing_count
                    ]
                }
            )

            st.bar_chart(
                skill_chart_data.set_index("Skill Type")
            )

            # --------------------------------------------------
            # Resume Skills
            # --------------------------------------------------

            st.subheader("🧠 Skills Detected in Resume")

            if resume_skills:
                st.write(
                    ", ".join(resume_skills)
                )
            else:
                st.info(
                    "No skills were detected."
                )

            # --------------------------------------------------
            # Resume Quality Analysis
            # --------------------------------------------------

            st.subheader("📋 Resume Quality Analysis")

            for check, completed in resume_checks.items():

                if completed:
                    st.success(
                        f"✅ {check}"
                    )
                else:
                    st.warning(
                        f"⚠️ {check} section may need improvement."
                    )

            # --------------------------------------------------
            # Recommendations
            # --------------------------------------------------

            st.subheader("💡 Recommendations")

            for recommendation in recommendations:
                st.write(
                    f"- {recommendation}"
                )
            st.divider()
            # --------------------------------------------------
            # Recommended Job Roles
            # --------------------------------------------------

            st.subheader("💼 Recommended Job Roles")

            if recommended_roles:

                for index, recommendation in enumerate(
                    recommended_roles,
                    start=1
                ):

                    role = recommendation["role"]
                    score = recommendation["score"]

                    st.write(
                        f"### {index}. {role}"
                    )

                    st.progress(
                        min(score / 100, 1.0)
                    )

                    st.write(
                        f"Skill compatibility: **{score}%**"
                    )

                    if recommendation["matching_skills"]:
                        st.caption(
                            "Matching skills: "
                            + ", ".join(
                                recommendation["matching_skills"]
                            )
                        )

            else:

                st.info(
                    "No suitable job roles could be recommended."
                )
            st.divider()

            # --------------------------------------------------
            # Analysis Summary
            # --------------------------------------------------

            st.subheader("📝 Analysis Summary")

            if match_score >= 80:
                summary = (
                    "Your resume is a strong match for this position. "
                    "Your skills and experience appear highly relevant "
                    "to the job requirements."
                )

            elif match_score >= 65:
                summary = (
                    "Your resume is a good match for this position. "
                    "Consider improving a few missing skills or keywords "
                    "to strengthen your application."
                )

            elif match_score >= 50:
                summary = (
                    "Your resume has a moderate match with this position. "
                    "Review the missing skills and consider highlighting "
                    "more relevant projects and experience."
                )

            else:
                summary = (
                    "Your resume currently has a lower match with this "
                    "position. Review the missing skills and tailor your "
                    "resume to the job description where appropriate."
                )

            st.write(summary)
            # --------------------------------------------------
            # Resume Preview
            # --------------------------------------------------

            with st.expander(
                "📃 View Extracted Resume Text"
            ):
                st.text(resume_text)

        except ValueError as e:
            st.error(
                f"⚠️ {e}"
            )

        except Exception as e:
            st.error(
                "⚠️ Something went wrong while analyzing the resume. "
                "Please check that the file is a valid PDF/DOCX and "
                "try again."
            )