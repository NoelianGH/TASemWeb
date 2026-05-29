import streamlit as st

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NusaRasa · Rekomendasi Kuliner Nusantara",
    page_icon="🍛",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Import Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Root palette ── */
:root {
    --brown-dark:   #2C1A0E;
    --brown-mid:    #5C3317;
    --brown-accent: #8B4513;
    --brown-warm:   #C4874B;
    --brown-light:  #E8C9A0;
    --cream:        #FAF6F0;
    --white:        #FFFFFF;
    --text-dark:    #1E120A;
    --text-muted:   #7A5C44;
}

/* ── Global background ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--cream);
    color: var(--text-dark);
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background-color: var(--cream);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: var(--brown-dark) !important;
}
[data-testid="stSidebar"] * {
    color: var(--white) !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stSlider label {
    color: var(--brown-light) !important;
}
[data-testid="stSidebar"] hr {
    border-color: var(--brown-mid) !important;
}

/* ── Hero banner ── */
.hero-banner {
    background: linear-gradient(135deg, var(--brown-dark) 0%, var(--brown-mid) 60%, var(--brown-accent) 100%);
    border-radius: 16px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    color: var(--white);
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: "🍛";
    position: absolute;
    right: 2rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.15;
}
.hero-banner h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    margin: 0 0 0.4rem 0;
    color: var(--white);
}
.hero-banner p {
    font-size: 1rem;
    color: var(--brown-light);
    margin: 0;
    font-weight: 300;
}
.hero-tag {
    display: inline-block;
    background: var(--brown-warm);
    color: var(--white);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    margin-bottom: 0.75rem;
}

/* ── Section headings ── */
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: var(--brown-dark);
    font-weight: 700;
    border-left: 4px solid var(--brown-warm);
    padding-left: 0.75rem;
    margin-bottom: 1rem;
}

/* ── Metric cards ── */
.metric-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.metric-card {
    background: var(--white);
    border: 1px solid var(--brown-light);
    border-top: 4px solid var(--brown-warm);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    flex: 1;
    text-align: center;
    box-shadow: 0 2px 8px rgba(44,26,14,0.06);
}
.metric-card .val {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--brown-accent);
}
.metric-card .lbl {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-top: 0.25rem;
    font-weight: 500;
}

/* ── Search box ── */
.stTextInput > div > div > input {
    border: 2px solid var(--brown-light) !important;
    border-radius: 10px !important;
    background: var(--white) !important;
    color: var(--text-dark) !important;
    font-size: 1rem !important;
    padding: 0.65rem 1rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--brown-warm) !important;
    box-shadow: 0 0 0 3px rgba(196,135,75,0.2) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: var(--brown-dark) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.5rem !important;
    letter-spacing: 0.03em;
    transition: background 0.2s;
}
.stButton > button:hover {
    background: var(--brown-accent) !important;
}

/* ── Dish cards ── */
.dish-card {
    background: var(--white);
    border: 1px solid var(--brown-light);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.9rem;
    box-shadow: 0 2px 8px rgba(44,26,14,0.06);
    transition: box-shadow 0.2s, transform 0.15s;
    cursor: default;
}
.dish-card:hover {
    box-shadow: 0 6px 18px rgba(44,26,14,0.13);
    transform: translateY(-2px);
}
.dish-card .dish-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--brown-dark);
    margin-bottom: 0.3rem;
}
.dish-card .dish-meta {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
}
.dish-card .dish-desc {
    font-size: 0.88rem;
    color: var(--text-dark);
    line-height: 1.55;
}
.tag {
    display: inline-block;
    background: var(--cream);
    border: 1px solid var(--brown-light);
    color: var(--brown-mid);
    font-size: 0.72rem;
    font-weight: 600;
    border-radius: 20px;
    padding: 0.18rem 0.6rem;
    margin: 0.15rem 0.15rem 0 0;
}

/* ── SPARQL preview ── */
.sparql-box {
    background: var(--brown-dark);
    color: #E8C9A0;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    font-family: 'Courier New', monospace;
    font-size: 0.82rem;
    line-height: 1.7;
    white-space: pre-wrap;
    word-break: break-all;
    margin-top: 0.5rem;
}

/* ── Info box ── */
.info-box {
    background: var(--white);
    border: 1px solid var(--brown-light);
    border-left: 5px solid var(--brown-warm);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-size: 0.88rem;
    color: var(--text-dark);
    line-height: 1.6;
    margin-bottom: 1rem;
}

/* ── Tabs ── */
[data-baseweb="tab-list"] {
    gap: 0.5rem;
    border-bottom: 2px solid var(--brown-light) !important;
}
[data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-muted) !important;
    border-radius: 8px 8px 0 0 !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.2rem !important;
}
[aria-selected="true"][data-baseweb="tab"] {
    background: var(--white) !important;
    color: var(--brown-dark) !important;
    border-bottom: 3px solid var(--brown-warm) !important;
    font-weight: 700 !important;
}

/* ── Expander ── */
[data-testid="stExpander"] > details {
    border: 1px solid var(--brown-light) !important;
    border-radius: 10px !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--cream); }
::-webkit-scrollbar-thumb { background: var(--brown-light); border-radius: 6px; }
::-webkit-scrollbar-thumb:hover { background: var(--brown-warm); }
</style>
""", unsafe_allow_html=True)


# ─── Mock Data ────────────────────────────────────────────────────────────────
DISHES = [
    {
        "name": "Rendang",
        "region": "Sumatera Barat",
        "culture": "Minangkabau",
        "ingredients": ["Daging Sapi", "Santan", "Cabai", "Serai", "Lengkuas"],
        "taste": "Pedas",
        "event": "Hari Raya",
        "desc": "Masakan daging sapi yang dimasak dengan santan dan bumbu rempah pilihan hingga kering. Diakui UNESCO sebagai warisan kuliner dunia.",
        "method": "Dimasak perlahan",
    },
    {
        "name": "Gudeg",
        "region": "DI Yogyakarta",
        "culture": "Jawa",
        "ingredients": ["Nangka Muda", "Santan", "Gula Merah", "Daun Salam", "Telur"],
        "taste": "Manis",
        "event": "Sehari-hari",
        "desc": "Makanan khas Yogyakarta dari nangka muda yang dimasak dengan santan dan gula merah. Cita rasa manis dengan tekstur lembut.",
        "method": "Dimasak lama",
    },
    {
        "name": "Soto Betawi",
        "region": "DKI Jakarta",
        "culture": "Betawi",
        "ingredients": ["Daging Sapi", "Santan", "Tomat", "Bawang Merah", "Kentang"],
        "taste": "Gurih",
        "event": "Sehari-hari",
        "desc": "Soto khas Betawi dengan kuah santan yang kaya. Disajikan dengan potongan daging sapi, kentang, dan tomat segar.",
        "method": "Direbus",
    },
    {
        "name": "Papeda",
        "region": "Papua",
        "culture": "Papua",
        "ingredients": ["Sagu", "Ikan Kuah Kuning", "Kunyit", "Jeruk Nipis"],
        "taste": "Tawar",
        "event": "Sehari-hari",
        "desc": "Makanan pokok masyarakat Papua berupa bubur sagu yang disantap bersama ikan kuah kuning. Kaya serat dan bebas gluten.",
        "method": "Direbus",
    },
    {
        "name": "Pempek",
        "region": "Sumatera Selatan",
        "culture": "Palembang",
        "ingredients": ["Ikan Tenggiri", "Tepung Tapioka", "Cuko", "Timun", "Ebi"],
        "taste": "Asam Pedas",
        "event": "Sehari-hari",
        "desc": "Makanan khas Palembang dari ikan tenggiri dan tepung sagu. Disajikan dengan kuah cuko yang asam, pedas, dan manis.",
        "method": "Digoreng/Direbus",
    },
    {
        "name": "Rawon",
        "region": "Jawa Timur",
        "culture": "Jawa",
        "ingredients": ["Daging Sapi", "Kluwek", "Serai", "Bawang Putih", "Tauge"],
        "taste": "Gurih",
        "event": "Sehari-hari",
        "desc": "Sup daging sapi berkuah hitam khas Jawa Timur. Warna hitam berasal dari kluwek yang memberikan cita rasa khas.",
        "method": "Direbus",
    },
]

PROVINCES = sorted(list(set(d["region"] for d in DISHES)) + [
    "Aceh", "Sumatera Utara", "Riau", "Jambi", "Bengkulu",
    "Lampung", "Banten", "Jawa Barat", "Jawa Tengah",
    "Kalimantan Barat", "Sulawesi Selatan", "Bali", "NTB", "NTT",
])

TASTES = ["Semua", "Pedas", "Manis", "Gurih", "Asam Pedas", "Tawar"]
CULTURES = ["Semua"] + sorted(list(set(d["culture"] for d in DISHES)))


# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🍛 NusaRasa")
    st.markdown("*Semantic Culinary Explorer*")
    st.markdown("---")

    st.markdown("#### 🔎 Filter Pencarian")

    selected_province = st.selectbox("Provinsi / Daerah", ["Semua"] + PROVINCES)
    selected_taste = st.selectbox("Cita Rasa", TASTES)
    selected_culture = st.selectbox("Budaya", CULTURES)

    st.markdown("---")
    st.markdown("#### ⚙️ Sistem")

    use_llm = st.toggle("Aktifkan LLM Interface", value=True)
    show_sparql = st.toggle("Tampilkan Query SPARQL", value=False)

    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.75rem; color:#C4874B; line-height:1.6'>
    <b>NusaRasa</b><br>
    Knowledge Graph + LLM<br>
    Kuliner Nusantara<br><br>
    Universitas Padjadjaran<br>
    Informatika · 2024
    </div>
    """, unsafe_allow_html=True)


# ─── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-tag">Semantic Web Project</div>
  <h1>Rekomendasi Kuliner <em>Nusantara</em></h1>
  <p>Berbasis Knowledge Graph & Large Language Model · Ontologi NusaRasa</p>
</div>
""", unsafe_allow_html=True)


# ─── Metrics ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="metric-row">
  <div class="metric-card"><div class="val">87</div><div class="lbl">Hidangan Terdokumentasi</div></div>
  <div class="metric-card"><div class="val">214</div><div class="lbl">Bahan &amp; Ingredien</div></div>
  <div class="metric-card"><div class="val">1.200+</div><div class="lbl">Triplet RDF</div></div>
  <div class="metric-card"><div class="val">26</div><div class="lbl">Provinsi Tercakup</div></div>
  <div class="metric-card"><div class="val">92%</div><div class="lbl">SPARQL Valid Rate</div></div>
</div>
""", unsafe_allow_html=True)


# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab_cari, tab_jelajah, tab_ontologi, tab_tentang = st.tabs([
    "🔍 Cari Hidangan",
    "🗺️ Jelajah Daerah",
    "🧠 Ontologi & KG",
    "ℹ️ Tentang Sistem",
])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — CARI HIDANGAN
# ══════════════════════════════════════════════════════════════════════════════
with tab_cari:
    st.markdown('<div class="section-heading">Tanya dengan Bahasa Alami</div>', unsafe_allow_html=True)

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        nl_query = st.text_input(
            label="",
            placeholder='Contoh: "Makanan Jawa yang manis dan menggunakan santan"',
            label_visibility="collapsed",
        )
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        search_clicked = st.button("🔍 Cari", use_container_width=True)

    # Quick chips
    st.markdown("""
    <div style='margin: 0.5rem 0 1.2rem 0; font-size:0.82rem; color:#7A5C44;'>
    💡 Coba:&nbsp;
    <span style='background:#E8C9A0;padding:0.2rem 0.7rem;border-radius:20px;margin-right:4px'>Makanan pedas dari Sumatera</span>
    <span style='background:#E8C9A0;padding:0.2rem 0.7rem;border-radius:20px;margin-right:4px'>Hidangan Lebaran Minangkabau</span>
    <span style='background:#E8C9A0;padding:0.2rem 0.7rem;border-radius:20px'>Makanan dengan santan dari Jawa</span>
    </div>
    """, unsafe_allow_html=True)

    # SPARQL preview
    if show_sparql and nl_query:
        sparql_preview = f"""PREFIX nusa: <http://nusarasa.id/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?hidangan ?daerah ?bahan WHERE {{
  ?hidangan rdf:type        nusa:Dish ;
            nusa:nama       ?nama ;
            nusa:berasal_dari ?daerah ;
            nusa:mengandung  ?bahan .
  FILTER(CONTAINS(LCASE(?nama), "{nl_query.lower()[:20]}"))
}}
LIMIT 10"""
        st.markdown('<div style="margin-bottom:0.3rem;font-size:0.82rem;color:#7A5C44;">📌 SPARQL yang di-generate LLM:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sparql-box">{sparql_preview}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # Results section heading
    st.markdown('<div class="section-heading">Hasil Rekomendasi</div>', unsafe_allow_html=True)

    # Filter dishes
    filtered = DISHES
    if selected_province != "Semua":
        filtered = [d for d in filtered if d["region"] == selected_province]
    if selected_taste != "Semua":
        filtered = [d for d in filtered if d["taste"] == selected_taste]
    if selected_culture != "Semua":
        filtered = [d for d in filtered if d["culture"] == selected_culture]
    if nl_query:
        q = nl_query.lower()
        filtered = [
            d for d in filtered
            if q in d["name"].lower()
            or q in d["region"].lower()
            or q in d["culture"].lower()
            or any(q in ing.lower() for ing in d["ingredients"])
            or q in d["taste"].lower()
        ] or filtered  # fallback: show all if no match

    if not filtered:
        st.info("Tidak ada hidangan yang cocok dengan filter yang dipilih.")
    else:
        st.markdown(f'<div style="font-size:0.82rem;color:#7A5C44;margin-bottom:0.8rem">Menampilkan <b>{len(filtered)}</b> hidangan</div>', unsafe_allow_html=True)
        for dish in filtered:
            tags_html = "".join(f'<span class="tag">{t}</span>' for t in dish["ingredients"])
            st.markdown(f"""
            <div class="dish-card">
                <div class="dish-name">🍽️ {dish['name']}</div>
                <div class="dish-meta">
                    📍 {dish['region']} &nbsp;·&nbsp;
                    🎭 {dish['culture']} &nbsp;·&nbsp;
                    👅 {dish['taste']} &nbsp;·&nbsp;
                    🎉 {dish['event']}
                </div>
                <div class="dish-desc">{dish['desc']}</div>
                <div style="margin-top:0.6rem">{tags_html}</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — JELAJAH DAERAH
# ══════════════════════════════════════════════════════════════════════════════
with tab_jelajah:
    st.markdown('<div class="section-heading">Jelajah Kuliner per Daerah</div>', unsafe_allow_html=True)

    region_dish_map = {}
    for d in DISHES:
        region_dish_map.setdefault(d["region"], []).append(d)

    col_left, col_right = st.columns([1, 2])
    with col_left:
        region_list = list(region_dish_map.keys())
        selected_region = st.radio("Pilih Daerah", region_list, label_visibility="collapsed")

    with col_right:
        if selected_region:
            dishes_in_region = region_dish_map[selected_region]
            st.markdown(f"""
            <div class="info-box">
            🗺️ <b>{selected_region}</b> memiliki <b>{len(dishes_in_region)}</b> hidangan terdokumentasi dalam Knowledge Graph NusaRasa.
            </div>
            """, unsafe_allow_html=True)
            for dish in dishes_in_region:
                tags_html = "".join(f'<span class="tag">{t}</span>' for t in dish["ingredients"])
                st.markdown(f"""
                <div class="dish-card">
                    <div class="dish-name">🍽️ {dish['name']}</div>
                    <div class="dish-meta">👅 {dish['taste']} &nbsp;·&nbsp; 🍳 {dish['method']}</div>
                    <div class="dish-desc">{dish['desc']}</div>
                    <div style="margin-top:0.6rem">{tags_html}</div>
                </div>
                """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — ONTOLOGI & KG
# ══════════════════════════════════════════════════════════════════════════════
with tab_ontologi:
    st.markdown('<div class="section-heading">Arsitektur Ontologi NusaRasa</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    Ontologi NusaRasa dibangun menggunakan standar <b>RDF/OWL</b> dengan 5 kelas utama dan 6+ properti objek.
    Divalidasi menggunakan <b>OWL Reasoner HermiT</b> dan disimpan di <b>Apache Jena Fuseki</b> sebagai SPARQL Endpoint.
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("##### 📦 Kelas Utama (Classes)")
        classes = {
            "Dish": "Hidangan / makanan",
            "Region": "Daerah asal (provinsi)",
            "Ingredient": "Bahan & ingredien",
            "Culture": "Budaya & etnis terkait",
            "Event": "Peristiwa / momen penyajian",
        }
        for cls, desc in classes.items():
            st.markdown(f"""
            <div style='background:white;border:1px solid #E8C9A0;border-left:4px solid #C4874B;
                        border-radius:8px;padding:0.6rem 1rem;margin-bottom:0.5rem;'>
            <b style='color:#5C3317'>:{cls}</b>
            <span style='float:right;color:#7A5C44;font-size:0.82rem'>{desc}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_b:
        st.markdown("##### 🔗 Object Properties")
        props = {
            "berasal_dari": "Dish → Region",
            "mengandung": "Dish → Ingredient",
            "terkait_budaya": "Dish → Culture",
            "disajikan_pada": "Dish → Event",
            "memiliki_varian": "Dish → Dish",
            "berbahan_dasar": "Dish → Ingredient",
        }
        for prop, mapping in props.items():
            st.markdown(f"""
            <div style='background:white;border:1px solid #E8C9A0;border-left:4px solid #2C1A0E;
                        border-radius:8px;padding:0.6rem 1rem;margin-bottom:0.5rem;'>
            <b style='color:#2C1A0E;font-family:monospace'>nusa:{prop}</b>
            <span style='float:right;color:#7A5C44;font-size:0.82rem'>{mapping}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 📝 Contoh Triplet RDF — Rendang")
    rdf_example = """\
:Rendang    rdf:type           nusa:Dish .
:Rendang    nusa:berasal_dari  :SumateraBarat .
:Rendang    nusa:mengandung    :Santan .
:Rendang    nusa:terkait_budaya :Minangkabau .
:Rendang    nusa:disajikan_pada :HariRaya .
:Rendang    nusa:memiliki_varian :RendangHijau ."""
    st.markdown(f'<div class="sparql-box">{rdf_example}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### ⚡ Pipeline: Bahasa Alami → SPARQL")
    col1, col2, col3, col4 = st.columns(4)
    steps = [
        ("💬", "INPUT", "Bahasa Alami", "Pengguna mengetik pertanyaan natural"),
        ("🤖", "PROSES", "LLM Translation", "LLM + skema ontologi → SPARQL"),
        ("🔗", "QUERY", "SPARQL Execution", "Eksekusi di KG endpoint + ranking"),
        ("✨", "OUTPUT", "Rekomendasi", "Hasil dalam bahasa natural + konteks"),
    ]
    for col, (icon, stage, title, detail) in zip([col1, col2, col3, col4], steps):
        with col:
            st.markdown(f"""
            <div style='background:white;border:1px solid #E8C9A0;border-top:4px solid #8B4513;
                        border-radius:10px;padding:1rem;text-align:center;height:140px'>
            <div style='font-size:1.8rem'>{icon}</div>
            <div style='font-size:0.65rem;color:#7A5C44;font-weight:700;letter-spacing:0.1em'>{stage}</div>
            <div style='font-weight:700;color:#2C1A0E;margin:0.3rem 0;font-size:0.9rem'>{title}</div>
            <div style='font-size:0.73rem;color:#7A5C44'>{detail}</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — TENTANG SISTEM
# ══════════════════════════════════════════════════════════════════════════════
with tab_tentang:
    st.markdown('<div class="section-heading">Tentang NusaRasa</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>NusaRasa</b> adalah sistem rekomendasi kuliner Nusantara berbasis <b>Semantic Web</b>,
    dibangun menggunakan <b>Knowledge Graph (KG)</b> dan <b>Large Language Model (LLM)</b>.
    Sistem ini memungkinkan pengguna mengeksplorasi kekayaan kuliner Indonesia melalui
    antarmuka bahasa alami tanpa harus memahami SPARQL.
    </div>
    """, unsafe_allow_html=True)

    col_res, col_team = st.columns([1, 1])
    with col_res:
        st.markdown("##### 📊 Hasil Evaluasi")
        results = [
            ("92%", "SPARQL valid secara sintaksis"),
            ("84%", "Kueri relevan dengan intensi pengguna"),
            ("+37%", "Lebih relevan vs pencarian kata kunci"),
            ("✓", "OWL inferensi relasi halal & geografis"),
        ]
        for val, label in results:
            st.markdown(f"""
            <div style='display:flex;align-items:center;background:white;border:1px solid #E8C9A0;
                        border-radius:8px;padding:0.65rem 1rem;margin-bottom:0.5rem;gap:1rem'>
            <span style='font-family:Playfair Display,serif;font-size:1.3rem;font-weight:700;
                         color:#8B4513;min-width:50px'>{val}</span>
            <span style='font-size:0.87rem;color:#2C1A0E'>{label}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_team:
        st.markdown("##### 👥 Tim Peneliti")
        team = [
            ("Francisco Gilbert Sondakh", "230004", "francisco23001@mail.unpad.ac.id"),
            ("Achmad Dzaki Azhari", "230034", "achmad23003@mail.unpad.ac.id"),
            ("Theophilus Samuel Ghozali", "230054", "theophilus23001@mail.unpad.ac.id"),
        ]
        for name, nim, email in team:
            st.markdown(f"""
            <div style='background:white;border:1px solid #E8C9A0;border-radius:10px;
                        padding:0.85rem 1rem;margin-bottom:0.6rem'>
            <div style='font-weight:600;color:#2C1A0E'>{name}</div>
            <div style='font-size:0.78rem;color:#7A5C44'>NIM: {nim}</div>
            <div style='font-size:0.78rem;color:#8B4513'>{email}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size:0.8rem;color:#7A5C44;margin-top:0.5rem'>
        Departemen Informatika · Universitas Padjadjaran · 2024
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 🚀 Rencana Pengembangan")
    roadmap = [
        ("Q1 2025", "Ekspansi ke 38 provinsi Indonesia"),
        ("Q2 2025", "Real-time user feedback loop"),
        ("Q3 2025", "KG Embedding (TransE/ComplEx)"),
        ("Q4 2025", "Mobile app & API publik"),
    ]
    cols = st.columns(4)
    for col, (period, plan) in zip(cols, roadmap):
        with col:
            st.markdown(f"""
            <div style='background:white;border:1px solid #E8C9A0;border-top:3px solid #C4874B;
                        border-radius:10px;padding:0.9rem;text-align:center'>
            <div style='font-size:0.72rem;font-weight:700;color:#7A5C44;letter-spacing:0.05em'>{period}</div>
            <div style='font-size:0.85rem;color:#2C1A0E;margin-top:0.4rem;font-weight:500'>{plan}</div>
            </div>
            """, unsafe_allow_html=True)


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;padding:1.5rem;border-top:1px solid #E8C9A0;
            color:#7A5C44;font-size:0.78rem;'>
🍛 <b>NusaRasa</b> · Semantic Web Project · Universitas Padjadjaran 2024 &nbsp;|&nbsp;
RDF/OWL · SPARQL · Apache Jena Fuseki · LLM Interface
</div>
""", unsafe_allow_html=True)
