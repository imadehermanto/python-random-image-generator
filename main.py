from PIL import Image
import requests
import os
from io import BytesIO
import sys
import concurrent.futures

# Fungsi untuk mengunduh gambar dari Lorem Picsum
def get_random_background(width, height):
    response = requests.get(f"https://picsum.photos/{width}/{height}")
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print("Error fetching background image:", response.status_code)
        return Image.new('RGB', (width, height), (255, 255, 255))  # Gambar putih sebagai fallback

# Membuat direktori untuk menyimpan gambar jika belum ada
output_dir = "random_banners"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Input ukuran banner dan jumlah gambar
width = int(input("Masukkan lebar banner (contoh: 3000): "))
height = int(input("Masukkan tinggi banner (contoh: 1000): "))
num_banners = int(input("Masukkan jumlah banner yang ingin dibuat: "))

def create_banner(i):
    background = get_random_background(width, height)
    banner = Image.new('RGB', (width, height))
    banner.paste(background.resize((width, height)))
    banner.save(f"{output_dir}/random_banner_{i+1}.png")

# Membuat banner dengan progress bar
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(create_banner, i) for i in range(num_banners)]
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        progress = (i + 1) / num_banners * 100
        sys.stdout.write(f"\rProgress: [{('=' * (i + 1))}{(' ' * (num_banners - (i + 1)))})] {progress:.2f}%")
        sys.stdout.flush()

print(f"\n{num_banners} random banners saved in '{output_dir}' directory.")
