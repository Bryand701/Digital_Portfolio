Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def insert(elem, lista):
	if len(lista) == 0:
		return lista + [elem]
	elif elem > lista[0]:
		return [elem] + lista
	else:
		return [lista[0]] + [elem] + lista[1:]

	
>>> insert(4, [1,2,3,4,5,6,7])
[4, 1, 2, 3, 4, 5, 6, 7]
>>> insert(4, [7,6,5,4,3,2,1])
[7, 4, 6, 5, 4, 3, 2, 1]
>>> def insert(elem, lista):
	if len(lista) == 0:
		return lista + [elem]
	elif elem > lista[0]:
		return [elem] + lista
	else:
		return [lista[0]] insert(elem, lista[1:])
	
SyntaxError: invalid syntax
>>> 
>>> def insert(elem, lista):
	if len(lista) == 0:
		return lista + [elem]
	elif elem > lista[0]:
		return [elem] + lista
	else:
		return [lista[0]] + insert(elem, lista[1:])

	
>>> insert(4, [7,6,5,4,3,2,1])
[7, 6, 5, 4, 4, 3, 2, 1]
>>> 
