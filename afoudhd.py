import streamlit as st
from datetime import date

st.set_page_config(page_title="Kartu Ucapan Ulang Tahun", page_icon="🎉", layout="centered")

# Tambahkan custom CSS untuk background pink
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .stApp {
        background-color: #ffe6f0;
        color: #4d0039;
    }
    h1, h2, h3, h4 {
        color: #cc0066;
    }
    </style>
""", unsafe_allow_html=True)


# Ucapan ulang tahun
st.markdown(f"""
## 생일 축하해 , **Aera!** 🌸

Hari Senin kemarin, 14 Juli 2025 is your really special day. Semoga tahun ini penuh dengan kebahagiaan, kesehatan, dan kesuksesan!
            
Ironically aku malah lebih sibuk pas libur, jd rada low effort ini. Tapi aku harap tetap tersampaikan lah ya (maaf maaf)
              
You've done A LOT of things for this celebration! your cover song, endurance stream 12 jam, karaoke stream, dan stream ini. (good job yah, i'm sure everyone appreciates it!) (HARUS APPRECIATE!)
            
Bahkan ditengah-tengah tugas kuliah (dan anggota kelompok) yang sulit (banget), kamu masih sempet-sempetin buat ngerayain bareng kita-kita. (Rispek, gongju!)
                 
Last, apa benar kartu ucapan dari jin gundul yang ini cukup tanpa yang dibawah? (seperti biasa audionya burik ya wkwkwk)

-azu


---
""")

# VN
audio_file = open('hbd.m4a', 'rb')
st.audio(audio_file.read(), format='audio/m4a')

