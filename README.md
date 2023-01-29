# Python Project
Self-Serivice Cashier Program sederhana yang menggunakan bahasa pemrograman Python

# Latar Belakang Project
Andi membutuhkan sebuah Program Cashier untuk tokonya. Program Cashier tersebut nantinya akan dibuat menggunakan
Program Python dan bersifat Self-Service

# Tujuan Pengerjaan Project
1. Membuat Program Cashier sederhana yang dapat melakukan tugas
    - Membuat Transaksi ID
    - Memasukan Nama, Jumlah, dan Harga item yang akan dibeli
    - Membuat koreksi atas Nama/Jumlah/Harga item yang akan dibeli
    - Melakukan pembatalan terhadap pesanan yang telah dibuat
    - Melihat pesanan yang sudah dibuat oleh customer (Check Order)
    - Meng-outpu total pesanan yang dibuat 
    - Menerapkan diskon ke total pesanan berdasarkan kriteria yang ditentukan
2. Membuat Program dengan bahasa pemrograman Python 
3. Mengaplikasi pembuatan program yang berbasi fungsi (Function)
4. Mengaplikasi penulisan code yang bersih (Clean Code), mengacu pada PEP 8

# Fungsi yang akan digunakan di dalam Program Cashier
1. id_transaksi(): Fungsi ini akan digunakan untuk men-generate ID_Transaksi yang dibuat
2. title(): digunaka untuk membuat tampilan header
3. nama(): memiliki fungsi untuk meng-input nama pelanggan
4. belanjaan(): untuk customer meng-input nama barang, jumlah, dan harga belanjaan
5. belanjaan2(): berfungsi sebagai konfirmasi tambahan barang belanja (multiple item)
6. fungsi_keranjang(): digunakan untuk menggabungkan variable belanjaan menjadi dictionary 
7. keranjang_belanja(): fungsi ini akan men-display pesanan pelanggan
8. ganti_nama(): untuk mengganti nama barang belanjaan
9. ganti_jumlah(): memiliki fungsi untuk mengganti jumlah barang belanjaan
10. ganti_harga(): digunakan untuk mengganti harga belanjaan
11. hapus_barang(): berfungsi untuk menghapus barang belanjaan
12. tambah_barang(): akan digunakan untuk menambah barang belanjaan
13. konfirmasi_pesanan(): mengkonfirmasi kesesuaian pesanan / ingin mengubah pesanan
14. belanja_final(): menghitung total belanja setelah menerapkan suatu kriteria

# Deskripsi Task
1. Module 'Cashier.py' memuat variable - variable dan function yang digunakan untuk membuat program self-service Cashier

# Cara menggunakan Program
1. Download semua file/module Python kedalam suatu direktori lokal
2. Buka terminal dan sesuaikan lokasi direktori lokal
3. Jalankan module Python 'Cashier.py' di terminal
4. Jalankan kembali 'Cashier.py' di terminal untuk menjalankannya lagi

# Hasil Test Case
Test Case 1 : Menambahkan 2 item
1. Ayam Goreng Qty : 2 Harga : 20000
2. Pasta Gigi Qty : 3 Harga : 15000
![Test_Case1](https://github.com/farhanamrin/Cashier-Project/blob/main/Test%20Case%201.png?raw=true)
