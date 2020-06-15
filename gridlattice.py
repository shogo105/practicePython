def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_once1():
    print('+ - - - - ', end = '')

def print_once2():
    print('|         ', end = '')
    
def print_twice1():
    do_twice(print_once1)
    print('+')

def print_twice2():
    do_twice(print_once2)
    print('|')
    
def print_wr():
    print_twice1()
    do_four(print_twice2)

do_twice(print_wr)
print_twice1()