import streamlit as st
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
if not firebase_admin._apps:
    cred=credentials.Certificate('firebasekey.json')
    app=firebase_admin.initialize_app(cred,{'databaseURL':'https://assignment-app-adc11-default-rtdb.firebaseio.com/'})

st.set_page_config(page_title="MyStreamlit",page_icon="random")
st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)  


emp_id=st.text_input('Enter employee ID : ')
emp_name=st.text_input('Enter employee name : ')
emp_salary=st.text_input("Enter your salary : ")
d={"EmployeeID":emp_id,"Name":emp_name,"Salary":emp_salary}
btn=st.button("Submit")
ref=db.reference("/")
ref.update(d)

st.write("Emloyee ID:",emp_id)
st.write(" Name: ",emp_name)
st.write(" Salary:",emp_salary)
