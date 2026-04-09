class Node:
    """ Class for any node in the tree """
    pass 

# Operators nodes 
class WhereNode:
    """Class for WHERE node"""
    def __init__(self, columns: list[str], operator: str, value: str | int | float) -> None:
        self.columns = columns
        self.operator = operator
        self.value = value
        
class FromNode:
    """Class for FROM node"""
    def __init__(self, tabels: list[str], value: str | int | float) -> None:
        self.tabels = tabels    
        self.valor = value
        

# Manipulate nodes
class SelectNode:
    """Class for SELECT node"""
    def __init__(self, cols: list[str], from_node: FromNode, where_node: WhereNode) -> None:
        self.cols = cols
        self.from_node = from_node
        self.where_node = where_node

class InsertNode:
    """Class for INSERT node"""
    def __init__(self, tabels: list[str], cols: list[str], values: list[str | int | float]) -> None:
        self.tabels = tabels
        self.cols = cols
        self.values = values
        
class DeleteNode:
    """Class for DELETE node"""
    def __init__(self, tabels: list[str], where_node: WhereNode) -> None:
        self.tabels = tabels
        self.where_node = where_node
        
class UpdateNode:
    """Class for UPDATE node"""
    def __init__(self, tabels: list[str], cols: list[str], values: list[str | int | float], where_node: WhereNode) -> None:
        self.tabels = tabels
        self.cols = cols
        self.values = values
        self.where_node = where_node
        
        
# AST tree
class ASTTree:
    """Class for AST tree"""
    def __init__(self, manipulate_node: SelectNode | InsertNode | DeleteNode | UpdateNode) -> None:
        self.manipulate_node = manipulate_node