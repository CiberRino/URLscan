def score(signs,score):

    if score <= 15:
        print(f"[*] possible low risk {signs} possible signs of phising. Total score {score}")
    elif score <= 25:
        print(f"[:] possible mid risk {signs} possible signs of phising. Total score {score}")
    elif score <= 45:
        print(f"[!] possible hight risk {signs} possible signs of phising. Total score {score}")
    