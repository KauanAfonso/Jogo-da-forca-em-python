


import random as r


jogoDaForca = '''
   ___                         _          __                    
  |_  |                       | |        / _|                   
    | | ___   __ _  ___     __| | __ _  | |_ ___  _ __ ___ __ _ 
    | |/ _ \ / _` |/ _ \   / _` |/ _` | |  _/ _ \| '__/ __/ _` |
/\__/ / (_) | (_| | (_) | | (_| | (_| | | || (_) | | | (_| (_| |
\____/ \___/ \__, |\___/   \__,_|\__,_| |_| \___/|_|  \___\__,_|
              __/ |                                             
             |___/                                              

'''

msg1 = '''
  O   
      

'''
msg2 = '''

  
  O   
  |   
      
'''
msg3 = '''

    
  O   
 /|   
      

'''
msg4 = '''
 

  O   
 /|\ 


'''
msg5 = '''


  O  
 /|\  
 /    
      

'''
msg6 ='''

  O  
 /|\ 
 / \  
      
'''

ms5 = '''

    Escolha um modo de jogo:
    1-Para Adicionar uma palavra na lista
    2-Para Excluir uma palavra na lista 
    3-Para Jogar o jogo
    4-Para Sair do jogo

'''

#Inicio do dicionario de palavras
dicionarioDePalavras = {
        "Carro":"Veiculo",
        "Kauan": "Nome",
        "Amarelo": "Cor"
    }



################################################  FUNCAO PARA O JOGO  ##############################################################

def jogo():

    numAleatorio = r.randint(0, len(dicionarioDePalavras) - 1) # gerando um número aletório do tamanho do dicionario
    palavra, dica = r.choice(list(dicionarioDePalavras.items())) #Escolhendo a palavra aleatoria de forma randomica 
    #Com a funcao choice que transforumou os itens em uma lista e atribuiu

    print(jogoDaForca) #print Desenho

    palavraEscondida = '' #Aqui ficara a palavra escolhida codificada
    contadorDeAsteristicos = 0 #contador de asteristicos
    letrasQueJaforam = []



    for i in palavra: # iterando sobre a palavra e escondendo ela
        palavraEscondida+= "*"

    palavraEscondida = list(palavraEscondida) #Transoformando a palavraEscondida em uma lista 
    palavra = list(palavra.lower()) #deixando as letras todas as letras minúsculas em uma lista 


    tentativas = 6

    while tentativas > 0:
        
        
        print("Dica: " + dica)
        palavraDoUsuario = input("Digite uma letra: ")

        letrasQueJaforam.append(palavraDoUsuario)
        
        print(F"Essas letras ja foram: {letrasQueJaforam}")

        if  palavraDoUsuario.lower() in palavra: #Se a letra do usuario estiver na lista palavra correta
            
            for letra in range(len(palavra)): #O for irá iterar a palavra para descobrir onde e a posicao da letra do meu usuario está
                if palavraDoUsuario == palavra[letra]: 
                    palavraEscondida[letra] = palavraDoUsuario #Atribuindo a letra presente na palavra correta na [] de palavra escondida 
            print(*palavraEscondida)
            
        else:
            tentativas-=1 #Se ele errar diminui a tentativa e parace a forma
            if tentativas == 5:
                print(msg1)
            elif tentativas == 4:
                print(msg2)
            elif tentativas == 3:
                print(msg3)
            elif tentativas == 2:
                print(msg4)
            elif tentativas == 1:
                print(msg5)
            

        for asteristico in palavraEscondida: #for para contar os * na palavra 
            if asteristico == "*":
                contadorDeAsteristicos +=1
        print(contadorDeAsteristicos)
        
        if contadorDeAsteristicos == 0: #Se não tiver * o jogo acaba !
            print('Acertou a palavra')
            break

          
        contadorDeAsteristicos = 0
        

            
    else:
        print("Você perdeu suas tentivas")  
        print(msg6)
        
################################################  FUCAO PARA ADICIONAR AS PALAVRAS  ##############################################################

def adicionarPalvraEdica():
        palavra = input("Digite uma palavra: ")
        dica = input("Digite uma dica: ")
        dicionarioDePalavras.setdefault(palavra,dica) #adicionando no dicionário com a função de sedefault()
        print(dicionarioDePalavras)

        #Escrevendo no arquivo a lista de palavras atualizada
        with open('palavras.txt' , 'a') as arquivo:
            arquivo.write("Conteudo adicionado com Sucesso !!\n")
            arquivo.write(f"Lista de palavras atualizada: {dicionarioDePalavras}\n\n")
            arquivo.close


################################################  FUCAO PARA REMOVER AS PALaVRAS  ##############################################################

#Essa função é o menu onde o usuário será capaz de remover uma palvra


def removerPalavraEDica():
    try:
        print(dicionarioDePalavras)
        palavraExcluida = input("Escolha a palavra que será excluída: ")
        dicionarioDePalavras.pop(palavraExcluida)
        print(dicionarioDePalavras)

        #Escrevendo no arquivo a palavra que foi excluida e mostrando a lista []
        with open('palavras.txt' , 'a') as arquivo:
            arquivo.write(f"Palavra exlcluida: {palavraExcluida}\n" )
            arquivo.write(f"Lista de palavra agora: {dicionarioDePalavras}\n\n" )
            arquivo.close

    except:
        print('Digite corretamente')

################################################  FUNCAO MENU CHAMA AS OUTRAS FUNÇÕES   ##############################################################

#Essa função é o menu onde o usuário será capaz de escolher suas opções

def menu():
    
    f = open('./palavras.txt', 'w')

    while True:

        print(ms5)
        resposta = input("Digite um número")
        

        if resposta == "1":
            adicionarPalvraEdica()
        elif resposta == "2":
            removerPalavraEDica()
        elif resposta == "3":
            jogo()
        elif resposta == '4':
            print("Você saiu ...")
            break
        else:
            print("Digite corretamente ! ! !")



   
        # return dicionarioDePalavras





##################################################################################################################



menu()


# print(palavra)
# print(palavraEscondida)