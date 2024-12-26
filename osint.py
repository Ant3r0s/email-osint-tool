import os
import re
import requests
import socket
import dns.resolver
import whois
from datetime import datetime
from bs4 import BeautifulSoup

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

def osint_menu():
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
        print("12. Salir")

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
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, inténtalo de nuevo.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    osint_menu()
