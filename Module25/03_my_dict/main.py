class MyDyct:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def remove(self, key):
        del self.data[key]

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value

    def get(self, key):
        return self.data.get(key, 0)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()


my_dict = MyDyct()
my_dict.add('apple', 'яблоко')
my_dict.add('banana', 'банан')
my_dict.add('orange', 'апельсин')

print(my_dict.get('apple'))
print(my_dict.get('peach'))

my_dict.update('apple', 'green apple')
print(my_dict.get('apple'))

my_dict.remove('banana')
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# зачтено
