from .parser.lexer import lexer
from .parser.recursive_descendent_parser import parse_query

class TSQL:
    def __init__(self) -> None:
        pass

    def run_query(self, query: str):
        query_lexical_trated = lexer(query)
        
        query_tree = parse_query(query_lexical_trated)
        
        return query_tree
