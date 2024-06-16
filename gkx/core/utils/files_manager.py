import patoolib
import os


__all__ = ["FileObject"]


class FileObject:
	def __init__(self, path="", dst=""):
		super().__init__()

		self.__path = path
		self.__dst = dst

	@property
	def path(self):
		return self.__path

	@path.setter
	def path(self, path: str):
		self.__path = path

	@property
	def dist(self):
		return self.__dst

	@dist.setter
	def dist(self, cat: str):
		self.__dst = cat

	def export(self):
		arch = self.path
		dst = self.dist

		if not os.path.exists(arch):
			return

		if not dst:
			return
		
		return patoolib.extract_archive(arch, -1, dst)