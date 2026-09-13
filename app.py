import streamlit as st 
st.title("BMI Calculator ")
name=st.text_input(":Name")
age=st.number_input("Age", min_value=1 , max_value=100)
gender = st.selectbox("Gender:", ["Female", "Male"])
weight = st.number_input("Weight (kg):", min_value=1.0, value=70.0)
height = st.number_input("height (m):", min_value=0.5, value=1.70)
if st.button("calculate BMI") :
    bmi=weight/height**2
    st.write(f"your bmi:{bmi:.1f}")
    if age <=18 :
         st.warning("you should use Percentiles for this group age")
    elif age<=65 and age>18 :
        if  bmi >= 30 :
            st.warning("Obesity")
        elif  bmi>=25 and bmi<29.9 : 
            st.warning("Over weight")
        elif   18.5<=bmi and 24.9> bmi : 
            st.success("normal weight")
        else :
            st.warning("under weight")
    else :
        if  bmi >= 30 :
            st.warning("Obesity")
        elif  27<=bmi and 29.9>bmi :
            st.warning("Over weight")
        elif   23<=bmi and 27>bmi : 
            st.success("normal weihgt")
        else :
            st.warning("under weight")
   