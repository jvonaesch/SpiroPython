
class EvaluationRecord:

    def __init__(self, x):
        self.__x = x
        self.evaluated = {}

    def __getitem__(self, key):
        if key in self.evaluated.keys():
            return self.evaluated[key]
        return None

    def __setitem__(self, key, value) -> bool:
        if key not in self.evaluated.keys():
            self.evaluated[key] = value
            return True
        return False

    @property
    def x(self):
        return self.__x