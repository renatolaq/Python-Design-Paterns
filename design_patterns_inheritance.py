class B:
    class A:
        def a1(self):
            print("a1")
            a = 0


    class B(A):
        def b(self):
            print("b")

if __name__ == '__main__':
    b = B.A()
    print(b.a1())
 
