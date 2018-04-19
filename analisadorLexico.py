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
        self.TOKEN_OPERADORES = set(['+','-','*','/','%','=','++','--','+=','-='])
        # Lista de Tokens
        self.Tokens = []

    def criarToken(self, tipo, valor):
        self.Tokens.append(Token(tipo, valor))

    @staticmethod
    def idCheck(substr):
        # Verifica se a substring não começa com números e se os caracteres são válidos para ser identificador
        if len(substr) == 0:
            return False
        isntLetter = lambda n: n < 65 or n > 122 or (n > 90 and n < 97) or n == 95 or n == 36
        isValid = lambda n: (n>47 and n<58) or (n>64 and n<91) or n == 95 or (n>96 and n<123) or n == 36
        if isntLetter(ord(substr[0])):
            return False
        return all([isValid(ord(i)) for i in substr[1:]])

    @staticmethod
    def numCheck(substr):
        if substr == "":
            return False
        isNum = lambda n: n > 47 and n < 57
        return all([isNum(ord(c)) for c in substr])

    def subParser(self, substr):
        aux = ""
        op = ""
        quotesOpen = False
        for c in substr:
            if quotesOpen:
                aux += c
                continue
            if op != "" and c not in self.TOKEN_OPERADORES:
                self.criarToken(self.OPERADOR, op)
                op = ""
            elif c in self.TOKEN_OPERADORES:
                if self.idCheck(aux):
                    self.criarToken(self.IDENTIFICADOR, aux)
                    aux = ""
                if op == "":
                    if c == '+' or c == '-' or '=':
                        op += c
                    else:
                        self.criarToken(self.OPERADOR, c)
                else:
                    if c == '+' or c == '-' or c == '=':
                        self.criarToken(self.OPERADOR, op+c)
                        op = ""
                    else:
                        self.criarToken(self.OPERADOR, c)
            elif c in self.TOKEN_DELIMITADORES:
                if self.idCheck(aux):
                    self.criarToken(self.IDENTIFICADOR, aux)
                    aux = ""
                self.criarToken(self.DELIMITADOR, c)
            # Verificar começo de string
            elif c == "\"" or c == "\'":
                if self.idCheck(aux):
                    self.criarToken(self.IDENTIFICADOR, aux)
                    aux = ""
                aux += c
                if not quotesOpen:
                    quotesOpen = True
                else:
                    quotesOpen = False
                    self.criarToken(self.STRING, aux)
            else:
                aux += c
                if aux in self.TOKEN_RESERVADAS:
                    self.criarToken(self.RESERVADA, aux)
                    aux = ""
        if self.idCheck(aux):
            self.criarToken(self.IDENTIFICADOR, aux)
        if op != "":
            self.criarToken(self.OPERADOR, op)
        if self.numCheck(aux):
            self.criarToken(self.NUMERO, aux)

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
                if ("//" in linha):
                    pos = linha.index("//")
                novaLinha = linha[:pos].split()
                for substr in novaLinha:
                    # Análise rápida
                    if substr in self.TOKEN_RESERVADAS:
                        self.criarToken(self.RESERVADA, substr)
                    # Análise caractere por caractere
                    else:
                        self.subParser(substr)
            self.printTokens()

def main():
    # Define o caminho do arquivo usado
    arquivo = 'teste1.j'
    lex = Anallex()
    lex(arquivo)

if __name__ == "__main__":
    main()




#Processa o arquivo acima e inclui uma linha
