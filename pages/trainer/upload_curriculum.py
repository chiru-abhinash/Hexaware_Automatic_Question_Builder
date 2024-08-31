# pages/trainer/upload_curriculum.py
import streamlit as st

def show_upload_curriculum_page():
    st.title("Upload Curriculum")
    
    technology = st.selectbox("Select Technology", ["Python", "Java", "JavaScript", "C++", "SQL"])
    uploaded_file = st.file_uploader("Upload Curriculum File", type=["csv", "xls", "xlsx"])
    
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        # Process the uploaded file as needed

    if st.button("Submit"):
        st.success(f"Curriculum for {technology} uploaded successfully.")

if __name__ == "__main__":
    show_upload_curriculum_page()
