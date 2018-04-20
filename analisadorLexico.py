RED     ="\x1b[31m"
GREEN   ="\x1b[32m"
YELLOW  ="\x1b[33m"
BLUE    ="\x1b[34m"
MAGENTA ="\x1b[35m"
CYAN    ="\x1b[36m"
RESET   ="\x1b[0m"
BOLD	="\033[1m"
NORMAL	="\033[0m"


class Token(object):

    def __init__(self, tipo, valor):
        # Provavelmente vai precisar adicionar mais atributos
        self.tipo = tipo
        self.valor = valor

class Anallex:
    def __init__(self):
        # Tokens Palavras reservadas
        self.RESERVADA = "RESERVADA"
        self.OPERADOR = "OPERADOR"
        self.DELIMITADOR = "DELIMITADOR"
        self.IDENTIFICADOR = "IDENTIFICADOR"
        self.NUMERO = "NUMERO"
        self.STRING = "STRING"
        self.TOKEN_RESERVADAS = set(["abstract", "extends", "int", "protected", "this", "boolean",
                  "false", "new", "public", "true", "char", "import", "null",
                  "return", "void", "class", "if", "package", "static", "while",
                  "else", "instanceof", "private", "super"])
        # Tokens delimitadores
        self.TOKEN_DELIMITADORES = set([',', ';', '(', ')', '{', '}', '[', ']', '.'])
        # Tokens Operadores
        self.TOKEN_OPERADORES = set(['+','-','*','/','%','=','++','--','+=','-=', '>', '<', '<=', '>='])
        # Lista de Tokens
        self.Tokens = []
        # Buffer da análise
        self.BuffLeitura = ""

    def criar_token(self, tipo, valor):
        self.Tokens.append(Token(tipo, valor))

    @staticmethod
    def id_check(substr):
        # Verifica se a substring não começa com números e se os caracteres são válidos para ser identificador
        if len(substr) == 0:
            return False
        isntLetter = lambda n: n < 65 or n > 122 or (n > 90 and n < 97) or n == 95 or n == 36
        isValid = lambda n: (n>47 and n<58) or (n>64 and n<91) or n == 95 or (n>96 and n<123) or n == 36
        if isntLetter(ord(substr[0])):
            return False
        return all([isValid(ord(i)) for i in substr[1:]])

    @staticmethod
    def num_check(substr):
        if substr == "":
            return False
        isNum = lambda n: n in range(47,57)
        return all([isNum(ord(c)) for c in substr])

    def id_or_num(self):
        if self.id_check(self.BuffLeitura):
            self.criar_token(self.IDENTIFICADOR, self.BuffLeitura)
        elif self.num_check(self.BuffLeitura):
            self.criar_token(self. NUMERO, self.BuffLeitura)
        else:
            # Tratar erro
            pass
        self.BuffLeitura = ""

    def lex_parser(self, novaLinha):
        openQuotes = False
        op = ""
        for substr in novaLinha:
            # Análise rápida
            if substr in self.TOKEN_RESERVADAS:
                self.criar_token(self.RESERVADA, substr)
                continue
            # Análise caractere por caractere
            print(substr)
            for c in substr:
                if c == "\"" or c == "\'":
                    if not openQuotes:
                        self.id_or_num()
                        openQuotes = True
                    else:
                        openQuotes = False
                        self.criar_token(self.STRING, self.BuffLeitura+c)
                        self.BuffLeitura = ""
                elif openQuotes:
                    self.BuffLeitura += c
                    continue
                if op != "" and c not in self.TOKEN_OPERADORES:
                    self.criar_token(self.OPERADOR, op)
                    op = ""
                elif c in self.TOKEN_OPERADORES:
                    self.id_or_num()
                    if op == "":
                        if c == '+' or c == '-' or '=':
                            op += c
                        else:
                            self.criar_token(self.OPERADOR, c)
                    else:
                        if c == '+' or c == '-' or c == '=':
                            self.criar_token(self.OPERADOR, op+c)
                            op = ""
                        else:
                            self.criar_token(self.OPERADOR, c)
                elif c in self.TOKEN_DELIMITADORES:
                    self.id_or_num()
                    self.criar_token(self.DELIMITADOR, c)
                # Verificar começo de string
                else:
                    self.BuffLeitura += c
                    if self.BuffLeitura in self.TOKEN_RESERVADAS:
                        self.criar_token(self.RESERVADA, self.BuffLeitura)
                        self.BuffLeitura = ""
            if not openQuotes:
                self.id_or_num()

    def printTokens(self):
        for t in self.Tokens:
            print(RED+"<{}, {}>".format(t.tipo, t.valor)+NORMAL)

    def __call__(self, arqFonte):
        # Processa arquivo com código fonte
        with open(arqFonte) as file:
            # incrementador para identificar linha atual
            contaLinha = 0
            for linha in file:
                pos = len(linha) - 1
                # Remover comentários
                if "//" in linha:
                    pos = linha.index("//")
                novaLinha = linha[:pos].split()
                self.lex_parser(novaLinha)
            self.printTokens()

def main():
    # Define o caminho do arquivo usado
    arquivo = 'teste1.j'
    lex = Anallex()
    lex(arquivo)

if __name__ == "__main__":
    main()




#Processa o arquivo acima e inclui uma linha
