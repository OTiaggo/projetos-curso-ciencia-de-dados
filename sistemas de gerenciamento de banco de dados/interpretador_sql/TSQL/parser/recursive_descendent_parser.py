from ast import parse
from nt import error
from .lexer import QueryToken

from .AST_tree import SelectNode, FromNode, WhereNode, ASTTree, InsertNode, DeleteNode, UpdateNode

def get_cols(query_list: list[QueryToken], i_init: int, keyword_stop: str) -> list[str]:
    i = i_init
    list_cols = []
    
    while query_list[i].value != keyword_stop:
        if query_list[i].value != ',':
            list_cols.append(query_list[i].value) 
        i += 1
    
    return list_cols, i+1



def parse_query(query_lexical_trated: list[QueryToken]) -> ASTTree: 
    query_tree = parse_manipulate_query(query_lexical_trated)
    
    return query_tree
    
def parse_manipulate_query(query_list: list[QueryToken]) -> ASTTree:
    manipulate_node = None 
       
    if(query_list.startswith("SELECT")):
        manipulate_node = SelectNode(query_list)
        manipulate_node.cols, indice = get_cols(query_list, 1, "FROM")
        manipulate_node.from_node = parse_from_node(query_list)
        manipulate_node.where_node = parse_where_node(query_list)
    elif (query_list.startswith("INSERT")):
        manipulate_node = InsertNode(query_list)
    elif (query_list.startswith("DELETE")):
        manipulate_node = DeleteNode(query_list)
    elif (query_list.startswith("UPDATE")):
        manipulate_node = UpdateNode(query_list)
    else:
        # Return sintatic error
        raise ValueError("Sintatic error: your query no have a manipulate command(example: SELECT, INSERT, DELETE, UPDATE)")
    
    return manipulate_node
    
def parse_from_node(query: str) -> FromNode:
    from_node = FromNode(query)
    from_node.tabels = get_cols(query, "FROM", "WHERE")
    from_node.value = get_value(query, "FROM", "WHERE")
    return from_node

def parse_where_node(query: str) -> WhereNode:
    where_node = WhereNode(query)
    where_node.columns = get_cols(query, "WHERE", "=")
    where_node.operator = get_operator(query, "WHERE", "=")
    where_node.value = get_value(query, "WHERE", "=")
    return where_node

