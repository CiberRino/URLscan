import ssl
import socket
import requests

def certificate(do):
    try:
        hostname = do
        port = 443

        context = ssl.create_default_context()

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                pass
    except ssl.SSLCertVerificationError as s:
       print(s)   

def HTLM(url,score):
    try:
        response = requests.get(url)

        if response.history:
            score += 5
            print("[!] there was a redirection")
            for redirect in response.history:
                print(redirect.status_code, redirect.url)

            print("End:", response.status_code, response.url)
        else:
                print(response.status_code)
                print(response.text)
    except requests.exceptions.RequestException as s:
        print(f"error: {s}")