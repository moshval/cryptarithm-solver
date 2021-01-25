'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 1 IF2211 Strategi Algoritma
            Cryptarithmetic Solver menggunakan Algoritma Brute Force
            (Only supports additions)
Deskripsi File : File Utama (Driver)
'''
import sys # Buat auto exit program
from time import time # Library Waktu
from util import reader,outputter # Utility
from sols import permute,slotfill,charvalue,sumChecker,isZero,permForm # Algo Solusi

print("\nCryptarithmetic Solver")
print("Dapat menyelesaikan persoalan penjumlahan cryptarithmetic")
print("Cr : Mohammad Sheva (13519018)\n")

parse = reader() # Parsing dari text file
inittime = time() # Initial Time

print("\nInput anda :\n")
outputter(parse[1])
print("Silakan tunggu, proses ini mungkin agak lama.\n")
if (len(parse[1][len(parse[1])-1]) < len(parse[1][0])): # Cek apakah banyak digit hasil lebih kecil atau lebih besar dari operand
    print("Tidak ditemukan solusi dari input anda")
    print("Lama eksekusi : ",time()-inittime," detik")
    sys.exit()

count = 0 # Counter jumlah tes
havesol = False # Apakah persoalan ini dapat ditemukan solusinya?
perm = permForm(permute(slotfill(parse[2]))) # Generate List of Permutation
for data in perm: # Iterasi untuk cek assigned value dari tiap char pada tiap permutasi
    cvlist=charvalue(parse[1],data) # Assign value ke char
    count+=1
    if(not isZero(cvlist)): # Cek leading zero pada operand/hasil
        if (sumChecker(cvlist)): # Cek kesamaan sum operand dan hasil
            havesol = True
            break # Terbatas ke 1 solusi

if(havesol):
    print("Solusi dari input anda :\n")
    outputter(cvlist)
else:
    print("Tidak ditemukan solusi dari input anda")

print("Total tes : ",count)
print("Lama eksekusi : ",time()-inittime," detik")
