barang = int(input('Masukan Jumlah Barang: '))
total_harga = 0
for i in range (barang):
    harga = float(input('Masukan Harga Barang Ke-' + str(i+1)))
    total_harga += harga
print(f'Total Harga Belanjaan Adalah: Rp{total_harga:,.2f}')