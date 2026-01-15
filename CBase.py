from parser import parse
from interpreter import execute

ast = parse("test.cb")
execute(ast)