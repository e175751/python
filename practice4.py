def add(x,y):
    print (x+y)

add(5,4)

def add2(x,y):
    ans = x+y
    return ans

n=add2(10,6)
print(n)

def repeat_msg(msg,repeat=3):
    for i in range(repeat):
        print(msg)

repeat_msg('hello')
repeat_msg('yahoo',5)

def func(a1,a2,*args,**params):
    print(a1)
    print(a2)
    print(args)
    print(params)

func('A','B','C','D',k1='k1',k2='k2')

def sam_fun1():
    return -1

def sam_fun2():
    pass

def sam_fun3():
    return 1,'b'

x = sam_fun1()
print(x)
y=sam_fun2()
print(y)
w,z=sam_fun3()
print(w,z)

def sample(x,args=None):
    if args is None:
        args=[]
    args.append(x)
    return args

print(sample(1))
print(sample(2))
print(sample(3))

x=100
def samp_fun():
    global x
    x=200
    print(x)

samp_fun()
print(x)
