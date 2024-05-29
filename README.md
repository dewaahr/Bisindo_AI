## Tugas untuk Kelas Kecerdasan Buatan UKDW
# AI Bisindo Sign Language App

Aplikasi ini adalah aplikasi yang menggunakan kecerdasan buatan (artificial intelligence/AI) untuk mendeteksi dan menerjemahkan Bahasa Isyarat Indonesia (BISINDO). Aplikasi ini memanfaatkan model deteksi objek YOLOv5 untuk mendeteksi tanda-tanda bahasa isyarat dari gambar atau video yang diberikan.

## Daftar Isi

- [Library yang Diperlukan](#library-yang-diperlukan)
- [Cara Menjalankan Aplikasi](#cara-menjalankan-aplikasi)

## Library yang Diperlukan

Untuk menjalankan aplikasi ini, Anda memerlukan beberapa library Python sebagai berikut:

- `torch`: Library PyTorch, digunakan untuk pemrosesan deep learning.
- `opencv-python-headless`: OpenCV, digunakan untuk pemrosesan gambar dan video.
- `flask`: Framework web yang digunakan untuk menyajikan hasil deteksi objek sebagai video stream.

## Cara Menjalankan Aplikasi

Anda dapat menjalankan aplikasi ini dengan mengikuti langkah-langkah berikut:

1. Pastikan Anda telah menginstal semua library yang diperlukan. Jika belum, Anda dapat menginstalnya dengan menggunakan pip:

    ```bash
    pip install torch opencv-python-headless Flask
    ```

2. Salin kode Python di atas ke dalam sebuah file Python (misalnya `app.py`).

3. Jalankan aplikasi dengan menjalankan file Python tersebut:

    ```bash
    python app.py
    ```

4. Setelah aplikasi berjalan, buka browser dan buka alamat `http://127.0.0.1:5000/` untuk melihat hasil deteksi objek secara real-time.
