# Case Study
# Data nilai siswa
list_nilai_siswa = [
    {
        'nama': 'anton',
        'BIndonesia': 80,
        'IPA': 42,
        'Matematika': 57,
    },
    {
        'nama': 'andi',
        'BIndonesia': 80,
        'IPA': 92,
        'Matematika': 85
    },
    {
        'nama': 'yaya',
        'BIndonesia': 72,
        'IPA': 80,
        'Matematika': 80
    }
]

def hitung_grade(jumlah):
    if jumlah >= 250:
        return "A"
    elif jumlah >= 210:
        return "B"
    else:
        return "C"

def menampilkan_daftar_siswa():
    print('DAFTAR NILAI SISWA\n')
    print('Index\t|Nama\t|B.Indonesia\t|IPA\t|Matematika\t|Jumlah\t|Nilai')
    for  i,j in enumerate(list_nilai_siswa):
        jumlah = j['BIndonesia'] + j['IPA'] + j['Matematika']
        j['jumlah'] = jumlah
        j['Nilai'] = hitung_grade(jumlah)
        print(f"{i}\t|{j['nama']}\t|{j['BIndonesia']}\t\t|{j['IPA']}\t|{j['Matematika']}\t\t|{jumlah}\t|{j['Nilai']}")

def menambah_siswa():
    nama_siswa = input('Masukkan nama siswa: ')
    BIndonesia_siswa = int(input('Masukkan nilai B.Indonesia siswa: '))
    IPA_siswa = int(input('Masukkan nilai IPA siswa: '))
    Matematika_siswa = int(input('Masukkan nilai Matematika siswa: '))
    list_nilai_siswa.append({
        'nama': nama_siswa,
        'BIndonesia': BIndonesia_siswa,
        'IPA': IPA_siswa,
        'Matematika': Matematika_siswa
    })
    print("\nSiswa berhasil ditambahkan.\n")
    menampilkan_daftar_siswa()

def menghapus_siswa():
    print("\nDaftar nilai siswa sebelum dihapus:\n")
    menampilkan_daftar_siswa()
    try:
        index_siswa = int(input('Masukkan index siswa yang ingin dihapus: '))
        if 0 <= index_siswa < len(list_nilai_siswa):
            del list_nilai_siswa[index_siswa]
            print("\nData siswa berhasil dihapus.\n")
        else:
            print("\nIndex tidak valid.\n")
    except ValueError:
        print("\nInput harus berupa angka.\n")
    menampilkan_daftar_siswa()

def mengurutkan_siswa():
    print("\nDaftar nilai siswa sebelum diurutkan:\n")
    menampilkan_daftar_siswa()
    # Mengurutkan berdasarkan jumlah nilai tertinggi
    list_nilai_siswa.sort(key=lambda urut: urut['jumlah'], reverse=True)
    print("\nDaftar nilai siswa setelah diurutkan:\n")
    menampilkan_daftar_siswa()

# Menu utama
while True:
    pilihan_menu = input('''
Selamat datang di daftar nilai siswa
List menu:
1. Menampilkan daftar siswa
2. Menambahkan nama siswa
3. Menghapus nama siswa
4. Mengurutkan siswa
5. Exit program
Masukkan angka menu yang ingin dijalankan: ''')

    if pilihan_menu == '1':
        menampilkan_daftar_siswa()
    elif pilihan_menu == '2':
        menambah_siswa()
    elif pilihan_menu == '3':
        menghapus_siswa()
    elif pilihan_menu == '4':
        mengurutkan_siswa()
    elif pilihan_menu == '5':
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
