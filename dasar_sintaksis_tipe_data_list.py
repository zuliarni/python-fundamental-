daftar_buku = ['seven habits', 'how to influencer', 'first things first', '4DX']
print ('tampilkan variable daftar buku')
print(daftar_buku)

print ('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print ('\ntampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\ntampilkan dengan for in range')
for i in range(0, len(daftar_buku)) :
    print (daftar_buku[i])

daftar_buku = [1, 'kenji vol 2', -313, 314]
print('\ntampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nkembalikan nilai awal daftar_buku')
daftar_buku = ['seven habits','how to influencer', 'first things first','4DX']
print('\ntambahkan 1 buku baru')
daftar_buku.append ('dunia matematik kelas 5')
for i in range (0, len (daftar_buku)):
    print (daftar_buku [i])

