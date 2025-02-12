def esconde_palavra(palavra: str, chutes: str) -> str:
    palavra_escondida = ""
    for letra in palavra:
        if letra in chutes:
            palavra_escondida = palavra_escondida + letra + " "
        else:
            palavra_escondida = palavra_escondida + "_ "
    return(palavra_escondida)

palavra = "abacateiro"
letras_chutadas = " "
erros = 0
segredo = esconde_palavra(palavra, letras_chutadas)

while "_" in segredo and erros < 6:
    print(segredo)
    print(f"erros {erros}")

    letra = input("Digite uma letra: ").lower()
    if not letra in palavra.lower(): 
        erros = erros + 1
    letras_chutadas = letras_chutadas + letra
    segredo = esconde_palavra(palavra, letras_chutadas)

if erros == 6:
    print(f"Perdeu! a palavra era {palavra}")
else:
    print("Parabéns!")
