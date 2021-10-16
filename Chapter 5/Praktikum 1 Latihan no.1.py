print('-----Program Menentukan Status Kelulusan-----')
print('--------------Ujian Mahasiswa----------------')

# input data
nilaiBhsIndonesia = int(input('Masukkan nilai Bhs Indonesia	: '))
nilaiIPA = int(input('Masukkan nilai IPA		: '))
nilaiMatematika = int(input('Masukkan nilai Matematika	: '))
print (' ')

# status kelulusan
if (nilaiBhsIndonesia < 60) or (nilaiIPA < 60) or (nilaiMatematika < 70) :
            print('Status Kelulusan		: TIDAK LULUS')
else :
    print ('Status Kelulusan		: LULUS')