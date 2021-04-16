import streamlit as st

value = st.sidebar.selectbox("Box",("HI","Hello"))

st.write(f"# {value} Vignesh")
value2 = st.sidebar.selectbox("Box2", ("HI", "Hello"))

file = st.file_uploader("Pick a File")
date = st.date_input("Date")
date_split = str(date).split("-")
st.write(int(date_split[2]), int(date_split[1]), int(date_split[0]))

with st.beta_container():
    st.write("This is inside the container")
    st.write("This is inside the container")
    st.write("This is inside the container")
st.write("This is outside the container")
