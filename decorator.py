def foo(bar):
    print "test1"
    return bar + 1


print("test2" ,foo(2))

def dec(foo ,arg):
   print "test3"
   print foo
   print arg
   return foo(arg)
res=dec(foo,2)
print res  

