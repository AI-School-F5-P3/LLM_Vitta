from llm_project.src.models.model_lo import GroqChat
import streamlit as st
import os
from pathlib import Path
from llm_project.src.frontend.styles import apply_theme_styles, apply_white_text_input


class ChatInterface:
    def __init__(self):
        self.llm = GroqChat()
        # Obtener la ruta base del proyecto
        self.base_path = Path(__file__).parent.parent.parent
        self.img_path = str(Path(self.base_path) / "img" / "Genievailogo.png")
        self.slider_img_path = str(Path(self.base_path) / "img" / "Genievai.1.png")
        # Añadir rutas para los avatares
        self.user_avatar = str(Path(self.base_path) / "img" / "user_avatar.png")
        self.assistant_avatar = str(Path(self.base_path) / "img" / "assistant_avatar.png")
        
        self.content_templates = {
            "Blog": """Genera un artículo de blog sobre {tema}. 
                      Debe incluir: título, introducción, desarrollo y conclusión.""",
            "Twitter": """Crea un hilo de Twitter sobre {tema}. 
                         Máximo 280 caracteres por tweet. Usa un tono informal y directo.""",
            "Instagram": """Genera una publicación de Instagram sobre {tema}. 
                          Incluye emojis relevantes y hashtags populares.""",
            "LinkedIn": """Crea una publicación profesional para LinkedIn sobre {tema}.
                          Utiliza un tono formal y profesional, incluye llamadas a la acción,
                          menciona aspectos relevantes para la red profesional y añade 3-5 hashtags estratégicos.
                          Máximo 3000 caracteres.""",
            "SEO": """Crea un artículo optimizado para SEO sobre {tema}. 
                     Incluye palabras clave, meta descripción y estructura H1, H2, H3.""",
            "Infantil": """Explica {tema} de forma divertida y simple para niños. 
                         Usa analogías y ejemplos cotidianos."""
        }
        self.main_bg_color = "#0f0f0f"
        self.secondary_bg_color = "#1f1f1f"
        self.text_color = "#ffffff"

    def initialize_session_state(self):
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if 'temperature' not in st.session_state:
            st.session_state.temperature = 0.7
        if 'max_length' not in st.session_state:
            st.session_state.max_length = 256

    def get_response(self, prompt: str, tema: str, platform: str) -> str:
        try:
            template = self.content_templates[platform]
            formatted_prompt = template.format(tema=tema)
            
            system_prompt = """Eres un experto en creación de contenido para diferentes 
            plataformas. Tu tarea es generar contenido optimizado y adaptado para la 
            plataforma especificada. IMPORTANTE: Siempre debes responder en español,
            independientemente del idioma del input."""
            
            full_prompt = f"""
            {system_prompt}
            
            PLATAFORMA: {platform}
            SOLICITUD: {formatted_prompt}
            CONTEXTO ADICIONAL: {prompt}
            
            RECUERDA: Tu respuesta debe ser SIEMPRE en español.
            """
            
            return self.llm.invoke(full_prompt).strip()
        except Exception as e:
            st.error(f"Error al generar respuesta: {str(e)}")
            return "Lo siento, hubo un error al procesar tu solicitud."

    def run(self):
        custom_css = f"""
        .main-container {{
            background-color: {self.main_bg_color};
        }}
        """
        
        # Crear layout con imagen y título en la misma línea
        col1, col2 = st.columns([1, 3])
        
        # Imagen en la columna izquierda
        with col1:
            st.image(self.img_path, use_container_width=True)
        
        # Título y subtítulo en la columna derecha
        with col2:
            st.title("GenievAI")
            st.subheader("Generador de Contenido Multiplataforma")
        
        # Primero el logo en el sidebar
        st.sidebar.image(self.slider_img_path, use_container_width=True)
        
        # Luego el selector de tema
        theme = st.sidebar.radio(
            "Tema",
            ["Claro", "Oscuro"]
        )
        
        # Definir colores según el tema
        if theme == "Oscuro":
            main_bg_color = "#261E2F"
            sidebar_bg_color = "#271827"
            header_bg_color = "#261E2F"
            text_color = "#ffffff"
        else:
            main_bg_color = "#ECE8EF"
            sidebar_bg_color = "#bcaedc"
            header_bg_color = "#ECE8EF"
            text_color = "#000000"
        
        # Aplicar estilos desde el módulo styles
        apply_theme_styles(theme, main_bg_color, sidebar_bg_color, header_bg_color, text_color)
        apply_white_text_input()
        
        # Añadir selector de plataforma
        platform = st.sidebar.selectbox(
            "Selecciona la plataforma",
            ["Blog", "Twitter", "Instagram", "LinkedIn", "SEO", "Infantil"]
        )
        
        # Añadir campo de entrada para el tema
        tema = st.sidebar.text_input(
            "Escribe el tema seleccionado",
            key="tema_input",
        )
        
        self.initialize_session_state()
        
        with st.sidebar:
            st.header("Configuración")
            st.session_state.temperature = st.slider(
                "Temperatura",
                min_value=0.0,
                max_value=1.0,
                value=0.7,
                step=0.1
            )
            
            if st.button("Limpiar conversación"):
                st.session_state.messages = []
                st.rerun()

        for message in st.session_state.messages:
            with st.chat_message(message["role"], avatar=self.user_avatar if message["role"] == "user" else self.assistant_avatar):
                st.markdown(message["content"])

        if prompt := st.chat_input("Escribe tu mensaje aquí..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user", avatar=self.user_avatar):
                st.markdown(prompt)

            with st.chat_message("assistant", avatar=self.assistant_avatar):
                with st.spinner("Pensando..."):
                    response = self.get_response(prompt, tema, platform)
                    st.markdown(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response})

        # Añadir opciones de exportacion
        if st.sidebar.button("Exportar contenido"):
            # Lógica para exportar el contenido generado
            pass
        
        # Añadir preview del contenido
        if st.sidebar.checkbox("Mostrar vista previa"):
            # Lógica para mostrar preview según la plataforma
            pass
        
        # Añadir métricas básicas
        if 'response' in locals():
            st.sidebar.markdown("### Métricas")
            st.sidebar.text(f"Caracteres: {len(response)}")
            st.sidebar.text(f"Palabras: {len(response.split())}")


if __name__ == "__main__":
    chat_interface = ChatInterface()
    chat_interface.run()
