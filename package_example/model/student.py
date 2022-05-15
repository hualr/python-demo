class Student(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __set_name__(self, name):
        self._name = name
