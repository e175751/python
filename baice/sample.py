class Test:
    def __init__(self,num):
        self.num = num

    def print_num(self):
        print('引数で渡された数字は{}です。'.format(self.num))

test = Test(10)
test.print_num()


class Test2:
    def __init__(self):
        print('コンストラクタが呼ばれました')

    def __del__(self):
        print('デストラクタが呼ばれました')

test2 = Test2()
del test2

class Bace:
    def __init__(self,num):
        self.num = num

    def print_num(self):
        print('引数で渡された数字は{}です'.format(self.num))

class Bace2(Bace):
    def print_num2(self):
        print('これはBaseクラスを継承しています')
        super().print_num()

bace = Bace2(20)
bace.print_num2()


class Test3:


    def test_print(self):
        print('This is test')

test3 = Test3()      #インスタンス生成
test3.test_print()  #メソッド呼び出し
