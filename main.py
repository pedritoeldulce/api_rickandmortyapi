# Vamos a consultar los datos de los primeros 10 personajes de la API
##  de estos vamos a mostrar solo los personajes que estan vivos en una lista
### campos: name, status: alive

import requests

## API de personajes
#url = 'https://rickandmortyapi.com/api/character/2'


data = []
for n in range(1,11):
   
    URL = 'https://rickandmortyapi.com/api/character/{}'.format(n)
    resp = requests.get(URL).json()

    # creamos una diccionario
    a={
        'name':resp['name'],
        'status':resp['status']
    }
    # agregamos el diccionario al final de la lista vacìa
    data.append(a)

# mostramos la lista con los primeros 10 personajes   
##print(data)

## iterar la lista data y mostrar guardarlos en lista de:(alive, dead y unknoum)

alive=[]
dead = []
unknoum=[]

for p in data:
    if p['status'] == 'Alive':
       alive.append(p['name'])
    elif p['status'] == 'Dead':
        dead.append(p['name'])
    else:    
        unknoum.append(p['name'])

print("Vivos: ")
print(alive)
print("Muertos: " )
print(dead)
print("Desconocido: " )
print(unknoum)




