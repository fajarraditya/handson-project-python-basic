# =============================================================================
# problems.py  –  Bank Soal Workshop Python Pemula
#
# Struktur data:
#   CATEGORIES  → urutan & pengelompokan soal pada sidebar
#   PROBLEMS    → detail tiap soal (deskripsi, starter code, test cases)
#
# Tipe soal ("type"):
#   "standard"  → fungsi mengembalikan nilai, diuji otomatis (default)
#   "visual"    → fungsi mengembalikan matplotlib.figure.Figure, ditampilkan
# =============================================================================

# =============================================================================
# KATEGORI  (urutan tampil di sidebar)
# =============================================================================

CATEGORIES = {
    "intro": {
        "icon": "🚀",
        "title": "Percobaan Pertama",
        "problems": ["print_hello_world", "hitung_penjumlahan", "variabel_simpan", "print_perkalian", "print_multi_baris"],
    },
    "dasar": {
        "icon": "🐣",
        "title": "Dasar Python",
        "subtitle": "Variabel, tipe data, dan operasi dasar",
        "problems": ["hello_nama", "luas_persegi_panjang", "konversi_suhu"],
    },
    "kondisi": {
        "icon": "🔀",
        "title": "Kondisi (if / else)",
        "subtitle": "Percabangan dan pengambilan keputusan",
        "problems": ["cek_lulus", "cek_bilangan", "fizzbuzz"],
    },
    "loop": {
        "icon": "🔁",
        "title": "Perulangan (for / while)",
        "subtitle": "Mengulang instruksi secara terstruktur",
        "problems": ["jumlah_1_n", "hitung_mundur", "maks_list"],
    },
    "list_data": {
        "icon": "📦",
        "title": "List & Struktur Data",
        "subtitle": "List, dict, dan manipulasi koleksi data",
        "problems": ["jumlah_genap", "filter_positif", "frekuensi_kata"],
    },
    "fungsi": {
        "icon": "⚙️",
        "title": "Fungsi (Function)",
        "subtitle": "Mendefinisikan dan menggunakan fungsi",
        "problems": ["balik_string", "cek_palindrom", "faktorial"],
    },
    "library": {
        "icon": "📚",
        "title": "Import Library",
        "subtitle": "Menggunakan library bawaan & pihak ketiga",
        "problems": ["akar_kuadrat", "acak_elemen", "rata_rata_numpy"],
    },
    "visualisasi": {
        "icon": "📊",
        "title": "Visualisasi Data",
        "subtitle": "Membuat grafik dengan Matplotlib",
        "problems": ["bar_chart_nilai", "line_chart_suhu"],
    },
}


# =============================================================================
# SOAL-SOAL
# =============================================================================

PROBLEMS = {

    # =========================================================================
    # �  PERCOBAAN PERTAMA  (script — langsung tulis, tanpa fungsi)
    # =========================================================================

    "print_hello_world": {
        "title": "👋 Hello, World!",
        "type": "script",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Cetaklah kalimat berikut ke layar:

```
Hello, World!
```

Ini adalah tradisi di dunia pemrograman — hampir semua programmer pertama kali menulis program ini!

---

## Cara Pengerjaan

Pada soal ini kamu **tidak perlu membuat fungsi**. Cukup tulis perintah Python langsung.

---

## Petunjuk

Gunakan `print()` untuk mencetak teks:

```python
print("Hello, World!")
```
""",
        "function_name": "",
        "starter_code": "# Cetak teks: Hello, World!\nprint(...)\n",
        "test_cases": [
            {
                "description": "Output harus: Hello, World!",
                "expected_output": "Hello, World!",
            },
        ],
    },

    "hitung_penjumlahan": {
        "title": "➕ Penjumlahan Sederhana",
        "type": "script",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Hitung **7 + 3** dan cetak hasilnya ke layar.

Hasil yang diharapkan:

```
10
```

---

## Cara Pengerjaan

Tulis langsung ekspresi matematika di dalam `print()`:

```python
print(7 + 3)
```

---

## Petunjuk

Python bisa langsung menghitung ekspresi matematika:
- Penjumlahan : `+`
- Pengurangan : `-`
- Perkalian   : `*`
- Pembagian   : `/`
""",
        "function_name": "",
        "starter_code": "# Hitung 7 + 3 dan cetak hasilnya\nprint(...)\n",
        "test_cases": [
            {
                "description": "Output harus: 10",
                "expected_output": "10",
            },
        ],
    },

    "variabel_simpan": {
        "title": "📦 Simpan & Cetak Variabel",
        "type": "script",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buat sebuah variabel bernama **`bahasa`** dan isi dengan teks **`Python`**,
lalu cetak isi variabel tersebut.

Hasil yang diharapkan:

```
Python
```

---

## Cara Pengerjaan

Tulis langsung di editor:

```python
bahasa = "Python"
print(bahasa)
```

---

## Petunjuk

Variabel adalah tempat menyimpan data. Cara membuat variabel:
```python
nama_variabel = nilai
```
Gunakan `print()` untuk menampilkan isinya.
""",
        "function_name": "",
        "starter_code": "# Buat variabel 'bahasa' berisi 'Python', lalu cetak\nbahasa = ...\nprint(bahasa)\n",
        "test_cases": [
            {
                "description": "Output harus: Python",
                "expected_output": "Python",
            },
        ],
    },

    "print_perkalian": {
        "title": "✖️ Operasi Perkalian",
        "type": "script",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Hitung **4 × 5** dan cetak hasilnya ke layar.

Hasil yang diharapkan:

```
20
```

---

## Cara Pengerjaan

Tulis langsung ekspresi di dalam `print()`.

---

## Petunjuk

Simbol perkalian di Python adalah `*`:

```python
print(4 * 5)
```
""",
        "function_name": "",
        "starter_code": "# Hitung 4 * 5 dan cetak hasilnya\nprint(...)\n",
        "test_cases": [
            {
                "description": "Output harus: 20",
                "expected_output": "20",
            },
        ],
    },

    "print_multi_baris": {
        "title": "📋 Print Beberapa Baris",
        "type": "script",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Cetak **tiga baris** teks berikut secara berurutan:

```
Baris 1
Baris 2
Baris 3
```

---

## Cara Pengerjaan

Gunakan tiga perintah `print()` secara berturut-turut:

```python
print("Baris 1")
print("Baris 2")
print("Baris 3")
```

---

## Petunjuk

Setiap `print()` otomatis pindah ke baris baru. Urutan penulisan = urutan tampil.
""",
        "function_name": "",
        "starter_code": "print(\"Baris 1\")\n# tambahkan dua baris print lagi di bawah...\n",
        "test_cases": [
            {
                "description": "Output harus: Baris 1 / Baris 2 / Baris 3 (tiga baris)",
                "expected_output": "Baris 1\nBaris 2\nBaris 3",
            },
        ],
    },

    # =========================================================================
    # �🐣  DASAR PYTHON
    # =========================================================================

    "hello_nama": {
        "title": "👋 Sapa dengan Nama",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `sapa` yang menerima satu parameter:
- `nama` → string nama seseorang

Fungsi harus **mengembalikan** string sapaan dengan format:

```
"Halo, <nama>! Selamat belajar Python!"
```

---

## Contoh

| Input | Output |
|-------|--------|
| `"Budi"` | `"Halo, Budi! Selamat belajar Python!"` |
| `"Sari"` | `"Halo, Sari! Selamat belajar Python!"` |

---

## Petunjuk

Gunakan **f-string** untuk menyisipkan variabel ke dalam string:

```python
pesan = f"Halo, {nama}!"
```

Jangan lupa menggunakan `return` untuk mengembalikan hasilnya.
""",
        "function_name": "sapa",
        "starter_code": """\
def sapa(nama):
    # Tulis kode kamu di sini
    # Hint: gunakan f-string  →  f"Halo, {nama}! ..."
    pass
""",
        "test_cases": [
            {
                "input": ("Budi",),
                "expected": "Halo, Budi! Selamat belajar Python!",
                "description": 'sapa("Budi") → "Halo, Budi! Selamat belajar Python!"',
            },
            {
                "input": ("Sari",),
                "expected": "Halo, Sari! Selamat belajar Python!",
                "description": 'sapa("Sari") → "Halo, Sari! Selamat belajar Python!"',
            },
            {
                "input": ("Python",),
                "expected": "Halo, Python! Selamat belajar Python!",
                "description": 'sapa("Python") → "Halo, Python! Selamat belajar Python!"',
            },
        ],
    },

    "luas_persegi_panjang": {
        "title": "📐 Luas Persegi Panjang",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `hitung_luas` yang menerima dua parameter:
- `panjang` → bilangan (int atau float)
- `lebar`   → bilangan (int atau float)

Fungsi harus **mengembalikan luas persegi panjang** (panjang × lebar).

---

## Contoh

| Panjang | Lebar | Output |
|---------|-------|--------|
| `5` | `3` | `15` |
| `7` | `2` | `14` |
| `4.5` | `2.0` | `9.0` |

---

## Petunjuk

```python
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas
```
""",
        "function_name": "hitung_luas",
        "starter_code": """\
def hitung_luas(panjang, lebar):
    # Tulis kode kamu di sini
    # Rumus: luas = panjang * lebar
    pass
""",
        "test_cases": [
            {"input": (5, 3),     "expected": 15,  "description": "hitung_luas(5, 3) → 15"},
            {"input": (7, 2),     "expected": 14,  "description": "hitung_luas(7, 2) → 14"},
            {"input": (4.5, 2.0), "expected": 9.0, "description": "hitung_luas(4.5, 2.0) → 9.0"},
            {"input": (1, 1),     "expected": 1,   "description": "hitung_luas(1, 1) → 1"},
        ],
    },

    "konversi_suhu": {
        "title": "🌡️ Konversi Suhu",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `celsius_ke_fahrenheit` yang menerima satu parameter:
- `celsius` → suhu dalam derajat Celsius (float atau int)

Fungsi harus **mengembalikan suhu dalam Fahrenheit**.

Rumus: **F = (C × 9/5) + 32**

---

## Contoh

| Input (°C) | Output (°F) |
|------------|-------------|
| `0` | `32.0` |
| `100` | `212.0` |
| `37` | `98.6` |

---

## Petunjuk

```python
fahrenheit = (celsius * 9/5) + 32
return fahrenheit
```
""",
        "function_name": "celsius_ke_fahrenheit",
        "starter_code": """\
def celsius_ke_fahrenheit(celsius):
    # Tulis kode kamu di sini
    # Rumus: (celsius * 9/5) + 32
    pass
""",
        "test_cases": [
            {"input": (0,),   "expected": 32.0,  "description": "0°C → 32.0°F"},
            {"input": (100,), "expected": 212.0, "description": "100°C → 212.0°F"},
            {"input": (37,),  "expected": 98.6,  "description": "37°C → 98.6°F"},
            {"input": (-40,), "expected": -40.0, "description": "-40°C → -40.0°F"},
        ],
    },

    # =========================================================================
    # 🔀  KONDISI (if / else)
    # =========================================================================

    "cek_lulus": {
        "title": "📝 Cek Kelulusan",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `cek_lulus` yang menerima satu parameter:
- `nilai` → bilangan bulat (0–100)

Fungsi harus mengembalikan:
- `"Lulus"` jika nilai **≥ 70**
- `"Tidak Lulus"` jika nilai **< 70**

---

## Contoh

| Input | Output |
|-------|--------|
| `85` | `"Lulus"` |
| `70` | `"Lulus"` |
| `65` | `"Tidak Lulus"` |

---

## Petunjuk

```python
if nilai >= 70:
    return "Lulus"
else:
    return "Tidak Lulus"
```
""",
        "function_name": "cek_lulus",
        "starter_code": """\
def cek_lulus(nilai):
    # Jika nilai >= 70, kembalikan "Lulus"
    # Jika tidak, kembalikan "Tidak Lulus"
    pass
""",
        "test_cases": [
            {"input": (85,),  "expected": "Lulus",       "description": "cek_lulus(85) → 'Lulus'"},
            {"input": (70,),  "expected": "Lulus",       "description": "cek_lulus(70) → 'Lulus' (tepat batas)"},
            {"input": (65,),  "expected": "Tidak Lulus", "description": "cek_lulus(65) → 'Tidak Lulus'"},
            {"input": (0,),   "expected": "Tidak Lulus", "description": "cek_lulus(0) → 'Tidak Lulus'"},
            {"input": (100,), "expected": "Lulus",       "description": "cek_lulus(100) → 'Lulus'"},
        ],
    },

    "cek_bilangan": {
        "title": "➕ Positif, Negatif, atau Nol?",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `cek_bilangan` yang menerima satu parameter:
- `n` → bilangan bulat

Fungsi harus mengembalikan:
- `"Positif"` jika `n > 0`
- `"Negatif"` jika `n < 0`
- `"Nol"`     jika `n == 0`

---

## Contoh

| Input | Output |
|-------|--------|
| `5` | `"Positif"` |
| `-3` | `"Negatif"` |
| `0` | `"Nol"` |

---

## Petunjuk

Gunakan `if`, `elif`, dan `else`:

```python
if n > 0:
    return "Positif"
elif n < 0:
    return "Negatif"
else:
    return "Nol"
```
""",
        "function_name": "cek_bilangan",
        "starter_code": """\
def cek_bilangan(n):
    # Cek apakah n positif, negatif, atau nol
    pass
""",
        "test_cases": [
            {"input": (5,),   "expected": "Positif", "description": "cek_bilangan(5) → 'Positif'"},
            {"input": (-3,),  "expected": "Negatif", "description": "cek_bilangan(-3) → 'Negatif'"},
            {"input": (0,),   "expected": "Nol",     "description": "cek_bilangan(0) → 'Nol'"},
            {"input": (100,), "expected": "Positif", "description": "cek_bilangan(100) → 'Positif'"},
        ],
    },

    "fizzbuzz": {
        "title": "🎯 FizzBuzz",
        "difficulty": "Sedang",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `fizzbuzz` yang menerima satu parameter:
- `n` → bilangan bulat positif

Fungsi harus mengembalikan:
- `"FizzBuzz"` jika `n` habis dibagi **3 dan 5**
- `"Fizz"`     jika `n` habis dibagi **3** saja
- `"Buzz"`     jika `n` habis dibagi **5** saja
- `str(n)`     jika tidak memenuhi kondisi di atas

---

## Contoh

| Input | Output |
|-------|--------|
| `15` | `"FizzBuzz"` |
| `9` | `"Fizz"` |
| `10` | `"Buzz"` |
| `7` | `"7"` |

---

## Petunjuk

> ⚠️ Cek kondisi `n % 3 == 0 and n % 5 == 0` **terlebih dahulu**!

```python
if n % 3 == 0 and n % 5 == 0:
    return "FizzBuzz"
```
""",
        "function_name": "fizzbuzz",
        "starter_code": """\
def fizzbuzz(n):
    # Hint: cek FizzBuzz dulu (habis dibagi 3 DAN 5),
    # baru cek Fizz, lalu Buzz, lalu kembalikan str(n)
    pass
""",
        "test_cases": [
            {"input": (15,), "expected": "FizzBuzz", "description": "fizzbuzz(15) → 'FizzBuzz'"},
            {"input": (9,),  "expected": "Fizz",     "description": "fizzbuzz(9) → 'Fizz'"},
            {"input": (10,), "expected": "Buzz",     "description": "fizzbuzz(10) → 'Buzz'"},
            {"input": (7,),  "expected": "7",        "description": "fizzbuzz(7) → '7'"},
            {"input": (30,), "expected": "FizzBuzz", "description": "fizzbuzz(30) → 'FizzBuzz'"},
            {"input": (1,),  "expected": "1",        "description": "fizzbuzz(1) → '1'"},
        ],
    },

    # =========================================================================
    # 🔁  PERULANGAN (for / while)
    # =========================================================================

    "jumlah_1_n": {
        "title": "Σ Jumlah 1 sampai N",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `jumlah_1_n` yang menerima satu parameter:
- `n` → bilangan bulat positif

Fungsi harus mengembalikan **jumlah semua bilangan dari 1 sampai n** (inklusif).

Hasil = 1 + 2 + 3 + ... + n

---

## Contoh

| Input | Output | Penjelasan |
|-------|--------|------------|
| `5` | `15` | 1+2+3+4+5 |
| `10` | `55` | 1+2+...+10 |
| `1` | `1` | hanya 1 |

---

## Petunjuk

```python
total = 0
for i in range(1, n + 1):
    total = total + i
return total
```
""",
        "function_name": "jumlah_1_n",
        "starter_code": """\
def jumlah_1_n(n):
    total = 0
    # Gunakan for loop untuk menjumlahkan 1 sampai n
    # Hint: for i in range(1, n + 1):
    pass
""",
        "test_cases": [
            {"input": (5,),   "expected": 15,   "description": "jumlah_1_n(5) → 15"},
            {"input": (10,),  "expected": 55,   "description": "jumlah_1_n(10) → 55"},
            {"input": (1,),   "expected": 1,    "description": "jumlah_1_n(1) → 1"},
            {"input": (100,), "expected": 5050, "description": "jumlah_1_n(100) → 5050"},
        ],
    },

    "hitung_mundur": {
        "title": "⏱️ Hitung Mundur",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `hitung_mundur` yang menerima satu parameter:
- `n` → bilangan bulat positif

Fungsi harus mengembalikan **list** berisi bilangan dari `n` turun ke `1`.

---

## Contoh

| Input | Output |
|-------|--------|
| `5` | `[5, 4, 3, 2, 1]` |
| `3` | `[3, 2, 1]` |
| `1` | `[1]` |

---

## Petunjuk

```python
for i in range(n, 0, -1):   # mulai dari n, berhenti sebelum 0, turun -1
    hasil.append(i)
```
""",
        "function_name": "hitung_mundur",
        "starter_code": """\
def hitung_mundur(n):
    hasil = []
    # Gunakan range(n, 0, -1) untuk menghitung mundur
    pass
""",
        "test_cases": [
            {"input": (5,), "expected": [5, 4, 3, 2, 1], "description": "hitung_mundur(5) → [5,4,3,2,1]"},
            {"input": (3,), "expected": [3, 2, 1],       "description": "hitung_mundur(3) → [3,2,1]"},
            {"input": (1,), "expected": [1],              "description": "hitung_mundur(1) → [1]"},
        ],
    },

    "maks_list": {
        "title": "🏆 Nilai Maksimum",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `cari_maks` yang menerima satu parameter:
- `numbers` → list bilangan (tidak kosong)

Fungsi harus mengembalikan **nilai terbesar** dalam list,
**tanpa menggunakan fungsi bawaan `max()`**.

---

## Contoh

| Input | Output |
|-------|--------|
| `[3, 1, 4, 1, 5, 9]` | `9` |
| `[10, 20, 5]` | `20` |
| `[7]` | `7` |

---

## Petunjuk

```python
terbesar = numbers[0]       # anggap elemen pertama terbesar
for angka in numbers:
    if angka > terbesar:
        terbesar = angka    # perbarui jika ketemu yang lebih besar
return terbesar
```
""",
        "function_name": "cari_maks",
        "starter_code": """\
def cari_maks(numbers):
    # Jangan gunakan max() bawaan Python!
    # Hint: simpan nilai terbesar sementara di variabel
    terbesar = numbers[0]
    pass
""",
        "test_cases": [
            {"input": ([3, 1, 4, 1, 5, 9],), "expected": 9,  "description": "cari_maks([3,1,4,1,5,9]) → 9"},
            {"input": ([10, 20, 5],),          "expected": 20, "description": "cari_maks([10,20,5]) → 20"},
            {"input": ([7],),                  "expected": 7,  "description": "cari_maks([7]) → 7"},
            {"input": ([-1, -5, -2],),         "expected": -1, "description": "cari_maks([-1,-5,-2]) → -1"},
        ],
    },

    # =========================================================================
    # 📦  LIST & STRUKTUR DATA
    # =========================================================================

    "jumlah_genap": {
        "title": "➕ Jumlah Bilangan Genap",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `jumlah_genap` yang menerima satu parameter:
- `numbers` → list bilangan bulat

Fungsi harus **mengembalikan jumlah semua bilangan genap** dalam list.

---

## Contoh

| Input | Output |
|-------|--------|
| `[1, 2, 3, 4, 5]` | `6` |
| `[10, 15, 20]` | `30` |
| `[1, 3, 5]` | `0` |

---

## Petunjuk

```python
if angka % 2 == 0:   # angka ini genap!
    total += angka
```
""",
        "function_name": "jumlah_genap",
        "starter_code": """\
def jumlah_genap(numbers):
    total = 0
    # Loop tiap angka, cek apakah genap (angka % 2 == 0)
    pass
""",
        "test_cases": [
            {"input": ([1, 2, 3, 4, 5],), "expected": 6,  "description": "jumlah_genap([1,2,3,4,5]) → 6"},
            {"input": ([10, 15, 20],),     "expected": 30, "description": "jumlah_genap([10,15,20]) → 30"},
            {"input": ([1, 3, 5],),        "expected": 0,  "description": "jumlah_genap([1,3,5]) → 0"},
            {"input": ([2, 4, 6, 8],),     "expected": 20, "description": "jumlah_genap([2,4,6,8]) → 20"},
            {"input": ([],),               "expected": 0,  "description": "jumlah_genap([]) → 0"},
        ],
    },

    "filter_positif": {
        "title": "🔍 Filter Bilangan Positif",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `filter_positif` yang menerima satu parameter:
- `numbers` → list bilangan bulat

Fungsi harus mengembalikan **list baru** yang hanya berisi bilangan **> 0**.

---

## Contoh

| Input | Output |
|-------|--------|
| `[-2, 3, 0, -1, 5]` | `[3, 5]` |
| `[1, 2, 3]` | `[1, 2, 3]` |
| `[-1, -2]` | `[]` |

---

## Petunjuk

```python
hasil = []
for angka in numbers:
    if angka > 0:
        hasil.append(angka)
return hasil
```
""",
        "function_name": "filter_positif",
        "starter_code": """\
def filter_positif(numbers):
    hasil = []
    # Loop tiap angka, tambahkan ke hasil jika > 0
    pass
""",
        "test_cases": [
            {"input": ([-2, 3, 0, -1, 5],), "expected": [3, 5],    "description": "filter_positif([-2,3,0,-1,5]) → [3,5]"},
            {"input": ([1, 2, 3],),          "expected": [1, 2, 3], "description": "filter_positif([1,2,3]) → [1,2,3]"},
            {"input": ([-1, -2],),           "expected": [],        "description": "filter_positif([-1,-2]) → []"},
            {"input": ([0, 0, 0],),          "expected": [],        "description": "filter_positif([0,0,0]) → []"},
        ],
    },

    "frekuensi_kata": {
        "title": "📊 Hitung Frekuensi Kata",
        "difficulty": "Sedang",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `hitung_frekuensi` yang menerima satu parameter:
- `kata_list` → list string

Fungsi harus mengembalikan **dictionary** yang berisi setiap kata
beserta jumlah kemunculannya.

---

## Contoh

```python
hitung_frekuensi(["apel", "jeruk", "apel", "mangga", "jeruk", "apel"])
# → {"apel": 3, "jeruk": 2, "mangga": 1}
```

---

## Petunjuk

```python
frekuensi = {}
for kata in kata_list:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1
return frekuensi
```
""",
        "function_name": "hitung_frekuensi",
        "starter_code": """\
def hitung_frekuensi(kata_list):
    frekuensi = {}
    # Loop tiap kata, tambahkan ke dictionary
    pass
""",
        "test_cases": [
            {
                "input": (["apel", "jeruk", "apel", "mangga", "jeruk", "apel"],),
                "expected": {"apel": 3, "jeruk": 2, "mangga": 1},
                "description": 'hitung_frekuensi([...]) → {"apel":3,"jeruk":2,"mangga":1}',
            },
            {
                "input": (["a", "b", "a"],),
                "expected": {"a": 2, "b": 1},
                "description": 'hitung_frekuensi(["a","b","a"]) → {"a":2,"b":1}',
            },
            {
                "input": (["satu"],),
                "expected": {"satu": 1},
                "description": 'hitung_frekuensi(["satu"]) → {"satu":1}',
            },
            {
                "input": ([],),
                "expected": {},
                "description": "hitung_frekuensi([]) → {}",
            },
        ],
    },

    # =========================================================================
    # ⚙️  FUNGSI (Function)
    # =========================================================================

    "balik_string": {
        "title": "🔄 Balik String",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `balik_string` yang menerima satu parameter:
- `s` → string

Fungsi harus **mengembalikan string yang dibalik**.

---

## Contoh

| Input | Output |
|-------|--------|
| `"hello"` | `"olleh"` |
| `"Python"` | `"nohtyP"` |
| `"abcde"` | `"edcba"` |

---

## Petunjuk

Kamu bisa menggunakan **slice** pada string Python:

```python
s[::-1]  # cara singkat untuk membalik string
```

Atau kamu bisa menggunakan **loop** biasa:

```python
hasil = ""
for karakter in s:
    hasil = karakter + hasil
return hasil
```

---

## Petunjuk

Cara singkat dengan **slice**:

```python
return s[::-1]
```

Atau dengan **loop**:

```python
hasil = ""
for karakter in s:
    hasil = karakter + hasil
return hasil
```
""",
        "function_name": "balik_string",
        "starter_code": """\
def balik_string(s):
    # Tulis kode kamu di sini
    # Cara mudah: return s[::-1]
    pass
""",
        "test_cases": [
            {"input": ("hello",),  "expected": "olleh",  "description": 'balik_string("hello") → "olleh"'},
            {"input": ("Python",), "expected": "nohtyP", "description": 'balik_string("Python") → "nohtyP"'},
            {"input": ("abcde",),  "expected": "edcba",  "description": 'balik_string("abcde") → "edcba"'},
            {"input": ("a",),      "expected": "a",      "description": 'balik_string("a") → "a"'},
            {"input": ("",),       "expected": "",       "description": 'balik_string("") → ""'},
        ],
    },

    "cek_palindrom": {
        "title": "🪞 Cek Palindrom",
        "difficulty": "Sedang",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `cek_palindrom` yang menerima satu parameter:
- `s` → string

Kembalikan `True` jika palindrom, `False` jika bukan.
> ⚠️ Tidak peka huruf besar/kecil. `"Katak"` → `True`.

---

## Contoh

| Input | Output |
|-------|--------|
| `"katak"` | `True` |
| `"Katak"` | `True` |
| `"hello"` | `False` |
| `"level"` | `True` |

---

## Petunjuk

```python
s = s.lower()          # ubah ke huruf kecil
return s == s[::-1]    # bandingkan dengan versi terbaliknya
```
""",
        "function_name": "cek_palindrom",
        "starter_code": """\
def cek_palindrom(s):
    # Hint 1: ubah ke huruf kecil → s.lower()
    # Hint 2: bandingkan dengan versi terbaliknya
    pass
""",
        "test_cases": [
            {"input": ("katak",), "expected": True,  "description": 'cek_palindrom("katak") → True'},
            {"input": ("Katak",), "expected": True,  "description": 'cek_palindrom("Katak") → True (case-insensitive)'},
            {"input": ("hello",), "expected": False, "description": 'cek_palindrom("hello") → False'},
            {"input": ("level",), "expected": True,  "description": 'cek_palindrom("level") → True'},
            {"input": ("a",),     "expected": True,  "description": 'cek_palindrom("a") → True'},
        ],
    },

    "faktorial": {
        "title": "🔢 Faktorial",
        "difficulty": "Sedang",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `faktorial` yang menerima satu parameter:
- `n` → bilangan bulat non-negatif

Fungsi harus mengembalikan **n!** (n faktorial).

n! = n × (n-1) × (n-2) × ... × 1, dan 0! = 1 (dengan definisi).

---

## Contoh

| Input | Output | Penjelasan |
|-------|--------|------------|
| `5` | `120` | 5×4×3×2×1 |
| `3` | `6` | 3×2×1 |
| `0` | `1` | definisi |

---

## Petunjuk

```python
hasil = 1
for i in range(1, n + 1):
    hasil *= i      # sama dengan: hasil = hasil * i
return hasil
```
""",
        "function_name": "faktorial",
        "starter_code": """\
def faktorial(n):
    hasil = 1
    # Kalikan hasil dengan setiap bilangan dari 1 sampai n
    # Hint: for i in range(1, n + 1):
    pass
""",
        "test_cases": [
            {"input": (5,), "expected": 120,  "description": "faktorial(5) → 120"},
            {"input": (3,), "expected": 6,    "description": "faktorial(3) → 6"},
            {"input": (0,), "expected": 1,    "description": "faktorial(0) → 1 (definisi)"},
            {"input": (1,), "expected": 1,    "description": "faktorial(1) → 1"},
            {"input": (7,), "expected": 5040, "description": "faktorial(7) → 5040"},
        ],
    },

    # =========================================================================
    # 📚  IMPORT LIBRARY
    # =========================================================================

    "akar_kuadrat": {
        "title": "√ Akar Kuadrat (math)",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `akar_kuadrat` yang menerima satu parameter:
- `n` → bilangan bulat positif

Fungsi harus mengembalikan **akar kuadrat dari n** (float),
menggunakan library **`math`**.

---

## Contoh

| Input | Output |
|-------|--------|
| `9` | `3.0` |
| `16` | `4.0` |

---

## Petunjuk

```python
import math

def akar_kuadrat(n):
    return math.sqrt(n)
```

> 💡 `import` ditulis di atas atau di dalam fungsi.
""",
        "function_name": "akar_kuadrat",
        "starter_code": """\
import math

def akar_kuadrat(n):
    # Gunakan math.sqrt(n) untuk menghitung akar kuadrat
    pass
""",
        "test_cases": [
            {"input": (9,),  "expected": 3.0, "description": "akar_kuadrat(9) → 3.0"},
            {"input": (16,), "expected": 4.0, "description": "akar_kuadrat(16) → 4.0"},
            {"input": (25,), "expected": 5.0, "description": "akar_kuadrat(25) → 5.0"},
            {"input": (1,),  "expected": 1.0, "description": "akar_kuadrat(1) → 1.0"},
        ],
    },

    "acak_elemen": {
        "title": "🎲 Ambil Elemen Acak (random)",
        "difficulty": "Mudah",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `ambil_acak` yang menerima dua parameter:
- `items` → list elemen
- `seed`  → bilangan bulat untuk mengatur hasil acak

Fungsi harus:
1. Set seed dengan `random.seed(seed)`
2. Mengembalikan **satu elemen acak** menggunakan `random.choice(items)`

---

## Contoh

```python
ambil_acak(["apel", "jeruk", "mangga"], seed=42)
# → "mangga"  (hasil tetap sama karena seed sama)
```

---

## Petunjuk

```python
import random

def ambil_acak(items, seed):
    random.seed(seed)
    return random.choice(items)
```

> 💡 `random.seed()` memastikan hasil "acak" bisa diprediksi untuk testing.
""",
        "function_name": "ambil_acak",
        "starter_code": """\
import random

def ambil_acak(items, seed):
    random.seed(seed)
    # Gunakan random.choice(items) untuk mengambil elemen acak
    pass
""",
        "test_cases": [
            {
                "input": (["apel", "jeruk", "mangga"], 42),
                "expected": "mangga",
                "description": 'ambil_acak(["apel","jeruk","mangga"], 42) → "mangga"',
            },
            {
                "input": ([1, 2, 3, 4, 5], 0),
                "expected": 4,
                "description": "ambil_acak([1,2,3,4,5], 0) → 4",
            },
            {
                "input": (["a", "b", "c"], 7),
                "expected": "a",
                "description": 'ambil_acak(["a","b","c"], 7) → "a"',
            },
        ],
    },

    "rata_rata_numpy": {
        "title": "📐 Statistik Array (NumPy)",
        "difficulty": "Sedang",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `hitung_statistik` yang menerima satu parameter:
- `data` → list bilangan

Fungsi harus mengembalikan **dictionary** berisi:
- `"mean"`   → rata-rata (`np.mean`)
- `"median"` → nilai tengah (`np.median`)
- `"std"`    → standar deviasi dibulatkan 2 desimal (`np.std`)

---

## Contoh

```python
hitung_statistik([2, 4, 4, 4, 5, 5, 7, 9])
# → {"mean": 5.0, "median": 4.5, "std": 1.77}
```

---

## Petunjuk

```python
import numpy as np

def hitung_statistik(data):
    arr = np.array(data)
    return {
        "mean":   float(np.mean(arr)),
        "median": float(np.median(arr)),
        "std":    round(float(np.std(arr)), 2),
    }
```
""",
        "function_name": "hitung_statistik",
        "starter_code": """\
import numpy as np

def hitung_statistik(data):
    arr = np.array(data)
    # Hitung mean, median, dan std
    # Kembalikan sebagai dictionary
    pass
""",
        "test_cases": [
            {
                "input": ([2, 4, 4, 4, 5, 5, 7, 9],),
                "expected": {"mean": 5.0, "median": 4.5, "std": 1.77},
                "description": "hitung_statistik([2,4,4,4,5,5,7,9]) → {mean:5.0, median:4.5, std:1.77}",
            },
            {
                "input": ([1, 2, 3, 4, 5],),
                "expected": {"mean": 3.0, "median": 3.0, "std": 1.41},
                "description": "hitung_statistik([1,2,3,4,5]) → {mean:3.0, median:3.0, std:1.41}",
            },
            {
                "input": ([10, 10, 10],),
                "expected": {"mean": 10.0, "median": 10.0, "std": 0.0},
                "description": "hitung_statistik([10,10,10]) → {mean:10.0, median:10.0, std:0.0}",
            },
        ],
    },

    # =========================================================================
    # 📊  VISUALISASI DATA  (type: "visual")
    #   Fungsi mengembalikan matplotlib.figure.Figure
    #   Dinilai secara visual, bukan dengan test case nilai
    # =========================================================================

    "bar_chart_nilai": {
        "title": "📊 Bar Chart Nilai Siswa",
        "difficulty": "Sedang",
        "type": "visual",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `buat_bar_chart` yang **tidak menerima parameter**.

Fungsi harus membuat dan **mengembalikan** sebuah `matplotlib.figure.Figure`
yang menampilkan **bar chart (diagram batang)** nilai 5 siswa:

| Nama | Nilai |
|------|-------|
| Andi | 85 |
| Budi | 72 |
| Cici | 90 |
| Dedi | 68 |
| Eka | 95 |

---

## Petunjuk

```python
import matplotlib.pyplot as plt

def buat_bar_chart():
    nama  = ["Andi", "Budi", "Cici", "Dedi", "Eka"]
    nilai = [85, 72, 90, 68, 95]

    fig, ax = plt.subplots()
    ax.bar(nama, nilai, color="steelblue")
    ax.set_title("Nilai Siswa")
    ax.set_xlabel("Nama")
    ax.set_ylabel("Nilai")

    return fig     # ← wajib dikembalikan!
```

> ⚠️ **Jangan gunakan `plt.show()`** — kembalikan objek `fig` saja.
""",
        "function_name": "buat_bar_chart",
        "starter_code": """\
import matplotlib.pyplot as plt

def buat_bar_chart():
    nama  = ["Andi", "Budi", "Cici", "Dedi", "Eka"]
    nilai = [85, 72, 90, 68, 95]

    fig, ax = plt.subplots()
    # Buat bar chart menggunakan ax.bar(...)
    # Tambahkan judul dan label sumbu
    # Jangan lupa: return fig

    pass
""",
        "test_cases": [],
    },

    "line_chart_suhu": {
        "title": "📈 Line Chart Suhu Mingguan",
        "difficulty": "Sedang",
        "type": "visual",
        "description": """
## Deskripsi Soal

Buatlah fungsi bernama `buat_line_chart` yang **tidak menerima parameter**.

Fungsi harus membuat dan **mengembalikan** sebuah `matplotlib.figure.Figure`
yang menampilkan **line chart (grafik garis)** suhu harian selama seminggu:

| Hari | Suhu (°C) |
|------|-----------|
| Senin | 28 |
| Selasa | 30 |
| Rabu | 27 |
| Kamis | 32 |
| Jumat | 29 |
| Sabtu | 26 |
| Minggu | 31 |

---

## Petunjuk

```python
import matplotlib.pyplot as plt

def buat_line_chart():
    hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    suhu = [28, 30, 27, 32, 29, 26, 31]

    fig, ax = plt.subplots()
    ax.plot(hari, suhu, marker="o", color="tomato")
    ax.set_title("Suhu Harian Minggu Ini")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Suhu (°C)")

    return fig
```

> ⚠️ **Jangan gunakan `plt.show()`** — kembalikan objek `fig` saja.
""",
        "function_name": "buat_line_chart",
        "starter_code": """\
import matplotlib.pyplot as plt

def buat_line_chart():
    hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    suhu = [28, 30, 27, 32, 29, 26, 31]

    fig, ax = plt.subplots()
    # Buat line chart dengan ax.plot(...)
    # Tambahkan marker, judul, dan label sumbu
    # Jangan lupa: return fig

    pass
""",
        "test_cases": [],
    },
}


# =============================================================================
# CARA MENAMBAHKAN SOAL BARU:
#
# 1. Tambahkan entry baru ke PROBLEMS (salin template di bawah)
# 2. Daftarkan key-nya ke CATEGORIES yang sesuai (atau buat kategori baru)
#
# Template soal standard:
# ─────────────────────────────────────────────────────────────────
# "key_soal": {
#     "title": "Judul Soal",
#     "difficulty": "Mudah",        # Mudah / Sedang / Sulit
#     "description": """...""",     # Markdown
#     "function_name": "nama_fungsi",
#     "starter_code": """\
# def nama_fungsi(param):
#     pass
# """,
#     "test_cases": [
#         {
#             "input": (arg1,),      # selalu tuple, tambah koma jika 1 argumen
#             "expected": hasil,
#             "description": "penjelasan",
#         },
#     ],
# },
#
# Template soal visual (matplotlib):
# ─────────────────────────────────────────────────────────────────
# "key_soal_visual": {
#     "title": "Judul Soal",
#     "difficulty": "Sedang",
#     "type": "visual",              # ← wajib untuk soal visualisasi
#     "description": """...""",
#     "function_name": "nama_fungsi",
#     "starter_code": """...""",
#     "test_cases": [],              # kosong – dinilai visual
# },
# =============================================================================
