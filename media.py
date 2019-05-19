import json

def Soma():
    soma = 0
    med = 0

    with open('person.json', 'r') as f:#lendo as notas n arquivo json
        data = f.read()
        apod_data = json.loads(data)

        soma = sum(apod_data['notas'])#soma as notas dentro arquivo json

        med = soma / len(apod_data['notas'])#media da nota 
        return med
        
