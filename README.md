# Tugas untuk Kelas Kecerdasan Buatan UKDW
## AI Bisindo Sign Language App

Aplikasi ini adalah aplikasi yang menggunakan kecerdasan buatan (artificial intelligence/AI) untuk mendeteksi dan menerjemahkan Bahasa Isyarat Indonesia (BISINDO). Aplikasi ini memanfaatkan model deteksi objek YOLOv5 untuk mendeteksi tanda-tanda bahasa isyarat dari gambar atau video yang diberikan.

## Syarat
- Python 3.6+
- Git
- PyTorch
- OpenCV
- Flask

## Tutorial Instalasi
1. **Kloning repositori:**
    ```sh
    git clone https://github.com/dewaahr/Bisindo_AI.git
    cd reponame
    ```

2. **Instal paket yang diperlukan:**
    - PyTorch:
        ```sh
        pip install torch
        ```

    - OpenCV:
        ```sh
        pip install opencv-python-headless
        ```

    - Flask:
        ```sh
        pip install Flask
        ```

3. **Unduh model YOLOv5:**
    Model YOLOv5 akan diunduh secara otomatis saat aplikasi dijalankan pertama kali. Pastikan Anda memiliki koneksi internet yang stabil.

## Penggunaan dengan Flask
1. Salin kode Python ke dalam sebuah file Python (misalnya `app.py`).
2. Jalankan aplikasi dengan perintah `python app.py`.
3. Buka browser dan buka alamat `http://127.0.0.1:5000/` untuk melihat hasil deteksi objek secara real-time.

## Penggunaan Tanpa GUI
1. Salin kode Python ke dalam sebuah file Python (misalnya `camera_detection.py`).
2. Jalankan kode dengan perintah `python camera_detection.py`.
3. Jendela video akan muncul dan menampilkan hasil deteksi objek secara real-time.

## Endpoint
- **`POST /start_camera`**: Memulai webcam.
- **`POST /stop_camera`**: Menghentikan webcam.

## Contoh Mengontrol Kamera
- Memulai Kamera: `curl -X POST http://127.0.0.1:5000/start_camera`
- Menghentikan Kamera: `curl -X POST http://127.0.0.1:5000/stop_camera`

## Catatan Tambahan
-

## Kontribusi
-
