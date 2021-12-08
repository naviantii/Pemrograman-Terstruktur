# import modul
from datetime import *

# function menghitung selisih hari
def diffDate (x) :
    y = datetime.date(datetime.now())
    selisihHari = abs(x - y)
    print('Selisih hari antara tanggal ', y, ' dengan ', x, ' adalah sebanyak ', selisihHari.days, ' hari.')

# tanggal yang akan dicari selisihnya
x = date(2003,7,23)

# call function
diffDate(x)