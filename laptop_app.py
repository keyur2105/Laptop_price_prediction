import streamlit as st
import numpy as np
import pandas as pd
import pickle


with open('df.pkl','rb') as file:
    df=pickle.load(file)
with open('pipe.pkl','rb') as file:
    pipe=pickle.load(file)


st.title("Laptop_price_prediction_application")
company = st.selectbox("Brand Name", df['Company'].unique())
typename = st.selectbox("type Name",df['TypeName'].unique())
cpu = st.selectbox("Cpu",df['Cpu'].unique())
ram = st.selectbox("Ram",[4,8,12,16,24,32,48])
gpu = st.selectbox("Gpu",df['Gpu'].unique())
opsys = st.selectbox("Operating System",df['OpSys'].unique())
weight = st.number_input("Weight of Laptop[KG]")
ips = st.selectbox("IPS Panel",['Yes','No'])
touchscreen = st.selectbox("Touch Screen",['Yes','No'])
Inch = st.number_input("Screen_Size")
resolution = st.selectbox("Resolution",['1366x768','1600x900','1920x1080','1920x1200','2560x1440','2560x1600','2304x1440','3200x1800','3840x2160','4096x2160'])
ssd = st.selectbox("SSD[GB]",[0,8,16,32,64,128,256,512,1024])
hdd = st.selectbox("HDD[GB]",[0,64,128,264,512,1024,2048])


if st.button("Predict"):

    if ips == "Yes":
        ips_panel = 1
    else:
        ips_panel = 0

    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0    

    X_res = int(resolution.split("x")[0])
    Y_res = int(resolution.split("x")[1])
    if Inch != 0:
        ppi = ((X_res**2)+(Y_res**2))**0.5/Inch
    else:
        ppi = 0

    predict_data = pd.DataFrame([[company,typename,cpu,ram,gpu,opsys,weight,ips_panel,touchscreen,ppi,ssd,hdd]],columns=['Company', 'TypeName', 'Cpu', 'Ram', 'Gpu', 'OpSys', 'Weight','IPS Panel', 'Touchscreen', 'price per inches', 'SSD', 'HDD'])
    print(predict_data)
    predict = pipe.predict(predict_data)
    Predict_price = np.exp(predict)[0]

    First_msg = "The price of your laptop can be around"
    second_msg = "depending on the above features."
    message = f"{First_msg} **{Predict_price:.2f}** {second_msg}"
    st.markdown(message)
    
    # st.title(message)
    # st.header(message)
    # st.subheader(message)