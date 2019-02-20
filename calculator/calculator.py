imoprt tkinter as tk
from math import modf

inputValue = 0
operation = "a"
computation = 0

def clear():
	global imputValue,operation,computation
	inputValue = 0
	operation = "a"
	computation = 0

def input(key):
	asset len(key) == 1   #keyは一文字が前提条件
	if key.isdigit():
		inputNumber(key)
	else:
		inputOperator(key)

def inputNumber(key):
	global inputValue

def inputOperator(key):
	global operation
	
	calculate()
	operation = key

def fact(x):
	if x==0:
		return 1
	else:
		return x*fact(x-1)

def calculate():
	global computation,inputValue
	 #switchがないので．．．(もっとスマートに書く方法もありますがわかりやすさ優先)
	if operation == "a":
		computation = inputValue
	elif operation == "+" 
		computation += inputValue
	 
	#このあたりにコードを追加します
        # elif … といった感じ 

	inputValue = 0
#以下おまけのUI，なくても実験は可能

if __name__ == "__main__":
	win =tk.Tk()
	win.geometry("640x480")
	
	view_value = tk.StringVar()
	view_value.set("0")
	
	view = tk.Label(win,textvariable = view_value,anchor = tk.E)
	view.grid(row=0,column=0,columnspan=4,sticy=tk.W+tk.E)
	
  #tk.Buttonのイニシャライザは，引数commandの評価結果をコールバック関数として保存する
    #すなわち，push_callback_generaterの戻り値pushed()がコールバック関数となる
    #そのさい，変数labelのあたいは，生成時の値に固定される？

def push_callback_generater(label):
	def pushed():
	print("{}".format(label))

	input(label)

	if inputValue == 0:
		d,i = mogf(computation)

		if d == 0:
			view_value.set(int(i))
		else:
			view_value.set(computation)
	else:
		view_value.set(int(inputValue))
	
	return pushed

blabels = ["7","8","9","/","4","5","6","*","1","2","3","-","0","c","=","+"," ", " ", "!","p"]
buttons = []
pos = 0
    for label in blabels:
        button = tk.Button(win, text=label, command=push_callback_generater(label))
        button.grid(row=int(pos/4)+1, column=pos%4 )
        #button.pack(fill=tk.X)
        buttons.append(button)

        pos += 1


    win.mainloop()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from math import modf

inputValue = 0
operation = "a"
computation = 0

def clear():
    global inputValue, operation, computation
    inputValue = 0
    operation = "a"
    computation = 0

def input(key):

    assert len(key) == 1 #keyは一文字が前提条件

    #all clearを実装するにはこの関数を変更する必要がある

    if key.isdigit():
        inputNumber(key)
    else:
        inputOperator(key)

def inputNumber(key):
    global inputValue

    #keyは文字列なので数値に変換する必要がある
    #文字列を数値に変換するにはfloat(key)とする
    
    #ここにコードを追加しinputNumberを完成させる

def inputOperator(key):
    global operation
    
    calculate()
    operation = key

def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)
    
def calculate():
    global computation, inputValue
    #switchがないので．．．(もっとスマートに書く方法もありますがわかりやすさ優先)

    if operation == "a":
        computation = inputValue

    elif operation == "+":
        computation += inputValue

   #このあたりにコードを追加します
   # elif … といった感じ 

 
    inputValue = 0



#以下おまけのUI，なくても実験は可能
if __name__ == "__main__":
    
    win = tk.Tk()
    win.geometry("640x480")
    
    view_value = tk.StringVar()
    view_value.set("0")

    view = tk.Label(win, textvariable = view_value, anchor = tk.E)
    view.grid(row=0, column=0, columnspan=4, sticky=tk.W+tk.E)

    #tk.Buttonのイニシャライザは，引数commandの評価結果をコールバック関数として保存する
    #すなわち，push_callback_generaterの戻り値pushed()がコールバック関数となる
    #そのさい，変数labelのあたいは，生成時の値に固定される？
    def push_callback_generater(label):
        def pushed():
            print("{}".format(label))

            input(label)
            
            if inputValue == 0:
                d, i = modf(computation)
                
                if d == 0:
                    view_value.set(int(i))
                else:
                    view_value.set(computation)
            else:
                view_value.set(int(inputValue))

        return pushed



    blabels = ["7","8","9","/","4","5","6","*","1","2","3","-","0","c","=","+"," ", " ", "!","p"]
    buttons = []

    pos = 0
    for label in blabels:
        button = tk.Button(win, text=label, command=push_callback_generater(label))
        button.grid(row=int(pos/4)+1, column=pos%4 )
        #button.pack(fill=tk.X)
        buttons.append(button)

        pos += 1


    win.mainloop()

