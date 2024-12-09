from langchain.llms.base import LLM
from typing import Any, List, Optional, Dict
from pydantic import PrivateAttr
from .model_loader import GroqLoader
from langchain_core.messages import HumanMessage
from pathlib import Path


class GroqChat(LLM):
    config_path: str = "configs/model_config.yaml"
    model_loader: GroqLoader = None

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        config_path = (
            str(self.config_path) if isinstance(self.config_path, (str, Path)) else "configs/model_config.yaml"
        )
        self.model_loader = GroqLoader(config_path)

    @property
    def _llm_type(self) -> str:
        return "groq_chat"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> str:
        try:
            model = self.model_loader.get_model()
            messages = [HumanMessage(content=prompt)]
            response = model.invoke(messages)
            return response.content.strip()
        except Exception as e:
            print(f"Error en la generación: {str(e)}")
            return "Lo siento, hubo un error al generar la respuesta."

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            "model_name": self.model_loader.model_name,
            **self.model_loader.parameters
        }