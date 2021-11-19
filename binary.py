#https://youtu.be/6oL-0TdVy28
class Node(object):
	def __init__ (self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__( self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder_print(tree.root, "")
		elif traversal_type == "inorder":
			return self.inorder_print(tree.root, "")
		elif traversal_type == "postorder":
			return self.postorder_print(tree.root, "")
		else:
			print("Traversal Type not supported")
			return False

	def preorder_print(self, start, traversal):
		#Root>Left>Right
		if start:
			#print(start.value)
			traversal += (str(start.value)+ " ")
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def inorder_print(self, start, traversal):
		if start:
			traversal = self.inorder_print(start.left, traversal)
			traversal += (str(start.value)+ " ")
			traversal = self.inorder_print(start.right, traversal)
		return traversal

	def postorder_print(self, start, traversal):
		if start:
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
			traversal += (str(start.value)+ " ")
		return traversal

tokens = ['^','/','*','+','-']

_v = False
variables = []

def is_negative(_int):
	try:
		if int(_int):
			return True
		else:
			return False
	except:
		return False

def poland(_string):
	global _v
	global variables
	pila = []
	_list = list(_string)
	x = 0
	print('')
	while True:
		if (x + 1) == len(_list):
			if _string.isnumeric():
				aux = Node(_string)
				return aux
			elif _string.isalpha():
				aux = Node(_string)
				_v = True
				if _string in variables:
					pass
				else:
					variables.append(_string)
				return aux
			else:
				pila.pop()
				_list.pop()
				_list = _list[::-1]
				_list.pop()
				_list = _list[::-1]
				_string = ''.join(_list)
				x = 0
				continue
		else:
			if _list[x] in tokens and len(pila) == 0:
				aux = Node(_list[x])
				print('valor', aux.value)
				#print(_list[x],' : ',_string[x])
				print('Izquierda: ',_string[:x])
				print('Derecha: ',_string[(x+1):])
				aux.left = poland(_string[:x])
				aux.right = poland(_string[(x+1):])
				return aux
			elif _list[x] == '(':
				pila.append('(')
			elif _list[x] == ')':
				try:
					pila.pop()
				except Exception as e:
					print("Falta un parentesis de apertura")
					raise e
		x += 1

def evaluacion(_list):
	pila = []
	for i in range(len(_list)):
		if len(pila) >= 2:
			if str(pila[len(pila)-1]).isnumeric() and pila[len(pila)-2] in tokens:
				if str(_list[i]).isnumeric() or is_negative(_list[i]):
					if pila[len(pila)-2] == '+':
						print('Sumando Valores {} + {}'.format(pila[len(pila)-1], _list[i]))
						aux = int(pila[len(pila)-1]) + int(_list[i])
						pila.pop()
						pila.pop()
						pila.append(aux)
					elif pila[len(pila)-2] == '-':
						print('Restando Valores {} - {}'.format(pila[len(pila)-1], _list[i]))	
						aux = int(pila[len(pila)-1]) - int(_list[i])
						pila.pop()
						pila.pop()
						pila.append(aux)
					elif pila[len(pila)-2] == '*':
						print('Multiplicando Valores {} * {}'.format(pila[len(pila)-1], _list[i]))
						aux = int(pila[len(pila)-1])*int(_list[i])
						pila.pop()
						pila.pop()
						pila.append(int(aux))
					elif pila[len(pila)-2] == '/':
						print('Dividiendo Valores {} / {}'.format(pila[len(pila)-1], _list[i]))	
						aux = int(pila[len(pila)-1])/int(_list[i])
						pila.pop()
						pila.pop()
						pila.append(int(aux))
					elif pila[len(pila)-2] == '^':
						print('{} elevado a la {} potencia'.format(pila[len(pila)-1], _list[i]))
						aux = pow(int(pila[len(pila)-1]),int(_list[i]))
						pila.pop()
						pila.pop()
						pila.append(aux)	
				else:
					pila.append(_list[i])
			else:
				pila.append(_list[i])
		else:
			pila.append(_list[i])
	return pila
#	   #
#	  / \
#   +	 None
#  / \
# *    /
#/ \  /	\
#4  4 a  5
tree =BinaryTree('#')
try:
	cadena = input("Menu Principal: \n 1-Introducir terminos\n")
	tree.root.left = poland(cadena)
	p = tree.print_tree("postorder")
	print('Notación Polaca: ',p)
	if _v:
		print('\nIntroduzca el valor de las variables')
		for i in range(len(variables)):
			_r = int(input('Variable {}:\n'.format(variables[i])))
			p = p.replace(variables[i], str(_r))
		print('Variables Remplazadas: ',p)
		_datos = p.split(' ')
		_datos.pop()
		_datos.pop()
		while len(_datos) != 1:
			#print(len(_datos))
			print('Cadena actual: ', _datos)
			_datos = evaluacion(_datos)
		print('\nLa respuesta es: ', _datos[0])
	else:
		_datos = p.split(' ')
		_datos.pop()
		_datos.pop()
		while len(_datos) != 1:
			#print(len(_datos))
			print('Cadena actual: ', _datos)
			_datos = evaluacion(_datos)
		print('La respuesta es: ', _datos[0])
	
	print("Otros Ordenes")
	print('En Orden',tree.print_tree("inorder"))
	print('Pre-Orden',tree.print_tree("preorder"))
	print('Post-Orden',tree.print_tree("postorder"))
except Exception as e:
	raise e