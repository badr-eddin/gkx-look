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
	
	def retrieve(self):
		return pd.DataFrame(self.__results)

	def export(self, to="csv"):
		pass
