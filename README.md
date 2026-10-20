# Jawaban Tugas Teori & Konsep Struktur Data Python

---

## Soal 1
**Jelaskan perbedaan mendasar antara list dan tuple dalam Python. Berikan contoh skenario di mana tuple lebih tepat digunakan daripada list, dan sebaliknya.**

### Jawaban:

### 1. Perbedaan Mendasar
| Karakteristik | List (`list`) | Tuple (`tuple`) |
|---|---|---|
| **Sintaks** | Didefinisikan dengan kurung siku `[...]` | Didefinisikan dengan kurung biasa `(...)` |
| **Mutabilitas (Mutability)** | **Mutable** (dapat diubah): elemen bisa ditambah, dihapus, atau diubah nilainya setelah dibuat. | **Immutable** (tidak dapat diubah): setelah dibuat, panjang dan elemennya tetap/konstan. |
| **Penggunaan Memori & Kinerja** | Mengalokasikan blok memori ekstra untuk menampung ekspansi elemen di masa depan (lebih berat). | Alokasi memori pas (*fixed size*), lebih hemat memori, dan pembuatan objeknya lebih cepat dibanding list. |
| **Kegunaan sebagai Key Dict/Set** | **Tidak bisa** dijadikan elemen `set` atau *key* pada `dict` karena mutable (unhashable). | **Bisa** dijadikan elemen `set` atau *key* pada `dict` (selama seluruh isinya juga hashable). |

---

### 2. Contoh Skenario Penggunaan

#### Kapan Tuple Lebih Tepat Digunakan?
- **Skenario:** Menyimpan data yang bersifat tetap, konstan, atau merepresentasikan record dengan struktur tertentu yang tidak boleh berubah secara tidak sengaja (*data integrity*).
- **Contoh Kasus:**
  - **Koordinat Geografis / Layar:** Titik koordinat latitude dan longitude: `titik_lokasi = (-6.2088, 106.8456)`.
  - **Kunci Dictionary:** Menggunakan pasangan nilai sebagai kunci: `rute_ongkir = {("Jakarta", "Bandung"): 25000}`.
  - **Nilai Return Fungsi:** Mengembalikan lebih dari satu nilai sekaligus dari suatu fungsi: `return luas, keliling`.

#### Kapan List Lebih Tepat Digunakan?
- **Skenario:** Mengelola koleksi data homogen atau kumpulan entitas yang dinamis, di mana data sering ditambah (*append/insert*), dihapus (*remove/pop*), atau diurutkan (*sort*).
- **Contoh Kasus:**
  - **Daftar Keranjang Belanja:** Barang belanjaan pengguna pada aplikasi e-commerce yang terus bertambah atau berkurang: `keranjang = ["Buku", "Pulpen"]`.
  - **Riwayat Nilai Mahasiswa:** Data input yang perlu difilter, diurutkan, atau dimodifikasi nilainya: `nilai_list = [80, 95, 75]`.

---

## Soal 2
**Mengapa set tidak mendukung pengindeksan seperti list dan tuple? Jelaskan kaitannya dengan implementasi hash table dan sifat unordered.**

### Jawaban:

1. **Sifat Unordered (Tidak Berurutan):**
   - Berbeda dengan list dan tuple yang merupakan tipe data *sequence* (urutan elemen dijaga berdasarkan indeks posisi $0, 1, 2, \dots$), elemen dalam `set` **tidak memiliki urutan posisi yang tetap**.

2. **Kaitannya dengan Implementasi Hash Table:**
   - Di balik layar, tipe data `set` diimplementasikan menggunakan **Hash Table** (tabel hash).
   - Ketika elemen dimasukkan ke dalam `set`, Python menghitung nilai hash dari elemen tersebut menggunakan fungsi `hash(elemen)`. Nilai hash ini kemudian menentukan letak/slot (*bucket*) memori tempat elemen tersebut disimpan.
   - Karena lokasi penyimpanan ditentukan murni oleh rumus hash dan ukuran tabel internal (yang sewaktu-waktu dapat berubah saat tabel mengalami penyesuaian ukuran/*resizing*), **tidak ada konsep elemen ke-0, ke-1, atau ke-n**.

3. **Kesimpulan:**
   - Sintaks pengindeksan seperti `my_set[0]` tidak diizinkan dan akan menghasilkan error `TypeError: 'set' object is not subscriptable`, karena indeks numerik tidak bermakna pada struktur data berbasis *hash table* yang tidak berurutan.

---

## Soal 3
**Apa yang dimaksud dengan hashable dalam konteks Python? Sebutkan tiga tipe data yang hashable dan tiga yang tidak hashable. Mengapa kunci dictionary harus hashable?**

### Jawaban:

### 1. Pengertian Hashable
Suatu objek di Python dikatakan **hashable** jika:
1. Objek tersebut memiliki nilai hash tetap sepanjang masa hidupnya (memiliki method `__hash__()`).
2. Objek tersebut dapat dibandingkan dengan objek lain untuk kesetaraan nilai (memiliki method `__eq__()`).
3. Jika dua objek bernilai sama (`a == b`), maka nilai hash keduanya harus identik (`hash(a) == hash(b)`).

Secara umum di Python, objek yang **immutable** (tidak dapat diubah) bersifat **hashable**, sedangkan objek yang **mutable** bersifat **unhashable**.

### 2. Tiga Tipe Data Hashable dan Tiga Tidak Hashable
- **Tipe Data Hashable:**
  1. `int` / `float` (bilangan bulat/desimal)
  2. `str` (string/teks)
  3. `tuple` (selama seluruh elemen di dalamnya juga bertipe hashable)
  *(Contoh lain: `bool`, `frozenset`)*

- **Tipe Data Tidak Hashable (Unhashable):**
  1. `list`
  2. `dict`
  3. `set`

### 3. Mengapa Kunci (Key) Dictionary Harus Hashable?
- Dictionary di Python diimplementasikan menggunakan **Hash Table** untuk mencapai kecepatan pencarian data $O(1)$ (*amortized constant time*).
- Ketika kita mengakses `my_dict[key]`, Python langsung memanggil `hash(key)` untuk mengkalkulasi indeks memori tempat nilai (*value*) disimpan tanpa perlu memeriksa elemen satu per satu.
- Jika sebuah *key* bersifat *mutable* (misalnya list), nilainya bisa berubah sewaktu-waktu di masa depan. Akibatnya, nilai hash objek tersebut akan berubah, sehingga Python tidak akan lagi bisa menemukan lokasi penyimpanan nilai yang berasosiasi dengan kunci tersebut pada tabel hash. Oleh sebab itu, kunci dictionary diwajibkan *hashable*.

---

## Soal 4
**Jelaskan mengapa pencarian keanggotaan (operator in) pada set memiliki kompleksitas O(1) sedangkan pada list O(n). Apa implikasi praktisnya untuk data besar?**

### Jawaban:

### 1. Mekanisme Pencarian: Set vs List
- **Pada List ($O(n)$ - Linear Search):**
  - List menyimpan elemen secara berurutan dalam memori kontigu.
  - Untuk mengecek apakah suatu elemen ada (`x in my_list`), Python harus memeriksa elemen dari indeks ke-0 sampai akhir satu per satu secara linear sampai elemen ditemukan atau daftar habis.
  - Jika list memiliki $n$ elemen, skenario terburuk (*worst-case*) memerlukan $n$ kali perbandingan.

- **Pada Set ($O(1)$ - Hash Table Lookup):**
  - Untuk operasi `x in my_set`, Python langsung menghitung nilai hash dari `x` melalui fungsi hash, lalu melompat langsung ke slot memori (*bucket*) yang ditunjuk oleh hash tersebut.
  - Pengecekan dilakukan dalam satu langkah komputasi langsung (rata-rata konstan / *amortized constant time*), terlepas dari berapapun jumlah data di dalam set.

### 2. Implikasi Praktis untuk Data Besar
- **Skalabilitas dan Efisiensi Waktu:**
  - Jika data berjumlah $1.000.000$ elemen, melakukan pencarian `x in my_list` dapat memakan hingga $1.000.000$ kali operasi. Jika pencarian dilakukan berulang kali dalam sebuah loop berukuran $m$, total kompleksitas menjadi $O(m \times n)$ (program menjadi sangat lambat/beku).
  - Sebaliknya, jika data disimpan dalam `set`, setiap pengecekan `x in my_set` hanya membutuhkan $1$ langkah rata-rata ($O(1)$), sehingga loop menjadi $O(m \times 1) = O(m)$ (selesai dalam hitungan milidetik).
- **Rekomendasi Praktis:**
  - Gunakan `set` untuk tugas-tugas seperti *filtering*, *deduplication* (menghapus duplikat), verifikasi blacklist/whitelist ID, atau pengujian keanggotaan pada dataset besar.

---

## Soal 5
**Apa perbedaan antara metode sort() dan fungsi sorted() pada list? Kapan sebaiknya menggunakan masing-masing?**

### Jawaban:

### 1. Perbedaan Utama
| Pembeda | `list.sort()` | `sorted(iterable)` |
|---|---|---|
| **Jenis** | Merupakan **method internal** dari objek list. | Merupakan **built-in function** bawaan Python. |
| **Tipe Data Target** | **Hanya bisa** dipanggil pada objek bertipe `list`. | **Bisa menerima iterable apapun** (`list`, `tuple`, `dict`, `set`, `string`, *generator*). |
| **Cara Kerja (In-place vs New Object)** | **In-place:** Mengurutkan list secara langsung di tempat memori aslinya. Tidak membuat list baru. | **Out-of-place:** Membuat dan mengembalikan **list baru** yang sudah terurut tanpa memodifikasi data aslinya. |
| **Return Value** | Mengembalikan `None`. | Mengembalikan objek `list` baru hasil pengurutan. |
| **Efisiensi Memori** | Lebih hemat memori karena tidak menduplikasi data. | Membutuhkan memori ekstra untuk mengalokasikan list baru. |

### 2. Kapan Sebaiknya Menggunakan Masing-Masing?

#### Gunakan `list.sort()` Ketika:
1. Anda sedang bekerja khusus dengan tipe data `list` dan **tidak membutuhkan data urutan aslinya lagi**.
2. Anda menangani **dataset yang sangat besar** dan ingin menghemat penggunaan memori RAM (menghindari duplikasi objek list).

#### Gunakan `sorted()` Ketika:
1. Anda **ingin mempertahankan data asli** agar tidak berubah untuk keperluan proses lain.
2. Data yang ingin diurutkan **bukan merupakan list**, melainkan `tuple`, `dictionary` (misal mengurutkan berdasarkan key atau value), `set`, atau `string`.
3. Anda ingin menulis kode fungsional atau langsung melakukan *chaining* (misal: `for item in sorted(data): ...`).
