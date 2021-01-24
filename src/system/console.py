from termcolor import colored

def show_in_console(mesaj, durum):
    if durum == 1:
        uyari= colored(mesaj, "green")
    elif durum == 2:
        uyari=  colored(mesaj, "red")
    elif durum == 3:
        uyari=  colored(mesaj, "blue")
    print(uyari)