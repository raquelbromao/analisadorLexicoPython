RED     ="\x1b[31m"
GREEN   ="\x1b[32m"
YELLOW  ="\x1b[33m"
BLUE    ="\x1b[34m"
MAGENTA ="\x1b[35m"
CYAN    ="\x1b[36m"
RESET   ="\x1b[0m"
BOLD	="\033[1m"
NORMAL	="\033[0m"

LISTA_TOKENS = dict()

#Tokens delimitadores
TOKEN_DELIMITADORES = set([',',';','(',')','{','}','[',']'])

#Tokens Operadores
TOKEN_OPERADORES = set(['+','-','*','/','%','=','++','--','+=','-='])

#Tokens Palavras reservadas
TOKEN_PALAVRASRESERVADAS = set(["int", "float", "boolean", "char", "string",
                                "function", "if", "else", "then", "while", "do"])


#Palavras reservadas
reservadas = set(["abstract", "extends", "int", "protected", "this", "boolean",
                  "false", "new", "public", "true", "char", "import", "null",
                  "return", "void", "class", "if", "package", "static", "while",
                  "else", "instanceof", "private", "super"])

def criarToken(tipo, valor):
    LISTA_TOKENS.

#Processa caractere atual da linha
def analisaCaractere(caractere, contaLinha,contaColuna):
    if (caractere == 'H'):
        print ("Char: ", caractere," | Linha: ", str(contaLinha)," | Coluna: ", str(contaColuna))

#Processa arquivo TXT incluindo uma linha        
def processaArquivo(arquivo):
    with open(arquivo) as file:
        #incrementador para identificar linha atual
        contaLinha = 0
        for linha in file:
            pos = len(linha)-1

            # Remover comentários
            if("//" in linha):
                pos = linha.index("//")
            queijo = linha[:pos].split()


            for i in queijo:
                if i in reservadas:
                    print(RED+str(i)+NORMAL)
                    #token reservada
                else:
                    aux = ""
                    for c in i:
                        if c in TOKEN_DELIMITADORES:
                            #token delim
                            pass
                        elif c in TOKEN_OPERADORES:
                            #token op
                            pass
                        else:
                            aux += c
                        if len(aux) <= 2:
                            if aux in TOKEN_OPERADORES:
                                #token
                                aux = ""
                                pass
                        if aux in TOKEN_PALAVRASRESERVADAS:
                            #token reservada
                            aux = ""
                            pass











            # contaLinha += 1
            # if (linha.startswith('//')):
            #     print("Linha foi pega: ",linha)
            #
            # #incrementador para identificar coluna atual
            # contaColuna = 0
            # for caractere in linha:
            #     contaColuna +=1
            #
            #     #Ignora todo o caractere que for espaço em branco
            #     if (caractere.strip()):
            #         analisaCaractere(caractere, contaLinha, contaColuna)


#Define o caminho do arquivo usado    
arquivo = 'teste1.j'


#Processa o arquivo acima e inclui uma linha
processaArquivo(arquivo)
