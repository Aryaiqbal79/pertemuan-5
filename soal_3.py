# Soal 3: Operasi Set Penerima Beasiswa
def analisis_beasiswa(beasiswa_a, beasiswa_b):
    set_a = set(beasiswa_a)
    set_b = set(beasiswa_b)

    # (a) Menerima kedua beasiswa (Intersection)
    kedua_beasiswa = set_a & set_b  # atau set_a.intersection(set_b)

    # (b) Hanya menerima beasiswa A (Difference A - B)
    hanya_a = set_a - set_b  # atau set_a.difference(set_b)

    # (c) Menerima beasiswa B tapi tidak A (Difference B - A)
    hanya_b = set_b - set_a  # atau set_b.difference(set_a)

    # (d) Semua mahasiswa unik yang menerima beasiswa (Union)
    semua_unik = set_a | set_b  # atau set_a.union(set_b)

    print("--- Data Penerima Beasiswa ---")
    print(f"List Beasiswa A: {beasiswa_a}")
    print(f"List Beasiswa B: {beasiswa_b}\n")

    print(f"(a) Menerima kedua beasiswa (irisan / A & B)  : {kedua_beasiswa}")
    print(f"(b) Hanya menerima beasiswa A (selisih / A - B): {hanya_a}")
    print(f"(c) Menerima beasiswa B bukan A (selisih B - A): {hanya_b}")
    print(f"(d) Semua mahasiswa unik (gabungan / A | B)   : {semua_unik}")

if __name__ == "__main__":
    # Contoh data ID Mahasiswa
    id_beasiswa_a = ["M001", "M002", "M003", "M005", "M007"]
    id_beasiswa_b = ["M002", "M004", "M005", "M006", "M008"]

    analisis_beasiswa(id_beasiswa_a, id_beasiswa_b)
