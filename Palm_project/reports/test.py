def deco(func):
	print('before Myfunc called')
	func()
	print('after Myfunc called')
	return func
	
@deco
def Myfunc():
	print('Myfunc called')

# Myfunc = deco(Myfunc)

