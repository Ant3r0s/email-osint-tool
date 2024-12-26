import os
import re
import requests
import socket
from bs4 import BeautifulSoup
import whois

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
    url = f"https://www.whois.com/whois/{domain}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()[:500]  # Return first 500 chars for preview
    except Exception as e:
        return f"Error fetching WHOIS: {e}"

def check_ssl(domain):
    try:
        response = requests.get(f"https://{domain}", timeout=5)
        return "SSL Certificate Valid" if response else "SSL Check Failed"
    except Exception as e:
        return f"Error checking SSL: {e}"

def consulta_whois(dominio):
    try:
        datos = whois.whois(dominio)
        print(f"\nInformación WHOIS para {dominio}:\n")
        print(datos)
    except Exception as e:
        print(f"Error al obtener información WHOIS para {dominio}: {e}")

def comprobar_brechas(dominio):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{dominio}"
        headers = {"hibp-api-key": "<tu_api_key_aqui>", "User-Agent": "email-osint-tool"}
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            brechas = respuesta.json()
            print(f"\nEl dominio {dominio} ha sido comprometido en las siguientes brechas:")
            for brecha in brechas:
                print(f"- {brecha['Name']}: {brecha['Description']}")
        elif respuesta.status_code == 404:
            print(f"\nNo se han encontrado brechas conocidas para el dominio {dominio}.")
        else:
            print(f"\nError al consultar brechas: {respuesta.status_code}")
    except Exception as e:
        print(f"Error al comprobar brechas para {dominio}: {e}")

def osint_menu():
    while True:
        clear_console()
        print_ascii_logo()
        print("""
1. Extraer dominio de un correo electrónico
   Ejemplo: 'example@domain.com' → Dominio: domain.com

2. Resolver dominio a IP
   Ejemplo: 'domain.com' → IP: 93.184.216.34

3. Realizar consulta WHOIS
   Ejemplo: 'domain.com' → WHOIS Data: [Información detallada del dominio]

4. Verificar SSL del dominio
   Ejemplo: 'domain.com' → SSL Certificate Valid

5. Comprobar si el dominio ha sido vulnerado
   Ejemplo: 'domain.com' → El dominio ha sido comprometido en las siguientes brechas: [Brechas encontradas]

6. Salir
""")
        try:
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 1:
                email = input("Introduce un correo electrónico: ").strip()
                domain = extract_domain(email)
                print(f"Dominio: {domain if domain else 'Correo no válido'}")
            elif opcion == 2:
                domain = input("Introduce el dominio: ").strip()
                ip = check_ip(domain)
                print(f"IP: {ip}")
            elif opcion == 3:
                domain = input("Introduce el dominio: ").strip()
                whois_data = whois_lookup(domain)
                print(f"WHOIS Data (Preview):\n{whois_data}")
            elif opcion == 4:
                domain = input("Introduce el dominio: ").strip()
                ssl_status = check_ssl(domain)
                print(f"SSL Status: {ssl_status}")
            elif opcion == 5:
                domain = input("Introduce un correo electrónico o dominio para comprobar: ").strip()
                comprobar_brechas(domain)
            elif opcion == 6:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
        except KeyboardInterrupt:
            print("\nSaliendo del programa. ¡Hasta la próxima!")
            break

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    osint_menu()

