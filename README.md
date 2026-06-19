# NusaRasa — Sistem Rekomendasi Kuliner Indonesia Berbasis Semantic Web

> Temukan kekayaan kuliner Nusantara melalui pencarian semantik bahasa alami — didukung Knowledge Graph RDF/OWL dan pipeline NL2SPARQL berbasis LLM.

---

## Tentang Proyek

**NusaRasa** adalah sistem rekomendasi kuliner lokal Indonesia yang dibangun di atas fondasi teknologi *Semantic Web*. Alih-alih mengandalkan pencarian kata kunci sederhana, NusaRasa memahami **relasi kontekstual** antara hidangan, bahan, daerah asal, budaya, dan momen penyajian — memungkinkan pertanyaan seperti:

> *"Makanan khas Jawa yang mengandung santan dan cocok disajikan saat Lebaran"*

dapat dijawab secara tepat dan bermakna.

Indonesia memiliki lebih dari **5.350 jenis hidangan tradisional** yang tersebar di 38 provinsi. NusaRasa hadir sebagai upaya pelestarian dan promosi warisan kuliner Nusantara secara digital, dengan merepresentasikan pengetahuan kuliner dalam format yang dapat dipahami mesin (*machine-readable*).

---

## Fitur Utama

- **Pencarian Bahasa Alami** — Ketik pertanyaan seperti berbicara biasa; LLM akan menerjemahkannya menjadi SPARQL query secara otomatis dengan fitur *Auto-Retry & Self-Correction* untuk memastikan hasil yang akurat.
- **Knowledge Graph Interaktif** — Visualisasi relasi semantik antar entitas kuliner secara komprehensif.
- **Kartu Rekomendasi Hidangan** — Tampilkan informasi lengkap: daerah asal, bahan, budaya, konteks penyajian, dan tingkat kepedasan.
- **Transparansi Query** — Kueri SPARQL yang dihasilkan beserta penjelasan cara kerjanya ditampilkan secara eksplisit kepada pengguna untuk keperluan edukasi.
- **Ontologi Terstruktur** — Dibangun dengan OWL 2 menggunakan Protégé, divalidasi oleh HermiT Reasoner.

---

## Arsitektur Sistem

```text
Pengguna (Bahasa Alami)
        │
        ▼
┌──────────────────┐
│   Web Frontend   │  Next.js / React / Tailwind CSS
│  (Antarmuka Web) │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Express Backend  │  Node.js API Gateway & NL2SPARQL
│                  │◄──── Groq API (Llama 3.3 70B)
└────────┬─────────┘      + Few-shot Prompting + Auto-Retry
         │
         ▼
┌──────────────────┐
│   SPARQL Server  │  Python + RDFLib (Port 3030)
│   (Standalone)   │  Dataset: nusarasa_data.ttl
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Knowledge Graph │  RDF Turtle (.ttl)
│  NusaRasa Onto.  │  OWL 2 — NusaRasa Ontology
└──────────────────┘
```

---

## Ontologi NusaRasa

Ontologi dirancang di **Protégé 5.x** dengan komponen berikut:

### Kelas Utama

| Kelas | Deskripsi |
|---|---|
| `nusa:Dish` | Representasi hidangan dengan metadata lengkap |
| `nusa:Region` | Wilayah geografis asal hidangan |
| `nusa:Ingredient` | Bahan penyusun hidangan |
| `nusa:Culture` | Kelompok budaya atau suku yang berafiliasi |
| `nusa:Event` | Peristiwa / konteks sosial penyajian hidangan |

### Object Properties

| Property | Relasi |
|---|---|
| `berasal_dari` | Dish → Region |
| `mengandung` | Dish → Ingredient |
| `terkait_budaya` | Dish → Culture |
| `disajikan_pada` | Dish → Event |
| `memiliki_varian` | Dish → Dish |
| `berkaitan_dengan` | Dish → Dish / Event |

### Data Properties

`nama` · `deskripsi` · `metode_memasak` · `tingkat_kepedasan` · `kategori_diet`

---

## 🛠️ Teknologi

| Komponen | Teknologi |
|---|---|
| Ontologi | Protégé 5.x (OWL 2) |
| RDF / Triple Store | RDFLib (Python) SPARQL Server |
| LLM / NL2SPARQL | Groq API (Llama-3.3-70b-versatile) |
| Web Backend | Node.js / Express |
| Web Frontend | Next.js / React |
| Dataset | CSV → RDF Turtle (`.ttl`) |

---

## Cara Menjalankan (Development)

Proyek ini terdiri dari dua bagian utama: `backend` dan `frontend`. 

### Prasyarat
- **Node.js** (v18+)
- **Python** (3.10+)
- **Groq API Key** (Dapatkan di [Groq Console](https://console.groq.com/keys))

### 1. Menyiapkan Backend (Express & SPARQL)
Buka terminal baru, lalu ikuti langkah berikut:
```bash
cd backend

# Install dependencies Node.js
npm install

# Install dependencies Python (untuk SPARQL Server)
pip install -r requirements.txt

# Buat file konfigurasi .env dari .env.example
cp .env.example .env
```
Buka file `backend/.env` dan masukkan API Key Groq Anda:
```env
PORT=5000
GROQ_API_KEY=gsk_kunci_api_anda_di_sini
GROQ_MODEL_NAME=llama-3.3-70b-versatile
```

Setelah itu, jalankan kedua layanan backend ini secara bersamaan (disarankan menggunakan 2 terminal atau mode *split terminal*):
```bash
# Di Terminal 1: Jalankan SPARQL Server (berjalan di Port 3030)
python sparql_server.py

# Di Terminal 2: Jalankan Express API Server (berjalan di Port 5000)
npm run dev
```

### 2. Menyiapkan Frontend (Next.js)
Buka terminal baru lainnya, navigasi ke folder frontend, lalu:
```bash
cd frontend

# Install dependencies
npm install

# Jalankan server frontend (berjalan di Port 3000)
npm run dev
```

Aplikasi siap digunakan dan dapat diakses melalui browser Anda di: **http://localhost:3000**

---

## Struktur Direktori Utama

```text
nusarasa/
├── backend/
│   ├── controllers/      # Logika API Express (Query, Data, Ontology)
│   ├── services/         # Layanan eksternal (NL2SPARQL, komunikasi RDFLib)
│   ├── data/             # File sumber data (.csv dan .ttl)
│   ├── ontology/         # File definisi dan arsitektur ontologi (.ttl)
│   ├── scripts/          # Skrip utilitas bantu (misal: pengujian LLM)
│   ├── server.js         # Entry point utama Node.js Express
│   └── sparql_server.py  # Server SPARQL mandiri berbasis Python & RDFLib
├── frontend/
│   ├── src/app/          # Halaman User Interface Next.js (App Router)
│   ├── src/components/   # Komponen UI React
│   └── public/           # Aset statis dan ikon
└── README.md             # Dokumentasi utama proyek
```

---

## Tim Pengembang

| Nama | NIM | Peran |
|---|---|---|
| Francisco Gilbert Sondakh | 140810230004 | Project Manager |
| Achmad Dzaki Azhari | 140810230034 | Front-End Developer |
| Theophilus Samuel Ghozali | 140810230054 | Back-End Developer |

**Universitas Padjadjaran — Fakultas MIPA**
Program Studi S-1 Teknik Informatika · Semester Genap 2025/2026

---

## Referensi

- Antoniou, G., & Van Harmelen, F. (2004). *A Semantic Web Primer*. MIT Press.
- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). The Semantic Web. *Scientific American*, 284(5), 34–43.
- Hitzler, P. (2021). A Review of the Semantic Web Field. *Communications of the ACM*, 64(2), 76–83.
- [RDFLib Documentation](https://rdflib.readthedocs.io/)
