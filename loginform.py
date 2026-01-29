import streamlit as st
#header
st.header("Anurag University Student Management")
#title
st.title("Welcome to Student Management System")
#subheader
st.subheader("Manage student records efficiently and effectively")
#horizontal line
st.markdown("------------------------------")
#text
st.text("This application allows you to perform CRUD operations on student records using mysql database")
#write
st.write("Hello Streamlit")
st.write(123)
st.write([1,2,3])
st.write({"name":"Anurag","course":"B.Tech"})
#markdown
st.markdown("### Features of Application")
st.markdown("**Bold Text**")
st.markdown("*Italic Text*")
st.markdown("-Item 1\n- Item 2")
st.markdown("<h3 style='color:red'>Red Text</h3>",unsafe_allow_html=True)
#caption
st.caption("This is a caption for student management system")
#code
st.code("""
def add(a,b):
return a+b
""",language="python")
#latex
st.latex(r''' 
a^2 + b^2 = c^2
''')
#divider
st.divider()
#button
if st.button("Click Me"):
    st.write("Button Clicked!") 
    st.success("operattion successful!")
    st.balloons()
    st.snow() 
else:
    st.write("Button not clicked yet.") 
    st.error("operation failed!")
#text 
name=st.text_input("Enter your name:")
st.write(f"Hello ,{name}!")

if name =="":
    st.warning("Name cannot be empty")
elif not name.isalpha():
    st.error("Invalid input please enter only alphabets(no numbers or symbols).")
else:
    st.success(f"Hello, {name}!")

feedback=st.text_area("Enter your feedback:")
st.write(feedback)

#checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!")

#radio button
gender=st.radio("Select your gender:",("Male","Female","Other"))
st.write(f"You selected: {gender}")

#selectbox
country=st.selectbox("Select your country:",["USA","Canada","UK","Australia"])
st.write(f"You selected: {country}")    

#multiselect
skills=st.multiselect("Select your skills:",["Python","Java","C++","JavaScript"])
st.write("Skills:",skills)

#slider
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age {age}years old.")

#uploader
uploaded_file=st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")

#form
with st.form("my_form"):
    name=st.text_input("Name")
    age=st.number_input("Age",0,100)
    submitted=st.form_submit_button("Submit")
if submitted:
    st.write(name,age)

#form_submit_button
with st.form("login"):  
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    login=st.form_submit_button("Login")    
if login:
    st.success(f"Login Successful")
st.divider()
#columns
col1,col2,col3=st.columns(3)    
with col1:
    st.header("Column 1")
    st.write("This is column 1")    
with col2:
    st.header("Column 2")
    st.write("This is column 2")
with col3:
    st.header("Column 3")
    st.write("This is column 3")
st.divider()

#container
container=st.container()
container.write("inside the container")
container.button("click")
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
st.divider()

#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
st.divider()    


@st.cache_data
def load_data():
    return [1,2,3,4]
data=load_data()
st.write(data)  
