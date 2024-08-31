import streamlit as st

def feedback_submission_page():
    st.title("Feedback Submission")

    # Feedback Form
    st.subheader("Provide Feedback")
    feedback_type = st.selectbox("Feedback Type", ["Learning Materials", "Question Banks"])
    feedback = st.text_area("Your Feedback", help="Provide detailed feedback.")
    
    if st.button("Submit Feedback"):
        # Logic to handle feedback submission
        st.success("Thank you! Your feedback has been submitted.")

# Call the function to render the page
if __name__ == "__main__":
    feedback_submission_page()
