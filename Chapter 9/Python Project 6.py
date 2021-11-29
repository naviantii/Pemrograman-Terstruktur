# data nilai
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	    {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	    {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

# menghitung nilai akhir dan status
data =[]
status =[]
for x in nilai :
    nilaiAkhir = round((x['mid'] + 2* x['uas'])/3, 3)
    data += [nilaiAkhir]
    if nilaiAkhir >= 60 :
        ket = 'LULUS'
        status += [ket]
    else :
        ket = 'TIDAK LULUS'
        status += [ket]

# output

print('=========================================================================')
print('NIM      NAMA            N.MID      N.UAS        N. AKHIR        STATUS')
print('-------------------------------------------------------------------------')

for i in range(len(nilai)) : 
    print(nilai[i]['nim'].ljust(9), end='')
    print(nilai[i]['nama'].ljust(16), end='')
    print(str(nilai[i]['mid']).rjust(5), end='')
    print(str(nilai[i]['uas']).rjust(11), end = '')
    print(str(data[i]). rjust(16), end ='')
    print(status[i].rjust(14))

print('-------------------------------------------------------------------------')