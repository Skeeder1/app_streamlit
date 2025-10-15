"""
Reusable UI components
"""
import streamlit as st
from typing import Optional


def render_title():
    """Render the main title of the application"""
    st.markdown("""
        <div class="title-container">
            <h1>🐦 Twitter Sentiment Analyzer</h1>
            <p>Analyse de sentiment avec Intelligence Artificielle et explicabilité LIME</p>
        </div>
    """, unsafe_allow_html=True)


def render_status_box(status: str, message: str):
    """
    Render a status box
    
    Args:
        status: Status type (success, error, warning, info)
        message: Message to display
    """
    box_class = f"{status}-box"
    icons = {
        "success": "✅",
        "error": "❌",
        "warning": "⚠️",
        "info": "ℹ️"
    }
    icon = icons.get(status, "")
    
    st.markdown(f"""
        <div class="{box_class}">
            {icon} {message}
        </div>
    """, unsafe_allow_html=True)


def render_section_title(title: str, icon: str = ""):
    """
    Render a section title
    
    Args:
        title: Title text
        icon: Optional emoji icon
    """
    st.markdown(f"""
        <div class="section-title">
            {icon} {title}
        </div>
    """, unsafe_allow_html=True)


def render_character_counter(text: str, max_length: int = 280):
    """
    Render character counter
    
    Args:
        text: Current text
        max_length: Maximum allowed length
    """
    char_count = len(text)
    color = "#64748b" if char_count <= max_length else "#ef4444"
    
    st.markdown(
        f'<p class="char-counter" style="color: {color};">'
        f'Caractères utilisés: {char_count}/{max_length}</p>',
        unsafe_allow_html=True
    )


def render_metric_card(label: str, value: str, delta: Optional[str] = None):
    """
    Render a metric card
    
    Args:
        label: Metric label
        value: Metric value
        delta: Optional delta value
    """
    st.metric(label=label, value=value, delta=delta)


def render_info_tip(message: str):
    """
    Render an info tip
    
    Args:
        message: Tip message
    """
    st.markdown(f"""
        <div class="info-box">
            💡 <strong>Astuce :</strong> {message}
        </div>
    """, unsafe_allow_html=True)


def render_loading_message(message: str):
    """
    Render a loading message with spinner
    
    Args:
        message: Loading message
    """
    return st.spinner(message)
