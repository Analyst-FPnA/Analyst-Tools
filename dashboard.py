import streamlit as st

# Judul Dashboard
st.title("Analyst Compile Data")

# Deskripsi dengan font khusus
st.markdown(
    "<h1 style='font-family:Roboto,sans-serif; font-size:25px; color:#FFF5E4;'>DASHBOARD</h1>", 
    unsafe_allow_html=True
)

# Layout kotak interaktif
app1= st.columns(1)

with app1:
    st.markdown(
        "<a href='https://docs.google.com/spreadsheets/d/1n8HHYmRPGFZH21bLVBkb13jxhWEwIpVQJZ0bO529gQ0/edit?gid=0#gid=0' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>Analyst Jobdesc Recap</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris kedua
app2= st.columns(1)

with app2:
    st.markdown(
        "<a href='https://docs.google.com/spreadsheets/d/15LL3oA7cfSFSHNWCjKLrRCywtNsaCsDqO0GSnHVX63Q/edit?gid=0#gid=0' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>Req CN to Validasi BA</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )