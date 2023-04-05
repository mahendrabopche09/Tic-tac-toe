# Function in python
'''def sum(x,y):
    print(x+y)
sum(2,8)
sum(6,7)
'''
#Function return keyword
'''
def sum(x,y):
    return x + y
print(sum(5,8))
print(sum(55,55))'''

# Function default parameter value
'''
def Student_names(names ='rahul'):
    print('hello  '+ names)
Student_names()
Student_names('mahendra')
'''

# Function keywords argument
'''
def more_num(a,b=7,c= 10):
    print('a is ',a,'b is ',b,'while c is',c)

more_num(3,7)
more_num(23,c=17)
more_num(c=40,a=80)'''

# Function returning other function
'''
def greeting():
    def say_hello():
        return 'Hello'
    return say_hello
    
hello = greeting()
print(hello())'''

#assigning functio  to variable
'''
def mynum(x):
    return x+1
num = mynum
print(num(7))'''

#Global vs local variable scope
'''
x = 10
def my_numbers():
    global x
    print(x)
    x = 7
    print('my number is',x)
my_numbers()
print(x)'''

#Nesting function
'''
def mynum(a):
    def num(a):
      return a + 1
    result = num(a)
    return result
print(mynum(9))  '''

#Nesting function accessing variable scope
'''
def display_message(message):
    'hello'
    #print('hello',message)
    def message_sender():
        'nesting function'
        print(message)
    message_sender()
display_message('show me the money')  '''

# function pass keyword(pass statement)
def dream_home():cd
    pass
#pass no error

# passing function as Arguments to other function.

def mynum(b):
    return b + 1
def addnum(c):
    new = 7
    return c(new)
print(addnum(mynum))
    
