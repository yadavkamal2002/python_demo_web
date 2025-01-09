import streamlit as st
import pandas as pd
# st.title("welcome to kamal")
# st.header("python")
# st.subheader("java")
# st.markdown("i love python")
# st.code("""for i in range (1,5,5):
#              print("hello")""")

#=========== student-excal-viewer ===========
# # Make sure you have 'openpyxl' installed: pip install openpyxl
# st.title("Student Attendance Viewer")
# # Reading Excel File Correctly
# try:
#     dataset = pd.read_excel("STUDENT-ATTENDANCE.xlsx", engine='openpyxl')
#     st.dataframe(dataset)
# except FileNotFoundError:
#     st.error("Error: File not found. Please check the file path!")
# except Exception as e:
#     st.error(f"An error occurred: {e}")


name =st.text_input("Enter Your Name : ")
fname =st.text_input("Enter Your Father Name : ")
adr = st.text_area ("Enter Your Text : ")
classdata = st.selectbox("Enter Your Class : ",(1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
Name : {name}
Father Name : {fname}
address : {adr}
class : {classdata}""")
