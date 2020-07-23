class User:
    counter = 0
    def __init__(self, name):
        self.name = name
        type(self).counter += 1
    def get_counter(self):
        count=self.counter
        return count