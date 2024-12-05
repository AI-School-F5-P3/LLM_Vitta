from llm_project.src.models.model_loader import RobertaGenerativeLLM


def test_roberta_generative():
    # Inicializar el LLM
    llm = RobertaGenerativeLLM()

    # Probar diferentes prompts
    prompts = [
        "En un día soleado,",
        "La historia de España",
        "Las principales características de"
    ]

    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        response = llm(prompt)
        print(f"Respuesta: {response}")


if __name__ == "__main__":
    test_roberta_generative()
