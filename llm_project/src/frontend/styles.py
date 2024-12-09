import streamlit as st

def apply_theme_styles(theme, main_bg_color, sidebar_bg_color, header_bg_color, text_color):
    st.markdown(f"""
        <style>
            /* Color de fondo principal */
            [data-testid="stAppViewContainer"] {{
                background-color: {main_bg_color};
            }}
            
            /* Color de la barra lateral */
            [data-testid="stSidebar"] {{
                background-color: {sidebar_bg_color};
            }}
            
            /* Color del header */
            [data-testid="stHeader"] {{
                background-color: {header_bg_color};
            }}
            
            /* Color del texto */
            .stMarkdown, .stText, p, h1, h2, h3 {{
                color: {text_color} !important;
            }}
            
            /* Color de los botones */
            .stButton button {{
                background-color: {sidebar_bg_color};
                color: {text_color};
            }}
            
            /* Color de los inputs */
            .stTextInput input {{
                color: {text_color};
            }}
            
            /* Color de los selectbox */
            .stSelectbox select {{
                color: {text_color};
            }}
        </style>
    """, unsafe_allow_html=True)


def apply_white_text_input():
    st.markdown("""
        <style>
            [data-testid="stTextInput"] input {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)