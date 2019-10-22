class Info():
    def __init__(self):
        self.name = ''
        self.age = 13

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name

    def printInfo(self):
        print("name：%s, age：%d" % (self.name, self.age))


class myInfo(Info):
    def __init__(self):  # 接受创建Car实例所需的信息
        super().__init__()

    def setAge(self, age):
        self.age = age + 1
