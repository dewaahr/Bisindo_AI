# Tugas untuk Kelas Kecerdasan Buatan UKDW
## AI Bisindo Sign Language App

Aplikasi ini adalah aplikasi yang menggunakan kecerdasan buatan (artificial intelligence/AI) untuk mendeteksi dan menerjemahkan Bahasa Isyarat Indonesia (BISINDO). Aplikasi ini memanfaatkan model deteksi objek YOLOv5 untuk mendeteksi tanda-tanda bahasa isyarat dari gambar atau video yang diberikan.

## Daftar Isi
- [Syarat](#syarat)
- [Tutorial Instalasi](#tutorial-instalasi)
- [Penggunaan dengan Flask](#penggunaan-dengan-flask)
- [Penggunaan Tanpa GUI](#penggunaan-tanpa-gui)
- [Endpoint](#endpoint)
- [Contoh Mengontrol Kamera](#contoh-mengontrol-kamera)
- [Catatan Tambahan](#catatan-tambahan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

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
    cd Bisindo_AI
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
1. Jalankan source code dengan perintah `python app.py`.
2. Buka browser dan buka alamat `http://127.0.0.1:5000/` untuk melihat hasil deteksi objek secara real-time.

## Penggunaan Tanpa GUI
1. Jalankan kode dengan perintah `python camera_detection.py`.
2. Jendela video akan muncul dan menampilkan hasil deteksi objek secara real-time.
3.  `q` untuk menghentikan program.

## Endpoint
- **`POST /start_camera`**: Memulai webcam.
- **`POST /stop_camera`**: Menghentikan webcam.

## Contoh Mengontrol Kamera
- Memulai Kamera: 
    ```sh
    curl -X POST http://127.0.0.1:5000/start_camera
    ```
- Menghentikan Kamera:
    ```sh
    curl -X POST http://127.0.0.1:5000/stop_camera
    ```

## Catatan Tambahan
- Model Dilatih menggunakan YOLOv5.
- `https://github.com/ultralytics/yolov5` 

## Kontribusi
-

