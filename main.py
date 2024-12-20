import pandas as pd
import csv
import os
from datetime import datetime
import time
from tabulate import tabulate

Username = None

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
        pd.DataFrame(columns=["Username", "Alamat", "Notelpn", "Password"]).to_csv('daftar_pengguna.csv', index=False) #index=False dipakai ketika kita menyimpan DataFrame (tabel data) ke file CSV agar tidak menyertakan kolom index ke dalam file tersebut.
    if not os.path.exists('stok_barang.csv'):
        pd.DataFrame(columns=["ID Produk", "Nama Produk", "Harga", "Stok", "status"]).to_csv('stok_barang.csv', index=False)
    if not os.path.exists('keranjang.csv'):
        pd.DataFrame(columns=['Username', "ID Produk", "Jumlah"]).to_csv('keranjang.csv', index=False)
    if not os.path.exists('riwayat_pembelian.csv'):
        pd.DataFrame(columns=["ID Riwayat", 'Username', "Tanggal", "Total pengeluaran"]).to_csv('riwayat_pembelian.csv', index=False)
    if not os.path.exists('detail_pembelian.csv'):
        pd.DataFrame(columns=["ID Riwayat", "Nama Produk", "Harga", "Jumlah", "Total"])
    
buat_file()


def main():
    os.system('cls')
    print('═════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ═══════════════════════')
    print('||----------- HAI! APA YANG AKAN KAMU LAKUKAN? -----------||')
    print('||                     1. LOGIN                           ||')
    print('||                     2. BUAT AKUN BARU                  ||')
    print('||                     3. KELUAR                          ||')
    print('═════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ═══════════════════════')
    pilih = input("Masukkan pilihan anda: ")

    if pilih == '1':
        login()
    elif pilih == '2':
        buat_akun()
    elif pilih == '3':
        keluar = input(
            'Apakah anda ingin keluar dari aplikasi (ya/tidak)? ').lower()
        if keluar == 'ya':
            os.system('cls')
            logout()
        elif keluar == 'tidak':
            os.system('cls')
            main()


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

    baru = {
        'Username': username,
        'Alamat': alamat,
        'Notelpn': notelp,
        'Password': password
    }
    pengguna = pd.concat([pengguna, pd.DataFrame([baru])], ignore_index=True)# digunakan ketika kita menggabungkan atau mengubah data di pandas agar nomor index diatur ulang dari awal. Ini memastikan nomor index baru berurutan tanpa peduli dari mana asal datanya.
    pengguna.to_csv('daftar_pengguna.csv', index=False)
    print('Akun berhasil dibuat!\n')
    input('Tekan enter untuk melanjutkan ke Log In ')
    os.system('cls')
    login()


def login():
    global Username
    os.system('cls')
    print('==================== LOGIN ====================')
    print('             Ayo masuk ke akun anda!           \n')
    akun = pd.read_csv('daftar_pengguna.csv')
    username = input('Masukkan username : ').strip().lower()
    password = input('Masukkan password : ').strip().lower()

    if username == 'admin' and password == 'sayaadmin123':
        print('\n============ Selamat datang Admin! ============')
        time.sleep(1)
        admin_menu()
    else:
        if username in akun['Username'].values:
            password_benar = akun.loc[akun['Username'] == username, 
                                      'Password'].values[0]
            if password == password_benar:
                Username = username
                print('\n=========== Anda berhasil Log In! ===========')
                print(f'============ Selamat datang {username}! ============')
                input('\nTekan enter untuk melanjutkan')
                tampilan_pembeli()
            else:
                print('Password yang anda masukkan salah!')
                input('Tekan enter untuk kembali melakukan login')
                login()
        else:
            print('Username tidak ditemukan!')
            input('Enter untuk kembali melakukan Login')
            login()


def admin_menu():
    os.system('cls')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ════════════════════════')
    print('||----------------------- MENU ADMIN ----------------------||')
    print('||                   1. Lihat Stok Barang                  ||')
    print('||                   2. Tambah Stok Barang                 ||')
    print('||                   3. Hapus Barang                       ||')
    print('||                   4. Lihat Data Transaksi               ||')
    print('||                   5. Status Pengiriman Admin            ||')
    print('||                   6. Lihat Daftar Pengguna              ||')
    print('||                   7. Keluar                             ||')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ════════════════════════')
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == "1":
        lihat_stok_barang()
    elif pilihan == "2":
        tambah_stok()
    elif pilihan == "3":
        hapus_barang()
    elif pilihan == "4":
        lihat_data_transaksi()
    elif pilihan == "5":
        status_pengiriman_admin()
    elif pilihan == "6":
        lihat_pengguna()
    elif pilihan == "7":
        print("Keluar dari akun admin")
        input("Tekan enter untuk kembali ke menu utama...")
        main()
    else:
        print("Pilihan anda tidak valid")
        input("Tekan enter untuk kembali...")
        admin_menu()


def lihat_stok_barang():
    os.system('cls')
    stok_barang = pd.read_csv('stok_barang.csv')
    
    if stok_barang.empty:
        print("Belum ada stok barang.")
        input("Tekan enter untuk kembali ke menu admin...")
        admin_menu()
    else:
        print('\n ======================= Daftar Produk =======================\n')
        print(tabulate(stok_barang.values, headers=stok_barang.columns, tablefmt="grid"))

    input("\nTekan enter untuk kembali ke menu admin...")
    admin_menu()


def tambah_stok():
    os.system('cls')
    print("===================== TAMBAH STOK PRODUK =====================\n")
    tambah = pd.read_csv('stok_barang.csv')
    if tambah.empty:
        print("Belum ada stok barang yang tercatat")
    else:
        print('\n ======================= Daftar Produk =======================\n')
        print(tabulate(tambah.values, headers=tambah.columns,tablefmt="grid"))
    
    print("\nMasukkan data poduk : ")
    id_produk = int(input('Masukkan ID produk : '))
    stok = int(input('Masukkan jumlah stok : '))

    if id_produk in tambah['ID Produk'].values:
        tambah.loc[tambah['ID Produk'] == id_produk, 'Stok'] += stok
        tambah.loc[tambah['Stok'] > 0, 'status'] = 'ada'
        print(f"Jumlah stok produk {id_produk} berhasil diperbarui!")
    else:
        nama_produk = input('Masukkan nama produk : ')
        harga = int(input('Masukkan harga : '))
        status = input('Masukkan status barang (ada/tidak tersedia) : ')
        
        baru = {
            'ID Produk': id_produk,
            'Nama Produk': nama_produk,
            'Harga': harga,
            'Stok': stok,
            'status': status
        }
        tambah = pd.concat([tambah, pd.DataFrame([baru])], ignore_index=True)
        tambah.to_csv('stok_barang.csv', index=False)
        print('Stok produk baru berhasil ditambahkan!')

    tambah.to_csv('stok_barang.csv', index=False)

    lagi = input(
        'Apakah anda ingin menambahkan stok barang lagi? (ya/tidak) ').lower()
    if lagi == 'ya':
        tambah_stok()
    else:
        admin_menu()


def hapus_barang():
    stok_barang = pd.read_csv('stok_barang.csv')
    os.system('cls')
    if stok_barang.empty:
        print("Belum ada stok barang.")
        input("Tekan enter untuk kembali ke menu admin...")
        admin_menu()
    else:
        print(
            '\n ======================= Daftar Produk =======================\n'
        )
        
        print(tabulate(stok_barang.values, headers=stok_barang.columns, tablefmt="grid"))

    id_produk = input('Masukkan ID produk yang ingin dihapus : ')

    try:
        id_produk = int(id_produk)
    except:
        print(
            'ID Produk tidak sesuai! pastikan ID Produk yang anda masukkan adalah Integer'
        )
        input('Tekan enter untuk kembali ke menu admin')
        admin_menu()

    if id_produk not in stok_barang['ID Produk'].values.tolist():
        print(
            'ID Produk tidak ditemukan! pastikan ID Produk yang anda masukkan benar'
        )
        input('Tekan enter untuk kembali ke menu admin')
        admin_menu()

    stok_barang = stok_barang[stok_barang['ID Produk'] != id_produk]
    stok_barang.to_csv('stok_barang.csv', index=False)
    print('Data Berhasil dihapus')
    input('Tekan enter untuk kembali ke menu admin')
    admin_menu()


def lihat_data_transaksi():
    os.system('cls')
    print("\n========== LIHAT DATA TRANSAKSI ==========")
    riwayat_pembelian = pd.read_csv('riwayat_pembelian.csv')
    detail_pembelian = pd.read_csv('detail_pembelian.csv')
    if riwayat_pembelian.empty:
        print("Belum ada transaksi yang tercatat")
        input("Tekan enter untuk kembali ke menu admin...")
        admin_menu()
    else:
        print(tabulate(riwayat_pembelian.values, headers=riwayat_pembelian.columns, tablefmt="grid"))
        print('Note: input 0 untuk kembali ke menu utama, input id_riwayat untuk melihat detail pembelian')
        pilih = input('Input ID Riwayat : ')
        try:
            pilih = int(pilih)
        except:
            print('ID Riwayat tidak sesuai! pastikan ID Riwayat yang anda masukkan integer')
            input("Tekan enter untuk kembali ke menu utama...")
            admin_menu()
        if pilih == 0:
            admin_menu()
        else:
            if pilih in riwayat_pembelian['ID Riwayat'].values:
                pembelian_detail = detail_pembelian[detail_pembelian['ID Riwayat'] == pilih]
                print(tabulate(pembelian_detail.values, headers=pembelian_detail.columns, tablefmt="grid"))
                input("Tekan enter untuk kembali ke riwayat transaksi")
                lihat_data_transaksi()
            else:
                print('ID Riwayat tidak ditemukan!\nPastikan ID Riwayat sesuai dengan yang tertera di tabel riwayat')
                input("Tekan enter untuk kembali ke riwayat transaksi")
                lihat_data_transaksi()


def status_pengiriman_admin():
    os.system('cls')
    try:
        pengiriman = pd.read_csv('riwayat_pengiriman.csv')
    except FileNotFoundError:
        pengiriman = pd.DataFrame(columns=['ID Riwayat', 'Username', 'Total Pembelian', 'Status'])

    print("\nDaftar status pengiriman")
    if pengiriman.empty:
        print("Belum ada data pengiriman tersedia.")
        input("Tekan enter untuk kembali...")
        return
    
    print(tabulate(pengiriman.values, headers=pengiriman.columns, tablefmt="grid"))
    print("\nOpsi")
    print("1. Pembaruan status pengiriman")
    print("2. Kembali")

    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        id_riwayat = input("\nMasukkan ID Riwayat yang ingin diperbarui: ")

        if id_riwayat not in pengiriman ['ID Riwayat'].astype(str).values:
            print("ID Riwayat tidak ditemukan.")
            input("Tekan enter untuk kembali...")
            return
        
        print("\nStatus Baru: ")
        print("1. Diproses")
        print("2. Dikirim")
        print("3. Selesai")
        Pilihan_status = input("Masukkan status baru(1/2/3): ")

        if Pilihan_status == "1":
            status_baru = "Diproses"
        elif Pilihan_status == "2":
            status_baru = "Dikirim"
        elif Pilihan_status == "3":
            status_baru = "Selesai"
        else:
            print("Pilihan tidak valid.")
            input("Tekan enter unuk kembali")
            return
        
        pengiriman.loc[pengiriman['ID Riwayat'].astype(str) == id_riwayat, 'Status'] = status_baru
        pengiriman.to_csv('riwayat_pengiriman.csv', index=False)
        print("Status pengiriman berhasil diperbarui.")
        input("Tekan enter untuk kembali...")
        admin_menu()
    elif pilihan == "2":
        admin_menu()
    else:
        print("Pilihan tidak valid")
        input("Tekan enter untuk kembali...")
        admin_menu()


def lihat_pengguna():
    os.system('cls')
    daftar_pengguna = pd.read_csv('daftar_pengguna.csv')
    
    if daftar_pengguna.empty:
        print("Belum ada daftar pengguna.")
        input("\nTekan enter untuk kembali ke menu admin...")
        admin_menu()
    else:
        if 'Password' in daftar_pengguna.columns:
            daftar_pengguna = daftar_pengguna.drop(columns=['Password'])

        print(
            '\n================= Daftar Pengguna =================\n'
        )
        print(tabulate(daftar_pengguna.values, headers=daftar_pengguna.columns, tablefmt="grid"))

    input("\nTekan enter untuk kembali ke menu admin...")
    admin_menu()


def tampilan_pembeli():
    os.system('cls')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ══════════════════════════')
    print('||---------------------- MENU PEMBELI ---------------------||')
    print('||                   1. Lihat Daftar Barang                ||')
    print('||                   2. Cari Barang                        ||')
    print('||                   3. Tambah ke Keranjang                ||')
    print('||                   4. Lihat Keranjang                    ||')
    print('||                   5. Reset Keranjang                    ||')
    print('||                   6. Transaksi                          ||')
    print('||                   7. Status Pengiriman Pembeli          ||')
    print('||                   8. Riwayat Pembelian                  ||')
    print('||                   9. Keluar                             ||')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ══════════════════════════')
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == '1':
        lihat_daftar_barang_pemb()
    elif pilihan == '2':
        cari_barang()
    elif pilihan == '3':
        tambah_keranjang()
    elif pilihan == '4':
        lihat_keranjang()
    elif pilihan == '5':
        reset_keranjang()
    elif pilihan == '6':
        transaksi()
    elif pilihan == '7':
        status_pengiriman_pemb()
    elif pilihan == "8":
        riwayat()
    elif pilihan == '9':
        print("Anda akan keluar dari menu pembeli...")
        time.sleep(2)
        main()
    else:
        print("Pilihan anda tidak valid")
        input("Tekan enter untuk kembali...")
        tampilan_pembeli()


def lihat_daftar_barang_pemb():
    os.system('cls')
    stok_barang = pd.read_csv('stok_barang.csv')

    stok_barang.loc[stok_barang['Stok'] == 0, 'status'] = 'habis'
    stok_barang.to_csv('stok_barang.csv', index=False)

    if stok_barang.empty:
        print("Belum ada stok barang.")
        input("Tekan enter untuk kembali ke menu utama...")
        tampilan_pembeli()
    else:
        print('\n ======================= Daftar Produk =======================\n')
        lihat = []
        with open('stok_barang.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                lihat.append(row)

        labels = lihat.pop(0)
        print(tabulate(lihat, headers=labels, tablefmt="grid"))
    input("\nTekan enter untuk kembali ke menu utama...")
    tampilan_pembeli()


def cari_barang():
    stok_barang = pd.read_csv('stok_barang.csv')
    
    print('1. Cari berdasarkan nama produk')
    print('2. Cari berdasarkan status produk')
    pilih = input('Ingin mencari berdasarkan? ')

    if pilih == '1':
        
        sn = input('Cari : ')
        barang_dicari = stok_barang[stok_barang['Nama Produk'] == sn]
        if barang_dicari.empty:
            print("\nBarang yang Anda cari tidak ditemukan!")
        else:
            print("\nBarang yang akan Anda cari:")
            print(tabulate(barang_dicari.values, headers=barang_dicari.columns, tablefmt="grid"))
        
    elif pilih == '2':
        print('Status : ada/habis')
        ss = input('cari : ')
        status_dicari = stok_barang[stok_barang['status'] == ss]
        if status_dicari.empty:
            print("\nBarang yang Anda cari tidak ditemukan!")
        else:
            print("\nBarang yang akan Anda cari:")
            print(tabulate(status_dicari.values, headers=status_dicari.columns, tablefmt="grid"))

    input("\nTekan enter untuk kembali ke menu utama...")
    tampilan_pembeli()


def tambah_keranjang():
    os.system('cls')
    global Username
    
    stok_barang = pd.read_csv('stok_barang.csv')
    
    if stok_barang.empty:
        print("Belum ada stok barang.")
        input("Tekan enter untuk kembali ke menu utama...")
        tampilan_pembeli()
    else:
        print(
            '\n ======================= Daftar Produk =======================\n'
        )
        print(tabulate(stok_barang.values, headers=stok_barang.columns, tablefmt="grid"))
        
    pil_ID = input('Pilih ID Produk : ')
    try:
        pil_ID = int(pil_ID)
    except:
        print(
            'ID Produk tidak sesuai! pastikan ID Produk yang anda masukkan adalah Integer'
        )
        input('Tekan enter untuk kembali ke menu utama')
        tampilan_pembeli()
    
    if pil_ID not in stok_barang['ID Produk'].values.tolist():
        print(
            'ID Produk tidak ditemukan! pastikan ID Produk yang anda masukkan benar'
        )
        input('Tekan enter untuk kembali ke menu utama')
        tampilan_pembeli()

    barang_dipilih = stok_barang[stok_barang['ID Produk'] == pil_ID]
    print("\nBarang yang akan Anda beli:")
    print(tabulate(barang_dipilih.values, headers=barang_dipilih.columns, tablefmt="grid"))
    jumlah = input('Masukkan jumlah barang yang ingin dibeli : ')
    try:
        jumlah = int(jumlah)
    except:
        print(
            'Jumlah barang tidak sesuai! pastikan jumlah barang yang anda masukkan adalah Integer'
        )
        input('Tekan enter untuk kembali ke menu utama')
        return tampilan_pembeli()
        
    if jumlah > stok_barang.loc[stok_barang['ID Produk'] == pil_ID, 'Stok'].values[0]:
        print('jumlah melebihi stok perhatikan input jumlah anda')
        input('Tekan enter untuk kembali ke menu utama')
        return tampilan_pembeli()

    keranjang = pd.read_csv('keranjang.csv')

    cari = False
    for index, row in keranjang.iterrows():
        if row['Username'] == Username and row['ID Produk'] == pil_ID:
            keranjang.at[index, 'Jumlah'] += jumlah
            cari = True
            print(f'Jumlah barang produk {pil_ID} telah diperbarui')
            break

    if not cari:
        data_baru = {
            "Username": Username,
            "ID Produk": pil_ID,
            "Jumlah": jumlah
        }
        keranjang = pd.read_csv('keranjang.csv')
        keranjang = pd.concat([keranjang, pd.DataFrame([data_baru])], ignore_index=True)
        keranjang.to_csv('keranjang.csv', index=False)
        print('Barang telah ditambahkan ke keranjang')
    input('Tekan enter untuk kembali ke menu utama...')
    tampilan_pembeli()


def lihat_keranjang():
    global Username
    keranjang = pd.read_csv('keranjang.csv')
    keranjang = keranjang[keranjang['Username'] == Username]
    if keranjang.empty:
        print("Belum ada barang dikeranjang.")
        input("Tekan enter untuk kembali ke menu utama...")
        tampilan_pembeli()
    else:
        print(tabulate(keranjang.values, headers=keranjang.columns, tablefmt="grid"))
        input("Tekan enter untuk kembali ke menu utama...")
        tampilan_pembeli()


def reset_keranjang():
    global Username
    keranjang = pd.read_csv('keranjang.csv')
    
    data_keranjang = keranjang[keranjang['Username'] == Username]
    for _, row in data_keranjang.iterrows():
        id_produk = row['ID Produk']
        jumlah_dikembalikan = row['Jumlah']
        
    data_keranjang = keranjang[keranjang['Username'] != Username]
    data_keranjang.to_csv('keranjang.csv', index=False)
    print('Keranjang berhasi di reset')
    input("Tekan enter untuk kembali ke menu utama...")
    tampilan_pembeli()


def transaksi():
    os.system('cls')
    global Username
    keranjang = pd.read_csv('keranjang.csv')
    stok_barang = pd.read_csv('stok_barang.csv')
    riwayat_pembelian = pd.read_csv('riwayat_pembelian.csv')
    detail_pembelian = pd.read_csv('detail_pembelian.csv')
    barang_dibeli = keranjang[keranjang['Username'] == Username]
    if barang_dibeli.empty:
        print("Belum ada barang dikeranjang.")
        input("Tekan enter untuk kembali ke menu utama...")
        tampilan_pembeli()
    else:
        print(tabulate(barang_dibeli.values, headers=barang_dibeli.columns, tablefmt="grid"))
        beli = input('Apakah anda ingin membeli barang-barang ini (y/n): ').lower()
        
        if beli == 'y':
            daftar_pembelian = []
            for _, row in barang_dibeli.iterrows():
                id_produk = row['ID Produk']
                jumlah = row['Jumlah']

                produk = stok_barang[stok_barang['ID Produk'] == id_produk]

                if produk.empty:
                    print(f"Produk dengan ID {id_produk} tidak ditemukan di stok_barang.")
                    continue

                stok_tersedia = produk['Stok'].values[0]
                if jumlah > stok_tersedia:
                    print(f"Produk dengan ID{produk['Nama Produk'].values[0]} tidak mencukupi! Tersisa {stok_tersedia}.")
                    continue

                nama_produk = produk['Nama Produk'].values[0]
                harga = produk['Harga'].values[0]
                total = jumlah * harga

                daftar_pembelian.append({
                    "Nama Produk": nama_produk,
                    "Harga": harga,
                    "Jumlah": jumlah,
                    "Total": total
                })

                stok_barang.loc[stok_barang['ID Produk'] == id_produk, 'Stok'] -= jumlah

            print("\nDetail Pembayaran:")
            print(tabulate(daftar_pembelian, headers='keys', tablefmt="grid"))
            total_pembelian = sum(item['Total'] for item in daftar_pembelian)
            print(f'\nTotal yang harus dibayar: Rp {total_pembelian:,}')

            print("\nPilih metode pembayaran: ")
            print("1. Tunai")
            print("2. Transfer Bank")
            print("3. E-Wallet")
            metode = input("Masukkan pilihan metode pembayaran (1/2/3): ")

            if metode not in ['1', '2', '3']:
                print("Metode pembayaran tidak valid.")
                input("Tekan enter untuk kembali")
                transaksi ()
            
            if metode == '1':
                while True:
                    bayar = input('Masukkan nominal pembayaran: Rp ')
                    try:
                        bayar = int(bayar)
                        if bayar < total_pembelian:
                            print("Nominal yang anda masukkan tidak cukup! Silakan masukkan nominal yang sesuai.")
                        elif bayar == total_pembelian:
                            print("Sip! Nominal pembayaranmu sudah sesuai")
                            input('Tekan enter untuk melanjutkan...')
                            break
                        else:
                            kembalian = bayar - total_pembelian
                            print(f"Kembalian anda: Rp {kembalian:,}")
                            print('Pastikan nominal yang anda setorkan kepada kurir sesuai!\nKembalian anda akan diantar oleh kurir')
                            break
                    except ValueError:
                            print("Nominal pembayaran anda tidak valid! masukkan angka.")
                            
            elif metode == '2':
                print("\nSilakan transfer ke rekening berikut:")
                print("Bank ABC - 1234567890 - a.n. Feedloop Store")
                input("Tekan enter setelah melakukan transfer...")

            elif metode == '3' :
                print("\nSilakan transfer ke E-Wallet berikut:")
                print("Gopay/Dana/OVO - 081234567890 - a.n. Feedloop Store")
                input("Tekan enter setelah melakukan transfer...")

            if not riwayat_pembelian.empty:
                riwayat_pembelian['ID Riwayat'] = pd.to_numeric(riwayat_pembelian['ID Riwayat'], errors='coerce').fillna(0).astype(int)
                id_riwayat_baru = riwayat_pembelian['ID Riwayat'].max() + 1
            else:
                id_riwayat_baru = 1

            tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            riwayat_pembelian = pd.concat([
                riwayat_pembelian,
                pd.DataFrame([{
                    'ID Riwayat' : id_riwayat_baru,
                    'Username' : Username,
                    'Tanggal' : tanggal,
                    'Total pengeluaran' : total_pembelian
                }])
            ], ignore_index=True)
            riwayat_pembelian.to_csv('riwayat_pembelian.csv', index=False)

            for barang in daftar_pembelian:
                detail_pembelian = pd.concat([
                    detail_pembelian,
                    pd.DataFrame([{
                        'ID Riwayat': id_riwayat_baru,
                        'Nama Produk': barang['Nama Produk'],
                        'Harga': barang['Harga'],
                        'Jumlah': barang['Jumlah'],
                        'Total': barang['Total']
                        }])
                ], ignore_index=True) 
            
            detail_pembelian.to_csv('detail_pembelian.csv', index=False)

            stok_barang.to_csv('stok_barang.csv', index=False)
            keranjang = keranjang[keranjang['Username'] != Username]
            keranjang.to_csv('keranjang.csv', index=False)

            status_pengiriman_data ={
                "ID Riwayat": id_riwayat_baru,
                "Username": Username,
                "Total Pembayaran": total_pembelian,
                "Status" : "Diproses"

            }
            if os.path.exists('riwayat_pengiriman.csv'):
                pengiriman = pd.read_csv('riwayat_pengiriman.csv')
            else:
                pengiriman = pd.DataFrame(columns=status_pengiriman_data.keys())

            pengiriman = pd.concat([pengiriman,pd.DataFrame([status_pengiriman_data])], ignore_index=True)
            pengiriman.to_csv('riwayat_pengiriman.csv', index=False)

            print("\nTransaksi berhasil!")
            print("Terimaksih telah menggunakan aplikasi Feedloop! Tungguin ya, pesananmu akan segera diantar!")
            input('Tekan enter untuk kembali ke menu utama...')
            tampilan_pembeli()
        else:
            print("Transaksi dibatalkan.")
            input("Tekan enter untuk kembali ke menu utama...")
            tampilan_pembeli()
        

def status_pengiriman_pemb():
    os.system('cls')
    global Username
    try:
        pengiriman = pd.read_csv('riwayat_pengiriman.csv')
    except FileNotFoundError:
        pengiriman = pd.DataFrame(columns=['ID Riwayat', 'Username', 'Alamat Pengiriman', 'Total Pembayaran', 'Status'])
    
    status_pengiriman_user = pengiriman[pengiriman['Username'] == Username]
    if status_pengiriman_user.empty:
        print("Belum ada data pengiriman terkait akun anda.")
    else:
        print("\nStatus Pengiriman Anda:")
        print(tabulate(status_pengiriman_user.values, headers=status_pengiriman_user.columns, tablefmt="grid"))
    
    input("\nTekan enter untuk kembali")
    tampilan_pembeli()


def riwayat():
    os.system('cls')
    global Username
    riwayat_pembelian = pd.read_csv('riwayat_pembelian.csv')
    detail_pembelian = pd.read_csv('detail_pembelian.csv')
    print("========== RIWAYAT PEMBELIAN ==========\n")
    riwayat_beli = riwayat_pembelian[riwayat_pembelian['Username'] == Username]
    if riwayat_beli.empty:
        print("Belum ada riwayat pembelian.")
        input("Tekan enter untuk kembali ke menu utama...")
        tampilan_pembeli()
    else:
        print(tabulate(riwayat_beli.values, headers=riwayat_beli.columns, tablefmt="grid"))
        print('Note: input 0 untuk kembali ke menu utama, input id_riwayat untuk melihat detail pembelian')
        pilih = input('Input ID Riwayat : ')
        try:
            pilih = int(pilih)
        except:
            print('ID Riwayat tidak sesuai! pastikan ID Riwayat yang anda masukkan integer')
            input("Tekan enter untuk kembali ke menu utama...")
            tampilan_pembeli()
        if pilih == 0:
            tampilan_pembeli()
        else:
            if pilih in riwayat_beli['ID Riwayat'].values:
                pembelian_detail = detail_pembelian[detail_pembelian['ID Riwayat'] == pilih]
                print(tabulate(pembelian_detail.values, headers=pembelian_detail.columns, tablefmt="grid"))
                input("Tekan enter untuk kembali ke riwayat transaksi")
                riwayat()
            else:
                print('ID Riwayat tidak ditemukan!\nPastikan ID Riwayat sesuai dengan yang tertera di tabel riwayat')
                input("Tekan enter untuk kembali ke riwayat transaksi")
                riwayat()


def logout():
    os.system('cls')
    print("\n#===============================================================================#")
    print("#           |                                                         |         #")
    print("#           |    Terima kasih telah menggunakan aplikasi FEEDLOOP!    |         #")
    print("#           |                         BYE-BYE                         |         #")
    print("#           |                                                         |         #")
    print("#===============================================================================#")


main()