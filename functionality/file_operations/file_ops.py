import pandas as pd
from io import StringIO


class FileOps:

    def __init__(self, path, filename):
        self.path = path
        self.file_name = filename

    def read_and_convert_content_to_dataframe(self):
        try:
            df = pd.read_excel(self.path + self.file_name)  # skip problematic rows
            return df
        except Exception as e:
            print(f"Error converting content to DataFrame: {e}")
            return None

