def my_decorator(some_function):
    print "test1", some_function
    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper
   # print "test2",wrapper
    #wrapper()

 
def some_function():
    print("Wheee!")

print ( "test" ,my_decorator(some_function))
just_some_function = my_decorator(some_function)

just_some_function()
