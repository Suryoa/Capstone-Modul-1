def pemisah():
    print("="*70)
def listMenuUtama():
    print("""SOLUSI ATASI BERBAGAI PENYAKIT SECARA HERBAL

LIST MENU UTAMA:
1. Menampilkan list produk
2. Menambah list produk
3. Update data list produk
4. Menghapus data produk
5. Total value produk di gudang
6. Omset harian
7. Exit
""")
def loginUser():
    print()
    print("===SELAMAT DATANG DI IWELL2U==")
    print()
    user=input('Masukan user id anda: ')
    password = input("Masukan password anda: ")
    userId= 'admin1'
    userPassword = "well"
    while password != userPassword or user != userId:
        print()
        print("Id atau Passwords tidak sesuai, silahkan coba lagi")
        print('-'*30)
        userId = input("Masukan user id anda: ")
        password = input("Masukan password anda: ")
    else:
        print()
        print("Berhasil Login")
        print("\n")

listProduk={
            "101":
                {"id":101,
                "nama":"Diabetter",
                "stok": 300,
                "harga": 399000,
                "bpom": "POM14048"
                },
            "102":
                {"id":102,
                "nama":"Gastrin",
                "stok": 105,
                "harga": 180000,
                "bpom": "POM88888"
                },
            "103":
                {"id":103,
                "nama":"Bio Young",
                "stok": 20,
                "harga": 270000,
                "bpom": "POM12388"
                },
            "104":
                {"id":104,
                "nama":"Hol Joint",
                "stok": 33,
                "harga": 199000,
                "bpom": "POM021048"
                },
            "105":
                {"id":105,
                "nama":"Nature-G",
                "stok": 33,
                "harga": 980000,
                "bpom": "POM20658"
                },   
            }
listProdukDitambahkan={}
listProdukDitambahkan.update(listProduk)
barangKeluar={}

#FUNSGI MENU READ ===========================
def menuRead():
    print("""=====HERBAL WORLD PRODUK=====
1. Tampilkan Produk Yang Tersedia
2. Cari Produk berdasarkan Nama
3. Produk yang perlu re-stok
4. Kembali ke Menu utama
""")
def readSemuaListProduk():
    print('ID\t| Nama Item  \t| Stok\t\t| Harga Produk\t| No BPOM')
    pemisah()
    for key in listProduk.keys():
        print('{}\t| {}   \t| {}\t\t| {}\t| {}'.format(listProduk[key]["id"],listProduk[key]["nama"],listProduk[key]["stok"],listProduk[key]["harga"],listProduk[key]["bpom"]))
    print('\n') 
def cariProduk():
    inputProdukCari=input("Masukan Nama produk yang dicari: ")
    print()
    # print('ID\t| Nama Item  \t| Stok\t\t| Harga Produks\t| No BPOM')
    for key in listProduk.keys():
        if inputProdukCari.lower() in listProduk[key]["nama"].lower() and len(inputProdukCari.lower()) >= 3:
            print('ID\t| Nama Item  \t| Stok\t\t| Harga Produks\t| No BPOM')
            pemisah()
            print('{}\t| {}   \t| {}\t\t| {}\t| {}'.format(listProduk[key]["id"],listProduk[key]["nama"],listProduk[key]["stok"],listProduk[key]["harga"],listProduk[key]["bpom"]))
            print('\n')
            break
        
    if inputProdukCari.lower() not in listProduk[key]["nama"].lower():
        print()
        print("Obat tidak ada, atau mungkin anda typo")
        print('\n')       
def urgenStok():
    print('ID\t| Nama Item  \t| Stok\t\t| Harga Produk\t| No BPOM')
    pemisah()
    for key in listProduk.keys():
        if listProduk[key]["stok"] <= 20:  
            print('{}\t| {}   \t| {}\t\t| {}\t| {}'.format(listProduk[key]["id"],listProduk[key]["nama"],listProduk[key]["stok"],listProduk[key]["harga"],listProduk[key]["bpom"]))
    print('\n')
    
#FUNGSI MENU CREAT ===========================
def menuCreate():
    print("""==== MENAMBAHKAN DATA PRODUK===
1. Menambahkan Produk
2. Kembali ke Menu Utama

""")
def opsiMenuCreate():
    while True:
        menuCreate()
        opsiMenuCreate = int(input("Pilih menu(1-2): "))
        # while True:
        if opsiMenuCreate == 1:
            inputProdukTambahan()
        elif opsiMenuCreate == 2:
            # list_menu_well2u()
            # break
            return
        else:
            continue
def inputProdukTambahan():   
    tambahIdProduk = input("Masukan ID produk(angka): ")
    if tambahIdProduk in listProduk:
        print()
        print(f"ID {tambahIdProduk} sudah ada")
        print("\n")
        # pass
    else:
        tambahNamaProduk= input("Masukan nama produk: ")
        namaProdukKapital=tambahNamaProduk.capitalize()
        tambahStokProduk= int(input("Masukan jumlah stok: "))
        while tambahStokProduk == 0:
            tambahStokProduk= int(input("Stok tidak boleh 0, masukan jumlah stok:  "))
        else:
            tambahHargaProduk = int(input("Masukan harga produk: "))
        while tambahHargaProduk == 0:
            tambahHargaProduk= int(input("Harga produk tidak boleh 0, Masukan harga produk: "))
        else:
            tambahNoBpom= input("Masukan no BPOM: ")
        valueProdukTambahan=(
        {"id": tambahIdProduk,
        "nama": namaProdukKapital,
        "stok": tambahStokProduk,
        "harga": tambahHargaProduk,
        "bpom": tambahNoBpom.upper()
        })
        
        
        konfirmasiTambahProduk= (input("Apakah data mau disimpan?(Ya/Tidak): ")).lower()
        if konfirmasiTambahProduk == "ya":
            listProduk[tambahIdProduk]=valueProdukTambahan
            listProdukDitambahkan.update(listProduk)
            print()
            print("DATA BERHASIL DISIMPAN")
            print('\n')
            # list_MenuUpdate_stok()
        else:
            print()
            print("Data tidak tersimpan")
            print('\n')

#FUNGSI MENU UPDATE ==========================
def menuUpdate():
    print("""==== MENGUPDATE DATA PRODUK===
1. Mengupdate Data Produk
2. Kembali ke Menu Utama

""")
def pilihMenuUpdate():
    print("""Pilih data yang mau diupdate: 
    1. Nama Produk
    2. Stok Produk
    3. Harga Produk
    4. No BPOM
    """)
def fUpdateNama():
    updateNama=input("Masukan nama produk ter-update: ")
    if verifUpdate() == "ya":
        # print(list_produk, "list_produk")
        listProdukDitambahkan[str(pilihIDupdate)]["nama"]= updateNama
        print()
        berhasilUpdate()
        print('\n')
    else:
        print()
        batalUpdate()
        print('\n')
def fUpdateStok():
    updateStok=int(input("Masukan stok terupdate: "))
    if verifUpdate() == "ya":
        listProdukDitambahkan[(pilihIDupdate)]["stok"]= updateStok
        print()
        berhasilUpdate()
        print('\n')
    else:
        print()
        batalUpdate()
        print('\n')
def fUpdateHarga():
    updateHarga=int(input("Masukan harga ter-update: "))
    if verifUpdate() == "ya":
        listProdukDitambahkan[(pilihIDupdate)]["harga"]= updateHarga
        print()
        berhasilUpdate()
        print('\n')
    else:
        print()
        batalUpdate()
        print('\n')       
def fUpdateBpom():
    updateBpom=input("Update nomer BPOM: ").upper()
    if verifUpdate() == "ya":
        listProdukDitambahkan[(pilihIDupdate)]["bpom"]= updateBpom
        print()
        berhasilUpdate()
    else:
        print()
        batalUpdate()
        print('\n')
def verifUpdate():
    verifikasiUpdate= (input("Apakah data mau disimpan?(Ya/Tidak): ")).lower()
    return verifikasiUpdate
def berhasilUpdate():
    print("DATA BERHASIL DISIMPAN")
    print()
def batalUpdate():
    print("Data tidak tersimpan") 
    print()

#FUNGSI MENU DELETE ===========================
def menuDelete():
    print("""==== MENGHAPUS DATA PRODUK===
1. Menghapus Data Produk
2. Kembali ke Menu Utama

""")   
def deleteId():
    while True:
            menuDelete()
            opsiMenuDelete = int(input("Pilih menu(1-2): "))  
            if opsiMenuDelete == 1:
                deleteIdProduk= input("Masukan ID produk yang mau dihapus: ")
                if deleteIdProduk in listProduk:
                    print()
                    konfirmasiHapus = input("Apakah anda yakin akan menghapus produk? (Ya/Batal): ").lower()
                    if konfirmasiHapus == 'ya':
                    
                        del listProduk[deleteIdProduk]
                        print()
                        print(f"ID produk {deleteIdProduk} berhasil dihapus.")
                        print()
                        readSemuaListProduk()
                    else:
                        print()
                        print(f"ID produk {deleteIdProduk} batal dihapus")
                        print()
                        readSemuaListProduk()
                        print()
                else:
                    print()
                    print(f"ID {deleteIdProduk} tidak ada")
                    print('\n')           
            elif opsiMenuDelete == 2:
                break
            else:
                continue
    
#FUNGSI VALUASI STOK ===========================
def totalValuasiProduk():
    totalValueStok=sum(valuasiStok['stok']*valuasiStok['harga'] for valuasiStok in listProduk.values()) 
    idrStandard = "Rp {:,.0f}".format(totalValueStok)
    print(f'Total value semua stok barang sebesar: {idrStandard}')

#FUNGSI CEK OMSET HARIAN ===========================
def verifCekOmset():
    verifikasiOmset= (input("Apakah anda mau mencatat produk lain yang keluar?(Ya/Tidak): ")).lower()
    return verifikasiOmset 
def OmsetHariIni():
    totalOmset = 0
    for key, values in barangKeluar.items():
        harga=listProduk[key]["harga"]
        itemKeluar=values['stok']
        rumus = harga*itemKeluar
        totalOmset += rumus
    IdrFormat = "Rp {:,.0f}".format(totalOmset)
    print()
    print(f"Omset hari ini: {IdrFormat}")
    print()
def cekDailyOmset():
    print()
    print('WELL2U DAILY OMSET')
    while True:
        produkIdOut= input('Masukan ID produk yang keluar: ')
        if produkIdOut in listProduk:
            print('ID\t| Nama Item  \t| Stok\t\t| Harga Produks\t| No BPOM')
            pemisah()
            print('{}\t| {}   \t| {}\t\t| {}\t| {}'.format(listProdukDitambahkan[produkIdOut]["id"],listProdukDitambahkan[produkIdOut]["nama"],listProdukDitambahkan[produkIdOut]["stok"],listProdukDitambahkan[produkIdOut]["harga"],listProdukDitambahkan[produkIdOut]["bpom"]))
            print('\n')
            stokOut=int(input('Masukan jumlah stok yang keluar: '))
            if stokOut > listProdukDitambahkan[produkIdOut]['stok']:
                print("Jumlah yang anda input melebihi stok")
            elif stokOut == 0:
                pass
            else:
                listProduk[(produkIdOut)]["stok"]= listProduk[(produkIdOut)]["stok"]- stokOut
                addToOutput=({
                    'id': produkIdOut,
                    'stok': stokOut
                })
                barangKeluar[produkIdOut]=addToOutput
            print()    
            validasi = input('Mau mencatat produk keluar yang lain? (Y/N) = ').lower()
            if(validasi == 'n') :
                break
        else:    
            print('ID tidak tersedia')
    OmsetHariIni()
    
#PROGRAM RUNNING DARI SINI
loginUser()
while True:
    listMenuUtama()
    opsiMenuUtama = input("Masukan Menu Yang Ingin di Pilih(1-7): ")
    if opsiMenuUtama == '1':
        while True:
            menuRead()
            opsiMenuRead = int(input("Pilih menu(1-4): "))
            if opsiMenuRead == 1:
                readSemuaListProduk()               
            elif opsiMenuRead == 2:
                cariProduk()
            elif opsiMenuRead ==3:   
                urgenStok()     
            elif opsiMenuRead == 4:
                break
            else:
                continue
        
    elif opsiMenuUtama == '2':
        opsiMenuCreate()
            
    elif opsiMenuUtama == '3':
        while True:
            menuUpdate()
            opsiMenuUpdate = int(input("Pilih menu(1-2): "))  
            if opsiMenuUpdate == 1:
                # list_Menu1()
                pilihIDupdate= input("Masukan ID produk yang mau di update: ")
                if pilihIDupdate in listProdukDitambahkan:
                    print('ID\t| Nama Item  \t| Stok\t\t| Harga Produks\t| No BPOM')
                    pemisah()
                    print('{}\t| {}   \t| {}\t\t| {}\t| {}'.format(listProdukDitambahkan[pilihIDupdate]["id"],listProdukDitambahkan[pilihIDupdate]["nama"],listProdukDitambahkan[pilihIDupdate]["stok"],listProdukDitambahkan[pilihIDupdate]["harga"],listProdukDitambahkan[pilihIDupdate]["bpom"]))
                    print('\n')
                    pilihMenuUpdate()
                    inputCatagoriUpdate = input("Pilih data yang ingin di update: ")
                    if inputCatagoriUpdate == '1':
                        fUpdateNama()
                            
                    elif inputCatagoriUpdate == '2':
                        fUpdateStok()
                    elif inputCatagoriUpdate == '3':
                        fUpdateHarga()    
                    elif inputCatagoriUpdate == '4':
                        fUpdateBpom()
                    else:
                        continue
                else:
                    print()
                    print("ID tidak tersedia!")
                    print('\n')
            elif opsiMenuUpdate == 2:
                break
            else:
                continue            
    
    elif opsiMenuUtama == '4':
        deleteId()
            
    elif opsiMenuUtama == '5':
        print()
        totalValuasiProduk()
        print('\n')
    elif opsiMenuUtama == '6':
        cekDailyOmset()
    elif opsiMenuUtama == '7':
        break