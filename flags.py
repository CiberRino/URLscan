import requests

def certificate(url):
    try:
        response = requests.get(url)
    except requests.exceptions.SSLError as s:
        print(F"bad ssl: {s}")
    except requests.exceptions.ConnectionError as c:
        print(f"connection error: {c}")

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
    



