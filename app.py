"""
Twitter Sentiment Analyzer - Main Application
A Streamlit app for analyzing tweet sentiment using AI and LIME explainability
"""
import streamlit as st
from src.config import Config
from src.api_client import APIClient
from src.ui import (
    get_custom_css,
    render_title,
    render_status_box,
    render_section_title,
    render_character_counter,
    render_info_tip,
    render_loading_message
)

# Page configuration
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon=Config.PAGE_ICON,
    layout=Config.LAYOUT
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize session state
if 'tweet_input' not in st.session_state:
    st.session_state.tweet_input = ""

# Sidebar configuration
st.sidebar.title("⚙️ Configuration")
api_url = st.sidebar.text_input(
    "URL de l'API",
    value=Config.API_URL,
    help="URL de base de l'API de prédiction"
)

# Initialize API client
api_client = APIClient(base_url=api_url)

# Main title
render_title()

# Check API health
health_status = api_client.check_health()

if health_status["status"] == "connected":
    render_status_box("success", health_status["message"])
    api_connected = True
else:
    render_status_box("error", health_status["message"])
    api_connected = False

# Tweet input section
render_section_title("Saisissez votre tweet à analyser", "📝")

tweet_text = st.text_area(
    "Texte du tweet",
    value=st.session_state.tweet_input,
    placeholder=f"Tapez votre tweet ici... ({Config.MAX_TWEET_LENGTH} caractères max)",
    max_chars=Config.MAX_TWEET_LENGTH,
    height=150,
    key="tweet_input_area",
    label_visibility="collapsed"
)

# Update session state
st.session_state.tweet_input = tweet_text

# Character counter
render_character_counter(tweet_text, Config.MAX_TWEET_LENGTH)

# Actions section
render_section_title("Actions", "🎮")

render_info_tip("Utilisez Ctrl+Entrée dans la zone de texte pour prédire rapidement")

# Action buttons
col1, col2, col3 = st.columns(3)

with col1:
    predict_button = st.button(
        "🔮 Prédire le Sentiment",
        use_container_width=True,
        type="primary"
    )

with col2:
    explain_button = st.button(
        "🔍 Expliquer avec LIME",
        use_container_width=True
    )

with col3:
    clear_button = st.button(
        "🗑️ Effacer",
        use_container_width=True
    )

# Handle clear button
if clear_button:
    st.session_state.tweet_input = ""
    st.rerun()

# Handle predict button
if predict_button:
    if not tweet_text.strip():
        st.warning("⚠️ Veuillez saisir un tweet à analyser")
    elif not api_connected:
        st.error("❌ Veuillez d'abord connecter l'API")
    else:
        try:
            with render_loading_message("🔮 Analyse en cours..."):
                result = api_client.predict_sentiment(tweet_text)
            
            st.success("✅ Analyse terminée !")
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Sentiment",
                    result.get("sentiment", "N/A").upper()
                )
            
            with col2:
                confidence = result.get("confidence", 0)
                st.metric(
                    "Confiance",
                    f"{confidence:.2%}" if isinstance(confidence, float) else str(confidence)
                )
            
            with col3:
                st.metric(
                    "Polarité",
                    result.get("polarity", "N/A").upper()
                )
                
        except Exception as e:
            st.error(f"❌ Erreur lors de la prédiction: {str(e)}")

# Handle explain button
if explain_button:
    if not tweet_text.strip():
        st.warning("⚠️ Veuillez saisir un tweet à analyser")
    elif not api_connected:
        st.error("❌ Veuillez d'abord connecter l'API")
    else:
        try:
            with render_loading_message("🔍 Génération de l'explication LIME..."):
                result = api_client.explain_prediction(tweet_text)
            
            st.success("✅ Explication générée !")
            
            # Display explanation
            if "explanation" in result:
                st.subheader("📊 Explication LIME")
                st.write(result["explanation"])
            
            if "image" in result:
                st.image(result["image"], caption="Visualisation LIME")
                
        except Exception as e:
            st.error(f"❌ Erreur lors de l'explication: {str(e)}")

# Additional tip
render_info_tip("Saisissez un tweet ci-dessus ou utilisez un exemple de la sidebar pour commencer !")

# Sidebar - Examples
st.sidebar.markdown("---")
st.sidebar.title("📚 Exemples de tweets")
st.sidebar.markdown("Cliquez sur un exemple pour l'utiliser :")

for i, example in enumerate(Config.TWEET_EXAMPLES, 1):
    if st.sidebar.button(f"Exemple {i}", key=f"example_{i}"):
        st.session_state.tweet_input = example
        st.rerun()

# Sidebar - About
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ À propos")
st.sidebar.markdown(f"""
Cette application utilise l'intelligence artificielle pour analyser le sentiment des tweets.

**Fonctionnalités :**
- 🔮 Prédiction de sentiment
- 🔍 Explicabilité avec LIME
- 📊 Visualisation des résultats

**Version :** {st.session_state.get('version', '1.0.0')}
""")

# Sidebar - Statistics (if connected)
if api_connected:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Statistiques")
    st.sidebar.metric("Statut API", "✅ Connecté")
    st.sidebar.metric("URL", api_url)
