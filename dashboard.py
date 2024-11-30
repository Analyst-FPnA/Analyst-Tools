import streamlit as st
import os

# Path untuk font dan background
font_path = os.path.join("assets", "fonts", "Cabo-Rounded-Regular.otf")
background_path = os.path.join("assets", "images", "Background.png")

# CSS untuk styling background dan font
st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'Cabo Rounded';
        src: url('{font_path}') format('opentype');
    }}
    body {{
        background-image: url('{background_path}');
        background-size: contain; /* Ukuran gambar disesuaikan agar terlihat utuh */
        background-repeat: no-repeat; /* Tidak mengulang gambar */
        background-position: center; /* Gambar berada di tengah */
        background-attachment: fixed; /* Background tetap saat scrolling */
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