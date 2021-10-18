class Car:
    def __init__(self, make):
        self.make = make

        @property
        def make(self):
            return self.__make

    def __init__(self, model):
        self.model = model

        @property
        def model(self):
            return self.__model

    def __init__(self, php):
        self.php = php

        @property
        def php(self):
            return self.__php

    def __init__(self, mph):
        self.mph = mph

        @property
        def mph(self):
            return self.__mph