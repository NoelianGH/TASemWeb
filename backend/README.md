# TASemWeb Backend API

Backend Express.js untuk sistem Semantic Web NusaRasa. Backend ini bertindak sebagai API Gateway yang menghubungkan antarmuka pengguna (Frontend) dengan mesin logika Semantic Web (SPARQL Server) dan Model Bahasa Besar (LLM).

## 🌟 Fitur Utama

- **NL2SPARQL Pipeline:** Mengonversi pertanyaan bahasa alami dari pengguna menjadi kueri SPARQL secara *real-time* menggunakan model LLM Groq (`llama-3.3-70b-versatile`).
- **Auto-Retry & Self-Correction:** Jika LLM menghasilkan kueri yang terlalu kaku atau salah secara sintaks sehingga tidak ditemukan data, sistem akan secara otomatis menginstruksikan ulang LLM dengan umpan balik (*feedback*) hingga maksimal 3 kali percobaan secara instan.
- **Case-Insensitive Searching:** LLM diatur untuk melakukan pencarian RDF menggunakan `LCASE(STR())` yang tangguh terhadap kesalahan pengetikan huruf kapital.
- **Data & Ontology Gateway:** Menyediakan endpoint RESTful untuk membaca struktur ontologi dan data hidangan.

## 📁 Struktur Project

```text
backend/
├── controllers/          # Logika bisnis untuk setiap endpoint API
│   ├── dataController.js
│   ├── ontologyController.js
│   └── queryController.js     # Menangani routing NL2SPARQL & Retry Loop
├── routes/               # Definisi Route API Express
│   ├── data.js
│   ├── ontology.js
│   └── query.js
├── services/             # Layer komunikasi dengan layanan eksternal
│   ├── dataService.js
│   ├── nl2sparqlService.js    # Koneksi API LLM Groq (Prompt & API Call)
│   ├── ontologyService.js
│   ├── queryService.js
│   └── sparqlClient.js        # Klien ke Python SPARQL Server
├── data/                 # Data RDF Graph
│   └── nusarasa_data.ttl
├── ontology/             # Definisi Arsitektur Ontology
│   └── nusarasa_ontology.ttl
├── scripts/              # Skrip untuk pengujian atau utilisasi
│   ├── csv_to_rdf.py
│   └── test_nl2sparql.js      # Alat tes LLM NL2SPARQL via CLI
├── sparql_server.py      # Server mandiri RDFLib untuk eksekusi kueri
├── server.js             # Entry point utama Express
└── package.json          # Node.js dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies
Anda memerlukan dependensi Node.js dan Python:
```bash
# Dependensi Express
npm install

# Dependensi SPARQL Server
pip install -r requirements.txt
```

### 2. Setup Environment Variables
Buat file `.env` (atau _copy_ dari `.env.example`) dan pastikan konfigurasi diatur seperti ini:
```env
PORT=5000
GROQ_API_KEY=gsk_kunci_groq_anda_di_sini
GROQ_MODEL_NAME=llama-3.3-70b-versatile
```
> **Catatan:** Anda bisa mendapatkan `GROQ_API_KEY` secara gratis di [Groq Console](https://console.groq.com/keys).

### 3. Jalankan Layanan Backend
Backend ini membutuhkan **dua** server yang berjalan bersamaan:

1. **Jalankan Python SPARQL Server (Port 3030)**
   Buka terminal pertama di dalam folder `backend`:
   ```bash
   python sparql_server.py
   ```
   *(Server ini mengeksekusi file `.ttl` menggunakan mesin RDFLib).*

2. **Jalankan Express API Gateway (Port 5000)**
   Buka terminal kedua di dalam folder `backend`:
   ```bash
   npm run dev
   ```

Server API siap menerima _request_ di `http://localhost:5000`.

## 📚 API Endpoints Terkini

### NL2SPARQL Query API (`/api/query`)
- **`POST /api/query/nl2sparql`** - (Endpoint Utama)
  - **Fungsi:** Menerima pertanyaan bahasa alami, diubah jadi SPARQL oleh LLM, dan langsung dieksekusi.
  - **Body:** `{ "question": "Makanan yang mengandung santan dan daging sapi" }`
  - **Response:** Akan mengembalikan Kueri SPARQL mentah, Penjelasan Kueri, dan Hasil eksekusi berformat JSON.

### SPARQL Biasa (`/api/query`)
- `POST /api/query/sparql` - Menjalankan kueri SPARQL manual secara langsung.
  - Body: `{ "query": "SELECT * WHERE { ... }" }`
- `POST /api/query/semantic-search` - Pencarian semantik sederhana menggunakan keyword.

### Ontology & Data API
- `GET /api/ontology/classes` - Daftar semua OWL class di ontologi
- `GET /api/data` - Ambil data semua instansiasi hidangan (terbatas)
- `GET /api/data/:id` - Detail spesifik hidangan dari ID.

## 📦 Tech Stack & Dependencies Utama

- **Node.js/Express.js:** Server API Gateway.
- **Groq SDK/Axios:** Koneksi API inferensi LLM ultra-cepat (LPU).
- **Python Flask & RDFLib:** Server khusus (*SPARQL endpoint*) untuk grafik memori.
- **Nodemon:** *Auto-reload* server saat mode pengembangan.

---
**Troubleshooting:**
Jika API merespons dengan *"Model decommissioned"*, pastikan Anda sudah mematikan (`Ctrl+C`) terminal Express dan menyalakannya lagi dengan `npm run dev` untuk membaca konfigurasi `.env` terbaru.
