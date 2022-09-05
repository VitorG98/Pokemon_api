import requests

def pegar_infos(poke):
    print(f'Habilidades do {pokemon}')
    for i in poke['abilities']:
        print(i['ability']['name'])

def pegar_forma(poke):
    print(f'Formas do {pokemon}:')
    for i in poke['forms']:
        print(i['name'])

def pegar_type(poke):
    print(f'O {pokemon} é do tipo:')
    for i in poke['types']:
        print(i['type']['name'])

def buscar_dados():
    global pokemon
    pokemon = str(input('Digite o nome do pokemon: '))
    api =f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    res = requests.get(api)
    poke = res.json()
    pegar_infos(poke)
    pegar_type(poke)
    pegar_forma(poke)

if __name__ == "__main__":
    buscar_dados()