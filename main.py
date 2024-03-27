from encoder import enc

phrase = input('Choose a phrase to encode: ').upper()
phrase = phrase.replace(' ', '')
phrase += ' '

key = int(input('Choose the cipher key: '))
if key < 0:
    key = key * -1
elif key > 0:
    key = key * -1
    key += + 26

codif_phrase = enc(phrase, key)

nothing = ''

for i in range(len(codif_phrase)):
    teste = nothing + codif_phrase[i]
    nothing = teste

print(f'Your encoded phrase is: {teste}')
