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
1. id_transaksi(): 
Fungsi ini akan digunakan untuk men-generate ID_Transaksi yang dibuat. Fungsi ini menggunakan module Random dan Date ID_Transaksi terdiri dari 6 random number,
4 random number tambahan, dan tanggal.


2. title(): 
Digunaka untuk membuat tampilan header


3. nama(): 
Memiliki fungsi untuk meng-input nama pelanggan dan nantinya akan di-display


4. belanjaan(): 
Untuk customer meng-input nama barang, jumlah, dan harga belanjaan. Fungsi ini memiliki 3 parameter, paramameter Nama berupa string,
parameter Jumlah berupa integer, dan parameter Harga berupa Integer.


5. belanjaan2(): 
Berfungsi sebagai konfirmasi tambahan barang belanja (multiple item). Parameter dari fungsi ini hanya 2 (True/False)


6. fungsi_keranjang(): 
Digunakan untuk menggabungkan variable belanjaan menjadi dictionary.


7. keranjang_belanja(): 
Fungsi ini akan men-display pesanan pelanggan


8. ganti_nama(): 
Untuk mengganti nama barang belanjaan jika terjadi kesalahan pada input. Fungsi ini memiliki 2 Parameter.
Parameter Nama_Lama berupa string, dan parameter Nama_Baru berupa string


9. ganti_jumlah(): 
Memiliki fungsi untuk mengganti jumlah barang belanjaan jika terjadi kesalahan pada input jumlah barang. Fungsi ini memiliki
2 parameter, parameter Nama_Barang berupa string, parameter Jumlah_Baru berupa integer


10. ganti_harga(): 
Memiliki fungsi untuk mengganti harga barang belanjaan jika terjadi kesalahan pada input harga barang. Fungsi ini memiliki
2 parameter, parameter Nama_Barang berupa string, parameter Harga_Baru berupa integer


11. hapus_barang(): 
Berfungsi untuk menghapus barang belanjaan. Fungsi ini menggunakan method .pop()


12. tambah_barang(): 
Fungsi ini digunakan untuk menambah barang belanjaan. Memiliki 3 parameter, yaitu Nama_Barang berupa string, Jumlah_Barang
berupa integer, dan Harga_Barang berupa integer


13. konfirmasi_pesanan(): 
Fungsi ini berguna untuk mengkonfirmasi kesesuaian pesanan / ingin mengubah pesanan Dengan Boolean (True/False)


14. belanja_final(): 
Menghitung total belanja setelah menerapkan suatu kriteria, berupa diskon yang nantinya akan mengurangi total harga belanjaan.
Menggunakan boolean (True/False) pada setiap kriteria

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

![Test_Case1](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Test%20Case%201.jpg?raw=true)

Test Case 2 : Menghapus Item

![Test_Case2](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Test%20Case%202.jpg?raw=true)

Test Case 3 : Menghapus Keranjang

![Test_Case3](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Test%20Case%203.jpg?raw=true)

Test Case 4 : Menampilkan Output Belanjaan

![Test_Case4](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Test%20Case%204.jpg?raw=true)
