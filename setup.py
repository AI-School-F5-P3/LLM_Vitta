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
    ],
    author="Vittoria De Novellis",
    author_email="vittoriadenovellis@gmail.com",
    description="Generador de contenido multiplataforma usando LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dolcevitta/llm_vitta",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
