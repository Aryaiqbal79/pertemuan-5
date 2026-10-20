# Soal 4: Manajemen Inventaris Toko
# Struktur data: {nama_barang: (harga, stok)}

inventaris = {
    "Buku Tulis": (5000, 50),
    "Pulpen": (3000, 100),
    "Penghapus": (2000, 30),
    "Penggaris": (4000, 25),
    "Buku Gambar": (8000, 15)
}

# (a) Menambah barang baru
def tambah_barang(data, nama, harga, stok):
    if nama in data:
        print(f"Barang '{nama}' sudah ada di inventaris. Gunakan update_stok jika ingin mengubah.")
        return False
    data[nama] = (harga, stok)
    print(f"Berhasil menambahkan '{nama}' dengan harga Rp{harga:,} dan stok {stok}.")
    return True

# (b) Mengupdate stok (bisa menambah stok atau set stok baru)
def update_stok(data, nama, stok_baru):
    if nama not in data:
        print(f"Barang '{nama}' tidak ditemukan di inventaris.")
        return False
    harga, _ = data[nama]
    data[nama] = (harga, stok_baru)
    print(f"Stok untuk '{nama}' berhasil diperbarui menjadi {stok_baru}.")
    return True

# (c) Mencari barang dengan harga dalam rentang tertentu
def cari_barang_rentang_harga(data, min_harga, max_harga):
    hasil = {}
    for nama, (harga, stok) in data.items():
        if min_harga <= harga <= max_harga:
            hasil[nama] = (harga, stok)
    return hasil

# (d) Menghitung total nilai inventaris
def hitung_total_nilai_inventaris(data):
    total = sum(harga * stok for harga, stok in data.values())
    return total

def tampilkan_inventaris(data):
    print("\n=== DAFTAR INVENTARIS TOKO ===")
    print(f"{'Nama Barang':<15} | {'Harga':>10} | {'Stok':>6} | {'Subtotal':>12}")
    print("-" * 52)
    for nama, (harga, stok) in data.items():
        subtotal = harga * stok
        print(f"{nama:<15} | Rp{harga:>8,} | {stok:>6} | Rp{subtotal:>10,}")
    print("-" * 52)

if __name__ == "__main__":
    tampilkan_inventaris(inventaris)

    # Uji Coba (a) Menambah barang baru
    print("\n--- (a) Menambah Barang Baru ---")
    tambah_barang(inventaris, "Spidol", 7500, 20)

    # Uji Coba (b) Mengupdate stok
    print("\n--- (b) Mengupdate Stok Barang ---")
    update_stok(inventaris, "Pulpen", 120)

    # Uji Coba (c) Mencari barang dengan rentang harga Rp3.000 s/d Rp7.500
    print("\n--- (c) Pencarian Barang (Rentang Rp3.000 - Rp7.500) ---")
    hasil_cari = cari_barang_rentang_harga(inventaris, 3000, 7500)
    for nama, (harga, stok) in hasil_cari.items():
        print(f"- {nama}: Rp{harga:,} (Stok: {stok})")

    # Uji Coba (d) Menghitung total nilai inventaris
    print("\n--- (d) Menghitung Total Nilai Inventaris ---")
    total_nilai = hitung_total_nilai_inventaris(inventaris)
    print(f"Total Nilai Seluruh Inventaris: Rp{total_nilai:,}")
