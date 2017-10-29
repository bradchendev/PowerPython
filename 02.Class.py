# 宣告class裡面的method用Tab縮排1次，method內的程式碼則要縮排2次
class Cat:
    def meow(self):
        print('Meow!')
pusheen = Cat()
pusheen.meow()


class Cat2:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name + ' Meow!')

pusheen2 = Cat2('pusheen')
pusheen2.meow()