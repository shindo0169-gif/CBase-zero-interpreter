TT_DOT = []
TT_LOG = []
TT_INPUT = []
TT_RARROW = []
TT_QUOTE = []
TT_IDENTIFIER = []
TT_COMMA = []

def tokenize(file_path):
	global TT_DOT, TT_LOG, TT_RARROW, TT_QUOTE, TT_IDENTIFIER, TT_INPUT, TT_COMMA
	TT_DOT = []
	TT_LOG = []
	TT_RARROW = []
	TT_QUOTE = []
	TT_IDENTIFIER = []
	TT_INPUT = []
	TT_COMMA = []

	with open(file_path, "r") as f:
		content = f.read()

	i = 0
	while i < len(content):
		char = content[i]

		if char in ['"', "'"]:
			quote_type = char
			val = char
			i += 1
			while i < len(content) and content[i] != quote_type:
				val += content[i]
				i += 1
			if i < len(content):
				val += quote_type
			TT_QUOTE.append(val)

		elif char == '.':
			TT_DOT.append(char)

		elif char == '>':
			TT_RARROW.append(char)
			
		elif char == ',':
			TT_COMMA.append(char)
			

		elif char.isalpha():
			word = char
			i += 1
			while i < len(content) and (content[i].isalnum() or content[i] == "_"):
				word += content[i]
				i += 1
			if word.lower() == 'log':
				TT_LOG.append(word)
			if word.lower() == 'input':
				TT_LOG.append(word)
			else:
				TT_IDENTIFIER.append(word)
			continue

		i += 1

	return TT_DOT, TT_LOG, TT_RARROW, TT_QUOTE, TT_IDENTIFIER, TT_INPUT, TT_COMMA