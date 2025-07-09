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
            'secondary-bg': '#F8F9FA',
            'tertiary-bg': '#E9ECEF',
            'text-color': '#212529',
            'label-color': '#212529',  # Darker for better contrast
            'text-muted': '#6c757d',
            'accent-color': '#0D6EFD',
            'border-color': '#CED4DA',
            'card-bg': '#FFFFFF',
            'text-muted': '#6C757D',
            'success': '#198754',
            'warning': '#FFC107',
            'danger': '#DC3545',
            'info': '#0DCAF0'
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
        --text-muted: {theme_vars.get('text-muted', '#6C757D')};
        --success: {theme_vars.get('success', '#198754')};
        --warning: {theme_vars.get('warning', '#FFC107')};
        --danger: {theme_vars.get('danger', '#DC3545')};
        --info: {theme_vars.get('info', '#0DCAF0')};
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
    .stTextInput input, .stNumberInput input, .stSelectbox select, 
    .stTextArea textarea, .stDateInput input {{
        background-color: var(--primary-bg) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 4px !important;
    }}
    
    /* Fix for input text color */
    .stTextInput input::placeholder, .stNumberInput input::placeholder,
    .stTextArea textarea::placeholder {{
        color: var(--text-muted) !important;
        opacity: 0.7 !important;
    }}
    
    /* Select box dropdown */
    .stSelectbox div[data-baseweb="select"] {{
        background-color: var(--primary-bg) !important;
        color: var(--text-color) !important;
    }}
    
    /* Form labels */
    label, .stRadio > label, .stCheckbox > label, .stSelectbox > label,
    .stNumberInput > label, .stTextInput > label, .stTextArea > label,
    .stDateInput > label, .stTimeInput > label {{
        color: var(--label-color, var(--text-color)) !important;
        font-weight: 500 !important;
    }}
    
    /* Checkbox and radio labels */
    .stCheckbox, .stRadio, .stCheckbox label, .stRadio label {{
        color: var(--text-color) !important;
    }}
    
    /* Fix for checkbox and radio button colors */
    .stCheckbox > label > div:first-child > div {{
        background-color: var(--primary-bg) !important;
        border-color: var(--border-color) !important;
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
    
    /* Sidebar - Base Styles */
    .stSidebar {{
        background-color: var(--secondary-bg) !important;
        color: var(--text-color) !important;
        padding: 1.5rem !important;
        border-right: 1px solid var(--border-color) !important;
    }}
    
    /* Sidebar Text - Catch All */
    .stSidebar *:not(button):not(input):not(select):not(textarea):not(svg):not(path) {{
        color: var(--text-color) !important;
    }}
    
    /* Sidebar Headers */
    .stSidebar h1,
    .stSidebar h2,
    .stSidebar h3,
    .stSidebar h4,
    .stSidebar h5,
    .stSidebar h6,
    .stSidebar .stMarkdown h1,
    .stSidebar .stMarkdown h2,
    .stSidebar .stMarkdown h3,
    .stSidebar .stMarkdown h4,
    .stSidebar .stMarkdown h5,
    .stSidebar .stMarkdown h6 {{
        color: var(--text-color) !important;
    }}
    
    /* Sidebar Form Elements */
    .stSidebar label,
    .stSidebar .stMarkdown,
    .stSidebar .stMarkdown p,
    .stSidebar .stMarkdown div,
    .stSidebar .stMarkdown span,
    .stSidebar .stRadio > label,
    .stSidebar .stCheckbox > label,
    .stSidebar .stSelectbox > label,
    .stSidebar .stNumberInput > label,
    .stSidebar .stTextInput > label,
    .stSidebar .stTextArea > label,
    .stSidebar .stDateInput > label,
    .stSidebar .stTimeInput > label,
    .stSidebar .stRadio,
    .stSidebar .stCheckbox,
    .stSidebar .stSelectbox,
    .stSidebar .stNumberInput,
    .stSidebar .stTextInput,
    .stSidebar .stTextArea,
    .stSidebar .stDateInput,
    .stSidebar .stTimeInput {{
        color: var(--text-color) !important;
    }}
    
    /* Fix for radio and checkbox labels specifically */
    .stSidebar .stRadio label,
    .stSidebar .stCheckbox label {{
        color: var(--text-color) !important;
        font-weight: normal !important;
    }}
    
    /* Fix for input placeholders */
    .stSidebar input::placeholder,
    .stSidebar textarea::placeholder {{
        color: var(--text-muted) !important;
        opacity: 0.7 !important;
    }}
    
    /* Fix for input values */
    .stSidebar input,
    .stSidebar select,
    .stSidebar textarea {{
        color: var(--text-color) !important;
    }}
    
    /* Fix for sidebar select boxes */
    .stSidebar .stSelectbox select {{
        background-color: var(--primary-bg) !important;
        color: var(--text-color) !important;
    }}
    
    /* Cards and expanders */
    .stExpander {{
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 1rem;
    }}
    
    /* Progress bars */
    .stProgress > div > div {{
        background-color: var(--accent-color) !important;
    }}
    
    /* Fix for success/warning/error messages */
    .stAlert {{
        background-color: var(--card-bg) !important;
        border-left: 3px solid var(--accent-color) !important;
    }}
    
    .stAlert .markdown-text-container {{
        color: var(--text-color) !important;
    }}
    
    /* Fix for expander content */
    .stExpander .streamlit-expanderContent {{
        background-color: var(--primary-bg) !important;
        color: var(--text-color) !important;
    }}
    
    /* Fix for metric cards */
    .stMetric {{
        background-color: var(--card-bg) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--border-color) !important;
    }}
    
    /* Fix for tooltips */
    .stTooltip {{
        background-color: var(--card-bg) !important;
        color: var(--text-color) !important;
    }}
    
    /* Main Content Text - Global */
    .stApp,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stMarkdown, .stMarkdown p, .stMarkdown div, .stMarkdown span,
    .stAlert, .stAlert p, .stAlert div,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4,
    .stMarkdown h5, .stMarkdown h6 {
        color: var(--text-color) !important;
    }
    
    /* BMI and Calorie Results - Specific Fixes */
    .stMetric, .stMetricLabel, .stMetricValue, .stMetricDelta,
    .stMetricLabel p, .stMetricValue p, .stMetricDelta p,
    .stMetricLabel div, .stMetricValue div, .stMetricDelta div {
        color: var(--text-color) !important;
    }
    
    /* Cards and Containers */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: var(--secondary-bg) !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre;
        background-color: var(--tertiary-bg);
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding: 10px 20px;
        margin-right: 4px;
        margin-left: 4px;
        color: var(--text-color) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--accent-color) !important;
        color: white !important;
    }
    
    /* Result Sections - Specific Elements */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: var(--text-color) !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Metrics and Results Containers */
    .stAlert, .stAlert p, .stAlert div,
    .stMarkdown, .stMarkdown p, .stMarkdown div,
    .stDataFrame, .stDataFrame th, .stDataFrame td,
    .element-container, .stMarkdownContainer {
        color: var(--text-color) !important;
    }
    
    /* Fix for any remaining text elements */
    .stApp *:not(button):not(input):not(select):not(textarea):not(svg):not(path) {
        color: var(--text-color) !important;
    }
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