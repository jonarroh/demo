# 📜 Documento de Diseño

---

## 🎯 Objetivos
- **Crear un Notebook de Jupyter** para la prueba de concepto.
- **Instalar Ollama** (phi3) de momento.
- **Configurar un entorno virtual** e instalar las librerías necesarias: `langchain`, `selenium`, `bs4` y `lxml`.
- **Desarrollar un agente** que, basado en un prompt, extraiga un JSON con la URL de la página y el código de rastreo del paquete.
- **Utilizar Selenium** para navegar a la URL extraída.
- **Raspar la página web** usando Selenium y `bs4`, parsear el HTML y filtrar los atributos no deseados usando una lista de elementos bloqueados.
- **Identificar el XPath** del input de búsqueda y el botón de envío usando una plantilla de Langchain.
- **Generar un informe** con la información del paquete extraído en formatos como CSV y PDF.

---

## 📝 Lista de Tareas

1. **Crear un Notebook de Jupyter para la Prueba de Concepto**
   - 📂 Organizar el notebook para una documentación clara y paso a paso.
   - 🖋️ Incluir celdas de markdown para explicaciones y celdas de código para la implementación.
   - 🧪 Asegurar la reproducibilidad de los resultados.

2. **Instalar Ollama (phi3)**
   - 🔧 Usar el gestor de paquetes adecuado para la instalación.
   - 📥 Verificar la instalación ejecutando una prueba simple.

3. **Configurar el Entorno Virtual e Instalar Librerías**
   - 🐍 Crear un entorno virtual: `python -m venv env`.
   - 📦 Instalar las librerías necesarias: `pip install langchain selenium bs4 lxml`.
   - 🔍 Asegurar que todas las librerías estén correctamente instaladas.

4. **Desarrollar un Agente para la Extracción de JSON**
   - ✍️ Escribir código para generar un JSON con la URL y el código de rastreo.
   - 📊 Asegurar que el formato JSON sea correcto e incluya toda la información necesaria.

5. **Utilizar Selenium para la Navegación Web**
   - 🌐 Pasar la URL extraída a Selenium.
   - 🧭 Escribir scripts para que Selenium navegue por la página web.

6. **Raspar la Página Web y Parsear el HTML**
   - 🕷️ Usar `bs4` para raspar el contenido HTML de la página web.
   - 🚫 Filtrar los atributos HTML no deseados basado en una lista de elementos bloqueados.
   - 🗃️ Asegurar que los datos restantes sean limpios y utilizables.

7. **Identificar el XPath usando una Plantilla de Langchain**
   - 🧩 Desarrollar una plantilla de Langchain para localizar el input de búsqueda y el botón de envío.
   - 🔍 Verificar la corrección de las expresiones XPath.

8. **Generar Informe con la Información Extraída**
   - 🗂️ Extraer la información del paquete y formatearla.
   - 📈 Generar un informe en formatos CSV y PDF.
   - 📤 Asegurar que el informe sea preciso e incluya todos los datos necesarios.

---

## 🛠️ Herramientas y Tecnologías
- **Jupyter Notebook**: Para la documentación y prueba de concepto.
- **Ollama (phi3)**: Como el modelo de lenguaje principal.
- **Entorno Virtual**: Para gestionar dependencias y asegurar una configuración limpia.
- **Librerías de Python**: `langchain`, `selenium`, `bs4`, `lxml` para diversas funcionalidades.
- **Selenium**: Para la automatización y navegación web.
- **BeautifulSoup (`bs4`)**: Para el análisis y extracción de datos HTML.
- **Langchain**: Para la identificación de XPath basada en plantillas.
- **Librerías de CSV/PDF**: Para la generación de informes.

---

## 📅 Cronograma

- **Día 1-2**: Configurar el entorno e instalar dependencias.
- **Día 3-4**: Crear el Notebook de Jupyter y desarrollar el agente para la extracción de JSON.
- **Día 5-6**: Implementar la navegación de Selenium y el raspado de HTML.
- **Día 7-8**: Desarrollar la plantilla de Langchain e identificar XPath.
- **Día 9-10**: Extraer información y generar informes.
- **Día 11**: Pruebas y depuración.
- **Día 12**: Revisión final y documentación.

---

## 📊 Visualización

- **Diagrama de Flujo**: Representación visual del flujo de trabajo desde el prompt hasta la generación del informe.
- **Fragmentos de Código**: Fragmentos de código clave resaltados para mayor claridad.
- **Ejemplos de Salida**: JSON de muestra, HTML raspado y los informes generados para referencia.

---

## 🌟 Resumen
Este proyecto tiene como objetivo crear un sistema automatizado que navegue a una página web, extraiga información de rastreo de paquetes y genere un informe completo. Utilizando una combinación de librerías y herramientas de Python, este sistema asegurará la extracción y presentación precisa de datos.
