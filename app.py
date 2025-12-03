import streamlit as st
import time
import random
import pandas as pd
import numpy as np
from transformers import pipeline

# --- CONFIGURATION ---
st.set_page_config(
    page_title="TrendHunter AI Pro",
    page_icon="🦄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PREMIUM ---
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(16, 20, 30) 0%, rgb(10, 10, 15) 90%);
        color: #e0e0e0;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    div[data-testid="stMetricValue"] {
        font-size: 24px;
        color: #00ffc3;
    }
    div.stButton > button {
        background: linear-gradient(45deg, #00C9FF, #92FE9D);
        color: #0f172a;
        font-weight: 800;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        width: 100%;
        transition: transform 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- AI ENGINE (Cached) ---
@st.cache_resource
def load_model():
    return pipeline('text-generation', model='distilgpt2')

try:
    text_gen = load_model()
    model_status = True
except:
    model_status = False

# --- DATA GENERATOR ---
def get_trend_data(niche):
    trends = {
        "Fashion": ["Y2K Cargo Parachute", "Cyberpunk Bomber Jacket", "Oversized Knit Beige", "Retro Sunglasses 90s"],
        "Gadget": ["Transparent Powerbank", "Smart Health Ring", "RGB Mechanical Keypad", "Mini Projector 4K"],
        "Home": ["Levitating Moon Lamp", "Sunset Projector", "Ergonomic Memory Pillow", "Aesthetic Glass Diffuser"],
        "Beauty": ["Gua Sha Jade Set", "Vegan Lip Stain", "Electric Face Massager", "Korean Sunscreen Stick"]
    }
    return random.choice(trends.get(niche, trends["Fashion"]))

def generate_chart_data():
    return pd.DataFrame(
        np.random.randn(20, 3).cumsum(axis=0),
        columns=['Search Volume', 'Social Mention', 'Sales Prediction']
    )

# --- UI LAYOUT ---
st.title("🦄 TrendHunter AI: Product Intelligence")
st.caption("AI-Powered E-commerce Research Assistant")

with st.sidebar:
    st.header("🎛️ Control Panel")
    selected_niche = st.selectbox("Pilih Niche Market:", ["Fashion", "Gadget", "Home", "Beauty"])
    tone_style = st.select_slider("Gaya Bahasa Copywriting:", options=["Formal", "Persuasif", "Viral/Hype"])
    st.markdown("---")
    st.info(f"⚡ AI Engine: {'Online' if model_status else 'Offline'}")

if st.button("🚀 TEMUKAN WINNING PRODUCT"):
    
    # Animation
    progress_text = "AI sedang memindai tren pasar global..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()

    product_name = get_trend_data(selected_niche)
    
    col_left, col_right = st.columns([1, 1.3])

    with col_left:
        st.markdown(f"### 🎯 Terpilih: {product_name}")
        
        clean_prompt = f"product photography of {product_name}, {selected_niche} aesthetic, studio lighting, 4k resolution, minimalistic background, commercial shot"
        img_url = f"https://image.pollinations.ai/prompt/{clean_prompt.replace(' ', '%20')}?width=800&height=800&nologo=true"
        
        st.image(img_url, caption=f"AI Prototype: {product_name}", use_column_width=True)
        
        st.markdown("<div class='glass-card'><b>📈 Trend Momentum</b>", unsafe_allow_html=True)
        st.line_chart(generate_chart_data(), height=150)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("### 🧠 AI Analysis & Strategy")
        
        base_price = random.randint(50, 500) * 1000
        margin = random.randint(30, 65)
        sell_price = base_price + (base_price * margin / 100)
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Modal Awal", f"Rp {base_price/1000:.0f}K")
        m2.metric("Harga Jual", f"Rp {sell_price/1000:.0f}K", f"+{margin}%")
        m3.metric("Potensi Viral", "Tinggi", "🔥")

        st.markdown("#### ✍️ Auto-Copywriting")
        with st.spinner("Writing magic words..."):
            seed = f"Get the viral {product_name} now. Perfect for {selected_niche} lovers."
            try:
                res = text_gen(seed, max_length=50, num_return_sequences=1)[0]['generated_text']
                final_copy = res.rsplit('.', 1)[0] + "."
            except:
                final_copy = "AI generated text unavailable."
        
        st.info(f'"{final_copy}"')
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("#### 🚀 Strategi Peluncuran")
        if selected_niche == "Fashion":
            st.write("👉 **Platform:** TikTok Shop & Instagram Reels")
            st.write("👉 **Content:** Video transisi 'Before-After' pemakaian.")
        elif selected_niche == "Gadget":
            st.write("👉 **Platform:** Shopee Video & YouTube Shorts")
            st.write("👉 **Content:** Unboxing ASMR & Zoom-in fitur utama.")
        else:
            st.write("👉 **Platform:** Facebook Ads & Marketplace")
            st.write("👉 **Content:** Foto estetik di dalam ruangan.")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("""
    <div style='text-align: center; padding: 50px; opacity: 0.7;'>
        <h2>👋 Ready to hunt?</h2>
        <p>Pilih niche di sebelah kiri dan biarkan AI menganalisis pasar untukmu.</p>
    </div>
    """, unsafe_allow_html=True)
