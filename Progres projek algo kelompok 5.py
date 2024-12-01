import pandas as pd
import csv
import os
from datetime import datetime
import time


def LaunchPage():
    os.system("cls") 
           
    Grafiti = '''
═════════════════════๑ஓஓ๑♡๑ஓ๑ஓ═══════════════════
                                                         
 ˚₊‧ ୨୧ ‧₊˚  	     SELAMAT DATANG       ˚₊‧ ୨୧ ‧₊˚         
                                                         
              ----------  DI  ----------                
                                                         
          █▀▀ █▀▀ █▀▀ █▀▀▄ █░░ █▀▀█ █▀▀█ █▀▀█           
          █▀▀ █▀▀ █▀▀ █░░█ █░░ █░░█ █░░█ █░░█           
          ▀░░ ▀▀▀ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀▀ █▀▀▀           
                                                         
 𖧷₊ Solusi Tepat untuk Pakan Ternak Berkualitas ₊𖧷    
                                                         
	             ≽^• ˕ • ྀི≼                         
                                                         
═════════════════════๑ஓஓ๑♡๑ஓ๑ஓ═══════════════════'''
    print(Grafiti)          
    print("\n#======================================================#")
    print("#           |                                |         #")
    print("#           |    Tekan Enter Untuk Lanjut    |         #")
    print("#           |                                |         #")
    print("#======================================================#")
    input("")
LaunchPage()


def buat_file():
    if not os.path.exists('daftar_pengguna.csv'):
        pd.DataFrame(columns=["Username", "Alamat", "Notelpn", "Password"]).to_csv('daftar_pengguna.csv', index=False)
    if not os.path.exists('stok_barang.csv'):
        pd.DataFrame(columns=["ID Produk", "Nama Produk", "Harga", "Stok", "status"]).to_csv('stok_barang.csv', index=False)
    if not os.path.exists('transaksi.csv'):
        pd.DataFrame(columns=["ID Transaksi", "ID Pembeli", "Tanggal", "Total", "status"]).to_csv('stok_barang.csv', index=False)
    if not os.path.exists('rekapitulasi.csv'):
        pd.DataFrame(columns=["ID Rekap", "Periode", "Total Penjualan", "Total Pendapatan"]).to_csv('rekapitulasi.csv', index=False)
    if not os.path.exists('pesanan.csv'):
        pd.DataFrame(columns=["ID Pesanan", "ID Pembeli", "Status", "Tanggal"]).to_csv('pesanan.csv', index=False)
    if not os.path.exists('notifikasi.csv'):
        pd.DataFrame(columns=["ID Notifikasi", "ID User", "Pesan", "Status", "Waktu"]).to_csv('notifikasi.csv', index=False)
    if not os.path.exists('keranjang.csv'):
        pd.DataFrame(columns=["ID Keranjang", "ID Pembeli", "ID Produk", "Jumlah"]).to_csv('keranjang.csv', index=False)
    if not os.path.exists('pembayaran.csv'):
        pd.DataFrame(columns=["ID Pembayaran", "ID Transaksi", "Metode", "Status", "Jumlah"]).to_csv('pembayaran.csv', index=False)
    if not os.path.exists('riwayat_pembelian.csv'):
        pd.DataFrame(columns=["ID Riwayat", "ID Pembeli", "ID Produk", "Tanggal", "Jumlah"]).to_csv('riwayat_pembelian.csv', index=False)

buat_file()


def main():
    os.system('cls')
    print('═════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ═══════════════════════')
    print('||----------- HAI! APA YANG AKAN KAMU LAKUKAN? -----------||')
    print('||                     1. LOGIN                           ||')
    print('||                     2. BUAT AKUN BARU                  ||')
    print('═════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ═══════════════════════')
    pilih = input("Masukkan pilihan anda: ")

    if pilih == '1':
        login()
    elif pilih == '2':
        buat_akun()
    else:
        keluar = input('Apakah anda ingin keluar dari aplikasi (ya/tidak)? ').lower()
        if keluar == 'ya':
            os.system('cls')
            print('Terima kasih telah menggunakan aplikasi FEEDLOOP!')
            print('                     BYE-BYE                     ')
        elif keluar == 'tidak':
            os.system('cls')
            main()
        else:
            print('jadi? anda ingin melakukan apa? ')


def buat_akun(): 
    os.system('cls')
    print('========== Hai! Ayo buat akun anda! ==========\n')
    pengguna = pd.read_csv('daftar_pengguna.csv')
    username = input('Masukkan username baru : ').strip().lower()
    alamat = input('Masukkan alamat anda : ').strip().lower()
    notelp = int(input('Masukkan no. telepon anda : '))
    password = input('Masukkan password baru : ').strip().lower()
    
    if username in pengguna['Username'].values:
        print('Username sudah ada! Gunakan username lain!')
        input('Enter untuk kembali')
        os.system('cls')
        buat_akun()
        return

    baru = {'Username' : username, 'Alamat' : alamat, 'NoTelpn' : notelp, 'Password' : password}
    pengguna = pd.concat([pengguna, pd.DataFrame([baru])], ignore_index=True)
    pengguna.to_csv('daftar_pengguna.csv', index=False)
    print('Akun berhasil dibuat!\n')
    input('Tekan enter untuk melanjutkan kr Log In ')
    os.system('cls')
    login()


def login():
    os.system('cls')
    # print('hai')
    print('==================== LOGIN ====================')
    print('             Ayo masuk ke akun anda!           \n')
    akun = pd.read_csv('daftar_pengguna.csv')
    username = input('Masukkan username : ').strip().lower()
    password = input('Masukkan password : ').strip().lower()

    if username == 'admin' in akun['Username'].values and password == 'sayaadmin123' in akun['Password'].values:
        print('\n============ Selamat datang Admin! ============')
        time.sleep(1)
        admin_menu()
    else:
        if username in akun['Username'].values:
            password_benar = akun.loc[akun['Username'] == username, 'Password'].values[0]
            if password == password_benar:
               print('\n============ Anda berhasil Log In! ============')
               print(f'============ Selamat datang {username}! ============')
               input('Enter untuk melanjutkan')
                # tampilan_pembeli
            else:
                print('Password yang anda masukkan salah!')
                input('Tekan enter untuk kembali melakukan login')
                login()
        else:
            print('Username tidak ditemukan!')
            input('Enter untuk kembali melakukan Login')
            login()


def baca_daftar_pengguna():
    try:
        return pd.read_csv('daftar_pengguna.csv')
    except FileNotFoundError:
        print("File daftar_pengguna.csv tidak ditemukan. Membuat file baru...")
        df = pd.DataFrame(columns=["Username", "Alamat", "Notelpn", "Password"])
        df.to_csv('daftar_pengguna.csv', index=False)
        return df


def admin_menu():
    os.system('cls')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ══════════════════════════')
    print('||----------------------- MENU ADMIN ----------------------||')
    print('||                      1.Lihat Stok Barang                ||')
    print('||                      2.Tambah Stok Barang               ||')
    print('||                      3.Lihat Data Transaksi             ||')
    print('||                      4.Lihat Rekapitulasi               ||')
    print('||                      5.Keluar                           ||')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ══════════════════════════')
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == "1":
        lihat_stok_barang()
    elif pilihan == "2":
        tambah_stok()
    elif pilihan == "3":
        lihat_data_transaksi()
    elif pilihan == "4":
        lihat_rekapitulasi()
    elif pilihan == "5":
        print("Keluar dari akun admin")
        input("Tekan enter untuk kembali ke menu utama...")
        main()
    else:
        print("Pilihan anda tidak valid")
        input("Tekan enter untuk kembali...")
        admin_menu()


def lihat_stok_barang():
    stok_barang = pd.read_csv('stok_barang.csv')
    os.system('cls')
    if stok_barang.empty:
        print("Belum ada stok barang.")
        input("Tekan enter untuk kembali ke menu admin...")
        admin_menu()
    else:
        print("\n========== STOK BARANG ==========")
        lihat = []
        with open('stok_barang.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                lihat.append(row)

        labels = lihat.pop(0)

        print(f'{labels[0]} \t {labels[1]} \t {labels[2]} \t\t {labels[3]} \t {labels[4]}')
        print('-'*50)
        for data in lihat:
            print(f'{data[0]} \t {data[1]} \t {data[2]} \t\t {data[3]} \t {data[4]}')
        input("Tekan enter untuk kembali ke menu admin...")
        admin_menu()


def tambah_stok():
    os.system('cls')
    print("========== TAMBAH STOK PRODUK ==========\n")
    tambah = pd.read_csv('stok_barang.csv')
    id_produk = int(input('Masukkan ID produk : '))
    nama_produk = input('Masukkan nama produk : ')
    harga = int(input('Masukkan harga : '))
    stok = int(input('Masukkan jumlah stok : '))
    status = input('Masukkan status barang (ada/tidak tersedia) : ')

    baru = {'id_produk' : id_produk, 'Nama' : nama_produk, 'Harga' : harga, 'Jumlah Stok' : stok, 'Status' : status}
    tambah = pd.concat([tambah, pd.DataFrame([baru])], ignore_index=True)
    tambah.to_csv('stok_barang.csv', index=False)
    print('Stok berhasil ditambahkan')

    lagi = input('Apakah anda ingin menambahkan stok barang lagi? (ya/tidak) ').lower()
    if lagi == 'ya':
        tambah_stok()
    else:
        admin_menu()


def lihat_data_transaksi():
    os.system('cls')
    print("\n========== LIHAT DATA TRANSAKSI ==========")
    try:
        transaksi = pd.read_csv('transaksi.csv')
        if transaksi.empty:
            print("Yah belum ada transaksi yang tercatat")
            input("Tekan enter untuk kembali ke menu admin...")
            admin_menu()
        else:
            print(transaksi)
    except FileNotFoundError:
        print("Mohon maaf data transaksi tidak tersedia")
        input("\n Tekan enter untuk kembali ke menu admin...")
        admin_menu()
        return


def lihat_rekapitulasi():
    os.system('cls')
    print("\n========== LIHAT REKAPITULASI PENJUALAN ==========")
    try:
       transaksi = pd.read_csv('transaksi.csv')
    except FileNotFoundError:
        print("Yah belum ada transaksi yang tercatat")
        input("\n Tekan enter untuk kembali ke menu admin...")
        admin_menu()
        return

    transaksi_selesai = transaksi[transaksi['status'] == "Selesai"]

    if transaksi_selesai.empty:
        print("Belum ada transaksi yang slesai")
        input("\n Tekan enter untuk kembali ke menu admin...")
        admin_menu()
        return
    
    print("Masukkan periode rekapitulasi dengan format (YYYY-MM-DD)")

    # while True:
    #     try:
    #         mulai = input("Tanggal mulai: ")
    #         selesai = input("Tanggal selesai: ")


def tampilan_pembeli():
    print('hai')


main()