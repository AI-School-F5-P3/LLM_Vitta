# GenievAI 🧞‍♂️
![GenievAI Logo](llm_project/img/Genievai.1.png)

## Acceso Rápido
Puedes utilizar GenievAI directamente en la web:
🌐 [Demo en Render](https://llm-vitta.onrender.com)

## Descripción
¡Bienvenido a GenievAI! 🧞‍♂️ Tu aliado en la creación de contenido innovador y cautivador. Impulsado por inteligencia artificial de vanguardia, GenievAI transforma tus ideas en contenido dinámico y adaptado para cualquier plataforma. Ya sea que necesites un artículo de blog inspirador, un tweet ingenioso, o una publicación visualmente impactante para Instagram, GenievAI está aquí para hacer realidad tus visiones creativas. Con nuestro modelo Mixtral 8x7B, experimenta la magia de la generación de contenido sin esfuerzo y lleva tu presencia digital al siguiente nivel.

## Características
- Generación de contenido para diferentes plataformas:
    - Blog
    - Twitter
    - Instagram
    - LinkedIn
    - SEO
    - Infantil
- Modelo Mixtral 8x7B de alto rendimiento
- Fácil instalación y configuración

## Instalación

### Clonar el Repositorio
```bash
git clone https://github.com/Dolcevitta95/LLM_Vitta
cd LLM_Vitta
```

### Configuración del Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Instalación de Dependencias
```bash
pip install -e .
pip install -r requirements.txt
```

### Configuración de Variables de Entorno
Crea un archivo `.env` en el directorio raíz y añade tu clave de API de Groq:
```
GROQ_API_KEY=tu_token_api_aqui
```
Pasos para obtener el token:
1. Ir a https://groq.com/
2. Crear una cuenta
3. Ir a https://api.groq.com/docs/
4. Crear un token
5. Copiar el token
6. Pegar el token en el archivo .env

## Configuración del Modelo

Modelo utilizado: Mixtral 8x7B
Parámetros:
- **Modelo**: mixtral-8x7b-32768
- **Temperatura**: 0.7
- **Top P**: 0.9
- **Máximo de Tokens**: 2000
- **Presencia Penalty**: 0.6
- **Frecuencia Penalty**: 0.6

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o realiza un pull request en el repositorio de GitHub.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

## Contacto
- LinkedIn: [Vittoria De Novellis](https://www.linkedin.com/in/vittoria-de-novellis-390aa9158/)

---

*Generado con ❤️ por GenievAI*
![Despedida Gatito](https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif)
