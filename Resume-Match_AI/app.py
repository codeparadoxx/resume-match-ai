import streamlit as st
import requests

st.title("ResumeMatch AI")

resume = st.text_area("Paste Resume")
job = st.text_area("Paste Job Description")

if st.button("Check Match"):
    if resume.strip() == "" or job.strip() == "":
        st.error("Please paste BOTH Resume and Job Description")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/match",
            json={
                "resume": resume,
                "job": job
            }
        )

        st.write("Raw API Response:", response.json())

        if "match_percentage" in response.json():
            st.success(
                f"Match Score: {response.json()['match_percentage']}%\n"
                f"Match Level: {response.json()['match_level']}"
            )
        else:
            st.error("API Error — check backend")
