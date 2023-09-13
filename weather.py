import requests

apiKey = "1091a6ac7fd857c4848b84c781f0a52e"

city = input("Coloque uma cidade: ")

link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang=pt_br"

requisicao = requests.get(link)
requisicaoDic = requisicao.json()
descricao = requisicaoDic['weather'][0]['description']
temperatura = requisicaoDic['main']['temp'] - 273.15
print(descricao ,f'{temperatura}'"°C")