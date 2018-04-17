TOKEN_DELIMITADORES = [',',';','(',')','{','}','[',']']
TOKEN_OPERADORES = ['+','-','*','/','%','=','++','--','+=','-=']
TOKEN_PALAVRASRESERVADAS = ["int", "float", "boolean", "char", "string", "function", "if", "else", "then", "while", "do"]

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
            contaLinha += 1
            if (linha.startswith('//')):
                print("Linha foi pega: ",linha)
            
            #incrementador para identificar coluna atual
            contaColuna = 0
            for caractere in linha:
                contaColuna +=1
                
                #Ignora todo o caractere que for espaço em branco
                if (caractere.strip()):
                    analisaCaractere(caractere, contaLinha, contaColuna)


#Define o caminho do arquivo usado    
arquivo = 'arquivo.txt'
#Processa o arquivo acima e inclui uma linha
processaArquivo(arquivo)
