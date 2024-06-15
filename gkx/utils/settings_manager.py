"""
load all settings to runtime variable, and save it later
"""
import dpath.util as dutil
import json


__all__ = ["config", "settings"]


class settings:
	def __init__(self):
		self.__settings = {}
		self.__is_saved = True

		self.load_all_settings()

	def load_all_settings(self):
		pass

	def read_field(self, key: str):
		pass

	def write_field(self, key: str, value: str | int | float | bool):
		pass


class config:
	@staticmethod
	def load_config():
		return json.loads(open("gkx/resources/config/store.json").read())
	
	@staticmethod
	def pull(path, sep="/"):
		return dutil.get(config.load_config(), path, separator=sep)
