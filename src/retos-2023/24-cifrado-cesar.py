### Reto #24: CIFRADO CÉSAR
### Publicación: 12/06/23 | FÁCIL

#Crea un programa que realize el cifrado César de un texto y lo imprima.
#También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#
#Te recomiendo que busques información para conocer en profundidad cómo realizar el cifrado. 
#Esto también forma parte del reto.

import random

class CeaseEncrypt:
    __displacement: int = 0
    __alphabet: list = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
    __alphabet_encrypted: dict = dict()
    __alphabet_decrypted: dict = dict()

    def __init__(self, displacement: int = 0):
        if displacement == 0:
            self.__displacement = self.__get_random_displacement()
        else:
            alphabet_size = len(self.__alphabet)
            self.__displacement = 1 if displacement < 0 else alphabet_size if displacement > alphabet_size else displacement
        self.__encrypt_alphabet()

    def __get_random_displacement(self) -> int: 
        return random.choice(range(len(self.__alphabet)))
    
    def displacement(self) -> int:
        return self.__displacement

    def __encrypt_alphabet(self) -> list():
        self.__alphabet_encrypted = dict()
        self.__alphabet_decrypted = dict()
        alphabet_size = len(self.__alphabet)
        for index in range(alphabet_size):
            new_index = index + self.__displacement
            key = self.__alphabet[index]
            if new_index < alphabet_size:
                value = self.__alphabet[new_index]
            else:
                value = self.__alphabet[new_index-alphabet_size]

            self.__alphabet_encrypted[key] = value
            self.__alphabet_decrypted[value] = key
    
    def encrypt(self, text: str) -> str:
        return self.__process(self.__alphabet_encrypted, text)

    def decrypt(self, text: str) -> str:
        return self.__process(self.__alphabet_decrypted, text)

    def __process(self, alphabet: dict, text: str) -> str:
        result = list()
        for letter in text.upper():
            letter_encrypted = alphabet.get(letter)
            result.append(letter_encrypted if letter_encrypted is not None else letter)
        return "".join(result)


if __name__ == '__main__':
    print('Reto #24: CIFRADO CÉSAR')
    print('Publicación: 12/06/23 | FÁCIL\n')

    # prueba con un desplazamiento random
    text = "El mañana nunca muere"
    ceaseEncrypt = CeaseEncrypt()
    displacement = ceaseEncrypt.displacement()
    text_encrypted = ceaseEncrypt.encrypt(text)
    print(text_encrypted)
    text_decrypted = ceaseEncrypt.decrypt(text_encrypted)
    print(text_decrypted)

    print()

    # prueba con un desplazamiento especifico
    ceaseEncrypt = CeaseEncrypt(displacement)
    text_encrypted = ceaseEncrypt.encrypt(text)
    print(text_encrypted)
    text_decrypted = ceaseEncrypt.decrypt(text_encrypted)
    print(text_decrypted)
