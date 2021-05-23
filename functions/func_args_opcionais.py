def func_1(arg_1, arg_2, arg_3=None):
	if arg_3 is None:
		print(arg_1, arg_2)
	else:
		print(arg_1, arg_2, arg_3)



# func_1(1, 2)
# func_1(1, 2, 3)



def func_2(*args):
	print("Quantidade de args: ",len(args))
	for arg in args:
		print(arg)


func_2(1, 2, 3, 4, 5, 6, 7, 8, 67)
