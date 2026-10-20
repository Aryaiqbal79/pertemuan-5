# Soal 2: Analisis Nilai Mahasiswa
def kategorikan_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

def analisis_nilai(list_nilai=None):
    if list_nilai is None:
        raw_input = input("Masukkan daftar nilai mahasiswa (pisahkan dengan koma/spasi): ")
        # Support input separated by comma or space
        tokens = raw_input.replace(",", " ").split()
        if not tokens:
            print("Tidak ada nilai yang dimasukkan.")
            return
        list_nilai = [float(x) for x in tokens]

    if not list_nilai:
        print("Daftar nilai kosong.")
        return

    # (a) Hitung rata-rata
    rata_rata = sum(list_nilai) / len(list_nilai)

    # (b) Tentukan nilai tertinggi dan terendah
    nilai_tertinggi = max(list_nilai)
    nilai_terendah = min(list_nilai)

    # (c) Kelompokkan nilai ke dalam kategori A/B/C/D/E
    # (d) Tampilkan frekuensi setiap kategori menggunakan dictionary
    frekuensi_kategori = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    pengelompokan = {"A": [], "B": [], "C": [], "D": [], "E": []}

    for n in list_nilai:
        kat = kategorikan_nilai(n)
        frekuensi_kategori[kat] += 1
        pengelompokan[kat].append(n)

    print("\n--- Hasil Analisis Nilai Mahasiswa ---")
    print(f"Data Nilai           : {list_nilai}")
    print(f"(a) Rata-rata        : {rata_rata:.2f}")
    print(f"(b) Nilai Tertinggi  : {nilai_tertinggi}")
    print(f"    Nilai Terendah   : {nilai_terendah}")
    print("\n(c) & (d) Frekuensi dan Pengelompokan Kategori:")
    for kat, count in frekuensi_kategori.items():
        print(f"    Kategori {kat} : {count} mahasiswa -> {pengelompokan[kat]}")

if __name__ == "__main__":
    analisis_nilai()
