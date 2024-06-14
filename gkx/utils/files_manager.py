


class FileObject:
	def __init__(self):
		self.__path = ""

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, path: str):
		self.__path = path

	def __extract(self):
		pass

	def export2(self, dst):
		pass
