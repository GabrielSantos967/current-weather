import requests
from tkinter import *

apiKey = "cb24804aca9b3a19690244edc902e4a8"
city = ""

def clima():
    global city
    city = entry.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang=pt_br"
    requisicao = requests.get(link)
    requisicaoDic = requisicao.json()
    descricao = requisicaoDic['weather'][0]['description']
    temperatura = requisicaoDic['main']['temp'] - 273.15
    texto = descricao, f'{round(temperatura, 1)}'"°C"
    L2["text"] = texto
    print(descricao, f'{round(temperatura, 1)}'"°C")

janela = Tk()
janela.title("Clima")
janela.geometry("250x400")
L1 = Label(janela, text="Coloque uma cidade", font=40)
L1.grid(row=0, column=1, padx=15)
L2 = Label(janela, text="", font=40)
L2.grid(row=3, column=1, padx=15, pady=20)
entry = Entry(janela)
entry.grid(row=1, column=1, padx= 15, pady=20)

botao = Button(janela, text="Pesquisar", command=clima, font=40)
botao.grid(row=2, column=1)
janela.mainloop()