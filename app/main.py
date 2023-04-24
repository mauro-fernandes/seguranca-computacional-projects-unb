from utils import *

entrada = "CYBERSECURITY"
chave = "BEST"


# Texto cifrado esperado: DCTXSWWVVVAMZ

#########################################################################
# Referências :::::::::::>
# https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Examples.html
# https://www.geeksforgeeks.org/vigenere-cipher/
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# https://intellipaat.com/blog/vigenere-cipher/
#########################################################################

# Método para gerar a chave completa
def generate_key_with_the_same_size_of_input(input_text, key):
    if does_cipher_key_has_the_same_size_of_input_text(input_text, key):
        return key
    else:
        while True:
            key += key
            if len(key) > len(input_text):
                break

    return key[:len(input_text)]


# Método para cifrar o texto
def generate_ciphed_text(input_text, key):
    result_text = ""
    for index in range(len(input_text)):
        decimal_asc_ii_position = find_character_position_for_cipher(index, input_text, key)
        result_text += chr(decimal_asc_ii_position)

    return result_text


# Método para decifrar o texto
def generate_original_text(input_text, key):
    result_text = ""
    for index in range(len(input_text)):
        decimal_asc_ii_position = find_character_position_for_original_text(index, input_text, key)
        result_text += chr(decimal_asc_ii_position)

    return result_text


if __name__ == '__main__':
    generated_key = generate_key_with_the_same_size_of_input(entrada, chave)
    ciphed_text = generate_ciphed_text(entrada, generated_key)
    original_text = generate_original_text(ciphed_text, generated_key)
    print('Testing ::::::::::::::> CIPHER -> ' + ciphed_text)
    print('Testing ::::::::::::::> ORIGINAL -> ' + original_text)
