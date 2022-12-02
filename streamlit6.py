import streamlit as st

# you can style your streamlit app using external css and loading it in it using file open
# to see which class need to change inspect streamlit app

with open("st6.css","r") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# layouts and containers  -> can add multiple widgets in same line
st.title("REGISTRATION FORM")

# using beta_column  --> use st.columns instead
# Insert containers laid out as side-by-side columns.
# first , last = st.beta_columns(2)  # takes no. of widgets in single row as argument --> returns container object
# first.text_input("First Name")
first , last = st.columns(2) # divide into 2 columns having uniform width
with first:
    fname = st.text_input("First Name")
with last:
    lname = st.text_input("Last Name")

email , phone = st.columns([3,1])  # divides into 2 columns having ratio 3:1
with email:
    email_id = st.text_input("Email")
with phone:
    mob_on = st.text_input("Mobile no.")

u_name , passwd , re_passwd = st.columns(3)
with u_name:
    username = st.text_input("Username")
with passwd:
    passwd = st.text_input("Password",type="password")
with re_passwd:
    retpe_passwd = st.text_input("Retype Your Password",type="password")
if(passwd != retpe_passwd and retpe_passwd != "" and passwd != ""):
    st.warning("Password and Retype Password doesn't Match!")

check_box , empty , submit = st.columns([20,60,20])
with check_box:
    ch_box = st.checkbox("I Agree")

with submit:
    sub = st.button("Submit")

if sub and not ch_box:
    st.warning("Please Agree First to Submit!")
elif sub and ch_box:
    st.write("### Form Submitted Successfully :smile:")

# you can add validation too with regex
