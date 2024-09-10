import streamlit as st

def feedback_submission_page():
    st.title("Feedback Submission")

    # Feedback Form
    st.subheader("Provide Feedback")
    feedback_type = st.selectbox("Feedback Type", ["Learning Materials", "Question Banks"])
    feedback = st.text_area("Your Feedback", help="Provide detailed feedback.")
    
    # Assign a unique key to each button
    if st.button("Submit Feedback", key="feedback_submit_button"):
        # Logic to handle feedback submission
        st.success("Thank you! Your feedback has been submitted.")

def another_function_with_button():
    if st.button("Submit The Feedback", key="another_unique_key"):
        # Logic for another button with the same label
        st.success("Another feedback was submitted.")

if __name__ == "__main__":
    feedback_submission_page()
    another_function_with_button()
