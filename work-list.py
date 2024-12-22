import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('instant-amp-443020-d9-83623d17cc94.json', scope)
client = gspread.authorize(creds)

sheet = client.open("to-do-task").sheet3

data = sheet.get_all_records()

st.write(data)


st.title("Make your work-list easily")
st.text("Here you can make your list in excel file just fill out the form and click DONE")

st.text_input("Day:")
st.text_input("The one thing I must do:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox1")
st.text_input("Second:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox2")
st.text_input("Third:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox7")
st.text_input("Fourth:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox3")
st.text_input("Fifth:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox4")
st.text_input("Sixth:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox5")
st.text_input("Seventh:")
st.selectbox("Choose a statue:", ["Not started", "In progress", "Completed"], key="selectbox6")

st.button("DONE")

