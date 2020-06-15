def check_fermat(a, b, c, n):
    if(n < 3):
        print("nは3以上で入力してください")
    elif(a ** n + b ** n == c ** n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work")

def imput_num():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    n = int(input('n='))
    check_fermat(a, b, c, n)
    
imput_num()