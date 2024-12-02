from typing import Optional, Dict, Any
from transformers import AutoModelForMaskedLM, AutoTokenizer, Pipeline, FillMaskPipeline
import torch
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class SpanishModelLoader:
    def __init__(
            self,
            model_name:str = "PlanTL-GOB-ES/roberta-large-bne",
            device: str = "cuda" if torch.cuda.is_available() else "cpu",
            **kwargs: Any
    ):
        self.model_name = model_name
        self.device = device
        self.model_kwargs = kwargs
        self.model = None
        self.tokenizer = None
        self.pipeline = None
    
    def load_model(self):
        # load RoBerta model and tokenizer
        print(f"Loading model {self.model_name} in {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            trust_remote_code=True
        )

        self.model = AutoModelForMaskedLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map=self.device,
            **self.model_kwargs
        )
    
    def create_embeddings(
            self,
            encode_kwargs: Optional[Dict[str, Any]] = None
    ) -> HuggingFaceEmbeddings:
        # Create a model compatible with LangChain
        embeddings = HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={"device": self.device},
            encode_kwargs=encode_kwargs
        )

        return embeddings
    
    def get_masked_pipeline(self) -> FillMaskPipeline:
        # Create a pipeline for masked language modeling
        if self.model is None or self.tokenizer is None:
            self.load_model()

        pipeline = FillMaskPipeline(
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if self.device == "cuda" else -1
        )

        return pipeline

    def get_embeddings_for_text(self, text: str) -> torch.Tensor:
        # Get embeddings for a specific text
        if self.model is None or self.tokenizer is None:
            self.load_model()
        
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            # Using the cls token as the text embedding 
            embeddings = outputs.last_hidden_state[:, 0, :]
        
        return embeddings
    
    def get_tokenizer(self):
        # Return the tokenizer
        if self.tokenizer is None:
            self.load_model()
        return self.tokenizer
    
    def get_model(self):
        # Return the model
        if self.model is None:
            self.load_model()
        return self.model
    
    def get_pipeline(self):
        # Return the pipeline
        if self.pipeline is None:
            self.pipeline = self.get_masked_pipeline()
        return self.pipeline
