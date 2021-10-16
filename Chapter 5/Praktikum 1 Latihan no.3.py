print('-----Program Menentukan Status Kelulusan-----')
print('--------------Ujian Mahasiswa----------------')

# input data
nilaiBhsIndonesia = int(input('Masukkan nilai Bhs Indonesia	: '))
nilaiIPA = int(input('Masukkan nilai IPA		: '))
nilaiMatematika = int(input('Masukkan nilai Matematika	: '))
print (' ')

# status kelulusan
if (nilaiBhsIndonesia < 0) or (nilaiBhsIndonesia > 100) or (nilaiIPA < 0) or (nilaiIPA > 100) or (nilaiMatematika < 0) or (nilaiMatematika > 100) :
    print('Maaf input ada yang tidak valid')
elif (nilaiBhsIndonesia < 60) or (nilaiIPA < 60) or (nilaiMatematika < 70) :
    print('Status Kelulusan		: TIDAK LULUS')
else :
    print ('Status Kelulusan		: LULUS')

# sebab
if (nilaiBhsIndonesia < 60) or (nilaiIPA < 60) or (nilaiMatematika < 70) :
    print("Sebab				: ")
if (nilaiBhsIndonesia < 60) :
    print('Nilai bahasa indonesia kurang dari 60')
if (nilaiIPA < 60) :
    print('Nilai IPA kurang dari 60')
if (nilaiMatematika < 70) :
    print('Nilai matematikanya kurang dari 70')