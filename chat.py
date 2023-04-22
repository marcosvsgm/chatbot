import openai
import openai_secret_manager

# Definir as credenciais da API
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# Função para enviar uma solicitação de conclusão para a API do ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Loop principal do chat bot
while True:
    user_input = input("Você: ")
    prompt = f"Usuário: {user_input}\nChatbot:"
    response = generate_response(prompt)
    print(f"Chatbot: {response}")
