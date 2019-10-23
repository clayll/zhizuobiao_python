class A():
    name="A"

    __nickName="bbbb"

    @property
    def price(self):
        print(1)

    def go(self):
        print("aaaa")




class B():
    def show(self):
        print(":bbbb")


class A1(A):
    def go(self):
        print("1111111111")
import numpy as np

print(np.array(list("1123")))

np.arange(10)

np.linspace()

