def main():

    originalText = getString("Digite o Texto: ").upper()
    selectedText = getString("Texto a Selecionar: ").upper()

    if selectedText in originalText:

        newText = getString("Novo Texto: ").upper()
        originalTextCaracters = getTextCaracters(originalText)
        selectedTextCaracters = getTextCaracters(selectedText)
        newTextCaracters = getTextCaracters(newText)

        index = getIndex(originalTextCaracters, selectedTextCaracters)
        selectedTextCaractersSize = getTextSize(selectedTextCaracters)

        finalText = getNewText(index, selectedTextCaractersSize, originalTextCaracters, newTextCaracters)

        print("\nTexto Original: %s" % originalText)
        print("Texto Selecionado: %s" % selectedText)
        print("Texto Final: %s" % finalText)
    else:

        print("Texto a selecionar nao existe no original")


def getIndex(originalTextCaracters, selectedTextCaracters):

    index = -1
    indexTemp = -1
    counter = 0
    isSequenceBroken = True

    selectedTextCaractersSize = getTextSize(selectedTextCaracters)
    originalTextCaractersSize = getTextSize(originalTextCaracters)

    while(True):

        for i in range(selectedTextCaractersSize):

            for j in range(indexTemp + 1, originalTextCaractersSize):

                if selectedTextCaracters[i] == originalTextCaracters[j] and index == -1:

                    index = j
                    indexTemp = j
                    counter += 1
                    isSequenceBroken = False
                    break
                elif (selectedTextCaracters[i] == originalTextCaracters[j]) and (j - 1 == indexTemp):

                    indexTemp = j
                    counter += 1
                    break
                else:

                    index = -1
                    indexTemp = j
                    counter = 0
                    isSequenceBroken = True
                    break

            if (isSequenceBroken):

                break
            if ((counter/float(selectedTextCaractersSize)) >= 0.74):

                return index


def getNewText(index, selectedTextCaractersSize, originalTextCaracters, newTextCaracters):

    newText = ""

    newTextCaractersSize = getTextSize(newTextCaracters)
    originalTextCaractersSize = getTextSize(originalTextCaracters)

    for i in range(index):

        newText += originalTextCaracters[i]

    for i in range(newTextCaractersSize):

        newText += newTextCaracters[i]

    indexTemp = index + selectedTextCaractersSize
    for i in range(indexTemp, originalTextCaractersSize):

        newText += originalTextCaracters[i]

    return newText



def getTextCaracters(text):

    textCaracters = []
    for caracter in text:
        textCaracters.append(caracter)

    return textCaracters


def getTextSize(text):

    size = 0
    for caracter in text:
        size += 1

    return size


def getString(msg):

    string = input(msg)

    if getTextSize(string) <= 0 or string.isspace():

        print("Erro! Entrada Vazia!")
        return getString(msg)
    else:
        return string


if __name__ == "__main__":
    main()