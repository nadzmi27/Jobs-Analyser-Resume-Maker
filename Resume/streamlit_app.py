import streamlit

# Streamlit UI
st.title('Resume Scorer')

# Text areas for user input
resume_text = st.text_area("Paste Your Resume Here")
jd_text = st.text_area("Paste Job Description Here")

if st.button('Match'):
    if resume_text and jd_text:
        # Calculate the match percentage
        match_percentage = calculate_match_percentage(resume_text, jd_text)
        st.write(f"Match Percentage: {match_percentage:.2f}%")

        # Extracting key terms from JD and checking against the resume
        jd_terms = extract_key_terms(jd_text)
        resume_terms = extract_key_terms(resume_text)
        missing_terms = jd_terms - resume_terms

        if match_percentage >= 70:
            st.success("Good Chances of getting your Resume Shortlisted.")
        elif 40 <= match_percentage < 70:
            st.warning("Good match but can be improved.")
            if missing_terms:
                st.info(f"Consider adding these key terms from the job description to your resume:\n {', '.join(missing_terms)}")
        elif match_percentage < 40:
            st.error("Poor match.")
            if missing_terms:
                st.info(f"Your resume is missing these key terms from the job description:\n {', '.join(missing_terms)}")
    else:
        st.warning("Please enter both Resume and Job Description.")