"""
load all settings to runtime variable, and save it later
"""
import dpath
import os


class settings:
	def __init__(self):
		self.__settings = {}
		self.__is_saved = True

	def load_all_settings(self):
		pass

	def read_field(self, key: str):
		pass

	def write_field(self, key: str, value: str | int | float | bool):
		pass
