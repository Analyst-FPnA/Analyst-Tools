import streamlit as st
import os
import base64

# Path untuk font
font_path = os.path.join("assets", "fonts", "Cabo-Rounded-Regular.otf")

# Load background image
background_image_path = "assets/images/Background.png"
with open(background_image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

# CSS untuk styling background dan font
st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'Cabo Rounded';
        src: url('{font_path}') format('opentype');
    }}
    h1 {{
        font-family: 'Cabo Rounded', sans-serif;
        font-size: 50px;
        color: #FFFFFF;
        text-align: center;
        padding: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
# Judul aplikasi
st.markdown("<h1>ANALYST DATABASE</h1>", unsafe_allow_html=True)


"SPREADSHEET"
# Layout kotak interaktif pertama
app1 = st.columns(1)[0]
with app1:
    st.markdown(
        """
        <a href='https://docs.google.com/spreadsheets/d/1n8HHYmRPGFZH21bLVBkb13jxhWEwIpVQJZ0bO529gQ0/edit?gid=0#gid=0' 
        target='_blank' style='text-decoration:none;'>
            <div style='background-color:#00B2D6; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Cabo Rounded,sans-serif; font-size:25px; border:4px solid black;'>
                <strong style='color:white;'>Analyst Jobdesc Recap</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

# Layout kotak interaktif kedua
app2 = st.columns(1)[0]
with app2:
    st.markdown(
        """
        <a href='https://docs.google.com/spreadsheets/d/15LL3oA7cfSFSHNWCjKLrRCywtNsaCsDqO0GSnHVX63Q/edit?gid=0#gid=0' 
        target='_blank' style='text-decoration:none;'>
            <div style='background-color:#00B2D6; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Cabo Rounded,sans-serif; font-size:25px; border:4px solid black;'>
                <strong style='color:white;'>Request Cancel Nota to Validasi BA</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )
"WEBSMART (TANPA LOGIN)"
# Layout kotak interaktif pertama
web1 = st.columns(1)[0]
with web1:
    st.markdown(
        """
        <a href='http://202.157.187.244/eng_esb/report/rpt_trans_perresto.php?idd=595' 
        target='_blank' style='text-decoration:none;'>
            <div style='background-color:#00B2D6; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Cabo Rounded,sans-serif; font-size:25px; border:4px solid black;'>
                <strong style='color:white;'>ESB</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

# Layout kotak interaktif kedua
web2 = st.columns(1)[0]
with web2:
    st.markdown(
        """
        <a href='http://202.157.187.244/dsppa/report/rpt_trans_perresto24.php?idd=595' 
        target='_blank' style='text-decoration:none;'>
            <div style='background-color:#00B2D6; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Cabo Rounded,sans-serif; font-size:25px; border:4px solid black;'>
                <strong style='color:white;'>SOLIS</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )
    