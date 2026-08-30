# CLI To-Do App

Aplikasi to-do list sederhana berbasis command line (CLI), dibuat menggunakan Python murni tanpa library eksternal. Ini adalah project pertama saya dalam roadmap belajar menuju Cloud Engineering.

## Fitur

- ✅ Tambah task baru
- ✅ Lihat semua task
- ✅ Tandai task sebagai selesai
- ✅ Hapus task
- ✅ Data tersimpan otomatis ke file (`tasks.json`), tidak hilang saat program ditutup

## Teknologi

- Python 3
- Modul `json` (bawaan Python, untuk penyimpanan data)

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstall di komputer kamu
2. Clone repository ini:

git clone https://github.com/nieshkhan/cli-todo-python.git

3. Masuk ke folder project:

cd Projek-2

4. Jalankan programnya:

python Main.py

5. Ikuti menu yang muncul di terminal untuk mulai menambah/mengelola task

## Cara Pakai

Setelah program berjalan, akan muncul menu:

1. Tambah
2. Lihat
3. Tandai Selesai
4. Hapus
5. Keluar

Ketik angka sesuai menu yang diinginkan, lalu ikuti instruksi selanjutnya.

## Apa yang Saya Pelajari

Project ini melatih dasar-dasar Python (function, list, dictionary, file I/O dengan JSON) sekaligus konsep penting seperti perbedaan variabel lokal vs global, konversi tipe data, dan alur program interaktif menggunakan while loop. Saya juga belajar dasar Git & GitHub untuk pertama kalinya — mulai dari commit, .gitignore, sampai push ke repository public.

## Rencana Pengembangan

- Tambahkan validasi input (misal: mencegah error kalau user memasukkan nomor task yang tidak ada)
- Tambahkan fitur edit task
- Migrasi penyimpanan dari file JSON ke database (SQLite)