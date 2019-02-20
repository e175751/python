def sample_function():
    text = 'sample'
    print(text)
    return '戻り値'

text = sample_function()
print(text)

f = sample_function
text = f()
print(text)

def parm_func():
    return 'sample'

def sam_func(f):
    x=f()
    print(x)

sam_func(parm_func)
