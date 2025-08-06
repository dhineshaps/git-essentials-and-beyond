import streamlit as st
import datetime

st.title("📝 Simple Streamlit Notes App")

note = st.text_area("Write your note:")

note_date = st.date_input("Pick a date", datetime.date.today())


if st.button("Save Note"):
    if note.strip():
        st.success(f"Note saved for {note_date}!")
        st.write(note)
    else:
        st.warning("Note is empty. Please write something.")