import random

def creazionePassword(lunghezza):
    password=""

    for x in range(lunghezza):
        password=password+caratteri_possibili[random.randint(0,len(caratteri_possibili)-1)]

    return password

def lunghezza():
    lunghezza=int(input("Lunghezza Password: "))

    while lunghezza==0:
        lunghezza=int(input("La lunghezza della password non può essere 0 - Riprova: "))

    return lunghezza

def caratteri_possibili():
    minuscoli=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    maiuscoli=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeri=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    speciali=['.', ':', ',', ';', '-', '_', '!', '?']
    tutti_caratteri=[minuscoli, maiuscoli, numeri, speciali]
    caratteri_possibili=[]
    caratteri=["caratteri minuscoli", "caratteri maiuscoli", "numeri", "caratteri speciali"]

    for tipo in caratteri:
        x=input("Vuoi i "+tipo+" nella password? [y] ")

        if x=="y" or x=="Y":
            x=0 if tipo=="caratteri minuscoli" else (1 if tipo=="caratteri maiuscoli" else (2 if tipo=="numeri" else 3))
            caratteri_possibili.extend(tutti_caratteri[x])

    return caratteri_possibili

lunghezza=lunghezza()
print("")
caratteri_possibili=caratteri_possibili()
print("")
print("Password Random:",creazionePassword(lunghezza))
