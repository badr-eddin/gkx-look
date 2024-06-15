# managing http requests
import requests
import urllib.parse as parse_url

# html analysing
from bs4 import BeautifulSoup
import re
import pandas as pd
from ..utils import get_time, format_tag_text
from .results_manager import ResultsManager

import os

class Scrapper:
	def __init__(self):
		self.src_url = "https://www.pling.com"
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
		pages = bs4.find_all("ul", class_="pagination")[0].findAllNext("li")
		pages_num = []

		for page in pages:
			index = re.findall(r"\s*(\d+)\s*", page.text)
			if len(index) == 1:
				pages_num.append(index[0])

		return int(pages_num[-1])

	def get_pages_content(self, url: str, obj=False):
		proxies = {
                        "http": "http://192.168.43.208:7071",
                        "https": "https://192.168.43.208:7071"
                }  # settings

		# response = requests.get(url) #, proxies=proxies)
		return open("test.html").read() # response if obj else response.content

	def search(self, query: str):
		"""
		the reason why surfin to page 99999,
		is to get all the pages available,
		probably less than that number (hope so)
		"""

		url = self.url_query(str(query), p=99999)
		content = self.get_pages_content(url)
		self.__pages_num = self.get_pages_number(content)
		self.__query = query

		return self.scrap_page(1)

	def scrap_page(self, page: int):
		# todo: check if item category is supported or not
		# todo: read classes used in bs4 from inner-config

		if page > self.__pages_num or self.__pages_num <= 0:
			return
		if not self.__query:
			return

		url = self.url_query(str(self.__query), p=page)
		content = self.get_pages_content(url)
		bs4 = BeautifulSoup(content, features="lxml")
		data = ResultsManager()

		items = bs4.find_all("div", class_="explore-product")

		for item in items:
			title = item.find_all_next("h3")[0]
			title = title.find_all_next("a")[0]

			if not title:
				continue

			publisher = item.find_all_next("a", class_="tooltip""user")
			update = item.find_all_next("div", class_="collected")
			rate = item.find_all_next("div", class_="kkSWyw")
			category = item.find_all_next("div", class_="title")
			category = category[0].find_all_next("b")[0]
			preview_img = item.find_all_next("img", class_="explore-product-image")

			item_id = format_tag_text(title["href"]).strip("/").split("/")[-1]
			title = format_tag_text(title.text)
			publisher = format_tag_text(publisher[0].text)
			update = format_tag_text( update[0].text)
			rate = format_tag_text(rate[0].text)
			category = format_tag_text(category.text)
			preview_img = format_tag_text(preview_img[0]["src"])

			data.add_data({
				"title": title,
				"category": category,
				"publisher": publisher,
				"id": item_id,
				"score": float(rate),
				"time": update,
				"datetime": get_time(update),
				"preview": preview_img
			})
		return data

	def get_download_links(self, pid):
		url = f"{self.src_url}/p/{pid}"
		js_files = self.get_pages_content(url, True).json()
		files = []

		for file in js_files:
			files.append({
				"size": file.get("size"),
				"url": parse_url.unquote(file.get("url") or ""),
				"active": file.get("active")
			})
		data_frame = pd.DataFrame(files)

		return data_frame

	def download(self, url: str):
		pass  # todo: use old Predator download manager

	def get_preview(self, url: str):
		content = self.get_pages_content(url)
		return content

