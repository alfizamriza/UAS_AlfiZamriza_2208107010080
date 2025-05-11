# 📝 Penulis Email Cerdas untuk Pelajar

Proyek ini adalah aplikasi web yang memungkinkan pelajar untuk menghasilkan email profesional secara otomatis menggunakan teknologi AI Gemini dari Google. Aplikasi ini menyediakan antarmuka yang ramah pengguna di mana pelajar dapat memasukkan detail dan poin penting, lalu menerima email yang terstruktur dengan baik.

## 📦 Fitur Utama

* Pilih kategori email: Akademik, Tesis, Magang, dll.
* Pilih nada penulisan: formal, netral, atau santai
* Dukungan untuk bahasa Inggris dan Indonesia
* Tambahkan poin-poin penting yang ingin disertakan dalam email
* Hasilkan email yang profesional, jelas, dan ringkas secara otomatis

## 📁 Struktur Proyek

```
intelligent_email_writer/
├── .env                    # Berisi kunci API Gemini (buat dari .env.template)
├── app.py                  # Frontend dengan Streamlit
├── backend/
│   └── main.py             # Backend API menggunakan FastAPI
├── requirements.txt        # Dependensi backend
├── requirements_frontend.txt # Dependensi frontend
├── README.md               # Dokumentasi proyek
```

## ⚙️ Instalasi dan Menjalankan Proyek

### 1. Kloning Repositori

```bash
git clone https://github.com/username/intelligent_email_writer.git
cd intelligent_email_writer
```

### 2. Siapkan dan Jalankan Backend (FastAPI)

```bash
# Buat dan aktifkan lingkungan virtual
python3 -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows

# Instal dependensi
pip install -r requirements.txt

# Jalankan server
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Siapkan dan Jalankan Frontend (Streamlit)

Buka terminal baru:

```bash
# Pastikan Anda berada di direktori proyek dan lingkungan virtual sudah diaktifkan
pip install -r requirements_frontend.txt

# Jalankan aplikasi Streamlit
streamlit run app.py
```

## 🔐 Konfigurasi Kunci API Gemini

1. Kunjungi https://aistudio.google.com/app/apikey
2. Klik **Buat Kunci API**
3. Salin kunci API dan simpan di file `.env` di root proyek dengan format:

```
GEMINI_API_KEY=kunci_api_anda_di_sini
API_URL=http://localhost:8000
```

Anda dapat menyalin file `.env.template` untuk membuat file `.env`:

```bash
cp .env.template .env
```

Kemudian edit file `.env` untuk menambahkan kunci API Anda.

## 📬 Contoh Penggunaan

1. Pilih kategori email dan gaya penulisan
2. Masukkan informasi penerima, subjek, dan poin-poin penting
3. Klik tombol **"Hasilkan Email"**
4. Email yang dihasilkan akan ditampilkan di halaman aplikasi
5. Gunakan tombol salin untuk menyalin email ke clipboard Anda

## 🚀 Teknologi yang Digunakan

- **Backend**: FastAPI, Google Generative AI (Gemini)
- **Frontend**: Streamlit
- **Lingkungan**: Python 3.8 atau lebih tinggi

## 🤔 Pemecahan Masalah

- Jika terjadi kesalahan koneksi, pastikan server backend sedang berjalan
- Jika terjadi kesalahan kunci API, periksa apakah kunci API Gemini Anda sudah benar di file `.env`
- Untuk masalah lain, periksa output konsol untuk pesan kesalahan

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detailnya.

## 🙏 Ucapan Terima Kasih

- Google Gemini AI untuk kemampuan model bahasa
- FastAPI dan Streamlit untuk kerangka kerja web yang luar biasa
