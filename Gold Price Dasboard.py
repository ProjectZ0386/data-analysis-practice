import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gold Price Dasboard")
st.title("Dasboard Gold")
st.write("dasboard by Kasem77")

df = pd.read_csv("Daily.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

for col in ["USD", "EUR", "JPY", "GBP", "CAD", "CHF", "INR", "CNY", "TRY", "SAR", "IDR", "AED", "THB", "VND", "EGP", "KRW", "RUB", "ZAR", "AUD"]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(",","").apply(pd.to_numeric, errors='coerce') 


currency = st.selectbox("เลือกสกุลเงิน",["USD", "EUR", "JPY", "GBP", "CAD", "CHF", "INR", "CNY", "TRY", "SAR", "IDR", "AED", "THB", "VND", "EGP", "KRW", "RUB", "ZAR", "AUD"])

year_range = st.slider("เลือกช่วงปี", 1978,2023, (2010,2023))
df_filterred = df[(df["Date"].dt.year >= year_range[0]) & (df["Date"].dt.year <= year_range[1])]

#df_filterred = df_filterred.dropna(subset=[currency])

if len(df_filterred) > 0:
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df_filterred["Date"],df_filterred[currency], linewidth=2, color='gold')
    ax.set_xlabel("Date")
    ax.set_ylabel(f"Price : {currency}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ราคาเฉลี่ย", f"{df_filterred[currency].mean():.2f}")
    with col2:
        st.metric("ราคาสูงสุด",f"{df_filterred[currency].max():.2f}")
    with col3:
        st.metric("ราคาต่ำสุด",f"{df_filterred[currency].min():.2f}")
else:
    st.error("❌ ไม่มีข้อมูล!")


