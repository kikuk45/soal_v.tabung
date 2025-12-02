import streamlit as st
import math
import random
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Soal Interaktif Volume Tabung", page_icon="🧮", layout="centered")

st.markdown("""
<style>
.main {background-color: #f7f7f7;}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 **Soal Interaktif Volume Tabung**")
st.write("Latihan hitung volume tabung dengan tampilan yang lebih interaktif dan visual!")

# ---------------------------
# Generate Soal
# ---------------------------

def generate_soal():
    r = random.randint(5, 14)
    t = random.randint(10, 30)
    volume = round(math.pi * r * r * t, 2)
    return r, t, volume

if "soal" not in st.session_state:
    st.session_state.soal = generate_soal()

r, t, jawaban_benar = st.session_state.soal

# ---------------------------
# Gambar Tabung
# ---------------------------

def gambar_tabung(r, t):
    fig, ax = plt.subplots(figsize=(4, 6))

    # Bagian lingkaran atas
    theta = np.linspace(0, 2 * np.pi, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta) + t

    # Tabung
    ax.plot(x, y)
    ax.plot(x, r * np.sin(theta))

    # Garis samping
    ax.plot([r, r], [0, t], linestyle="--")
    ax.plot([-r, -r], [0, t], linestyle="--")

    ax.set_aspect("equal")
    ax.axis("off")
    st.pyplot(fig)

# ---------------------------
# Kartu soal
# ---------------------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📘 Soal")
st.write(f"""
Sebuah tabung memiliki:
- Jari-jari: **{r} cm**  
- Tinggi: **{t} cm**  

Hitunglah **volume tabung** (gunakan π = 3.14).
""")

# Gambar tabung
st.subheader("📷 Gambar Tabung")
gambar_tabung(r, t)

# ---------------------------
# Jawaban
# ---------------------------

jawaban_siswa = st.number_input("Masukkan jawabanmu:", value=0.0)

cek = st.button("Periksa Jawaban 🔍")

if cek:
    if abs(jawaban_siswa - jawaban_benar) < 0.01:
        st.success(f"🎉 **Benar!** Volume tabung = {jawaban_benar} cm³")
    else:
        st.error(f"❌ Masih salah. Jawaban yang benar adalah **{jawaban_benar} cm³**")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Tombol Soal Baru
# ---------------------------

if st.button("🔄 Buat Soal Baru"):
    st.session_state.soal = generate_soal()
    st.rerun()

# ---------------------------
# Penjelasan
# ---------------------------

st.markdown("---")
st.subheader("📘 Penjelasan Rumus")
st.info("""
Volume tabung adalah:

### V = π × r² × t

di mana:
- r = jari-jari alas
- t = tinggi tabung
""")
