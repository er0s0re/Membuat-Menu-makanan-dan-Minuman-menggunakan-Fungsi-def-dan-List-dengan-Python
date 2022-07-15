
print('========== Toko Jirolu ==========')


def makanan():
    print("\nA. Nasi Goreng Ayam")
    print("B. Nasi Goreng Babat")
    print("C. Nasi Goreng Seafood")
    print("D. Nasi Goreng telur")
    print("E. Kwetiau\n")
    pilihMakanan = input('Pilih Menu Makanan A - E / X untuk selesai : ').upper()
    while pilihMakanan != "X":
        if pilihMakanan == "A":
            list.append('Nasi Goreng Ayam')
        elif pilihMakanan == "B":
            list.append('Nasi Goreng Babat')
        elif pilihMakanan == "C":
            list.append('Nasi Goreng Seafood')
        elif pilihMakanan == "D":
            list.append('Nasi Goreng Telur')
        elif pilihMakanan == "E":
            list.append('Kwetiau')
        else:
            print('pilihan tidak ditemukan')
        pilihMakanan = input('pilih Menu Makanan :  A - E / X untuk selesai : ').upper()
    pilihan1 = input("apakah anda mau minum ? Y/T ? ").upper()
    if pilihan1 == "Y":
        minuman()
    elif pilihan1 == "T":
        hasil()

def minuman():
    print("\nA. Teh")
    print("B. Coklat")
    print("C. Jeruk")
    print("D. Lemon")
    pilihMinuman = input('Pilih Menu Minuman A - D / X Untuk selesai : ').upper()
    while pilihMinuman != 'X':
        if pilihMinuman == "A":
            pilihSuhu = input("Pilih : A. Dingin atau B. Panas ? ").upper()
            if pilihSuhu == "A":
                list.append('Es Teh')
            elif pilihSuhu == "B":
                list.append('Teh Panas')
        elif pilihMinuman == "B":
            pilihSuhu = input("Pilih A. Dingin atau B. Panas ? ").upper()
            if pilihSuhu == "A":
                list.append('Es Coklat')
            elif pilihSuhu == "B":
                list.append('Coklat Panas')
        elif pilihMinuman == "C":
            pilihSuhu = input("Pilih A. Dingin atau B. Panas ? ").upper()
            if pilihSuhu == "A":
                list.append('Es Jeruk')
            elif pilihSuhu == "B":
                list.append('Jeruk Panas')
        elif pilihMinuman == "D":
            pilihSuhu = input("Pilih A. Dingin atau B. Panas ? ").upper()
            if pilihSuhu == "A":
                list.append('Es Lemon')
            elif pilihSuhu == "B":
                list.append('Lemon Panas')
        pilihMinuman = input('pilih Menu Minumnan : A - D / X Untuk selesai : ').upper()
    hasil()

def hasil():
    print("\nPesanan anda : \n")
    for i in list:
        print(i)
        print()

def pilihan():
    pilih = int(input(" Pilih menu 1. makanan dan 2. minuman atau X untuk keluar : "))
    if pilih == 1:
        makanan()
    elif pilih == 2:
        minuman()

list = []
pilihan()

# menghapus item
print("\nApakah anda mau menghapus item ? Y/T ? ")
pilihan = input(" ").upper()
if pilihan == "Y":
    print("\nPilih item yang ingin dihapus : ")
    for i in list:
        print(i)
    item = input(" ")
    list.remove(item)
    print("\nPesanan anda : \n")
    for i in list:
        print(i)
        print()
    hasil()
elif pilihan == "T":
    print("\nPesanan anda : \n")
    for i in list:
        print(i)
        print()
    hasil()
else:
    print("\nPesanan anda : \n")
    for i in list:
        print(i)
        print()
    hasil()
    
