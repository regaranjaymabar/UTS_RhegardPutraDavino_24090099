def is_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False
tahun_input = int(input('MASUKAN TAHUN :'))

if is_kabisat(tahun_input):
    print(f'Tahun {tahun_input} MERUPAKAN TAHUN KABISAT')
else:
    print(f'Tahun {tahun_input} BUKAN TAHUN KABISAT')