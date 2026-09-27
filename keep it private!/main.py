class myclss:
    __privateVar = 27;
    def __privmethod(self):
        print("I am inside my class!")
    def hello(self):
        print("the private variable is:",myclss.__privateVar)
foo = myclss()
foo.hello()
foo.__privmethod



