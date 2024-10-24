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


##################################################################################################################

print(jogoDaForca)

palavra = "VERMELHO" #palavraEscolhida
palavraEscondida = '' #Aqui ficara a palavra escolhida codificada
contadorDeAsteristicos = 0 #contador de asteristicos
palvrasQueJAforam = []



for i in palavra: # iterando sobre a palavra e escondendo ela
    palavraEscondida+= "*"

palavraEscondida = list(palavraEscondida) #Transoformando a palavraEscondida em uma lista 
palavra = list(palavra.lower()) #deixando as letras todas as letras minúsculas em uma lista 


tentativas = 6

while tentativas > 0:
    
    
    print("DICA: COR")
    palavraDoUsuario = input("Digite uma letra: ")

    palvrasQueJAforam.append(palavraDoUsuario)
    
    print(F"Essas letras ja foram: {palvrasQueJAforam}")

    if  palavraDoUsuario.lower() in palavra: #Se a letra do usuario estiver na lista palavra correta
        
        for letra in range(len(palavra)): #O for irá iterar a palavra para descobrir onde e a posicao da letra do meu usuario está
            if palavraDoUsuario == palavra[letra]: 
                palavraEscondida[letra] = palavraDoUsuario #Atribuindo a letra presente na palavra correta na [] de palavra escondida 
        print(*palavraEscondida)
        
    else:
        tentativas-=1
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
    
    if contadorDeAsteristicos == 0: #Se não tiver * o jogo acaba !
        print('Acertou a palavra')
        break

    
    contadorDeAsteristicos = 0
    

        
else:
    print("Você perdeu suas tentivas")  
    print(msg6)
    



