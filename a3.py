import re

especificacao_tokens = [
    ('NUMERO',    r'\d+(\.\d*)?'),        
    ('STRING',    r'\'[^\']*\'|\"[^\"]*\"'), 
    ('IDENTIFICADOR', r'[A-Za-z_]\w*'),      
    ('IGUAL',     r'='),                     
    ('MAIS',      r'\+'),           
    ('MENOS',     r'-'),            
    ('MULTIPLICACAO', r'\*'),          
    ('DIVISAO',   r'/'),                
    ('PARENTESE_ESQ', r'\('),             
    ('PARENTESE_DIR', r'\)'),          
    ('CHAVE_ESQ', r'\{'),             
    ('CHAVE_DIR', r'\}'),               
    ('PONTO_VIRGULA', r';'),            
    ('ESPACO',    r'[ \t]+'),     
    ('DESCONHECIDO', r'.'),    
]

# Compila os padrões em uma expressão regular única
regex_tokens = '|'.join('(?P<%s>%s)' % par for par in especificacao_tokens)
encontrar_token = re.compile(regex_tokens).match

def analisador_lexico(codigo):
    pos = 0
    mo = encontrar_token(codigo)
    while mo is not None:
        tipo = mo.lastgroup
        valor = mo.group()
        if tipo == 'NUMERO':
            valor = float(valor) if '.' in valor else int(valor)
            yield (tipo, valor)
        elif tipo == 'STRING':
            yield (tipo, valor) 
        elif tipo == 'IDENTIFICADOR':
            yield (tipo, valor) 
        elif tipo == 'ESPACO':
            pass
        elif tipo == 'DESCONHECIDO':
            raise RuntimeError(f'Caractere inesperado {valor!r}')
        else:
            yield (tipo, valor)
        pos = mo.end()
        mo = encontrar_token(codigo, pos)
    if pos != len(codigo):
        raise RuntimeError(f'Caractere inesperado {codigo[pos]!r}')
    
codigo = input("Digite o trecho de código para análise léxica: ")

tokens = list(analisador_lexico(codigo))
print("Tokens identificados:")
for token in tokens:
    print(token)
