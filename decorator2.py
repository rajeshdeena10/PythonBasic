import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """
    print "test", some_function
    def wrapper():
        t1 = time.time()
        print "time 1", t1
        print (type(t1))
        some_function()
        t2 = time.time()
        print "time2" ,t2
        print (type(t2))
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


print ("test2")
@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10)):
        num_list.append(num)
        total = sum(num_list)
        print total
    print("\nSum of all the numbers: " + str((sum(num_list))))

my_function()

@timing_function
def my_function2():
    num_list = []
    for num in (range(0, 5)):
        num_list.append(num)
        total = sum(num_list)
        print total
    print("\nSum of all the numbers: " + str((sum(num_list))))

my_function2()

