alphabetic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

codif_list = []


def enc(phrase, key):
    codif_phrase = []
    for i in phrase:
        if i == ' ' in phrase:
            for item in codif_list:
                codif_phrase.append(item)
        elif i in alphabetic:
            index = alphabetic.index(i)
            value = index - key
            codif_list.append(i.replace(i, alphabetic[value]))
    return codif_phrase
