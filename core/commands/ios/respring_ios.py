#!/usr/bin/env python3

import core.helper as h
import time

class command:
	def __init__(self):
		self.name = "respring"
		self.description = "Restart SpringBoard."

	def run(self,session,cmd_data):
		h.info_general("Restarting SpringBoard...")
		time.sleep(1)
		session.send_command({"cmd":"killall","args":"SpringBoard"})
