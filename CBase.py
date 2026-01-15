from parser import parse
from interpreter import execute

ast = parse("tests/test.cb")
execute(ast)