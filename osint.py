import os
import re
import requests
import socket
import dns.resolver
import whois
from datetime import datetime
from bs4 import BeautifulSoup

# Funciones de utilidad
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_logo():
    logo = r"""
    ███████╗███╗   ███╗ █████╗ ██╗     
    ██╔════╝████╗ ████║██╔══██╗██║     
    █████╗  ██╔████╔██║███████║██║     
    ██╔══╝  ██║╚██╔╝██║██╔══██║██║     
    ███████╗██║ ╚═╝ ██║██║  ██║███████╗
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝

    😈 EvilMailOSINT 😈
    """
    print(logo)

# Funciones de OSINT
def google_dorks():
    query = input("Introduce el término para generar un Google Dork: ")
    print(f"Ejemplo de Dork: site:{query} filetype:pdf")

def extract_links():
    url = input("Introduce la URL: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print("Enlaces encontrados:")
        for link in links:
            print(link)
    except Exception as e:
        print(f"Error extrayendo enlaces: {e}")

def metadata_analysis():
    print("Análisis de metadatos no implementado, pero puedes usar herramientas como ExifTool.")

def email_verification():
    email = input("Introduce el correo electrónico: ")
    if re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        domain = email.split('@')[-1]
        try:
            dns.resolver.resolve(domain, 'MX')
            print("Correo válido y dominio con servidores MX.")
        except:
            print("Dominio no tiene servidores MX válidos.")
    else:
        print("Correo no válido.")

def basic_crawling():
    print("Crawling básico con BeautifulSoup completado en extract_links().")

def ip_information():
    ip = input("Introduce la dirección IP: ")
    try:
        host = socket.gethostbyaddr(ip)
        print(f"Nombre de host asociado: {host[0]}")
    except socket.herror:
        print("No se encontró un nombre de host para esta IP.")

def subdomain_check():
    print("Para comprobar subdominios puedes usar sublist3r o Subfinder.")

def hash_lookup():
    print("Búsqueda de hashes con bases de datos como VirusTotal.")

def dns_history():
    print("Historial DNS puede ser consultado con herramientas como ViewDNS.")

def http_headers_analysis():
    url = input("Introduce la URL para analizar las cabeceras HTTP: ")
    try:
        response = requests.get(url)
        print(f"Cabeceras HTTP de {url}:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener cabeceras: {e}")

def data_leak_check():
    print("Puedes comprobar fugas de datos con servicios como HaveIBeenPwned.")

def social_media_scraping():
    print("Scraping de redes sociales en público puede realizarse con BeautifulSoup o Selenium.")

def ip_geolocation():
    ip = input("Introduce la IP para geolocalizar: ")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(f"Información geolocalizada de {ip}:")
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener geolocalización: {e}")

def cms_detection():
    url = input("Introduce la URL para detectar el CMS: ")
    try:
        response = requests.get(url)
        if 'wp-content' in response.text:
            print("El sitio parece estar usando WordPress.")
        elif 'Joomla' in response.text:
            print("El sitio parece estar usando Joomla.")
        else:
            print("No se detectó un CMS conocido.")
    except requests.exceptions.RequestException as e:
        print(f"Error al comprobar CMS: {e}")

# Funciones de Reconocimiento y Enumeración
def extract_domain(email):
    match = re.search(r'@([\w.-]+)', email)
    return match.group(1) if match else None

def check_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Unable to resolve domain"

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Error fetching WHOIS: {e}"

def check_ssl(domain):
    try:
        response = requests.get(f"https://{domain}", timeout=5)
        return "SSL Certificate Valid" if response else "SSL Check Failed"
    except Exception as e:
        return f"Error checking SSL: {e}"

def check_mx_records(domain):
    try:
        result = dns.resolver.resolve(domain, 'MX')
        mx_records = [str(record.exchange) for record in result]
        print(f"Registros MX para {domain}: {', '.join(mx_records)}")
    except Exception as e:
        print(f"Error al obtener registros MX para {domain}: {e}")

def check_dns_records(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        ip_addresses = [str(ip) for ip in result]
        print(f"Direcciones IP asociadas a {domain}: {', '.join(ip_addresses)}")
    except Exception as e:
        print(f"Error al obtener registros DNS para {domain}: {e}")

def check_web_server(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        server = response.headers.get('Server', 'Desconocido')
        print(f"Servidor web detectado para {domain}: {server}")
    except requests.exceptions.RequestException as e:
        print(f"Error al comprobar el servidor web para {domain}: {e}")

def domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = datetime.now() - creation_date
        print(f"La antigüedad del dominio {domain} es de {age.days} días.")
    except Exception as e:
        print(f"Error al obtener la antigüedad del dominio {domain}: {e}")

def check_similar_domains(domain):
    domain_parts = domain.split('.')
    for i in range(1, len(domain_parts)):
        similar_domain = '.'.join(domain_parts[i:])
        print(f"Posible dominio similar: {similar_domain}")

def check_login_page(domain):
    login_pages = ['/login', '/signin', '/user', '/account']
    for page in login_pages:
        try:
            response = requests.get(f"http://{domain}{page}", timeout=5)
            if response.status_code == 200:
                print(f"Página de inicio de sesión encontrada en: {domain}{page}")
        except requests.exceptions.RequestException as e:
            print(f"No se pudo acceder a {domain}{page}: {e}")

def check_privacy_policy(domain):
    privacy_pages = ['/privacy-policy', '/privacy', '/terms', '/legal']
    for page in privacy_pages:
        try:
            response = requests.get(f"http://{domain}{page}", timeout=5)
            if response.status_code == 200:
                print(f"Política de privacidad encontrada en: {domain}{page}")
        except requests.exceptions.RequestException as e:
            print(f"No se pudo acceder a {domain}{page}: {e}")

# Menús principales
def osint_menu():
    while True:
        clear_console()
        print_ascii_logo()
        print("1. Búsquedas en Google con Dorks")
        print("2. Extracción de enlaces de una URL")
        print("3. Análisis de metadatos")
        print("4. Verificación de correos electrónicos")
        print("5. Crawling básico")
        print("6. Información de IPs")
        print("7. Comprobación de subdominios")
        print("8. Hash Lookup")
        print("9. Historial de DNS")
        print("10. Análisis de cabeceras HTTP")
        print("11. Comprobación de fugas de datos")
        print("12. Scraping de redes sociales (público)")
        print("13. Geolocalización de IPs")
        print("14. Detección de CMS")
        print("15. Volver al menú principal")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            google_dorks()
        elif choice == '2':
            extract_links()
        elif choice == '3':
            metadata_analysis()
        elif choice == '4':
            email_verification()
        elif choice == '5':
            basic_crawling()
        elif choice == '6':
            ip_information()
        elif choice == '7':
            subdomain_check()
        elif choice == '8':
            hash_lookup()
        elif choice == '9':
            dns_history()
        elif choice == '10':
            http_headers_analysis()
        elif choice == '11':
            data_leak_check()
        elif choice == '12':
            social_media_scraping()
        elif choice == '13':
            ip_geolocation()
        elif choice == '14':
            cms_detection()
        elif choice == '15':
            break
        else:
            print("Opción no válida, inténtalo de nuevo.")

        input("\nPresiona Enter para continuar...")

def reconocimiento_menu():
    while True:
        clear_console()
        print_ascii_logo()
        print("1. Extraer dominio de un correo electrónico")
        print("2. Resolver dominio a IP")
        print("3. Realizar consulta WHOIS")
        print("4. Verificar SSL del dominio")
        print("5. Comprobar registros MX del dominio")
        print("6. Comprobar registros DNS (A) del dominio")
        print("7. Detectar servidor web del dominio")
        print("8. Comprobar antigüedad del dominio")
        print("9. Comprobar dominios similares")
        print("10. Verificar página de inicio de sesión")
        print("11. Comprobar política de privacidad del dominio")
        print("12. Volver al menú principal")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            email = input("Introduce el correo electrónico: ")
            domain = extract_domain(email)
            print(f"Dominio: {domain if domain else 'Correo no válido'}")
        elif choice == '2':
            domain = input("Introduce el dominio: ")
            ip = check_ip(domain)
            print(f"IP: {ip}")
        elif choice == '3':
            domain = input("Introduce el dominio: ")
            whois_data = whois_lookup(domain)
            print(f"WHOIS Data:\n{whois_data}")
        elif choice == '4':
            domain = input("Introduce el dominio: ")
            ssl_status = check_ssl(domain)
            print(f"SSL Status: {ssl_status}")
        elif choice == '5':
            domain = input("Introduce el dominio: ")
            check_mx_records(domain)
        elif choice == '6':
            domain = input("Introduce el dominio: ")
            check_dns_records(domain)
        elif choice == '7':
            domain = input("Introduce el dominio: ")
            check_web_server(domain)
        elif choice == '8':
            domain = input("Introduce el dominio: ")
            domain_age(domain)
        elif choice == '9':
            domain = input("Introduce el dominio: ")
            check_similar_domains(domain)
        elif choice == '10':
            domain = input("Introduce el dominio: ")
            check_login_page(domain)
        elif choice == '11':
            domain = input("Introduce el dominio: ")
            check_privacy_policy(domain)
        elif choice == '12':
            break
        else:
            print("Opción no válida, inténtalo de nuevo.")

        input("\nPresiona Enter para continuar...")

# Menú principal
def main_menu():
    while True:
        clear_console()
        print_ascii_logo()
        print("1. OSINT (Open Source Intelligence)")
        print("2. Reconocimiento y Enumeración")
        print("3. Salir")

        choice = input("\nSelecciona una opción: ")

        if choice == '1':
            osint_menu()
        elif choice == '2':
            reconocimiento_menu()
        elif choice == '3':
            print("Saliendo... ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, inténtalo de nuevo.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main_menu()

