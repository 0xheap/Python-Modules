
import dis

def ft_hello_garden():
    print("Hello, Garden Community!")

dis.dis(ft_hello_garden)


"""
import tokenize
import inspect
from io import BytesIO

def ft_hello_garden():
	x = 1 + 3

source = inspect.getsource(ft_hello_garden)

tokens = tokenize.tokenize(BytesIO(source.encode()).readline)

for tok in tokens:
    print(tok)





import ast
import inspect

def ft_hello_garden(x =None):
    print("Hello, Garden Community!")

source = inspect.getsource(ft_hello_garden)
tree = ast.parse(source)

print(ast.dump(tree, indent=4))

"""