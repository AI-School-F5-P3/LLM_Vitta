import yaml
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class GroqLoader:
    def __init__(self, config_path: str = "llm_project/configs/model_config.yaml"):
        try:
            with open(config_path, "r") as file:
                config = yaml.safe_load(file)
            if not config or 'model' not in config:
                raise ValueError("Configuración inválida")
            
            self.model_name = config['model']['name']
            self.parameters = config['model'].get('parameters', {})
            
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró: {config_path}")
        except yaml.YAMLError:
            raise ValueError(f"Error en YAML: {config_path}")

    def get_model(self):
        if not hasattr(self, 'model'):
            print(f"Inicializando modelo {self.model_name}...")
            api_key = os.getenv('GROQ_API_KEY')
            if not api_key:
                raise ValueError("GROQ_API_KEY no encontrada en variables de entorno")
                
            self.model = ChatGroq(
                groq_api_key=api_key,
                model_name=self.model_name,
                temperature=self.parameters.get('temperature', 0.7),
                max_tokens=self.parameters.get('max_tokens', 500)
            )
        return self.model
