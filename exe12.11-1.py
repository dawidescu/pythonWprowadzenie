"""
Ćwiczenie 1. Zmień program używający gniazda socket1.py tak, aby poprosić użytkownika o podanie
adresu URL i by mógł on przeczytać dowolną stronę internetową. Możesz użyć split('/'), aby rozbić
URL na części składowe, dzięki czemu łatwo wyodrębnisz nazwę hosta dla metody connect(). Dodaj
sprawdzanie błędów przy użyciu try i except, aby poradzić sobie z przypadkiem, w którym użytkownik
wprowadzi nieprawidłowo sformatowany lub nieistniejący adres URL. Przetestuj działanie na http:
//data.pr4e.org/romeo.txt.
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
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()

if __name__ == "__main__":
    main()




# Z Użyciem metody split()
"""
def parse_url(user_url):
    # Sprawdź, czy adres URL zaczyna się od 'http://' lub 'https://'
    if user_url.startswith('http://') or user_url.startswith('https://'):
        # Usuń protokół z adresu URL
        url_without_protocol = user_url.split('://', 1)[1]
    else:
        url_without_protocol = user_url

    # Podziel adres URL na części
    parts = url_without_protocol.split('/', 1)
    if len(parts) == 2:
        netloc, path = parts
    else:
        netloc = parts[0]
        path = ''

    return netloc, path

def main():
    user_url = input("Podaj poprawny URL strony z której chcesz pobrać plik: ")
    netloc, path = parse_url(user_url)

    # Reszta Twojego kodu (pobieranie zawartości strony, połączenie z serwerem, itp.)

if __name__ == "__main__":
    main()
"""

"""import re
import socket
import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

users_url = input("Podaj poprawny URL strony z której chcesz pobrać plik: ")
html = urllib.request.urlopen(users_url, context=ctx).read()
links = re.findall(b'href="http[s]?://.*?"', html)
for link in links:
    print(link.decode())


mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()"""