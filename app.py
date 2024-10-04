import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

title=st.title('Red Bus')
subtitle=st.markdown('Online Bus Ticket Booking Site')

andhra=[]
df=pd.read_csv("all_data_ap.csv")
for i,r in df.iterrows(): 
    andhra.append(r['Route_name'])

kerala=[]
df=pd.read_csv("all_data_k.csv")
for i,r in df.iterrows():
    kerala.append(r['Route_name'])

telungana=[]
df=pd.read_csv("all_data_t.csv")
for i,r in df.iterrows():
    telungana.append(r['Route_name'])

kadamba=[]
df=pd.read_csv("all_data_kad.csv")
for i,r in df.iterrows():
    kadamba.append(r['Route_name'])


rajasthan=[]
df=pd.read_csv("all_data_r.csv")
for i,r in df.iterrows():
    rajasthan.append(r['Route_name'])

southbengal=[]
df=pd.read_csv("all_data_sb.csv")
for i,r in df.iterrows():
    southbengal.append(r['Route_name'])

hp=[]
df=pd.read_csv("all_data_hp.csv")
for i,r in df.iterrows():
    hp.append(r["Route_name"])

assam=[]
df=pd.read_csv("all_data_a.csv")
for i,r in df.iterrows():
    assam.append(r['Route_name'])

up=[]
df=pd.read_csv("all_data_up.csv")
for i,r in df.iterrows():
    up.append(r["Route_name"])

bihar=[]
df=pd.read_csv("all_data_b.csv")
for i,r in df.iterrows():
    bihar.append(r['Route_name'])


web=option_menu(menu_title="Online Bus",
                options=["Home","States and Routes"],
                icons=["House","Info_circle"],
                orientation="horizontal"
                )  

if web=="Home":
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    
if web=="States and Routes":
    states=st.selectbox("Lists of states",['Andhra Pradesh','Kerala','Telungana','Kadamba','Rajasthan','South Bengal','Himachal Pradesh','Assam','Uttar Pradesh','Bihar'])
    fare=st.radio("Choose bus fare range",['50-500','500-1000','1000-2000'])


if states=="Andhra Pradesh":
    A=st.selectbox("List of Routes",andhra)
    if fare=='50-500':
        df=pd.read_csv("all_bus_details_ap.csv")
        st.write(df)

if states=="Kerala":
    K=st.selectbox("List of Routes",kerala)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_k.csv")
        st.write(df)
   
if states=="Telungana":
    T=st.selectbox("List of Routes",telungana)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_t.csv")
        st.write(df)

if states=="Kadamba":
    Kad=st.selectbox("List of Routes",kadamba)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_kad.csv")
        st.write(df)

if states=="Rajasthan":
    R=st.selectbox("List of Routes",rajasthan)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_r.csv")
        st.write(df)

if states=="South Bengal":
    SB=st.selectbox("List of Routes",southbengal)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_sb.csv")
        st.write(df)

if states=="Himachal Pradesh":
    HP=st.selectbox("List of Routes",hp)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_hp.csv")
        st.write(df)

if states=="Assam":
    As=st.selectbox("List of Routes",assam)
    if fare=='50-500'  and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_a.csv")
        st.write(df)

if states=="Uttar Pradesh":
    UP=st.selectbox("List of Routes",up)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_up.csv")
        st.write(df)

if states=="Bihar":
    B=st.selectbox("List of Routes",bihar)
    if fare=='50-500' and '500-1000'and'1000-2000':
        df=pd.read_csv("all_bus_details_b.csv")
        st.write(df)