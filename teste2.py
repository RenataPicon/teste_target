def contar_letra_a(texto):
    texto = texto.lower()
    quantidade_a = texto.count('a')
    existe_a = quantidade_a > 0
    return existe_a, quantidade_a

texto_usuario = input("Digite uma string para verificar a presença da letra 'a': ")
existe, quantidade = contar_letra_a(texto_usuario)

if existe:
    print(f"A letra 'a' (ou 'A') aparece {quantidade} vez(es) na string.")
else:
    print("A letra 'a' (ou 'A') não aparece na string.")
