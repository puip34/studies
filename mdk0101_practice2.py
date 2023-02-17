class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def method1(self):
        print("Вызов метода 1")

    def method2(self):
        print("Вызов метода 2")

    def method3(self):
        print("Вызов метода 3")
class B(A):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def method1(self):
        print("Переопределенный метод 1")


class C(A):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def method4(self):
        print("Вызов метода 4")

    def method5(self):
        print("Вызов метода 5")
# создание экземпляра класса A
a = A(1, 2)
print(a.x, a.y)
a.method1()
a.method2()
a.method3()

# создание экземпляра класса B
b = B(1, 2, 3)
print(b.x, b.y, b.z)
b.method1()
b.method2()
b.method3()

# создание экземпляра класса C
c = C()
print(c.x, c.y, c.z)
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
