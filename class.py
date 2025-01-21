class Animal:
    def __init__(self , name):
        self.name = name

    def funk(self):
        return self.name

result = Animal("Mushuk")   
print(result.funk())