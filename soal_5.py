# Soal 5: Analisis Frekuensi Kata dan TTR dari File Teks
import os
import string

def bersihkan_dan_tokenisasi(teks):
    # Mengubah ke huruf kecil dan menghapus tanda baca
    teks_bersih = teks.lower()
    for tanda_baca in string.punctuation:
        teks_bersih = teks_bersih.replace(tanda_baca, " ")
    
    # List of tokens (kata-kata)
    kata_list = teks_bersih.split()
    return kata_list

def analisis_teks_file(filepath=None):
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, "sample_teks.txt")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            konten = f.read()
    except FileNotFoundError:
        print(f"File '{filepath}' tidak ditemukan.")
        return

    # List token kata
    kata_list = bersihkan_dan_tokenisasi(konten)
    total_kata = len(kata_list)

    if total_kata == 0:
        print("File teks kosong.")
        return

    # (a) Menghitung frekuensi setiap kata menggunakan dictionary
    frekuensi_kata = {}
    for kata in kata_list:
        frekuensi_kata[kata] = frekuensi_kata.get(kata, 0) + 1

    # (b) Menampilkan 10 kata paling sering muncul
    # Diurutkan berdasarkan frekuensi secara descending
    top_10 = sorted(frekuensi_kata.items(), key=lambda item: item[1], reverse=True)[:10]

    # (c) Mengidentifikasi kata yang hanya muncul sekali (hapax legomena) menggunakan set/list
    hapax_legomena = {kata for kata, count in frekuensi_kata.items() if count == 1}

    # (d) Menghitung rasio kata unik terhadap total kata (Type-Token Ratio / TTR)
    kata_unik = set(kata_list)
    ttr = len(kata_unik) / total_kata

    print(f"=== HASIL ANALISIS TEKS DARI FILE: {filepath} ===")
    print(f"Total Kata (Tokens)      : {total_kata}")
    print(f"Kata Unik (Types)        : {len(kata_unik)}")
    print(f"(d) Type-Token Ratio (TTR): {ttr:.4f} ({ttr * 100:.2f}%)\n")

    print("(b) 10 Kata Paling Sering Muncul:")
    for idx, (kata, count) in enumerate(top_10, 1):
        print(f"    {idx:>2}. '{kata}' : {count} kali")

    print(f"\n(c) Jumlah Kata yang Hanya Muncul Sekali (Hapax Legomena): {len(hapax_legomena)}")
    contoh_hapax = list(hapax_legomena)[:10]
    print(f"    Contoh 10 kata hapax legomena: {contoh_hapax}")

    print("\n(a) Sampel Frekuensi Kata (Dictionary):")
    for kata in list(frekuensi_kata.keys())[:10]:
        print(f"    '{kata}': {frekuensi_kata[kata]}")

if __name__ == "__main__":
    analisis_teks_file()
