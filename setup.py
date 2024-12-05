from setuptools import setup, find_packages

setup(
    name="llm_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.200",
        "pydantic>=2.0.0",
        "streamlit>=1.24.0",
        "pyyaml>=6.0",
        "python-dotenv>=0.19.0",
        "langchain-groq>=0.0.1"
    ]
)
