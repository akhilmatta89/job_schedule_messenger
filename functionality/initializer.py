from functionality.file_operations.file_ops import FileOps


class TriggerIntializer:

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name

    def init_trigger(self):
        file_handler = FileOps(path=self.path, filename=self.file_name)
        return file_handler
