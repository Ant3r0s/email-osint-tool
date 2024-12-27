# Email OSINT Tool

![Logo](https://via.placeholder.com/728x90.png?text=EvilMailOSINT)  
**😈 EvilMailOSINT 😈**

---

## 📜 Descripción
**Email OSINT Tool** es una herramienta creada en Python que permite analizar dominios de correos electrónicos y recopilar información OSINT (Open Source Intelligence) sobre ellos. Incluye funcionalidades como extracción de dominios, resolución de IP, consultas WHOIS, y verificación de certificados SSL, entre otras :)


---
### Más Funcionalidades:
- **Google Dorks:** Añadido ejemplo simple de uso con un término de búsqueda.
- **Extracción de enlaces:** Implementación para extraer enlaces de una página web usando BeautifulSoup.
- **Verificación de correos electrónicos:** Validación del formato del correo y comprobación de registros MX en el dominio.
- **Crawling básico:** Redirige a la función de extracción de enlaces de una URL.
- **Análisis de cabeceras HTTP:** Añadido análisis de cabeceras HTTP con requests.
- **Geolocalización de IPs:** Implementada la función usando la API de ipinfo.io.
- **Detección de CMS:** Añadida detección básica para WordPress y Joomla en URLs.
- **Historial de DNS y fugas de datos:** Comentarios indicativos del uso de herramientas externas (ViewDNS, HaveIBeenPwned).
  
- **Funciones de Reconocimiento y Enumeración:**
    - Extracción de dominio de un correo electrónico.
    - Resolución de dominio a IP usando socket.gethostbyname.
    - Consulta WHOIS con la librería whois.
    - Comprobación de SSL a través de una solicitud HTTP.
    - Detección de servidor web mediante las cabeceras HTTP.
    - Comprobación de antigüedad del dominio con datos WHOIS.
    - Búsqueda de dominios similares basados en las partes del dominio principal.
  
### Interfaz de Usuario:

- **Menú principal: Creación de un menú principal para navegar entre las opciones de OSINT y Reconocimiento/Enumeración.
- **Menús secundarios: Añadidos menús interactivos con opciones para cada categoría, pidiendo la entrada del usuario y ejecutando las funciones correspondientes.
  
### Nuevas Funcionalidades:
- **Comprobar registros MX**: Verifica los registros de intercambio de correo de un dominio.
- **Comprobar registros DNS (A)**: Muestra las direcciones IP asociadas a un dominio.
- **Detectar servidor web**: Detecta qué servidor web está ejecutando un dominio.
- **Comprobar antigüedad del dominio**: Calcula la antigüedad del dominio.
- **Comprobar dominios similares**: Muestra dominios que podrían ser similares al introducido.
- **Verificar página de inicio de sesión**: Verifica si el dominio tiene una página de inicio de sesión.
- **Comprobar política de privacidad**: Verifica la existencia de una página de política de privacidad.

## ⚙️ Características

- Extrae el dominio de correos electrónicos.
- Resuelve dominios a direcciones IP.
- Realiza consultas WHOIS sobre dominios.
- Verifica certificados SSL para dominios HTTPS.
- Comprobar registros MX de un dominio.
- Comprobar registros DNS (A) de un dominio.
- Detecta el servidor web de un dominio.
- Calcula la antigüedad del dominio.
- Comprobar la existencia de dominios similares.
- Verifica si el dominio tiene una página de inicio de sesión.
- Comprobar si el dominio tiene política de privacidad.

## 🚀 Instalación y uso

### 1. Clona el repositorio:
```bash
git clone https://github.com/Ant3r0s/email-osint-tool.git
```

### 2. Entra en el directorio del proyecto:
```bash
cd email-osint-tool
```

### 3. Instala las dependencias necesarias:
Asegúrate de tener Python 3.x instalado. Luego, ejecuta:
```bash
pip install -r requirements.txt
```

### 4. Ejecuta la herramienta:
```bash
python osint.py
```

---

## 🛠️ Requisitos
- Python 3.7 o superior.
- Librerías requeridas: `requests`, `BeautifulSoup4`.

Para instalarlas:
```bash
pip install requests beautifulsoup4 whois dnspython
```

---

Cada opción está diseñada para ser intuitiva y rápida. 💡

---

## 🖤 Contribuciones
¡Se aceptan pull requests y sugerencias! Crea un issue si encuentras algún bug o tienes alguna idea nueva.

---

## 📝 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## ✉️ Contacto
Creador: David Simarro Benavides  
GitHub: [Ant3r0s](https://github.com/Ant3r0s)
