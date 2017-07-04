#
#
from base1 import Base1

class Child1(Base1):
    def __init__(self, arg):
        Base1.__init__(self, arg)

    def method2(self):
        print("child1 method2")

print 'start driver child1'

if __name__ == '__main__':
    driver = Child1('testaroo')
    driver.method1()
    driver.method2()
    print(driver)

print 'stop driver child1'
