# 🐦 Twitter Sentiment Analyzer

Application web interactive pour analyser le **sentiment de tweets** avec l’IA (Streamlit + API).

## ✨ Fonctionnalités

* 🔮 Prédiction de sentiment en temps réel
* 🔍 Explicabilité des décisions avec **LIME**
* 📊 Interface moderne et intuitive
* 📚 Exemples de tweets intégrés

---

## 🚀 Installation

```bash
# 1) Installer les dépendances
pip install -r requirements.txt

# 2) Configurer l'API (optionnel)
cp .env.example .env
# puis éditez .env (voir section Configuration)

# 3) Lancer l'application
streamlit run app.py
```

L’application s’ouvrira sur : `http://localhost:8501`

---

## 📁 Structure du projet

```text
streamlit/
├─ app.py                 # Application principale (Streamlit)
├─ requirements.txt       # Dépendances
├─ .env.example           # Exemple de configuration
├─ README.md              # Ce fichier
│
├─ src/                   # Code source
│  ├─ config.py           # Configuration (thème, exemples, etc.)
│  ├─ api_client.py       # Client HTTP pour l'API
│  └─ ui/                 # Composants UI réutilisables
│     ├─ styles.py        # Styles CSS-like pour Streamlit
│     └─ components.py    # Widgets / vues
│
├─ assets/                # Ressources statiques
│  └─ examples/           # Exemples de tweets
│
└─ tests/                 # Tests unitaires
   └─ test_api_client.py
```

---

## ⚙️ Configuration

Créer (ou éditer) un fichier `.env` à la racine :

```env
API_URL=http://localhost:8000
API_TIMEOUT=30
```

> `API_URL` : endpoint de l’API de prédiction.
> `API_TIMEOUT` : délai max en secondes pour les requêtes HTTP.

Pour personnaliser l’interface (exemples de tweets, thème, etc.), modifiez `src/config.py`.

---

## 🔗 Intégration API

L’application consomme une API avec les endpoints suivants :

### Health check

**GET /**

```json
{"status": "ok"}
```

### Prédiction de sentiment

**POST /predict**

**Requête**

```json
{"text": "I love this!"}
```

**Réponse**

```json
{"sentiment": "positive", "confidence": 0.95}
```

### Explication LIME

**POST /explain**

**Requête**

```json
{"text": "I love this!"}
```

**Réponse**

```json
{"explanation": "...", "image": "..."}
```

---

## 🧪 Tests

```bash
# Lancer l’ensemble des tests
pytest tests/

# Couverture de code
pytest --cov=src tests/
```

---

## 👥 Auteur

**ESIEA MLOps Team** — [Skeeder1](https://github.com/Skeeder1)

---

## 📜 Licence

MIT — voir le fichier [LICENSE](LICENSE)
