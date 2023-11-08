import streamlit as st

# App to calculate compound interest
# Formula for compound interest
# Amount = Principal(1+rate/number of times interest applied per time period)^(n*t)
# t is number of time periods elapsed

#Text box for
#1. Principal

#Slider for 
#2. Rate of Interest

#Dropdown for 
#3. n 
#4. t


st.markdown("<h1 style='text-align: center;'>Compound Interest Calculator</h1>", unsafe_allow_html=True)


with st.form("compound_interest_form"):
    P = float(st.text_input("**Principal Amount**",value=212000).strip())
    r = float(st.text_input("**Rate**",value=5.5).strip())/100
    n_key = st.selectbox("**How many times per year interest is applied**",("Monthly","Quarterly","Semi-Annually","Annually"))
    t = st.slider("**Length in Years**",min_value=1,max_value=50,value=10,step=1)
    submitted = st.form_submit_button("**Submit**")

n_dict = {"Monthly":12,"Quarterly":3,"Semi-Annually":2,"Annually":1}
n = n_dict[n_key]

amount = P*(1 + r/n)**(n*t)
amount = round(amount,2)

#------Create empty result container  at the top of the page which will be populated after all the calcullations
#Result container
st.divider()
result_container = st.container()
st.divider()

if submitted:
    #Show results in result container
    with result_container:
        #Show one liner result summary at the bottom of the page
        result_summary = f'You will get ${amount} in {t} year/s'
        st.markdown(f"<h2 style='text-align: center;'>{result_summary}</h1>", unsafe_allow_html=True)
        