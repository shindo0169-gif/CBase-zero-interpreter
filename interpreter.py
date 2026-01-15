from parser import parse

symbol_table = {}

def execute(node):
    global symbol_table

    if node.type == "PROGRAM":
        for child in node.children:
            execute(child)

    elif node.type == "VARIABLE_STATEMENT":
        var_name = None
        var_value = None
        for child in node.children:
            if child.type == "IDENTIFIER":
                var_name = child.value
            elif child.type == "STRING":
                var_value = child.value[1:-1]
        if var_name:
        	symbol_table[var_name] = var_value

    elif node.type == "LOG_STATEMENT":
        for child in node.children:
            if child.type == "STRING":
                
                print(child.value[1:-1])
            elif child.type == "IDENTIFIER":
                
                val = symbol_table.get(child.value, f"Undefined: {child.value}")
                print(val)