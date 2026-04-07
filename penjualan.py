# Modul penjualan.py

def hitung_total_harga(harga_satuan, jumlah):
    return harga_satuan * jumlah

def hitung_diskon(total_harga, persen_diskon):
    diskon = total_harga * (persen_diskon / 100)
    return total_harga - diskon

def hitung_pajak(total_harga, persen_pajak):
    pajak = total_harga * (persen_pajak / 100)
    return total_harga + pajak