# Soal 1: Analisis Teks Sederhana
def analisis_kalimat():
    kalimat = input("Masukkan sebuah kalimat: ").strip()
    if not kalimat:
        print("Kalimat tidak boleh kosong.")
        return

    # Pecah menjadi kata-kata (membuang spasi berlebih)
    kata_list = kalimat.split()

    # (a) Hitung jumlah kata
    jumlah_kata = len(kata_list)

    # (b) Hitung jumlah karakter (termasuk dan tanpa spasi)
    jumlah_karakter = len(kalimat)
    jumlah_karakter_tanpa_spasi = len(kalimat.replace(" ", ""))

    # (c) Tampilkan kata terpanjang
    # Jika ada beberapa kata dengan panjang maksimal yang sama, ambil yang pertama atau list-nya
    panjang_maks = max(len(k) for k in kata_list)
    kata_terpanjang = [k for k in kata_list if len(k) == panjang_maks]

    # (d) Tampilkan kalimat dengan setiap kata dikapitalisasi (title case)
    kalimat_title = kalimat.title()

    print("\n--- Hasil Analisis Kalimat ---")
    print(f"Kalimat Asli         : {kalimat}")
    print(f"(a) Jumlah Kata      : {jumlah_kata}")
    print(f"(b) Jumlah Karakter  : {jumlah_karakter} (tanpa spasi: {jumlah_karakter_tanpa_spasi})")
    print(f"(c) Kata Terpanjang  : {', '.join(kata_terpanjang)} ({panjang_maks} karakter)")
    print(f"(d) Title Case       : {kalimat_title}")

if __name__ == "__main__":
    analisis_kalimat()
