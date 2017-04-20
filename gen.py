



import string

List1=[2**i for i in range(5)]
print type(List1)
for i in List1:
 print "The List elements are", i
length = len(List1)
print length

generator= (2**i for i in range(5))
for i in generator:
 print i
#length = len(generator)
print type(range(5))

li = xrange(6)
print type(li)
for xra in li:
 print xra


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
gen=fib(10)
print gen
print gen.next
