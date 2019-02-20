print("ハローワールド")

num1 = 1
num2 = 2
result = num1+num2
print(result)

String1 = 'a'
String2 = 'b'
concat = String1 + String2
print(concat)

import sys
sys.stdout.write("hello world\n")

print("hello world",end="")

print('2+1=',2+1)
print('10-3=',10-3)
print('7*4=',7*4)
print('5/2=',5/2)
print('5//2=',5//2)
print('10%3=',10%3)
print('2**10=',2**10)

for x in range(0,9):
    for y in range(0,9):
        print('{0}'.format('%2d'%((x+1)*(y+1))),end="")
    print('')
