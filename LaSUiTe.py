import time

def display_instant(text):
    print(text)

def display_slowly(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_message(message, prefix="[Coco] "):
    display_instant(prefix + message)

def cocobot():
    display_slowly("Salut ! C'est moi, cocobot 2.0... Juste arrête de me ping !")

def mylife():
    display_slowly("CEST MA VIE PRIVEE !!1!!!!!")

def babouchesmp():
    display_slowly("Ah donc toi aussi tu veux nous rejoindre ! C'est ici : babouchesmp.rf.gd/discord")

def ihategulli():
    display_slowly("Ah ok, on est ensemble... Bah tsé quoi, tiens la suite de l'épreuve est dans le dossier B situé dans le dossier A.")

def quoi():
    display_slowly("Feur")

def money():
    display_slowly("Virement de 10 783 DHS effectué vers MR. #!@_é")

def hack():
    display_slowly("HACK lancé...")
    time.sleep(2)
    display_slowly("Récupération des infos :")
    time.sleep(2)
    display_slowly("+-+-+-+-+-+-+-+-+-+-+-+-+")
    display_slowly("INFORMATIONS RECEIVED TO MR. #!@_é")

def console():
    display_slowly("Connecting to Console...")
    time.sleep(2)
    display_slowly("Hack de la console lancé...")
    time.sleep(2)
    display_slowly("+-+-+-+-+-+-+-+-+-+-+-+-+")
    display_slowly("INFORMATIONS RECEIVED TO MR. #!@_é")

def cat():
    display_slowly("Trop mimii !! ")
    display_slowly("[image de chat : https://us.123rf.com/450wm/nuevoimg/nuevoimg2307/nuevoimg230704423/208133186-mignon-petit-chaton-bengal-assis-sur-le-sol-et-regardant-la-cam%C3%A9ra.jpg]")

def help_cmd():
    display_instant("|| **Voici le Menu d'aide** ||")
    display_instant("cocobot")
    display_instant("money")
    display_instant("mylife")
    display_instant("hack")
    display_instant("babouchesmp")
    display_instant("console")
    display_instant("ihategulli")
    display_instant("cat")
    display_instant("quoi")

def main():
    startup_text = '''
 ______     ______     ______     ______     ______     ______     ______  
/\  ___\   /\  __ \   /\  ___\   /\  __ \   /\  == \   /\  __ \   /\__  _\ 
\ \ \____  \ \ \/\ \  \ \ \____  \ \ \/\ \  \ \  __<   \ \ \/\ \  \/_/\ \/ 
 \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
  \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/     \/_/ 
                                                                           
    '''
    display_slowly(startup_text, delay=0.01)

    while True:
        command = input(">")
        args = command.split()

        if not args:
            display_message("Veuillez entrer une commande.")
            continue

        if args[0] == 'cocobot':
            cocobot()
        elif args[0] == 'mylife':
            mylife()
        elif args[0] == 'babouchesmp':
            babouchesmp()
        elif args[0] == 'ihategulli':
            ihategulli()
        elif args[0] == 'quoi':
            quoi()
        elif args[0] == 'money':
            money()
        elif args[0] == 'hack':
            hack()
        elif args[0] == 'console':
            console()
        elif args[0] == 'cat':
            cat()
        elif args[0] == 'help':
            help_cmd()
        elif args[0] == 'exit':
            print("Goodbye!")
            break
        else:
            display_message("Cette commande n'existe pas !")

if __name__ == "__main__":
    main()
