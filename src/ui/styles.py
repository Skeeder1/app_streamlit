"""
Custom CSS styles for the application
"""
from src.config import Config


def get_custom_css() -> str:
    """
    Get custom CSS styles for the application
    
    Returns:
        CSS string
    """
    return f"""
    <style>
    /* Main app styling */
    .main {{
        background: linear-gradient(135deg, {Config.PRIMARY_COLOR} 0%, {Config.SECONDARY_COLOR} 100%);
    }}
    
    .stApp {{
        background: linear-gradient(135deg, {Config.PRIMARY_COLOR} 0%, {Config.SECONDARY_COLOR} 100%);
    }}
    
    /* Title container */
    .title-container {{
        background: linear-gradient(135deg, {Config.PRIMARY_COLOR} 0%, {Config.SECONDARY_COLOR} 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    
    .title-container h1 {{
        color: white;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }}
    
    .title-container p {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
    }}
    
    /* Success box */
    .success-box {{
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
        animation: slideIn 0.3s ease-in;
        color: #333333; /* Changed text color to dark gray */
    }}
    
    /* Info box */
    .info-box {{
        background-color: #87CEEB; /* Changed to a lighter blue */
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }}
    
    /* Warning box */
    .warning-box {{
        background-color: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }}
    
    /* Error box */
    .error-box {{
        background-color: #fee2e2;
        border-left: 4px solid #ef4444;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }}
    
    /* Section title */
    .section-title {{
        display: flex;
        align-items: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: {Config.SECONDARY_COLOR};
        font-weight: 600;
    }}
    
    /* Metrics card */
    .metric-card {{
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.2s;
    }}
    
    .metric-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }}
    
    /* Animations */
    @keyframes slideIn {{
        from {{
            opacity: 0;
            transform: translateY(-10px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    /* Character counter */
    .char-counter {{
        text-align: right;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }}
    
    /* Button styling */
    .stButton > button {{
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }}
    
    /* Sidebar styling */
    .css-1d391kg {{
        background-color: #fdfdfd; /* Changed to a lighter gray */
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Responsive design */
    @media (max-width: 768px) {{
        .title-container h1 {{
            font-size: 2rem;
        }}
        
        .title-container p {{
            font-size: 1rem;
        }}
    }}
    </style>
    """
