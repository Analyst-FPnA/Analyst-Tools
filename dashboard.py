import streamlit as st

# Judul Dashboard
st.title("Analyst Database")

# Deskripsi dengan font khusus
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    h1 {
        font-family: 'Roboto', sans-serif;
        font-size: 25px;
        color: #222831;
    }
    </style>
    <h1>DASHBOARD</h1>
    """,
    unsafe_allow_html=True,
)

# Layout kotak interaktif
app1 = st.columns(1)[0]

with app1:
    st.markdown(
        """
        <a href='https://docs.google.com/spreadsheets/d/1n8HHYmRPGFZH21bLVBkb13jxhWEwIpVQJZ0bO529gQ0/edit?gid=0#gid=0' 
           target='_blank' style='text-decoration:none;'>
            <div style='background-color:#CDC1FF; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Roboto,sans-serif; font-size:16px;'>
                <strong style='color:white;'>Analyst Jobdesc Recap</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

# Baris kedua
app2 = st.columns(1)[0]

with app2:
    st.markdown(
        """
        <a href='https://docs.google.com/spreadsheets/d/15LL3oA7cfSFSHNWCjKLrRCywtNsaCsDqO0GSnHVX63Q/edit?gid=0#gid=0' 
           target='_blank' style='text-decoration:none;'>
            <div style='background-color:#CDC1FF; padding:20px; text-align:center; border-radius:10px; color:#222831; 
                        font-family:Roboto,sans-serif; font-size:16px;'>
                <strong style='color:white;'>Req CN to Validasi BA</strong>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )
