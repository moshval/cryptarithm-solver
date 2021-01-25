'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 1 IF2211 Strategi Algoritma
            Cryptarithmetic Solver menggunakan Algoritma Brute Force
            (Only supports additions)
Deskripsi File : Algoritma Penyelesaian
'''
def slotfill(charlist):
    '''
    Mengisi slot pada list of unique char hingga maksimum (pada kasus ini,10) dengan dummy character "*"
    charlist: List yang berisi karakter unik dari operand dan hasil
    '''
    slotlist = charlist
    while(len(slotlist)<10):
        slotlist.append("*")
    return slotlist
    

def permute(charlist): 
    '''
    Mencari permutasi dari list of unique char (charlist);naive, rekursif
    '''
    permlist = []  #List permutasi dari string charlist
    if len(charlist)==0: #Kasus List Kosong
        return []
    elif len(charlist)==1: # Basis List 1 karakter
        return charlist
    else:
        # Rekurens; melakukan iterasi kepada tiap karakter dalam list sehingga terbentuk list permutasi 
        # dengan karakter tersebut sebagai elemen pertama, dilakukan recursively
        for i in range(len(charlist)): 
            first = charlist[i] # Ambil elemen ke i sebagai index pertama dari suatu list permutasi
            rest = charlist[:i] + charlist[i+1:] # Elemen sisa 
            for p in permute(rest): #Iterasi permutasi elemen sisa secara rekursif 
                # Menambahkan elemen ke i sebagai index 0 dalam list of list permutasi,
                # dilanjutkan dengan menambahkan permutasi selanjutnya ke permlist secara rekursif 
                # dengan memanggil kembali fungsi permute
                permlist.append(first+p)
            permlist = list(dict.fromkeys(permlist)) 
        return permlist

def charvalue(isi,charlist):
    '''
    Assign value untuk tiap operand dan hasil
    isi : List yang berisi operand dan hasil
    charlist: List yang berisi karakter unik dari operand dan hasil
    '''
    cvlist = []
    for kalimat in isi:
        opvalue = ""
        for char in kalimat:
            opvalue+=str(charlist.index(char))
        cvlist.append(opvalue)
    return cvlist

def sumChecker(cvlist):
    '''
    Buat cek kesamaan sum operand dengan hasil
    cvlist : List yang berisi value dari tiap operand dan hasil
    '''
    opsum = 0
    for i in range(len(cvlist)-1):
        opsum+=int(cvlist[i])
    hasil = int(cvlist[len(cvlist)-1])
    return(opsum==hasil)

def isZero(cvlist):
    '''
    Cek char pertama dalam operand atau hasil bernilai nol atau tidak
    cvlist : List yang berisi value dari tiap operand dan hasil
    '''
    iszero = False
    for cv in cvlist:
        if int(cv[0])==0:
            iszero = True
            break
    return iszero

def permForm(charlist):
    '''
    Buat ubah format hasil permutasi
    '''
    rdlist = []
    for p in charlist:
        rdlist.append(list(p))
    return rdlist