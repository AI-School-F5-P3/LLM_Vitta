from llm_project.src.models.model_lo import GroqChat
import streamlit as st


class ChatInterface:
    def __init__(self):
        self.llm = GroqChat()
        
    def initialize_session_state(self):
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if 'temperature' not in st.session_state:
            st.session_state.temperature = 0.7
        if 'max_length' not in st.session_state:
            st.session_state.max_length = 256

    def get_response(self, prompt: str) -> str:
        try:
            formatted_prompt = f"""
            Usuario: {prompt}
            Asistente: """
            
            return self.llm(formatted_prompt).strip()
        except Exception as e:
            st.error(f"Error al generar respuesta: {str(e)}")
            return "Lo siento, hubo un error al procesar tu solicitud."

    def run(self):
        st.title("Chat con Ollama")
        
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
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Escribe tu mensaje aquí..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    response = self.get_response(prompt)
                    st.markdown(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response})


if __name__ == "__main__":
    chat_interface = ChatInterface()
    chat_interface.run()
