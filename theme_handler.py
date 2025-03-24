import streamlit as st

def apply_theme(theme):
    """Applies selected theme with comprehensive styling"""
    if theme == "Dark Mode":
        st.markdown(
            """
            <style>
            :root {
                --primary-bg: #121212;
                --secondary-bg: #1E1E1E;
                --tertiary-bg: #333333;
                --text-color: #FFFFFF;
                --accent-color: #4CAF50;
                --border-color: #555555;
                --card-bg: #252525;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            :root {
                --primary-bg: #FFFFFF;
                --secondary-bg: #F5F5F5;
                --tertiary-bg: #E0E0E0;
                --text-color: #000000;
                --accent-color: #2196F3;
                --border-color: #DDDDDD;
                --card-bg: #FAFAFA;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    
    st.markdown(
        """
        <style>
        /* Base styles */
        body {
            background-color: var(--primary-bg);
            color: var(--text-color);
        }
        
        /* Main content area */
        .main .block-container {
            background-color: var(--primary-bg);
            padding: 2rem 3rem;
        }
        
        /* Input elements */
        .stTextInput, .stNumberInput, .stSelectbox, 
        .stCheckbox, .stTextArea, .stDateInput {
            background-color: var(--secondary-bg);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            border-radius: 4px;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: var(--accent-color);
            color: white;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            border: none;
            font-weight: 500;
        }
        .stButton>button:hover {
            opacity: 0.9;
        }
        
        /* Radio buttons and checkboxes */
        .stRadio label, .stCheckbox label {
            color: var(--text-color) !important;
        }
        
        /* Sidebar */
        .stSidebar {
            background-color: var(--secondary-bg) !important;
            padding: 1.5rem;
            border-right: 1px solid var(--border-color);
        }
        
        /* Cards and expanders */
        .stExpander {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .stExpander .streamlit-expanderHeader {
            background-color: var(--tertiary-bg);
            color: var(--text-color);
            border-radius: 8px 8px 0 0;
        }
        
        /* Metrics */
        .stMetric {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
        }
        
        /* Progress bars */
        .stProgress > div > div {
            background-color: var(--accent-color) !important;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            background-color: var(--secondary-bg);
            border-radius: 8px;
        }
        .stTabs [data-baseweb="tab"] {
            color: var(--text-color) !important;
        }
        .stTabs [aria-selected="true"] {
            background-color: var(--accent-color) !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )