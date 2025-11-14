# 🤖 Chatbot Rekomendasi Program Studi

Ini adalah proyek chatbot cerdas yang dibuat dengan Python & Streamlit. Bot ini dapat merekomendasikan jurusan kuliah berdasarkan minat dan hobi yang diketik oleh pengguna.

## ✨ Fitur Unggulan

* **UI Interaktif:** Tampilan dibuat modern seperti aplikasi chat sungguhan menggunakan Streamlit.
* **Pemrosesan Bahasa Alami:** Pengguna bisa mengetik dalam kalimat sehari-hari (contoh: "aku suka gambar tapi gak suka hitungan").
* **Logika Fuzzy (Fuzzy Logic):** Bot bisa mentolerir salah ketik atau kata berimbuhan (misal: "koding" vs "coding") menggunakan library `thefuzz`.
* **Penanganan Negasi:** Bot mengerti jika pengguna mengetik kata negatif (contoh: "gak mau jadi dokter" atau "bukan teknik") dan akan menghindari rekomendasi tersebut.

## 📸 Tampilan Aplikasi
![Tampilan Chatbot](https://github.com/ImStevanus/project-chatbot-studi/blob/main/tampilanchatbotprodi.png?raw=true)

## 💻 Teknologi yang Digunakan

* Python
* Streamlit (Untuk UI)
* TheFuzz (Untuk Fuzzy Logic)
* JSON (Sebagai database jurusan)

## 🚀 Cara Menjalankan Proyek di Lokal

1.  Clone repository ini ke komputer Anda.
2.  Install semua library yang dibutuhkan:
    ```bash
    pip install streamlit thefuzz
    ```
3.  Jalankan aplikasi melalui terminal:
    ```bash
    streamlit run uichatbot.py
    ```
