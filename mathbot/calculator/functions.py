class BuiltinFunction:

	def __init__(self, func, name = None):
		self.func = func
		self.name = name or getattr(func, '__name__', '<unnamed>')
		self.macro = False
		
	def __call__(self, *args):
		return self.func(*args)

	def __str__(self):
		return 'Builtin Function {}'.format(self.name)


class Function:

	def __init__(self, address, scope, macro): # , variadic):
		self.address = address
		self.scope = scope
		self.macro = macro
		# self.variadic = variadic
		# assert(not (macro and variadic))

	def __repr__(self):
		return ('m' if self.macro else 'f') + '({})'.format(self.address)


class Array:

	def __init__(self, items):
		self.items = items
		self.macro = False

	def __call__(self, index):
		return self.items[index]

	def __len__(self):
		return len(self.items)

	def __str__(self):
		return 'array(' + ', '.join(map(str, self.items)) + ')'


class Expanded:

	def __init__(self, array):
		assert(isinstance(array, Array))
		self.array = array

	def __len__(self):
		return len(self.array)

	def __str__(self):
		return 'expanded({})'.format(', '.join(map(str, self.array.items)))