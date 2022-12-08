import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
 


def hangman():
    word = get_valid_word(words)
    letras= set(words) # Guarda las letras de la palabra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set() #Va registrando las letras que va adivinando el usuario


    lives = 6

    #Entrada Usuario

    while len(letras) > 0 and lives > 0:
        print( 'TIENES', lives, 'VIDAS', 'HAS USADO ESTAS LETRAS: ', ' '.join(letras_usadas))
        lista_letras= [letra if letra in letras_usadas else '-' for letra in word]
    
        print('PALABRA ACTUAL: ', ' '.join(lista_letras))
        letras_ingresadas = input('INGRESE UNA LETRA: ').upper()  
        if letras_ingresadas in alfabeto - letras_usadas:
            letras_usadas.add(letras_ingresadas)
            if letras_ingresadas in letras:
                letras.remove(letras_ingresadas)
                print(' ')
           
            else:
                lives = lives - 1
                print('LA LETRA,', letras_ingresadas, 'NO ESTA EN LA PALABRA')
    
        elif letras_ingresadas in letras_usadas:
            print("YA USO ESTA LETRA")
        
        else:   
            print("LETRA INVALIDA")
    
    if lives == 0:
        print("HAS PERDIDO")
    else:
        print("HAS ADIVINADO LA PALABRA")




if __name__ == '__main__':
    hangman()









