print('Nhập vào 3 cạnh của tam giác')
class Tamgiac:
    def __init__(self, A = None, B = None, C = None):
        self.A = int(input('A = '))
        self.B = int(input('B = '))
        self.C = int(input('C = '))

    def XacDinhTamGiac(self):
        A = self.A
        B = self.B
        C = self.C
        if (A + B < C) or (A + C < B) or (B + C < A):
            print('Đây không phải là một tam giác')
        else:
            print('Đây là một tam giác')

a = Tamgiac()
a.XacDinhTamGiac()
print('OK')