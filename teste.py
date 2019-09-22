from Routeirizador import Router


obj = Router()

'''resultado = obj.ConsultaDistancia('CEP 74785240','Siagri')
print(resultado['distance']['value'])'''

obj.CalculaRotaComFinal('Goiania','Trindade',['Senador Canedo','Bonfinopolis','Terezopolis'])

