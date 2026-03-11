# =============================================================================
# app.py  –  Workshop Python Pemula: LeetCode-style Problem Solver
# Framework: Streamlit
#
# Cara menjalankan:
#   streamlit run app.py
# =============================================================================

import io
import contextlib
import traceback
import streamlit as st
from streamlit_ace import st_ace
from problems import PROBLEMS, CATEGORIES

# =============================================================================
# KONFIGURASI HALAMAN
# =============================================================================

st.set_page_config(
    page_title="Python Workshop – Hands-on Project",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# CUSTOM CSS
# =============================================================================

st.markdown(
    """
    <style>
    /* Warna latar belakang utama */
    .main { background-color: #0f1117; }

    /* Kartu hasil test case */
    .test-pass {
        background-color: #1a3a2a;
        border-left: 4px solid #00c853;
        padding: 10px 14px;
        border-radius: 6px;
        margin-bottom: 8px;
        color: #e0ffe0;
    }
    .test-fail {
        background-color: #3a1a1a;
        border-left: 4px solid #ff1744;
        padding: 10px 14px;
        border-radius: 6px;
        margin-bottom: 8px;
        color: #ffe0e0;
    }
    .test-error {
        background-color: #3a2a1a;
        border-left: 4px solid #ff9100;
        padding: 10px 14px;
        border-radius: 6px;
        margin-bottom: 8px;
        color: #fff3e0;
    }

    /* Ringkasan skor */
    .score-box {
        text-align: center;
        padding: 16px;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 16px;
    }
    .score-all-pass  { background-color: #1b5e20; color: #b9f6ca; }
    .score-some-pass { background-color: #e65100; color: #ffe0b2; }
    .score-all-fail  { background-color: #b71c1c; color: #ffcdd2; }

    /* Badge kesulitan */
    .badge-mudah  { color: #00e676; font-weight: bold; }
    .badge-sedang { color: #ffab40; font-weight: bold; }
    .badge-sulit  { color: #ff5252; font-weight: bold; }

    /* Area kode lebih luas */
    .stTextArea textarea {
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        background-color: #1e1e2e !important;
        color: #cdd6f4 !important;
        border: 1px solid #444 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =============================================================================
# HELPER: FORMAT PESAN ERROR YANG RAMAH PEMULA
# =============================================================================

def format_error_ramah(exc: Exception, kode: str = "") -> str:
    """
    Mengubah exception Python menjadi pesan yang mudah dipahami pemula.
    Mendukung SyntaxError, IndentationError, NameError, TypeError, dll.
    """
    baris_kode = kode.splitlines()

    if isinstance(exc, (SyntaxError, IndentationError)):
        tipe   = "IndentationError (lekukan salah)" if isinstance(exc, IndentationError) else "SyntaxError (penulisan salah)"
        nomor  = exc.lineno or "?"
        baris  = (baris_kode[exc.lineno - 1].rstrip() if exc.lineno and exc.lineno <= len(baris_kode) else "")
        pesan  = exc.msg

        # Terjemahan pesan umum ke Bahasa Indonesia
        terjemahan = {
            "expected an indented block after function definition": "Setelah `def ....:` harus ada isi fungsi. Pastikan baris berikutnya menjorok ke dalam (indentasi).",
            "expected an indented block": "Blok kode ini kosong. Tambahkan isi atau gunakan `pass` sementara.",
            "unindent does not match any outer indentation level": "Jumlah spasi lekukan tidak konsisten. Gunakan 4 spasi untuk setiap tingkat.",
            "unexpected indent": "Baris ini tidak seharusnya menjorok. Hapus spasi/tab di awal baris.",
            "invalid syntax": "Penulisan kode tidak valid. Periksa tanda kurung, titik dua, atau tanda kutip.",
        }
        for kunci, nilai in terjemahan.items():
            if kunci in pesan.lower():
                pesan = nilai
                break

        msg = f"🔴 {tipe}\n"
        msg += f"   Baris ke-{nomor}: {baris}\n\n"
        msg += f"   💡 {pesan}"
        return msg

    elif isinstance(exc, NameError):
        return (
            f"🔴 NameError — Nama tidak dikenali\n"
            f"   {exc}\n\n"
            f"   💡 Pastikan variabel/fungsi sudah didefinisikan sebelum digunakan."
        )

    elif isinstance(exc, TypeError):
        return (
            f"🔴 TypeError — Tipe data tidak sesuai\n"
            f"   {exc}\n\n"
            f"   💡 Periksa apakah operasi yang kamu lakukan cocok dengan tipe datanya\n"
            f"      (misalnya: tidak bisa menjumlahkan string + angka langsung)."
        )

    elif isinstance(exc, ZeroDivisionError):
        return (
            f"🔴 ZeroDivisionError — Pembagian dengan nol\n"
            f"   💡 Kamu membagi sebuah angka dengan 0. Pastikan pembagi tidak nol."
        )

    else:
        # Fallback: tampilkan traceback ringkas
        return f"🔴 {type(exc).__name__}\n   {exc}\n\n{traceback.format_exc()}"


# =============================================================================
# FUNGSI PLAYGROUND: JALANKAN KODE BEBAS & TANGKAP OUTPUT
# =============================================================================

def jalankan_playground(kode: str) -> dict:
    """
    Menjalankan kode Python bebas (tanpa fungsi).
    Menangkap output print() dan mengembalikan error yang ramah.
    """
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            exec(kode, {"__builtins__": __builtins__})  # noqa: S102
        output = buffer.getvalue()
        return {
            "status": "ok",
            "output": output if output.strip() else "(kode berjalan, tapi tidak ada output print())",
        }
    except (SyntaxError, IndentationError) as e:
        return {"status": "error", "output": format_error_ramah(e, kode)}
    except Exception as e:
        return {"status": "error", "output": format_error_ramah(e, kode)}


# =============================================================================
# FUNGSI INTI SCRIPT: JALANKAN KODE BEBAS & BANDINGKAN OUTPUT
# =============================================================================

def jalankan_kode_script(kode_peserta: str, test_cases: list) -> list:
    """
    Menjalankan kode tanpa fungsi, menangkap stdout, dan membandingkan
    dengan expected_output pada tiap test case.
    """
    hasil = []
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            exec(kode_peserta, {"__builtins__": __builtins__})  # noqa: S102
        output = buffer.getvalue().strip()
        for tc in test_cases:
            expected = tc["expected_output"].strip()
            if output == expected:
                hasil.append({
                    "status": "pass",
                    "description": tc["description"],
                    "message": f"Output  : `{output}`",
                })
            else:
                hasil.append({
                    "status": "fail",
                    "description": tc["description"],
                    "message": f"Expected: `{expected}`\nOutput  : `{output}`  \u2190 \u274c tidak sesuai",
                })
    except (SyntaxError, IndentationError) as e:
        for tc in test_cases:
            hasil.append({"status": "error", "description": tc["description"], "message": format_error_ramah(e, kode_peserta)})
    except Exception as e:
        for tc in test_cases:
            hasil.append({"status": "error", "description": tc["description"], "message": format_error_ramah(e, kode_peserta)})
    return hasil


# =============================================================================
# FUNGSI INTI: MENJALANKAN & MENILAI KODE PESERTA
# =============================================================================

def jalankan_kode(kode_peserta: str, test_cases: list, function_name: str) -> list:
    """
    Menjalankan kode peserta dan mengujinya terhadap semua test case.

    Parameter:
        kode_peserta  : string kode Python yang ditulis peserta
        test_cases    : list dict berisi 'input', 'expected', 'description'
        function_name : nama fungsi yang harus didefinisikan peserta

    Mengembalikan:
        list of dict, masing-masing berisi:
            - status : "pass" | "fail" | "error"
            - description : deskripsi test case
            - message : pesan detail
    """
    hasil = []
    namespace = {}  # ruang nama terpisah agar kode peserta tidak mengganggu app

    # ---- Langkah 1: Jalankan definisi fungsi peserta ----
    try:
        exec(kode_peserta, namespace)  # noqa: S102
    except (SyntaxError, IndentationError) as e:
        pesan_error = format_error_ramah(e, kode_peserta)
        for tc in test_cases:
            hasil.append({
                "status": "error",
                "description": tc["description"],
                "message": pesan_error,
            })
        return hasil
    except Exception as e:
        pesan_error = format_error_ramah(e, kode_peserta)
        for tc in test_cases:
            hasil.append({
                "status": "error",
                "description": tc["description"],
                "message": pesan_error,
            })
        return hasil

    # ---- Langkah 2: Pastikan fungsi yang diminta ada ----
    if function_name not in namespace:
        for tc in test_cases:
            hasil.append({
                "status": "error",
                "description": tc["description"],
                "message": (
                    f"❌ Fungsi `{function_name}` tidak ditemukan.\n"
                    "Pastikan nama fungsi kamu sudah benar!"
                ),
            })
        return hasil

    fungsi = namespace[function_name]

    # ---- Langkah 3: Jalankan setiap test case ----
    for tc in test_cases:
        try:
            output = fungsi(*tc["input"])   # panggil fungsi dengan argumen test case

            if output == tc["expected"]:
                hasil.append({
                    "status": "pass",
                    "description": tc["description"],
                    "message": (
                        f"Input   : `{tc['input']}`\n"
                        f"Expected: `{tc['expected']}`\n"
                        f"Output  : `{output}`"
                    ),
                })
            else:
                hasil.append({
                    "status": "fail",
                    "description": tc["description"],
                    "message": (
                        f"Input   : `{tc['input']}`\n"
                        f"Expected: `{tc['expected']}`\n"
                        f"Output  : `{output}`  ← ❌ tidak sesuai"
                    ),
                })

        except Exception as e:
            hasil.append({
                "status": "error",
                "description": tc["description"],
                "message": (
                    f"Input   : {tc['input']}\n"
                    f"\n{format_error_ramah(e, kode_peserta)}"
                ),
            })

    return hasil


# =============================================================================
# SIDEBAR – PILIH SOAL
# =============================================================================

with st.sidebar:
    st.title("🐍 Python Workshop")
    st.caption("Hands-on Problem Solver")
    st.divider()

    # ── Tingkat 1: Pilih Kategori ──────────────────────────────────
    st.subheader("📚 Pilih Materi")

    cat_keys   = list(CATEGORIES.keys())
    cat_labels = [
        f"{CATEGORIES[k]['icon']}  {CATEGORIES[k]['title']}"
        for k in cat_keys
    ]

    cat_idx = st.selectbox(
        "Materi:",
        options=range(len(cat_keys)),
        format_func=lambda i: cat_labels[i],
        label_visibility="collapsed",
        key="sidebar_kategori",
    )
    kat_dipilih_key = cat_keys[cat_idx]
    kat_dipilih     = CATEGORIES[kat_dipilih_key]

    # Tampilkan subtitle kategori
    st.caption(kat_dipilih["subtitle"])

    st.divider()

    # ── Tingkat 2: Pilih Soal dalam Kategori ───────────────────────
    st.subheader("📋 Pilih Soal")

    soal_dalam_kat = kat_dipilih["problems"]
    soal_labels    = [PROBLEMS[k]["title"] for k in soal_dalam_kat]

    soal_idx = st.selectbox(
        "Soal:",
        options=range(len(soal_dalam_kat)),
        format_func=lambda i: soal_labels[i],
        label_visibility="collapsed",
        key=f"sidebar_soal_{kat_dipilih_key}",
    )
    soal_dipilih_key = soal_dalam_kat[soal_idx]
    soal             = PROBLEMS[soal_dipilih_key]

    # Tampilkan badge kesulitan
    difficulty = soal.get("difficulty", "Mudah")
    badge_class = {
        "Mudah": "badge-mudah",
        "Sedang": "badge-sedang",
        "Sulit": "badge-sulit",
    }.get(difficulty, "badge-mudah")

    st.markdown(
        f"**Tingkat Kesulitan:** <span class='{badge_class}'>{difficulty}</span>",
        unsafe_allow_html=True,
    )

    # Badge tipe soal
    tipe_soal = soal.get("type", "standard")
    if tipe_soal == "visual":
        st.markdown(
            "**Tipe:** <span style='color:#64b5f6;font-weight:bold'>📊 Visualisasi</span>",
            unsafe_allow_html=True,
        )
    elif tipe_soal == "script":
        st.markdown(
            "**Tipe:** <span style='color:#a5d6a7;font-weight:bold'>🖨️ Script Bebas</span>",
            unsafe_allow_html=True,
        )
    # Progress kategori ini
    st.divider()
    st.caption(f"Soal {soal_idx + 1} dari {len(soal_dalam_kat)} dalam materi ini")
    st.progress((soal_idx + 1) / len(soal_dalam_kat))

    st.divider()
    st.caption("💡 **Tips:** Klik 'Run Test' setelah menulis kode kamu!")
    if tipe_soal == "script":
        st.caption("📌 **Ingat:** Gunakan `print()` untuk menampilkan hasil.")
    else:
        st.caption("📌 **Ingat:** Gunakan `return` untuk mengembalikan nilai.")


# =============================================================================
# INISIALISASI SESSION STATE
# =============================================================================

kode_key  = f"kode_{soal_dipilih_key}"
hasil_key = f"hasil_{soal_dipilih_key}"

if kode_key not in st.session_state:
    st.session_state[kode_key] = soal["starter_code"]
if hasil_key not in st.session_state:
    st.session_state[hasil_key] = None

if "playground_kode" not in st.session_state:
    st.session_state["playground_kode"] = """\
# Tulis kode Python apa saja di sini!
# Gunakan print() untuk menampilkan hasil.

nama = "Python"
print(f"Halo, {nama}!")

# Coba operasi matematika
angka = 10
print(angka * 2)
"""
if "playground_hasil" not in st.session_state:
    st.session_state["playground_hasil"] = None


# =============================================================================
# LAYOUT UTAMA – TABS
# =============================================================================

tab_playground, tab_soal = st.tabs(["🧪  Python Playground", "📚  Latihan Soal"])


# ═══════════════════════════════════════════════════════════════════════════
# TAB 1 — LATIHAN SOAL
# ═══════════════════════════════════════════════════════════════════════════
with tab_soal:

 st.title(soal["title"])
 st.divider()

 kolom_soal, kolom_editor = st.columns([1, 1], gap="large")

 # -----------------------------------------------------------------------
 # KOLOM KIRI: Deskripsi Soal
 # -----------------------------------------------------------------------
 with kolom_soal:
    st.subheader("📄 Deskripsi Soal")
    st.markdown(soal["description"], unsafe_allow_html=False)

    if tipe_soal in ("standard", "script") and soal["test_cases"]:
        with st.expander("👀 Lihat semua test case yang akan diuji", expanded=False):
            for i, tc in enumerate(soal["test_cases"], start=1):
                st.markdown(f"**Test {i}:** {tc['description']}")
    elif tipe_soal == "visual":
        st.info("💡 Soal ini dinilai secara visual — fungsi kamu harus mengembalikan objek `matplotlib.figure.Figure`.")


 # -----------------------------------------------------------------------
 # KOLOM KANAN: Editor Kode + Tombol + Hasil
 # -----------------------------------------------------------------------
 with kolom_editor:
    st.subheader("✏️ Editor Kode Python")

    _ace_val = st_ace(
        value=st.session_state[kode_key],
        language="python",
        theme="monokai",
        keybinding="vscode",
        font_size=14,
        tab_size=4,
        show_gutter=True,
        show_print_margin=False,
        wrap=False,
        auto_update=True,
        height=280,
        key=f"ace_{soal_dipilih_key}",
    )
    kode_peserta = _ace_val if _ace_val is not None else st.session_state[kode_key]
    st.session_state[kode_key] = kode_peserta

    col_run, col_reset = st.columns([2, 1])
    with col_run:
        tombol_run = st.button("▶️ Run Test", type="primary", use_container_width=True)
    with col_reset:
        tombol_reset = st.button("🔄 Reset", type="secondary", use_container_width=True)

    if tombol_reset:
        st.session_state[kode_key] = soal["starter_code"]
        st.session_state[hasil_key] = None
        st.rerun()

    if tombol_run:
        if not kode_peserta.strip():
            st.warning("⚠️ Editor kode masih kosong. Tulis kode kamu terlebih dahulu!")
        elif tipe_soal == "visual":
            # ── Mode Visual: jalankan & tampilkan figure ──────────────
            with st.spinner("⏳ Menjalankan kode..."):
                namespace = {}
                try:
                    exec(kode_peserta, namespace)  # noqa: S102
                    func = namespace.get(soal["function_name"])
                    if func is None:
                        st.session_state[hasil_key] = {
                            "status": "error",
                            "message": f"❌ Fungsi `{soal['function_name']}` tidak ditemukan.",
                        }
                    else:
                        fig = func()
                        import matplotlib.figure
                        if isinstance(fig, matplotlib.figure.Figure):
                            st.session_state[hasil_key] = {"status": "visual", "fig": fig}
                        else:
                            st.session_state[hasil_key] = {
                                "status": "error",
                                "message": (
                                    "❌ Fungsi harus mengembalikan objek "
                                    "`matplotlib.figure.Figure`.\n"
                                    f"Tapi yang dikembalikan: `{type(fig)}`"
                                ),
                            }
                except Exception as e:
                    st.session_state[hasil_key] = {
                        "status": "error",
                        "message": format_error_ramah(e, kode_peserta),
                    }
        elif tipe_soal == "script":
            # ── Mode Script: tangkap stdout & bandingkan ───────────────
            with st.spinner("⏳ Menjalankan kode..."):
                hasil_uji = jalankan_kode_script(kode_peserta, soal["test_cases"])
            st.session_state[hasil_key] = hasil_uji
        else:
            # ── Mode Standard: uji test cases ─────────────────────────
            with st.spinner("⏳ Menjalankan kode..."):
                hasil_uji = jalankan_kode(
                    kode_peserta,
                    soal["test_cases"],
                    soal["function_name"],
                )
            st.session_state[hasil_key] = hasil_uji

    # --- Tampilkan Hasil ---
    hasil_tersimpan = st.session_state[hasil_key]

    if hasil_tersimpan is not None:
        st.divider()
        st.subheader("📊 Hasil Test")

        # ── Tampilan hasil untuk soal VISUAL ──────────────────────────
        if isinstance(hasil_tersimpan, dict) and hasil_tersimpan.get("status") == "visual":
            st.markdown(
                "<div class='score-box score-all-pass'>🎨 Grafik berhasil dibuat!</div>",
                unsafe_allow_html=True,
            )
            st.pyplot(hasil_tersimpan["fig"])

        elif isinstance(hasil_tersimpan, dict) and hasil_tersimpan.get("status") == "error":
            st.markdown(
                "<div class='score-box score-all-fail'>❌ Kode mengandung error</div>",
                unsafe_allow_html=True,
            )
            st.code(hasil_tersimpan["message"], language="text")

        # ── Tampilan hasil untuk soal STANDARD ────────────────────────
        elif isinstance(hasil_tersimpan, list):
            total  = len(hasil_tersimpan)
            lulus  = sum(1 for h in hasil_tersimpan if h["status"] == "pass")

            if lulus == total:
                score_class = "score-all-pass"
                score_msg   = f"🎉 Sempurna! Semua {total} test case lulus!"
            elif lulus > 0:
                score_class = "score-some-pass"
                score_msg   = f"😅 {lulus} dari {total} test case lulus. Terus semangat!"
            else:
                score_class = "score-all-fail"
                score_msg   = f"😓 Belum ada yang lulus. Coba periksa kode kamu lagi!"

            st.markdown(
                f"<div class='score-box {score_class}'>{score_msg}</div>",
                unsafe_allow_html=True,
            )

            for i, h in enumerate(hasil_tersimpan, start=1):
                if h["status"] == "pass":
                    ikon  = "✅"
                    css   = "test-pass"
                    label = "LULUS"
                elif h["status"] == "fail":
                    ikon  = "❌"
                    css   = "test-fail"
                    label = "GAGAL"
                else:
                    ikon  = "⚠️"
                    css   = "test-error"
                    label = "ERROR"

                st.markdown(
                    f"""
                    <div class='{css}'>
                        <strong>{ikon} Test {i} – {label}</strong><br>
                        <small>{h['description']}</small>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                with st.expander(f"Detail Test {i}"):
                    st.code(h["message"], language="text")


# ═══════════════════════════════════════════════════════════════════════════
# TAB 2 — PYTHON PLAYGROUND
# ═══════════════════════════════════════════════════════════════════════════
with tab_playground:

    st.title("🧪 Python Playground")
    st.caption("Coba-coba syntax Python bebas di sini. Tidak perlu bikin fungsi — langsung tulis dan jalankan!")
    st.divider()

    col_pg_editor, col_pg_output = st.columns([1, 1], gap="large")

    with col_pg_editor:
        st.subheader("✏️ Tulis Kode Python")

        _pg_ace_val = st_ace(
            value=st.session_state["playground_kode"],
            language="python",
            theme="monokai",
            keybinding="vscode",
            font_size=14,
            tab_size=4,
            show_gutter=True,
            show_print_margin=False,
            wrap=False,
            auto_update=True,
            height=380,
            key="ace_playground",
        )
        pg_kode = _pg_ace_val if _pg_ace_val is not None else st.session_state["playground_kode"]
        st.session_state["playground_kode"] = pg_kode

        col_pg_run, col_pg_reset = st.columns([2, 1])
        with col_pg_run:
            pg_run = st.button("▶️ Jalankan", type="primary",
                               use_container_width=True, key="btn_pg_run")
        with col_pg_reset:
            pg_reset = st.button("🔄 Reset", type="secondary",
                                 use_container_width=True, key="btn_pg_reset")

        if pg_reset:
            st.session_state["playground_kode"] = ""
            st.session_state["playground_hasil"] = None
            st.rerun()

        if pg_run:
            if not pg_kode.strip():
                st.warning("⚠️ Editor masih kosong!")
            else:
                st.session_state["playground_hasil"] = jalankan_playground(pg_kode)

        # Tips referensi cepat
        with st.expander("💡 Referensi Cepat", expanded=False):
            st.markdown("""
**Cetak ke layar**
```python
print("Hello, World!")
print(3 + 7)
```
**Variabel**
```python
nama   = "Budi"
umur   = 20
tinggi = 1.75
print(f"{nama} berumur {umur} tahun")
```
**List**
```python
buah = ["apel", "jeruk", "mangga"]
print(buah[0])    # apel
print(len(buah))  # 3
```
**For loop**
```python
for i in range(1, 6):
    print(i)
```
**If / else**
```python
nilai = 85
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")
```
            """)

    with col_pg_output:
        st.subheader("📤 Output")

        hasil_pg = st.session_state["playground_hasil"]

        if hasil_pg is None:
            st.markdown(
                "<div style='color:#888;font-style:italic;padding:12px'>"
                "Output akan muncul di sini setelah kamu klik ▶️ Jalankan"
                "</div>",
                unsafe_allow_html=True,
            )
        elif hasil_pg["status"] == "ok":
            st.markdown(
                "<div class='score-box score-all-pass'>✅ Kode berhasil dijalankan!</div>",
                unsafe_allow_html=True,
            )
            st.code(hasil_pg["output"], language="text")
        else:
            st.markdown(
                "<div class='score-box score-all-fail'>❌ Ada error pada kode kamu</div>",
                unsafe_allow_html=True,
            )
            st.code(hasil_pg["output"], language="text")