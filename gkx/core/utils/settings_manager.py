"""
load all settings to runtime variable, and save it later
"""
import dpath.util as dutil
import os
import toml


__all__ = ["config", "settings"]


class settings:
	default = """
wallpaper = "~/Pictures/Wallpapers"
timeout = 10
search_history = []
src_url = "https://www.pling.com"
	"""

	@staticmethod
	def _load(df=False):
		path = os.path.expanduser(config.pull("settings/path"))
		if os.path.exists(path) and not df:
			sett = open(path, "r").read()
		else:
			if not df:
				print("settings file not exist! loading defaults instead.")

			sett = settings.default

			with open(path, "w") as file:
				file.write(sett)

		return toml.loads(sett)

	@staticmethod
	def read(key: str):
		value = config.pull(key, obj=settings._load())
		value = value or config.pull(key, obj=settings._load(True))
		return value

	@staticmethod
	def write(key: str, value):
		sett = settings._load()
		sett.update({key: value})
		path = os.path.expanduser(config.pull("settings/path"))

		with open(path, "w") as file:
			file.write(toml.dumps(sett))


class config:
	_config = {
		"categories": {
			"GTK3/4 Themes": "~/.themes",
			"Plank Themes": "~/.local/share/plank/themes",
			"Icon Themes": "~/.icons",
			"Cursor Themes": "~/.icons",
			"GNOME Shell Themes": "~/.themes",
			"Cinnamon Themes": "~/.themes",
			"XFCE/XFWM4 Themes": "~/.themes",
			"KDE Plasma Themes": "~/.local/share/plasma/desktoptheme",
			"LXQt Themes": "~/.local/share/lxqt/themes",
			"Wallpapers": "settings.wallpapers"
		},
		"settings": {
			"path": "~/.gkx-config"
		},
		"table": {
			"cats": [
				"title", "category", "publisher", "id", 
				"score", "time", "datetime", "preview", "dist"
			]
		},
		"html": {
			"pages": {
				"name": "ul",
				"class_": "pagination"
			},
			"pub": {
				"name": "a",
				"class_": "tooltipuser"
			},
			"time": {
				"name": "div",
				"class_": "collected"
			},
			"score": {
				"name": "div",
				"class_": "kkSWyw"
			},
			"cat": {
				"name": "div",
				"class_": "title"
			},
			"cat_sub": {
				"name": "b"
			},
			"preview": {
				"name": "img",
				"class_": "explore-product-image"
			},
			"item": {
				"name": "div",
				"class_": "explore-product"
			},
			"title": {
				"name": "h3"
			},
			"id": {
				"name": "a"
			}
		},
		"export": {
			"formats": {
				"csv": "to_csv"
			}
		}
	}

	@staticmethod
	def pull(path, sep="/", obj=None, df=""):
		return dutil.get(obj or config._config, path, separator=sep, default=df)
