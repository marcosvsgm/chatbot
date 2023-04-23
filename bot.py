from twilio.rest import Client 
from flask import Flask, request
import requests
import sqlite3

app = Flask(__name__)

# configurações da Twilio
account_sid = 'SK992d28de2ce4c19b9e96016355c08892'
auth_token = 'zg2g68fTPv6OY43c9iKk5u4YfPzZAifY'
client = Client(account_sid, auth_token)

# rota para receber as mensagens do WhatsApp
@app.route('/bot', methods=['POST'])
def bot():
    # obtém o número do remetente e a mensagem recebida
    from_number = request.form['From']
    message = request.form['Body']

    # envia uma resposta automática
    if message.lower() == 'oi':
        response_text = 'Olá, como posso ajudar?'
    elif message.lower() == 'previsão do tempo':
        # faz uma requisição para a API do OpenWeatherMap
        api_key = 'zg2g68fTPv6OY43c9iKk5u4YfPzZAifY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q=Rio+de+Janeiro,BR&appid={api_key}'
        response = requests.get(url).json()
        temperature = round(response['main']['temp'] - 273.15, 2)
        description = response['weather'][0]['description']
        response_text = f'No momento, faz {temperature} graus em Rio de Janeiro e o tempo está {description}.'
    else:
        response_text = 'Desculpe, não entendi o que você quis dizer. Tente novamente.'

    # envia a resposta para o remetente
    message = client.messages.create(
        from_='whatsapp:+5596991117995', 
        to=f'whatsapp:{from_number}',
        body=response_text)

    return '', 200

# roda o servidor Flask
if __name__ == '__main__':
    app.run()
    
    
    # configurações do banco de dados SQLite
conn = sqlite3.connect('chatbot.db')
c = conn.cursor()

# rota para receber as mensagens do WhatsApp
@app.route('/bot', methods=['POST'])
def bot():
    # obtém o número do remetente e a mensagem recebida
    from_number = request.form['From']
    message = request.form['Body']
    message_time = request.form['Timestamp']

    # salva as informações do usuário no banco de dados
    c.execute('INSERT INTO users (phone_number, message_time) VALUES (?, ?)', (from_number, message_time))
    conn.commit()

    # ...

# rota para listar as informações dos usuários
@app.route('/users')
def users():
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    return {'users': users}
