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

# Alur Code Program 
1. Fase Pertama
Pada fase ini disimulasikan pembeli datang ke cashier dan melakukan self-checkout. Pembeli menginput nama, kemudian menginput barang, jumlah
dan harga belanjaan yang akan dibeli.

![fase_pertama](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/fase%20pertama.jpg?raw=true)

2. Fase Kedua
Pada fase ini diasumsikan pembeli sudah meng-input barang belanjaannya. Kemudian pembeli bisa memilih untuk melanjutkan prosess atau
membatalkan belanjaannya. 
Jika melanjutkan, pembeli daftar belanja akan di-display(output) untuk kemudian bisa diubah jika terjadi kesalahanpada belanjaannya. 

![fase_kedua](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/fase%20kedua.jpg?raw=true)

Jika memilih tidak melanjutkan, maka keranjang belanja akan dikosongkan.

![fase_kedua2](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/fase%20kedua%202.jpg?raw=true)

3. Fase Ketiga
Di fase ini, diasumsikan pembeli sudah mengubah kesalahan pada belanjanya. Kemudian pembeli memilih untuk melanjutkan ke proses pembayaran
yang akan menampikan total harga belanja setelah kalkulasi (PPN/Diskon). 

![fase_ketiga](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/fase%20ketiga.jpg?raw=true)

Pada fase ini, pembeli juga masih bisa menghapus atau mengubah belanjaan yang dibuat
![fase_ketiga2] (https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/fase%20ketiga.jpg?raw=true)

Jika pembeli memilih melanjutkan, akan diminta melakukan pembayaran. Nantinya akan di-display Id_transaksi beserta tanggal dan waktu
![pembayaran](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/pembayaran.jpg?raw=true)

# Fungsi yang akan digunakan di dalam Program Cashier
1. id_transaksi(): 
Fungsi ini akan digunakan untuk men-generate ID_Transaksi yang dibuat. Fungsi ini menggunakan module Random dan Date ID_Transaksi terdiri dari 6 random number,
4 random number tambahan, dan tanggal.

![id_transaksi](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Id%20Transaksi.jpg?raw=true)

2. title(): 
Digunaka untuk membuat tampilan header

![title](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Title.jpg?raw=true)

3. nama(): 
Memiliki fungsi untuk meng-input nama pelanggan dan nantinya akan di-display

![nama](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Nama.jpg?raw=true)

4. belanjaan(): 
Untuk customer meng-input nama barang, jumlah, dan harga belanjaan. Fungsi ini memiliki 3 parameter, paramameter Nama berupa string,
parameter Jumlah berupa integer, dan parameter Harga berupa Integer.

![belanjaan](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/Belanjaan.jpg?raw=true)

5. belanjaan2(): 
Berfungsi sebagai konfirmasi tambahan barang belanja (multiple item). Parameter dari fungsi ini hanya 2 (True/False)

![belanjaan2](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/belanjaan2.jpg?raw=true)

6. fungsi_keranjang(): 
Digunakan untuk menggabungkan variable belanjaan menjadi dictionary.

![fungsi_keranjang](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/fungsi%20keranjang.jpg?raw=true)

7. keranjang_belanja(): 
Fungsi ini akan men-display pesanan pelanggan

![keranjang_belanja](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/keranjang%20belanja.jpg?raw=true)

8. ganti_nama(): 
Untuk mengganti nama barang belanjaan jika terjadi kesalahan pada input. Fungsi ini memiliki 2 Parameter.
Parameter Nama_Lama berupa string, dan parameter Nama_Baru berupa string

![ganti_nama](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/ganti%20nama.jpg?raw=true)

9. ganti_jumlah(): 
Memiliki fungsi untuk mengganti jumlah barang belanjaan jika terjadi kesalahan pada input jumlah barang. Fungsi ini memiliki
2 parameter, parameter Nama_Barang berupa string, parameter Jumlah_Baru berupa integer

![ganti_jumlah](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/ganti%20jumlah.jpg?raw=true)

10. ganti_harga(): 
Memiliki fungsi untuk mengganti harga barang belanjaan jika terjadi kesalahan pada input harga barang. Fungsi ini memiliki
2 parameter, parameter Nama_Barang berupa string, parameter Harga_Baru berupa integer

![ganti_harga](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/ganti%20harga.jpg?raw=true)

11. hapus_barang(): 
Berfungsi untuk menghapus barang belanjaan. Fungsi ini menggunakan method .pop()

![hapus_barang](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/hapus%20barang.jpg?raw=true)

12. tambah_barang(): 
Fungsi ini digunakan untuk menambah barang belanjaan. Memiliki 3 parameter, yaitu Nama_Barang berupa string, Jumlah_Barang
berupa integer, dan Harga_Barang berupa integer

![tambah_barang](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/tambah%20barang.jpg?raw=true)

13. konfirmasi_pesanan(): 
Fungsi ini berguna untuk mengkonfirmasi kesesuaian pesanan / ingin mengubah pesanan Dengan Boolean (True/False)

![konfirmasi_pesanan](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/konfirmasi%20pesanan.jpg?raw=true)

Mengantisipasi jika jawaban yang di-input tidak sesuai dengan pilihan
![konfirmasi_pesanan](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/konfirmasi%20pesanan%202.jpg?raw=true)

14. belanja_final(): 
Menghitung total belanja setelah menerapkan suatu kriteria, berupa diskon yang nantinya akan mengurangi total harga belanjaan.
Menggunakan boolean (True/False) pada setiap kriteria

![belanja_final](https://github.com/farhanamrin/Cashier-Project/blob/main/Doc/belanja%20final.jpg?raw=true)

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
