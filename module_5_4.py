class Buiding:
    total = []
    def __init__(self, house, name):
        self.name = name
        self.house = house

        t1 = []
        i = 0
        for i in range(0, house):
            i = i + 1
            t1.append(i)
            t1.append(name)
            t1.append(',')
            Buiding.total = t1

Village = Buiding(40, 'дом')

print(*Buiding.total)

