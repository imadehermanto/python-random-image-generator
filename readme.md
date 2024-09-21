# Random Banner Generator

Repository ini berisi skrip Python untuk menghasilkan gambar banner acak menggunakan gambar dari Lorem Picsum. Skrip ini memungkinkan Anda untuk mengunduh gambar acak dengan ukuran yang ditentukan dan menyimpannya di direktori lokal. Penjelasan lengkap bisa dilihat di [medium.com](https://imadehermanto.medium.com/membuat-gambar-banner-acak-dengan-python-010be472d16b)

## Fitur

- Mengunduh gambar acak dari Lorem Picsum.
- Membuat beberapa gambar banner dalam satu proses.
- Menampilkan progress bar selama proses pembuatan gambar.

## Prerequisites

Pastikan Anda telah menginstal Python di komputer Anda. Selain itu, Anda perlu menginstal pustaka yang diperlukan dengan menjalankan:

```bash
pip install Pillow requests
```
## Cara Menggunakan
- Clone repository ini:
```
git clone https://github.com/imadehermanto/python-random-image-generator.git 
cd python-random-image-generator
``` 
- Jalankan skrip:
```
python3 main.py
```
- Masukkan ukuran banner dan jumlah gambar:
   - Masukkan lebar banner (contoh: 3000)
   - Masukkan tinggi banner (contoh: 1000)
   - Masukkan jumlah banner yang ingin dibuat
- Gambar banner acak akan disimpan di direktori `random_banners`.

## Struktur Direktori

```
.
├── main.py           # Skrip utama untuk menghasilkan gambar banner
└── random_banners/   # Direktori untuk menyimpan gambar yang dihasilkan
```

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka isu jika Anda menemukan bug.

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat [LICENSE](https://github.com/imadehermanto/python-random-image-generator/blob/main/LICENSE) untuk informasi lebih lanjut.