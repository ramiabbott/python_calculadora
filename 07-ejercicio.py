def no_space(text): 
    nuevo_texto = ""
    for char in text:
        if char != " ": 
            nuevo_texto += char
        return nuevo_texto
    
def es_palindromo(text):
    result = no_space(text)
