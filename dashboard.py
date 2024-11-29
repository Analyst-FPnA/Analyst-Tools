import streamlit as st
import os

# Tentukan path font
font_path = os.path.join('assets', 'fonts', 'Cabo-Rounded-Regular.otf')

# Deskripsi dengan font khusus
st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'Cabo Rounded';
        src: url('{font_path}') format('opentype');
    }}
    h1 {{
        font-family: 'Cabo Rounded', sans-serif;
        font-size: 25px;
        color: #FFFFFF;
        text-align: center;
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
            <div style='background-color:#00B2D6; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Cabo Rounded,sans-serif; font-size:16px; border:3px solid black;'>
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
                        font-family:Cabo Rounded,sans-serif; font-size:16px; border:3px solid black;'>
                <strong style='color:white;'>Req CN to Validasi BA</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )