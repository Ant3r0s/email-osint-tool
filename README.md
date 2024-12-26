# Email OSINT Tool

![Logo](https://via.placeholder.com/728x90.png?text=EvilMailOSINT)  
**😈 EvilMailOSINT 😈**

---

## 📜 Descripción
**Email OSINT Tool** es una herramienta creada en Python que permite analizar dominios de correos electrónicos y recopilar información OSINT (Open Source Intelligence) sobre ellos. Incluye funcionalidades como extracción de dominios, resolución de IP, consultas WHOIS, y verificación de certificados SSL, entre otras :)


---
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

## 🌐 Ejemplo de uso
Extraer dominio de un correo electrónico:

Introduce un correo como: example@domain.com.
El programa extraerá el dominio: domain.com.
Resolver dominio a IP:

Introduce el dominio: domain.com.
Obtendrás la IP asociada al dominio.
Realizar consulta WHOIS:

Introduce el dominio: domain.com.
El programa te mostrará la información WHOIS del dominio.
Verificar SSL:

Introduce el dominio: domain.com.
El programa te mostrará el estado del certificado SSL.
Comprobar registros MX:

Introduce el dominio: domain.com.
Obtendrás los registros MX de ese dominio.
Comprobar registros DNS (A):

Introduce el dominio: domain.com.
Obtendrás las direcciones IP asociadas a ese dominio.
Detectar servidor web:

Introduce el dominio: domain.com.
El programa detectará y mostrará el servidor web del dominio.
Comprobar antigüedad del dominio:

Introduce el dominio: domain.com.
El programa te mostrará la antigüedad del dominio en días.
Comprobar dominios similares:

Introduce el dominio: domain.com.
El programa te mostrará posibles dominios similares.
Verificar página de inicio de sesión:

Introduce el dominio: domain.com.
El programa verificará si existe una página de inicio de sesión en el dominio.
Comprobar política de privacidad:
Introduce el dominio: domain.com.
El programa verificará si existe una página de política de privacidad en el dominio.

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
