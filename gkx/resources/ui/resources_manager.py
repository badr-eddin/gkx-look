import os


class resources:
    @staticmethod
    def _1_read_file(file):
        if not os.path.exists(file):
            raise FileNotFoundError(f"H: '{file}' not found!")

        return open(file, "r")
    
    @staticmethod
    def _2_read_file(file):
        """
        use QFile
        """
    
    @staticmethod
    def import_(file, read=None):
        if os.getenv("dev"):
            return resources.read_file()
        
        return
