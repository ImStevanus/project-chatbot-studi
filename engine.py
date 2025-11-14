import string
from thefuzz import fuzz, process

def proses_input_text(teks):
    """Membersihkan teks user"""
    teks = teks.lower()
    for tanda_baca in string.punctuation:
        teks = teks.replace(tanda_baca, " ")
    return teks.split()

def cek_apakah_negasi(index_kata, list_semua_kata):
    """
    Mengecek apakah ada kata negatif dalam jarak 3 kata sebelum target.
    Ini akan menangkap frasa seperti:
    - "GAK dokter" (Jarak 1)
    - "GAK MAU dokter" (Jarak 2)
    - "GAK MAU JADI dokter" (Jarak 3)
    - "JANGAN SAMPAI dokter" (Jarak 2)
    """
    # Daftar kata pemicu negatif
    kata_negatif = [
        "tidak", "gak", "enggak", "bukan", "gamau", "anti", "jangan", "ogah", 
        "benci", "ga", "ndak", "stop", "hindari", "malas"
    ]
    
    # Kita cek mundur 3 langkah ke belakang
    # range(1, 4) artinya cek index -1, -2, dan -3
    jarak_cek = 3 
    
    for i in range(1, jarak_cek + 1):
        index_cek = index_kata - i
        
        # Pastikan index tidak minus (tidak mundur kelewatan sampai sebelum kata pertama)
        if index_cek >= 0:
            kata_sebelumnya = list_semua_kata[index_cek]
            if kata_sebelumnya in kata_negatif:
                return True # Ketemu kata "gak" / "jangan"!
            
    return False

def hitung_kecocokan(input_teks_user, data_jurusan):
    kata_user_list = proses_input_text(input_teks_user)
    
    skor_tertinggi = -99 
    jurusan_terpilih = "Maaf, saya bingung. Coba ceritakan dengan kata-kata lain."
    
    THRESHOLD = 85 

    for nama_jurusan, keywords_database in data_jurusan.items():
        skor_jurusan = 0
        
        for i, kata_user in enumerate(kata_user_list):
            
            if len(kata_user) < 3: continue 
            
            best_match, nilai_kemiripan = process.extractOne(kata_user, keywords_database)
            
            if nilai_kemiripan >= THRESHOLD:
                # CEK NEGASI (Sekarang lebih canggih, bisa cek sampai 3 kata belakang)
                is_negasi = cek_apakah_negasi(i, kata_user_list)
                
                if is_negasi:
                    skor_jurusan -= 5 # Hukuman poin
                    print(f"❌ Deteksi Penolakan: '{kata_user}' di jurusan {nama_jurusan}")
                else:
                    skor_jurusan += 1 # Tambah poin
        
        if skor_jurusan > skor_tertinggi:
            skor_tertinggi = skor_jurusan
            jurusan_terpilih = nama_jurusan
            
    if skor_tertinggi <= 0:
        return "Sepertinya kamu menghindari bidang-bidang tersebut. Coba sebutkan apa yang kamu SUKA."
        
    return jurusan_terpilih