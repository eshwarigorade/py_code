class A:
    def function1(self):
        print('function1 in A')

    def function2(self):
        print('function2 in A')

    # def function3(self):
    #     print('function3 in A')

class B:
    def function1(self):
        print('function1 in B')

    def function3(self):
        print('function3 in B')

class C(A, B):
    # def function1(self):
    #     print('function1 in C')

    # def function3(self):
    #     print('function3 in C')

    def function4(self):
        print('function4 in C')

c1 = C()
c1.function1()
c1.function2()
# c1.function4()
c1.function3()



