# Tugas Kelompok - Pengolahan Sinyal Digital (PSD)
## Proyek: Deteksi Gerakan Objek pada Rekaman CCTV Menggunakan Pemrosesan Citra Digital

### Kelompok
- 442023611098 wafa bila syaefurokhman
- 442023611104 sabri mutiur rahman
- 442023611083 Nero Caesar Suprobo
- 442023611105 Mauludha Fiozaki
- 442023611089 Muhammad haekal
- 442023611091 Muhammad Abbas Al Badawi

### Deskripsi Singkat
Proyek ini merupakan bagian dari tugas kelompok pada mata kuliah Pengolahan Sinyal Digital. Tujuan utama dari proyek ini adalah menerapkan teknik pemrosesan sinyal/citra digital untuk mendeteksi dan menandai objek yang bergerak pada rekaman CCTV.

### Fitur Utama
- Membaca data video dari kamera CCTV atau file video.
- Konversi frame ke format grayscale untuk efisiensi pengolahan.
- Penerapan teknik perbedaan frame (frame differencing) untuk mendeteksi pergerakan.
- Prapemrosesan: thresholding, morfologi, dan segmentasi objek.
- Deteksi dan pelacakan objek menggunakan kontur.
- Visualisasi hasil dengan anotasi objek yang terdeteksi.

### File
- `cctv-psd.ipynb` – Notebook utama berisi kode dan visualisasi hasil.
- `README.md` – Deskripsi proyek.
- https://www.kaggle.com/datasets/suryaprabhakaran2005/road-accidents-from-cctv-footages-dataset – Dataset

### Kebutuhan Sistem
- Python ≥ 3.8
- OpenCV (`cv2`)
- NumPy
- Matplotlib (opsional, untuk visualisasi tambahan)
