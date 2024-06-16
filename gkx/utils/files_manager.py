import io


__all__ = ["FileObject"]


class FileObject(io.BytesIO):
	def __init__(self, path=""):
		super().__init__()

		self.__path = path

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
