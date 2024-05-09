#I can run it at https://colab.research.google.com/

import requests
import random

#url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
url = 'https://raw.githubusercontent.com/ricardofluiz2024/alura-imersao-ia/main/words.json'

resposta = requests.get(url)
data = resposta.json()
#len(data)
#data[-1]

valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']

#print(f'A palavra secreta tem {len(palavra_secreta)} letras -> {dica}')

#receber o palpite da tecnologia
chute = input(f'A palavra secreta tem {len(palavra_secreta)} letras -> {dica}')

if chute == palavra_secreta:
  print(f'Isso mesmo, a palavra secreta é {palavra_secreta}')
else:
  print(f'Não, a palavra secreta é {palavra_secreta}')








