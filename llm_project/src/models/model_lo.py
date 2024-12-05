from langchain.llms.base import LLM
from typing import Any, List, Optional, Dict
from pydantic import Field, PrivateAttr
from .model_loader import GroqLoader
from langchain_core.messages import HumanMessage


class GroqChat(LLM):
    config_path: str = Field(default="llm_project/configs/model_config.yaml")
    _model_loader: GroqLoader = PrivateAttr()

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self._model_loader = GroqLoader(self.config_path)

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
            model = self._model_loader.get_model()
            messages = [HumanMessage(content=prompt)]
            response = model.invoke(messages)
            return response.content.strip()
        except Exception as e:
            print(f"Error en la generación: {str(e)}")
            return "Lo siento, hubo un error al generar la respuesta."

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            "model_name": self._model_loader.model_name,
            **self._model_loader.parameters
        }