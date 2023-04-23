# rota para enviar as respostas para as perguntas frequentes
@app.route('/faq', methods=['POST'])
def faq():
    # obtém a pergunta do usuário
    message = request.form['Body']

    # verifica se a pergunta está no banco de dados
    c.execute('SELECT * FROM faqs WHERE question = ?', (message,))
    faq = c.fetchone()

    # envia a resposta correspondente
    if faq:
        response_text = faq[1]
    else:
        response_text = 'Desculpe, não entendi o que você quis dizer. Tente novamente.'

    # envia a resposta para o remetente
    message = client.messages.create(
        from_='whatsapp:+14155238886', 
        to=f'whatsapp:{from_number}',
        body=response_text)

    return '', 200
