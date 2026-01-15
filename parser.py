from lexer import tokenize

class ASTNode:
	def __init__(self, type_, value=None):
		self.type = type_
		self.value = value
		self.children = []

	def add_child(self, node):
		self.children.append(node)

	def __repr__(self, level=0):
		ret = "\t" * level + f"{self.type}: {self.value}\n"
		for child in self.children:
			ret += child.__repr__(level + 1)
		return ret

def parse(file_path):
	TT_DOT, TT_LOG, TT_RARROW, TT_QUOTE, TT_IDENTIFIER = tokenize(file_path)
	ast_root = ASTNode("PROGRAM")
	
	for i, token in enumerate(TT_IDENTIFIER):
		if i + 1 < len(TT_IDENTIFIER) and TT_IDENTIFIER[i+1] == '=':
			node = ASTNode("VARIABLE_STATEMENT")
			node.add_child(ASTNode("IDENTIFIER", TT_IDENTIFIER[i]))
			
			if TT_QUOTE:
				node.add_child(ASTNode("STRING", TT_QUOTE.pop(0)))
				ast_root.add_child(node)

	for log_token in TT_LOG:
		node = ASTNode("LOG_STATEMENT")
		
		if TT_QUOTE:
			node.add_child(ASTNode("STRING", TT_QUOTE.pop(0)))

		if TT_RARROW:
			node.add_child(ASTNode("RARROW", TT_RARROW.pop(0)))
		if TT_DOT:
			node.add_child(ASTNode("DOT", TT_DOT.pop(0)))
			
		ast_root.add_child(node)

	return ast_root