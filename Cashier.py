import random # Untuk membuat ID Transaksi
from datetime import date, datetime # Untuk mendisplay Waktu dan tanggal
# variable yang nantinnya akan digunakan
barang = []
jumlah = []
harga= []
keranjang_customer = []
tanggal = str(datetime.now())
hari = datetime.today().strftime('%A')

## Fungsi cashier yang akan digunakan

def id_transaksi(): # Fungsi untuk mmbuat ID-Transaksi
    ## generate ID-Number dengan menggunakan kombinasi random dan date module 
    nomor_transaksi = random.randint(0, 999999) 
    nomor_transaksi2 = random.randint(0, 9999)
    return f"{str(nomor_transaksi).zfill(6)}-{str(nomor_transaksi2).zfill(4)}.{date.today()}"
transaksi_id = id_transaksi()

# Berfungsi sebgai Header
def title(): 
    print('Toko Self-Service M.ANDIRI')
    print('*'*len('Toko Self-Service M.ANDIRI'))
    
# Fungsi untuk meng-input nama customer    
def nama(): 
    print('Selamat datang di Self-Service Toko M. ANDIRI')
    print("*"*len('Selamat datang di Self-Service Toko M. ANDIRI'))
    nama_customer = input('Masukin nama kamu dulu yuk ')
    print(f'Hallo, {nama_customer}')
    return nama_customer

# Fungsi untuk meng-input barang belanja
def belanjaan(): 
    print('') 
    ## Pembeli meng-input barang,jumlah,dan harga belanjaan
    print('*'*len('Silahkan Masukan Belanjaan kamu'))
    print('Silahkan Masukan Belanjaan kamu')
    print('*'*len('Silahkan Masukan Belanjaan kamu'))
    nama_barang = str(input('Nama Barang = ').upper())
   
    # Menggunakan loop untuk memastikan input integer
    while True: 
        jumlah_barang = input('Jumlah Barang = ')
        if jumlah_barang.isdigit() == False:
            print('Mohon masukan jumlah dengan benar... ')
        else:
            jumlah_barang = int(jumlah_barang)
            break
    while True: # Menggunakan loop untuk memastikan input integer
        harga_barang = input('Harga Barang = ')
        if harga_barang.isdigit() == False:
            print('Mohon masukan harga dengan benar... ')
        else:
            harga_barang = int(harga_barang)
            break
    ## element tersebut akan ditambah(.append) ke masing - masing list
    return barang.append(nama_barang), jumlah.append(jumlah_barang), harga.append(harga_barang), 

# Fungsi untuk konfirmasi item tambahan (multiple item)
def belanjaan2(): 
    print('Apakah masih ada lagi ?')
    jawaban = str(input('YA(Y) atau TIDAK(N)').upper())
    return jawaban

# Fungsi untuk proses penghitungan keranjang
def fungsi_keranjang(): 
## Menggabungkan lists belanja menjadi Dictionary dengan menggunakan zip method.
    jumlah_barang = dict(zip(barang, jumlah))
    harga_barang = dict(zip(barang, harga))
    sorted_harga = {i:harga_barang[i] for i in jumlah_barang.keys()}
    keys = jumlah_barang.keys()
    values = zip(jumlah_barang.values(), sorted_harga.values()) ##Menggunakan nama barang sebagai keys
    gabungan = dict(zip(keys, values)) ## jumlah dan harga menjadi values(list)
    return gabungan

# Fungsi untuk men-display keranjang belanja
def keranjang_belanja(): 
    print(' ')
    print('Keranjang Belanja Kamu')
    print('*'*len('Keranjang Belanja Kamu'))
    ## Untuk memasukan total harga ke Dictionary sebagai value
    for key, values in gabungan.items():
        total_harga = values[0] * values[1]
        gabungan.update({key : [values[0], values[1], total_harga]})
        ## Men-Display belanja customer
        print(f'Nama : {key} | Jumlah : {values[0]} | Harga : Rp.{values[1]:,} | Total : Rp.{total_harga:,}')

# Fungsi untuk menghitung dan men-display total belanja customer       
def total_belanja(): 
    keranjang_customer.clear()
    for key, value in gabungan.items():
        total_belanja_cust = value[2]
        keranjang_customer.append(total_belanja_cust)

# Fungsi Untuk mengganti nama barang belanja
def ganti_nama():
    # Menggunakan loop untuk mengantisipasi kesalahan input
    while True:
        daftar_nama = list(gabungan.keys())
        nama_lama = input('Nama barang yang ingin di ganti...(X) untuk BATAL.. ').upper()
        if nama_lama == 'X': ## Konfirmasi pembatalan ganti nama
            break
        elif nama_lama not in daftar_nama: ## Konfirmasi ketersediaan barng di keranjang
            print('Mohon maaf, barang tidak tersedia di keranjang anda.. ')
        else: ## Mengganti nama barang lama dengan yang baru
            nama_baru = input('Nama barang yang baru...').upper()
            gabungan[nama_baru] = gabungan[nama_lama]
            del gabungan[nama_lama]
            break

# Fungsi untuk Mengganti jumlah barang belanja
def ganti_jumlah():
    # Menggunakan loop untuk mengantisipasi kesalahan input
    while True:
        jumlah_lama = str(input('Nama barang yang ingin diganti jumlahnya..(X) untuk BATAL.. ').upper())
        daftar_nama = list(gabungan.keys())
        if jumlah_lama == 'X': ## Konfirmasi pergantian jumlah barang
            break
        elif jumlah_lama not in daftar_nama: ## Konfirmasi ketersediaan barng di keranjang
            print('Mohon maaf, barang tidak tersedia di keranjang anda..')
        else:
            while True: 
                jumlah_barang = input('Jumlah baru = ')
                if jumlah_barang.isdigit() == False: # Memastikan input integer
                    print('Mohon masukan jumlah dengan benar... ')
                else:
                    jumlah_baru = int(jumlah_barang)
                    break
            gabungan[jumlah_lama] = (jumlah_baru, int(gabungan.get(jumlah_lama)[1]))
            break

# Fungsi untukMengganti harga barang
def ganti_harga(): 
    while True:
        harga_lama = str(input('Nama barang yang ingin diganti harganya...(X) untuk BATAL.. ').upper())
        daftar_nama = list(gabungan.keys()) ## Konfirmasi pergantian harga
        if harga_lama == 'X':
            break
        ## Konfirmasi ketersediaan barng di keranjang
        elif harga_lama not in daftar_nama: 
            print('Mohon maaf, barang tidak tersedia di keranjang anda..')
        else:
            # Memastikan input integer
            while True:
                harga_barang = input('Harga baru = ')
                if harga_barang.isdigit() == False: 
                    print('Mohon masukan harga dengan benar... ')
                else:
                    harga_baru = int(harga_barang)
                    break
            gabungan[harga_lama] = (int(gabungan.get(harga_lama)[0]), harga_baru)
            break

# Fungsi untuk Menghapus barang belanja
def hapus_barang(): 
    while True:
        daftar_nama = list(gabungan.keys())
        nama_barang = str(input('Nama barang yang ingin di hapus (X) untuk BATAL ').upper())
        if nama_barang == 'X':## Konfirmasi hapus barang
            break
        elif nama_barang not in daftar_nama:  ## Konfirmasi ketersediaan barng di keranjang
            print('Mohon maaf, barang tidak tersedia di keranjang anda..')
        else:
            del gabungan[nama_barang] ## Mengapus barang dari keranjang
            break

# Fungsi untuk Menambah barang ke keranjang
def tambah_barang(): 
    while True:
        barang_baru = input('Masukan nama barang ....(X) untuk BATAL ').upper()
        if barang_baru == 'X': ## Konfirmasi menambah barang
            break
        
        ## Meng-input nama, harga, dan jumlah barang baru
        else: 
            # Memastikan input integer
            while True:
                harga_barang_baru = input('Harga barang = ')
                if harga_barang_baru.isdigit() == False: 
                    print('Mohon masukan harga dengan benar... ')
                else:
                    harga_barang_baru = int(harga_barang_baru)
                    break
            
            # Memastikan input integer
            while True:
                jumlah_baru = input('Jumlah barang = ')
                if jumlah_baru.isdigit() == False: 
                    print('Mohon masukan jumlah dengan benar... ')
                else:
                    jumlah_baru = int(jumlah_baru)
                    break
            
            # Menghitung total harga barang baru
            total_harga = (jumlah_baru, harga_barang_baru, jumlah_baru * harga_barang_baru, )
            gabungan[barang_baru] = total_harga
            break

# Fungsi Untuk Konfirmasi keranjang belanja
def konfirmasi_pesanan(): 
    ## Menggunakan While Loop untuk mengantisipasi adanya kesalahan belanja lebih dari satu
    while True:
        total_belanja()
        jawaban_koreksi = str(input('Apakah belanjaan kamu sudah benar ?(Y/N) ')).upper()
        if jawaban_koreksi == 'N': ## Konfirmasi adanya kesalahan pada keranjang
            keranjang_belanja()
            title()
            print('Pilih bagian yang salah ') ## Melihat letak kesalaha pada keranjang belanja
            kesalahan = str(input('Nama/Jumlah/Harga/Tambah/Hapus..masukan(X) untuk Lanjut/Batalkan Proses ini.. ')).upper()
            ## Kesalahan pada NAMA barang
            if kesalahan == 'NAMA': 
                jawaban_koreksi = ganti_nama() 
                keranjang_belanja()
            ## Kesalahan pada Jumlah barang
            elif kesalahan == 'JUMLAH':
                jawaban_koreksi = ganti_jumlah()
                keranjang_belanja()
            ## Kesalahan pada Harga barang
            elif kesalahan == 'HARGA':
                jawaban_koreksi = ganti_harga()
                keranjang_belanja()
            ## Menambah barang pada pesanan
            elif kesalahan == 'TAMBAH':
                tambah_barang()
                fungsi_keranjang()
                keranjang_belanja()
            ## Membatalkan/Menghapus pesanan
            elif kesalahan == 'HAPUS':
                hapus_barang()
                keranjang_belanja()
            
            elif kesalahan == 'X': ## Antisipasi untuk pembatalan prosess
                continue

            else:
                print('Mohon masukan jawaban sesuai dengan pilihan yang tersedia.....')

        elif jawaban_koreksi == 'Y': ## Konfirmasi sudah tidak ada kesalahan
            print(f'Total belanja kamu adalah Rp.{sum(keranjang_customer):,} belum termasuk PPN/Potongan')
            break

        else: ## antisipasi jika input tidak sesuai dengan yang diminta
            print('Mohon masukan jawaban dengan Y(IYA)/N(TIDAK) ')

# Fungsi untuk Menghitung total belanja setelah diskon (jika termasuk)            
def belanja_final():
    total_keranjang_customer = int(sum(keranjang_customer))
    ## Belanja diatas 500_000 diskon 10%
    if  total_keranjang_customer >= 500_000:
        besar_diskon = int(total_keranjang_customer * (10/100))
        total_pembelian = total_keranjang_customer * (90/100)
        ## Men-display besar diskon yang didapatkan
        print(f'Selamat {nama_pembeli}, belanja kamu mendapatkan diskon sebesar 10% Rp. {besar_diskon:,}')
    
    ## Belanja diatas 300_000 diskon 8%
    elif total_keranjang_customer >= 300_000: 
        besar_diskon = int(total_keranjang_customer * (8/100))
        total_pembelian = total_keranjang_customer * (92/100)
        ## Men-display besar diskon yang didapatkan
        print(f'Selamat {nama_pembeli}, belanja kamu mendapatkan diskon sebesar 8% Rp. {besar_diskon:,}')
    
    ## Belanja diatas 200_000 diskon 5%
    elif total_keranjang_customer >= 200_000: 
        besar_diskon = int(total_keranjang_customer * (5/100))
        total_pembelian = total_keranjang_customer * (95/100)
        ## Men-display besar diskon yang didapatkan
        print(f'Selamat {nama_pembeli}, belanja kamu mendapatkan diskon sebesar 5%Rp. {besar_diskon:,}')
    
    ## Belanja dibawah 200_000 tidak mendapat diskon
    elif total_keranjang_customer <= 199_999:
        total_pembelian = total_keranjang_customer
        print(f'Mohon maaf, kamu belum bisa mendapatkan diskon')
        print(' ')
    return total_pembelian ## Akan digunakan untuk melakukan penghitungan pebayaran


''' 
Fase Pertama
Di fase ini pembeli akan menginput barang belanja yang dibeli menggunakan function belanjaan()
kemudian, di fase ini akan mengeluarkan output berupa daftar tabel transaksi
'''
# MengInput nama pembeli
nama_pembeli = nama()
print('')
belanjaan() # Menjalankan fungsi belanjaan

# Me-loop fungsi belanjaan() (Jika terdapat lebih dari satu item yang akan di-input)
while True: 
    jawaban = belanjaan2() 
    if jawaban == 'Y':
        belanjaan()
        continue
    elif jawaban == 'N':
        break
    elif jawaban != 'Y' or 'N':
        print('Mohon masukan jawaban dengan benar...')

# Variable gabungan digunakan sebagai tempat menjalankan fungsi keranjang(dictionary)
gabungan = fungsi_keranjang()

# Men-display item - item yang ada pada keranjang (dict gabungan)
print(' ')
keranjang_belanja()
total_belanja()
print(f'Total belanja kamu adalah Rp.{sum(keranjang_customer):,}')


''' 
Fase Kedua
Di fase ini pembeli meng-input pilihan untuk melanjutkan proses atau menghentikan proses
jika melanjutkan proses, pembeli meng-update pesanannya. Jika batal proses akan berakhir
'''
## me-loop pertanyaan untuk antisipasi pembatalan hapus pesanan.
while True: 
    lanjut_proses = str(input('Lanjutkan proses belanja...(Y) atau batalkan belanja(X) ').upper())
    
    # Jika pembeli memutuskan melanjutkan proses belanja 
    if lanjut_proses == 'Y':  
        keranjang_belanja()
        # Menjalankan fungsi_konfirmasi_pesanan untuk mengecek keranjang belanja
        konfirmasi_pesanan() 
        break
    
    # Mengakhiri proses pesanan.
    elif lanjut_proses == 'X': 
        # Konfirmasi pembatalan
        batalkan_pesanan = str(input('Keranjang akan Kami kosongkan ...IYA(Y) atau tidak jadi BATAL(N)? ').upper())
        
        # Jika tidak jadi melanjutkan proses pembatalan belanja dijalankan 
        if batalkan_pesanan == 'N':
            ## Kembali pada proses konfirmasi pesanan
            keranjang_belanja()
            konfirmasi_pesanan()
            break
        
        # Jika melanjutkan proses pembatalan   
        elif batalkan_pesanan == 'Y':
            ## Variable gabungan(keranjang belanja) akan dihapus(clear)
            gabungan.clear() 
            print(' ')
            print('Terima kasih telah berkunjung ke TOKO SELF-SERVICE M.ANDIRI')
            print(hari, tanggal[0:len('2023-01-23 01:17:38')])
            break
        ## Pesan untuk kesalahan input pada loop    
        else:
            print('Mohon masukan jawaban dengan benar(Y/N)...')
    
    # mem-break loop pertanyaan, dan mengakhiri proses       
        break
    
    # Pesan jika adanya kesalahan input pada loop
    else:
        print('Mohon masukan jawaban dengan benar....')
        print('Masukan Y jika ingin melanjutkan belanja atau X jika ingin MEMBATALKAN pesanan ')
        

''' 
Fase Ketiga
Di fase ini pesanan Pembeli bisa mengubah atau menghapus pesanan sebelum melanjutkan ke proses pembayaran
Kemudian pembeli meng-input jumlah pembayaran, dan output transaksi akan ditampilkan
'''
# Untuk melihat kelanjutan proses transaksi (jika kosong maka tidak melanjutkan)
if len(gabungan) != 0:
    # Menjalankan function keranjang_belanja untuk output daftar pesanan
    keranjang_belanja()
    print(f'Total belanja kamu adalah Rp.{sum(keranjang_customer):,} belum termasuk PPN/Potongan')
    
    # Loop Konfirmasi untuk melanjutkan proses
    while True:
        print('Melanjutkan ke proses pembayaran....') 
        konfirmasi_belanja = str(input('Melanjutkan...?(Y/N) ').upper())
        
        # Menjalankan function belanja_final untuk menghitung total pesanan
        if konfirmasi_belanja == 'Y':
            keranjang_belanja()
            total_pembelian = belanja_final()
            
            # Menambah PPN ke total pesanan
            besar_belanja_customer = int(total_pembelian + (total_pembelian*(11/100)))
            print(f'Total belanja kamu sebesar Rp. {besar_belanja_customer:,}, (termasuk PPN 11%)')
            print(' ')
            break
            
        # Konfirmasi Mengubah/Menghapus pesanan
        elif konfirmasi_belanja == 'N': 
            konfirmasi_customer = str(input('Ubah Pesanan(Y)/Hapus Pesanan(N) ').upper())
            if konfirmasi_customer == 'N':
                
                # Menghapus(clear) variable gabungan(keranjang belanja)
                gabungan.clear() 
                print(' ')
                title()
                print('Sampai Kembali Lagi')
                print(hari, tanggal[0:len('2023-01-23 01:17:38')])
                break
            
           # Mengubah pesanan
            elif konfirmasi_customer =='Y':
                 # Menjalankan function keranjang_belanja dan konfirmasi_pesanan 
                keranjang_belanja()
                konfirmasi_pesanan()
                continue

# Untuk melihat kelanjutan proses transaksi (jika kosong maka tidak melanjutkan)               
if len(gabungan) != 0:
    ## Me-loop input uang pembeli untuk antisipasi pembayaran tidak sesuai
    while True:
        
        # Loop input pembayaran Memastikan input berupa integer
        while True: 
            uang_customer = input('Tolong Masukan Uang Kamu.. ')
            if uang_customer.isdigit() == False:
                print('Mohon masukan jumlah dengan benar... ')  
            else:
                uang_customer = int(uang_customer)
                break
        
        # Menghitung jumlah kembalian pembeli
        kembalian = int(uang_customer - besar_belanja_customer)
        # Meng-output kembalian pembeli serta menjalankan function transaksi_id
        if uang_customer > besar_belanja_customer:
            print(f'Pembayaran sebesar Rp.{uang_customer:,} dan total belanja sebesar Rp.{besar_belanja_customer:,}')
            print(f'Kembalian sebesar Rp.{kembalian:,}')
            print(' ')
            print('Terima kasih telah berbelanja di Toko Self-serfice M.ANDIRI')
            print('*'*len('Toko Self-Service M.ANDIRI'))
            print(f'ID TRANSAKSI : {transaksi_id}')
            print(hari, tanggal[0:len('2023-01-23 01:17:38')])
            break
        
        # Meng-output pesan jika pembayaran tidak sesuai
        elif uang_customer < besar_belanja_customer:
            print('Mohon maaf, uang kamu tidak cukup..')