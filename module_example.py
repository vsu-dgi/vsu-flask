import math

def some_func(x):
	if type(x) is float:
		return math.sin(x) + 1
	else:
		print('type of x is not float')
		return None
