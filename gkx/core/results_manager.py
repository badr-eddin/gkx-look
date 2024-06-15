import pandas as pd


class ResultsManager:
	def __init__(self):
		self.__results = []

	def add_data(self, obj: dict):
		self.__results.append(obj)

	def remove(self, index: int):
		if index < len(self.__results):
			self.__results.pop(index)

	def filter_by(self, filter_s):
		data = self.retrieve()
		cols = data.columns

		if isinstance(filter_s, (list, tuple)):
			for flt in filter_s:
				if flt not in cols:
					continue

				data = data.sort_values(by=flt)

		else:
			if filter_s in cols:
				data = data.sort_values(by=filter_s)
		
		return data

	def filter_by_word(self, words: str, case_sens=False, field="title"):
		words = (words if case_sens else words.lower()).split(";")
		data = self.retrieve()

		def containts_words(text, ws):
			return any(w in (text if case_sens else text.lower()) for w in ws)
		
		data = data[data[field].apply(lambda x: containts_words(x, words))]

		return data

	def filter_by_category(self, cats):
		return self.filter_by_word(cats, False, "category")

	def filter_by_time(self, t1, t2):
		pass

	def filter_by_score(self, s1, s2):
		if not isinstance(s1, (float, int)):
			return
		
		if not isinstance(s2, (float, int)):
			return

		data = self.retrieve()
		data = data[(data["score"] >= s1) & (data["score"] <= s2)]
		return data
	
	def retrieve(self):
		return pd.DataFrame(self.__results)

	def export(self, to="csv"):
		pass
