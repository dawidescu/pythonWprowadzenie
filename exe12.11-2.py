"""
Ćwiczenie 2. Zmień swój program używający gniazda tak, by zliczał liczbę otrzymanych znaków
i przestawał wyświetlać jakikolwiek tekst po wyświetleniu 3000 znaków. Program powinien pobrać
cały dokument, zliczyć całkowitą liczbę znaków oraz na końcu ją wyświetlić. Przetestuj działanie na
http://data.pr4e.org/romeo-full.txt.
"""

import re
import socket
import urllib.request
from urllib.parse import urlparse
import ssl

def get_url():
    while True:
        try:
            user_url = input("Podaj poprawny URL strony z której chcesz pobrać plik: ")
            parsed_url = urlparse(user_url)
            if parsed_url.scheme and parsed_url.netloc:
                return user_url
            else:
                print("Nieprawidłowy adres URL. Spróbuj ponownie.")
        except ValueError:
            print("Nieprawidłowy adres URL. Spróbuj ponownie.")

def main():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    user_url = get_url()

    try:
        html = urllib.request.urlopen(user_url, context=ctx).read()
        links = re.findall(b'href="http[s]?://.*?"', html)
        for link in links:
            print(link.decode())
    except urllib.error.URLError as e:
        print(f"Wystąpił błąd: {e.reason}")

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))

    cmd = f'GET {user_url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1 or len(data.decode()) >= 3000:
            break
        print(data.decode(), end='')

    mysock.close()

if __name__ == "__main__":
    main()


   # http://data.pr4e.org/romeo.txt