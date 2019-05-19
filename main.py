import json
import media
with open('person.json', 'r') as f:
     data = f.read()

apod_data = json.loads(data)


print("")
print("Data da avaliação : ", apod_data['date'])
print("Nome: " ,apod_data['nome'])
print("Cidade: ",apod_data['city'])
print("Telefone : " ,apod_data['tel'])
print("E-mail : " ,apod_data['email'])
print("Media obtida: ", media.Soma())