import streamlit as st
import requests
import json

# Configuration de la page
st.set_page_config(
    page_title="Twitter Sentiment Analyzer",
    page_icon="🐦",
    layout="wide"
)

# CSS personnalisé pour le style de l'interface
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0ea5e9 0%, #1e293b 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #0ea5e9 0%, #1e293b 100%);
    }
    .title-container {
        background: linear-gradient(135deg, #0ea5e9 0%, #1e293b 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .title-container h1 {
        color: white;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .title-container p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
    }
    .success-box {
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #0e9fe1;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .section-title {
        display: flex;
        align-items: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# URL de l'API (à configurer)
API_URL = st.sidebar.text_input("URL de l'API", "http://localhost:8003")

# Titre principal
st.markdown("""
    <div class="title-container">
        <h1>🐦 Twitter Sentiment Analyzer</h1>
        <p>Analyse de sentiment avec Intelligence Artificielle et explicabilité LIME</p>
    </div>
""", unsafe_allow_html=True)

# Vérification de la connexion API
try:
    response = requests.get(f"{API_URL}/", timeout=2)
    if response.status_code == 200:
        st.markdown("""
            <div class="success-box">
                ✅ API connectée avec succès
            </div>
        """, unsafe_allow_html=True)
        api_connected = True
    else:
        st.error("❌ Erreur de connexion à l'API")
        api_connected = False
except:
    st.error("❌ Impossible de se connecter à l'API. Vérifiez que l'API est démarrée.")
    api_connected = False

# Section de saisie du tweet
st.markdown("""
    <div class="section-title">
        📝 Saisissez votre tweet à analyser
    </div>
""", unsafe_allow_html=True)

# Zone de texte pour le tweet
tweet_text = st.text_area(
    "",
    placeholder="Tapez votre tweet ici... (280 caractères max)",
    max_chars=280,
    height=150,
    key="tweet_input",
    label_visibility="collapsed"
)

# Compteur de caractères
char_count = len(tweet_text)
st.markdown(f"<p style='text-align: right; color: #64748b;'>Caractères utilisés: {char_count}/280</p>", unsafe_allow_html=True)

# Section Actions
st.markdown("""
    <div class="section-title">
        🎮 Actions
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="info-box">
        💡 Utilisez Ctrl+Entrée dans la zone de texte pour prédire rapidement
    </div>
""", unsafe_allow_html=True)

# Boutons d'action
col1, col2, col3 = st.columns(3)

with col1:
    predict_button = st.button("🔮 Prédire le Sentiment", use_container_width=True, type="primary")

with col2:
    explain_button = st.button("🔍 Expliquer avec LIME", use_container_width=True)

with col3:
    clear_button = st.button("🗑️ Effacer", use_container_width=True)

# Astuce
st.markdown("""
    <div class="info-box">
        💡 <strong>Astuce :</strong> Saisissez un tweet ci-dessus ou utilisez un exemple de la sidebar pour commencer !
    </div>
""", unsafe_allow_html=True)

# Traitement des boutons
if clear_button:
    st.session_state.tweet_input = ""
    st.rerun()

if predict_button and tweet_text:
    if api_connected:
        try:
            with st.spinner("Analyse en cours..."):
                response = requests.post(
                    f"{API_URL}/predict",
                    json={"text": tweet_text},
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.success("✅ Analyse terminée !")
                    
                    # Affichage des résultats
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Sentiment", result.get("sentiment", "N/A"))
                    
                    with col2:
                        confidence = result.get("confidence", 0)
                        st.metric("Confiance", f"{confidence:.2%}")
                    
                    with col3:
                        st.metric("Polarité", result.get("polarity", "N/A"))
                    
                else:
                    st.error(f"Erreur lors de la prédiction: {response.status_code}")
        except Exception as e:
            st.error(f"Erreur: {str(e)}")
    else:
        st.warning("⚠️ Veuillez d'abord connecter l'API")
elif predict_button:
    st.warning("⚠️ Veuillez saisir un tweet à analyser")

if explain_button and tweet_text:
    if api_connected:
        try:
            with st.spinner("Génération de l'explication LIME..."):
                response = requests.post(
                    f"{API_URL}/explain",
                    json={"text": tweet_text},
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.success("✅ Explication générée !")
                    
                    # Affichage de l'explication
                    if "explanation" in result:
                        st.subheader("📊 Explication LIME")
                        st.write(result["explanation"])
                    
                    if "image" in result:
                        st.image(result["image"], caption="Visualisation LIME")
                    
                else:
                    st.error(f"Erreur lors de l'explication: {response.status_code}")
        except Exception as e:
            st.error(f"Erreur: {str(e)}")
    else:
        st.warning("⚠️ Veuillez d'abord connecter l'API")
elif explain_button:
    st.warning("⚠️ Veuillez saisir un tweet à analyser")

# Sidebar avec des exemples
st.sidebar.title("📚 Exemples de tweets")
st.sidebar.markdown("Cliquez sur un exemple pour l'utiliser :")

examples = [
    "I love this product! It's amazing! 😍",
    "This is the worst experience ever. Very disappointed.",
    "The weather is nice today.",
    "I'm not sure how I feel about this...",
    "Absolutely fantastic! Best day of my life! 🎉"
]

for i, example in enumerate(examples, 1):
    if st.sidebar.button(f"Exemple {i}", key=f"example_{i}"):
        st.session_state.tweet_input = example
        st.rerun()

# Informations supplémentaires
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ À propos")
st.sidebar.markdown("""
Cette application utilise l'intelligence artificielle pour analyser le sentiment des tweets.

**Fonctionnalités :**
- 🔮 Prédiction de sentiment
- 🔍 Explicabilité avec LIME
- 📊 Visualisation des résultats
""")
