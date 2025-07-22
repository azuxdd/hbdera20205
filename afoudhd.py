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
## 생일 축하해 , **Aera!** 🎈

Hari Senin kemarin, 14 Juli 2025 is your really special day. Semoga tahun ini penuh dengan kebahagiaan, kesehatan, dan kesuksesan!
            
Ironically, aku malah lebih sibuk pas libur, jd rada low effort ini. Tapi aku harap tetap tersampaikan lah ya (maaf maaf)
              
You've done A LOT of things for this celebration, your cover song, your 12 hour endurance stream, the karaoke stream, and this as well. (good job yah)
            
Bahkan ditengah tugas kuliah (dan anggota kelompok) yang sulit, kamu masih sempet-sempetin buat ngerayain bareng jingundul-jingundul ini. (rispek gongju)
                 
Lastly, apa benar kartu ucapan dari azu cukup tanpa hal satu ini? 
            
---
""")

# VN
audio_file = open('hbd.m4a', 'rb')
st.audio(audio_file.read(), format='audio/m4a')

# Pesan penutup
st.markdown("📝 Dibuat dengan ❤️ menggunakan Streamlit.")
