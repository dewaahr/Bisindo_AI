# Tugas untuk Kelas Kecerdasan Buatan UKDW
# AI Bisindo Sign Language App

Aplikasi ini adalah aplikasi yang menggunakan kecerdasan buatan (artificial intelligence/AI) untuk mendeteksi dan menerjemahkan Bahasa Isyarat Indonesia (BISINDO). Aplikasi ini memanfaatkan model deteksi objek YOLOv5 untuk mendeteksi tanda-tanda bahasa isyarat dari gambar atau video yang diberikan.

## Daftar Isi

- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan dengan Flask](#penggunaan-dengan-flask)
- [Penggunaan Tanpa GUI](#penggunaan-tanpa-gui)
- [Endpoint](#endpoint)
- [Contoh Mengontrol Kamera](#contoh-mengontrol-kamera)
- [Catatan Tambahan](#catatan-tambahan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Fitur

- Penangkapan video real-time dari webcam.
- Deteksi objek menggunakan YOLOv5.
- Streaming video langsung dengan objek yang terdeteksi disorot.

## Instalasi

### Prasyarat

- Python 3.6+
- pip
- Git

### Langkah-langkah

1. **Kloning repositori:**

   ```sh
   git clone https://github.com/username/reponame.git
   cd reponame
