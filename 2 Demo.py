
# passing function as arguments to other function
'''
def mynum(b):
    return b + 1
def addnum(c):
    newnum = 7
    return c(newnum)
print(addnum(mynum)) '''

# anonymous function(Lambda , map )
'''
a = lambda b : b + 4
print(a(6))

c = lambda d,e : d + e
print(c(8,3))

def ghost_number(n):
    return lambda f : f *n
num = ghost_number(2)
print(num(20))  '''

#Python decorator
'''
def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper
@my_decorator
def say_hello():
    return 'hello world'
print(say_hello())  '''
    
# python method and function ( built in)
'''
b = 'hello'
print(len(b))

c = b.upper()
print(c)

print(b)

print('Hii')
'''

