# managing http requests
import requests
import urllib.parse as parse_url

# html analysing
from bs4 import BeautifulSoup
import re
import pandas as pd
from . import xget
from ..utils import get_time, format_tag_text, config, settings
from ..utils import ResultsManager, FileObject
from fuzzywuzzy import fuzz

class Scrapper:
	def __init__(self):
		self.src_url = settings.read("src_url")
		self.__pages_num = -1
		self.__query = ""

	def url_query(self, q, p=None):
		url = f"{self.src_url}/find?"  # use settings
		queries = {"search": str(q)[:15]}

		if str(p).isdigit():
			queries.update({"page": str(p)})

		url = url + parse_url.urlencode(queries)

		return url

	def get_pages_number(self, page):
		bs4 = BeautifulSoup(page, features="lxml")
		pages = bs4.find_all(**config.pull("html/pages"))[0].find_all_next("li")

		pages_num = []

		for page in pages:
			index = re.findall(r"\s*(\d+)\s*", page.text)
			if len(index) == 1:
				pages_num.append(index[0])

		return int(pages_num[-1])

	def get_pages_content(self, url: str, obj=False):
		proxies = config.pull("proxies") or {}
		tm = int(settings.read("timeout"))
		response = requests.get(url, proxies=proxies, timeout=tm)

		return response if obj else response.content

	def search(self, query: str):
		"""
		the reason why surfing to page 99999,
		is to get all the pages available,
		probably less than that number (hope so)
		"""

		url = self.url_query(str(query), p=99999)
		content = self.get_pages_content(url)
		self.__pages_num = self.get_pages_number(content)
		self.__query = query

		return self.scrap_page(1)

	@staticmethod
	def get_cat_path(cat, threshold=60):
		if not cat:
			return False
		
		cat = str(cat).lower()
		cats = config.pull("categories")

		for category in cats:
			similarity = fuzz.ratio(cat.lower(), category.lower())

			if similarity >= threshold:
				return cats[category]
			
		return False

	def scrap_page(self, page: int):
		if page > self.__pages_num or self.__pages_num <= 0:
			return
		
		if not self.__query:
			return
		
		cols = config.pull("table/cats")
		url = self.url_query(str(self.__query), p=page)
		content = self.get_pages_content(url)
		bs4 = BeautifulSoup(content, features="lxml")
		data = ResultsManager(columns=cols)
		items = bs4.find_all(**config.pull("html/item"))

		for item in items:
			title = item.find_all_next(**config.pull("html/title"))[0]
			title = title.find_all_next(**config.pull("html/id"))[0]

			if not title:
				continue

			category = item.find_all_next(**config.pull("html/cat"))
			category = category[0].find_all_next(**config.pull("html/cat_sub"))[0]
			category = format_tag_text(category.text)
			dst = self.get_cat_path(category, 70)
			
			publisher = item.find_all_next(**config.pull("html/pub"))
			update = item.find_all_next(**config.pull("html/time"))
			rate = item.find_all_next(**config.pull("html/score"))
			preview_img = item.find_all_next(**config.pull("html/preview"))

			item_id = format_tag_text(title["href"]).strip("/").split("/")[-1]
			title = format_tag_text(title.text)
			publisher = format_tag_text(publisher[0].text)
			update = format_tag_text( update[0].text)
			rate = format_tag_text(rate[0].text)
			preview_img = format_tag_text(preview_img[0]["src"])

			data.add_data(
				[title, category, publisher, item_id, float(rate), 
	 			update, get_time(update), preview_img, dst])
		return data

	def get_download_links(self, pid):
		url = f"{self.src_url}/p/{pid}/loadFiles"
		js_files = self.get_pages_content(url, True).json()
		files = []
		
		for file in js_files.get("files") or []:
			files.append({
				"size": file.get("size"),
				"url": parse_url.unquote(file.get("url") or ""),
				"active": file.get("active"),
				"id": file.get("id") or "0"
			})
		data_frame = pd.DataFrame(files)

		return data_frame

	def download(self, url: str, dst: str, manager=xget, callback=None):
		if not manager:
			raise ValueError("download manager not provided!")

		if not callable(callback):
			callback = None

		if callback:
			dwl = manager.download(url, dst, callback)
		else:
			dwl = manager.download(url, dst)

		return FileObject(dwl, dst)

	def get_preview(self, url: str):
		content = self.get_pages_content(url)
		return content
