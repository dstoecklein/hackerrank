from typing import List


class Storage():
    pass

class ListStorage(Storage):
    def __init__(self, a: any, b: any):
        super().__init__()
        self.a = a
        self.b = b

    def get_dic(self):
        return {self.a: self.b}

print(ListStorage(2, "b").get_dic())