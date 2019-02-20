def function_in_sub_module():
	print("sub_moduleの関数が呼び出された")

print("ここは必ず実行される")

if __name__ == "__main__":
	print("sub_moduleがコマンドラインから直接実行された")
	function_in_sub_module()
else:
    print("sub_moduleがimportされた")


