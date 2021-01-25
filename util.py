'''
Deskripsi File : Fungsi Utility
'''
'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 1 IF2211 Strategi Algoritma
            Cryptarithmetic Solver menggunakan Algoritma Brute Force
            (Hanya support penjumlahan)
'''

def reader(): 
    '''
    Reader file text, mereturn nama file, list isi file perbaris, dan list char unik
    '''
    notfound = True
    while notfound :
        fname = input("Masukkan Nama File (dengan ekstensi, sebagai contoh : tc1.txt) : ")
        try:
            file = open(fname,"r")
            notfound = False
        except:
             print("File tidak ditemukan. Ulangi lagi")

    isi = file.readlines() # Membaca isi file
    file.close()
    # Mengubah ke array, menghapus karakter tak guna
    for i in range(len(isi)):
        isi[i] = isi[i].replace("\n","")
        isi[i] = isi[i].replace(" ","")

    # Format Checking
    if((len(isi) < 4) or (isi[len(isi)-2]!="------") or (isi[len(isi)-3][len(isi[len(isi)-3])-1]!="+")):
        print("File tidak sesuai format, pembacaan file akan diulangi...")
        return reader()

    isi[len(isi)-3]=isi[len(isi)-3][:-1] #Remove plus sign di operand terakhir
    isi[len(isi)-2] = isi[len(isi)-1] #Delete ------
    isi = isi[:-1]

    # Another format checking dan penambahan list berisi karakter unik pada operand/hasil
    charlist = []
    isalfa = True
    for string in isi: 
        if(not string.isalpha()):
            isalfa = False
            break
        for kar in string : #List of unique chars
            try:
                charlist.index(kar)
            except:
                charlist.append(kar)

    if((not isalfa) or (len(charlist)>10)):
        print("File tidak sesuai format, pembacaan file akan diulangi...")
        return reader()

    print("Pembacaan file berhasil")

    return fname,isi,charlist

def outputter(list):
    '''
    Mengoutput persoalan maupun solusi sesuai format
    '''
    for i in range(len(list)-2): #Iterate hingga sebelum baris yang ada plus sign nya
        space = len(list[len(list)-1]) - len(list[i])
        print(space*' '+list[i])

    space = len(list[len(list)-1]) - len(list[len(list)-2]) # Baris yang ada plus sign nya
    print(space*' '+list[len(list)-2]+"+")
    print("------")
    print(list[len(list)-1],"\n")
    
    


