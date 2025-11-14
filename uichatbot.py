import streamlit as st
import time
import loader
import engine

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Campus AI Advisor", 
    page_icon="🤖",
    layout="centered" # Tampilan fokus di tengah seperti aplikasi HP
)

# --- 2. INISIALISASI MEMORI CHAT (SESSION STATE) ---
# Ini supaya chat tidak hilang saat user menekan enter
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Pesan pembuka dari bot
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Halo! 👋 Aku AI Advisor kampusmu. \n\nCeritakan pelajaran kesukaanmu, hobimu, atau cita-citamu. Aku akan bantu carikan jurusan yang cocok!"
    })

# --- 3. SIDEBAR (PROFIL & RESET) ---
with st.sidebar:
    st.header("👤 Profil Kamu")
    nama_user = st.text_input("Nama Panggilan:", placeholder="Ketik namamu...")
    
    st.divider()
    st.caption("Tips: Ceritakan dengan kalimat santai.")
    st.caption("Contoh: *'Aku suka main game dan ngulik komputer, tapi aku lemah di hafalan.'*")
    
    # Tombol Reset Chat
    if st.button("🔄 Ulangi Percakapan"):
        st.session_state.messages = [] # Kosongkan memori
        st.rerun() # Refresh halaman

# --- 4. TAMPILAN JUDUL ---
st.title("🤖 Campus AI Advisor")
st.caption("🚀 Powered by Python & Fuzzy Logic")
st.divider()

# --- 5. MENAMPILKAN RIWAYAT CHAT ---
# Loop ini menggambar ulang semua chat dari memori ke layar
for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# --- 6. INPUT USER (CHAT BOX DI BAWAH) ---
# st.chat_input membuat kotak ketik menempel di bawah layar
prompt = st.chat_input("Ketik minatmu di sini...")

if prompt:
    # A. Simpan & Tampilkan Pesan User
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # B. Proses Jawaban Bot
    data_kampus = loader.muat_data()
    
    if data_kampus is None:
        response = "❌ Maaf, Database jurusan (file json) tidak ditemukan."
    else:
        # Efek "Bot sedang mengetik..." biar terlihat real
        with st.chat_message("assistant"):
            with st.spinner("Sedang menganalisis minatmu..."):
                time.sleep(1.5) # Jeda 1.5 detik
                
                # Panggil Otak (Engine)
                hasil_rekomendasi = engine.hitung_kecocokan(prompt, data_kampus)
                
                # Susun kalimat jawaban
                sapaan = f"Halo **{nama_user}**! " if nama_user else ""
                response = f"{sapaan}Berdasarkan ceritamu, aku merekomendasikan jurusan:\n\n### ✨ {hasil_rekomendasi} ✨\n\nApakah sesuai dengan keinginanmu?"
                
                st.markdown(response)
    
    # C. Simpan Pesan Bot ke Memori
    st.session_state.messages.append({"role": "assistant", "content": response})