import re
from collections import namedtuple

KEYWORDS = [
    "SELECT", "FROM", "WHERE", "AND", "OR", "NOT", "INSERT", "INTO", "VALUES",
    "UPDATE", "SET", "DELETE", "CREATE", "TABLE", "DROP", "ALTER", "JOIN",
    "ON", "GROUP", "BY", "ORDER", "LIMIT", "DISTINCT", "AS", "NULL", "LIKE",
    "EXISTS", "BETWEEN", "CASE", "WHEN", "THEN", "ELSE", "END", "COMMIT", "ROLLBACK", "BEGIN", "TRANSACTION"
]
keywords_pattern = r'\b(' + '|'.join(KEYWORDS) + r')\b'

QueryToken = namedtuple('Token', ['type', 'value'])

def lexer(query: str) -> list[QueryToken]:
    regex = (
        rf'(?P<COMMENT_MULTI>/\*[\s\S]*?\*/)|'
        rf'(?P<COMMENT_SINGLE>--[^\n]*)|'
        rf'(?P<KEYWORD>{keywords_pattern})|'
        rf'(?P<NUMERIC>[0-9]*\.?[0-9]+)|'
        rf"(?P<STRING>'[^']*')|"
        rf'(?P<IDENTIFIER>[a-zA-Z_][a-zA-Z0-9_]*)|'
        rf'(?P<OPERATOR>>=|<=|!=|<>|>|<|=)|'
        rf'(?P<PUNCTUATION>[,;])|'
        rf'(?P<WHITESPACE>\s+)'
    )
    
    tokens = []
    
    for match in re.finditer(regex, query, re.IGNORECASE):
        kind = match.lastgroup
        value = match.group()
        
        if kind in ['COMMENT_MULTI', 'COMMENT_SINGLE', 'WHITESPACE']:
            continue
        
        if kind == 'KEYWORD':
            value = value.upper()
            
        tokens.append(QueryToken(type=kind, value=value))
    
    return tokens