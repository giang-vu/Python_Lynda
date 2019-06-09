#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("This is myClass, method1")

    def method2(self, stringArg):
        print("This is myClass, method2 and " + stringArg)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("This is anotherClass, method1")

    def method2(self, stringArg):
        myClass.method2(self, stringArg)
        print("This is anotherClass, method2 and " + stringArg)

def main():
    c1 = myClass()
    c1.method1()
    c1.method2("a string argument")

    c2 = anotherClass()
    c2.method1()
    c2.method2("another string argument")

if __name__ == "__main__":
    main()
