
class DataCleaning:
    def __init__(self):
        self.data = []
        self.headers = []
        self.db = {
            "headers": [],
            "data":[],
        }
    def read_csv(self, path: str) -> list:
        """
            Read CSV file given a specific path
            input: path -> str
            output: list with data -> list
        """
        try:
            with open(path) as file:
                self.data = file.readlines()
            return self.data
        except:
            raise Exception("invalid path: file not found")
        finally:
            file.close()
    
    def clean_data(self, headers:bool = True) -> object:
        if headers:
            self.headers = self.data[1].replace("\n", "").replace("\"", "").split(" ")
            self.db["headers"] = self.headers
        count = 1
        line = ""
        for row in self.data[2:]:
            if '\"' not in row and row != self.data[1]:
                try:
                    int(row[0])
                except:
                    row = row.replace(" ", "_")
                line += row
            else:
                if '\"' not in row[0]:
                    count += 1
                    line =line+row
                    self.db["data"].append(line.replace("\n", " ").replace("\"", "").split(" ")[:-1])               
                    line = ""
        return self.db

