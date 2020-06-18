def is_triangle(a, b, c):
    if(a + b >= c and b + c >= a and c + a >= b):
        print('Yes')
    else:
        print('No')

def imput_sticks():
    a = int(input('1本目='))
    b = int(input('2本目='))
    c = int(input('3本目='))
    is_triangle(a, b, c)
    
imput_sticks()