from enum import Enum, auto



class Filers(Enum):
	Word = auto()
	Category = auto()
	Rate = auto()
	Date = auto()


class ResultsManager:
	def __init__(self):
		self.__results = []

	def add_data(self, obj: dict):
		pass

	def filter_by(self, rmf: Filters):
		pass

	def retrieve(self):
		pass

	def export(self, to="csv"):
		pass
