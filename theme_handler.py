import streamlit as st
from typing import Literal, Dict, Any

def init_session_state() -> None:
    """Initialize session state variables if they don't exist."""
    if 'theme' not in st.session_state:
        st.session_state.theme = 'Light Mode'  # Default theme

def get_theme_vars(theme: str) -> Dict[str, str]:
    """Return CSS variables for the specified theme."""
    themes = {
        'Dark Mode': {
            'primary-bg': '#121212',
            'secondary-bg': '#1E1E1E',
            'tertiary-bg': '#333333',
            'text-color': '#FFFFFF',
            'accent-color': '#4CAF50',
            'border-color': '#555555',
            'card-bg': '#252525',
        },
        'Light Mode': {
            'primary-bg': '#FFFFFF',
            'secondary-bg': '#F5F5F5',
            'tertiary-bg': '#E0E0E0',
            'text-color': '#000000',
            'accent-color': '#2196F3',
            'border-color': '#DDDDDD',
            'card-bg': '#FAFAFA',
        }
    }
    return themes.get(theme, themes['Light Mode'])

def get_theme_css(theme_vars: Dict[str, str]) -> str:
    """Generate CSS styles based on theme variables."""
    return f"""
    <style>
    :root {{
        --primary-bg: {theme_vars['primary-bg']};
        --secondary-bg: {theme_vars['secondary-bg']};
        --tertiary-bg: {theme_vars['tertiary-bg']};
        --text-color: {theme_vars['text-color']};
        --accent-color: {theme_vars['accent-color']};
        --border-color: {theme_vars['border-color']};
        --card-bg: {theme_vars['card-bg']};
    }}
    
    /* Base styles */
    body {{
        background-color: var(--primary-bg);
        color: var(--text-color);
    }}
    
    /* Main content area */
    .main .block-container {{
        background-color: var(--primary-bg);
        padding: 2rem 3rem;
    }}
    
    /* Input elements */
    .stTextInput, .stNumberInput, .stSelectbox, 
    .stCheckbox, .stTextArea, .stDateInput {{
        background-color: var(--secondary-bg);
        color: var(--text-color);
        border: 1px solid var(--border-color);
        border-radius: 4px;
    }}
    
    /* Buttons */
    .stButton>button {{
        background-color: var(--accent-color);
        color: white;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: 500;
    }}
    .stButton>button:hover {{
        opacity: 0.9;
    }}
    
    /* Radio buttons and checkboxes */
    .stRadio label, .stCheckbox label {{
        color: var(--text-color) !important;
    }}
    
    /* Sidebar */
    .stSidebar {{
        background-color: var(--secondary-bg) !important;
        padding: 1.5rem;
        border-right: 1px solid var(--border-color);
    }}
    
    /* Cards and expanders */
    .stExpander {{
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        margin-bottom: 1rem;
    }}
    .stExpander .streamlit-expanderHeader {{
        background-color: var(--tertiary-bg);
        color: var(--text-color);
        border-radius: 8px 8px 0 0;
    }}
    
    /* Metrics */
    .stMetric {{
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 1rem;
    }}
    
    /* Progress bars */
    .stProgress > div > div {{
        background-color: var(--accent-color) !important;
    }}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: var(--secondary-bg);
        border-radius: 8px;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: var(--text-color) !important;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: var(--accent-color) !important;
        color: white !important;
    }}
    </style>
    """

@st.cache_data(ttl=3600)  # Cache the theme for 1 hour
def apply_theme(theme: Literal['Light Mode', 'Dark Mode'] = None) -> None:
    """
    Applies the selected theme with comprehensive styling.
    
    Args:
        theme: The theme to apply ('Light Mode' or 'Dark Mode'). If None, uses the current session theme.
    """
    if theme is not None:
        st.session_state.theme = theme
    
    current_theme = st.session_state.theme
    theme_vars = get_theme_vars(current_theme)
    css = get_theme_css(theme_vars)
    
    st.markdown(css, unsafe_allow_html=True)