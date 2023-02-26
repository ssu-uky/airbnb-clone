class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print(super().__str__())
        return f"Dog: {self.name}"

jia = Dog("jia")
print(dir(jia))