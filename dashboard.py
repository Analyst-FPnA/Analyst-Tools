import streamlit as st
import os

# Tentukan direktori file statis
static_dir = os.path.join(os.path.dirname(__file__), "public")

# Path gambar dan font
font_path = os.path.join("assets", "fonts", "Cabo-Rounded-Regular.otf")
background_path = "/public/assets/images/Background.png"  # Path URL untuk gambar

# Deskripsi dengan font khusus dan background
st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'Cabo Rounded';
        src: url('{font_path}') format('opentype');
    }}
    h1 {{
        font-family: 'Cabo Rounded', sans-serif;
        font-size: 45px;
        color: #FFFFFF;
        text-align: center;
        padding: 20px;
        background-image: url('{background_path}');
        background-size: cover; /* Memastikan gambar menutupi area */
        background-repeat: no-repeat;
        background-position: center; /* Pusatkan gambar */
        border-radius: 10px; /* Membuat sudut lebih lembut */
    }}
    </style>
    <h1>ANALYST DATABASE</h1>
    """,
    unsafe_allow_html=True,
)

# Layout kotak interaktif pertama
app1 = st.columns(1)[0]

with app1:
    st.markdown(
        """
        <a href='https://docs.google.com/spreadsheets/d/1n8HHYmRPGFZH21bLVBkb13jxhWEwIpVQJZ0bO529gQ0/edit?gid=0#gid=0' 
           target='_blank' style='text-decoration:none;'>
            <div style='background-color:#00B2D6; padding:25px; text-align:center; border-radius:10px; color:#222831; 
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