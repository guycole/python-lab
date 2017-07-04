#
#
class Base1:
    def __init__(self, arg):
        self.ctor_arg = arg

    def __str__(self):
        return "Base1:%s" % self.ctor_arg

    def method1(self):
        print("base1 method1")

print 'start driver base1'

if __name__ == '__main__':
    driver = Base1('arg1')
    driver.method1()
    print(driver)

print 'stop driver base1'