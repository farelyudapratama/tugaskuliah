print('PROGRAM BIODATA')
def biodata():
    nama = input('Input Nama: ')
    kelas = input('Input Kelas: ')
    npm = input('Input NPM: ')
    print('================================')
    print('Biodata anda adalah: ')
    print('Nama: ' + nama)
    print('Kelas: ' + kelas)
    print('NPM: ' + npm)
d=biodata()
print()
print('===================================')
print()
print('PROGRAM LUAS SEGITIGA')
def segitiga():
    a =float(input('Masukkan alas:'))
    t =float(input('Masukkan tinggi:'))
    luas= a*t*0.5
    print('===============================')
    print('Luas adalah:',luas)
c=segitiga()