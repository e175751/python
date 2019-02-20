print("うるう年の判定を行います")
input_number = int(input(">>"))
#print('入力された数字は%dです') % (input_number)
if (input_number % 4 == 0 and input_number % 100 != 0) or input_number % 400 == 0:
    print("うるう年である")
else:
    print("うるう年出ない")
