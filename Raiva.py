import spacy


# Carregar o modelo de idioma inglês do spaCy
nlp = spacy.load("en_core_web_sm")

# Dicionário de respostas para diferentes palavras-chave
responses = {
    "greetings": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm here to help.",
    "help": "Sure, I'm here to assist. What do you need help with?",
    "weather": "I'm unable to check the weather currently, but you can try a weather app!"
}

# Função para analisar a entrada do usuário e responder
def generate_response(user_input):
    doc = nlp(user_input.lower())  # Analisar o texto em minúsculas para consistência
    
    # Definir uma resposta padrão caso nenhuma palavra-chave seja encontrada
    default_response = "I'm not sure how to respond to that. Can you ask something else?"

    # Verificar palavras-chave no texto
    for token in doc:
        if token.lemma_ in responses:
            return responses[token.lemma_]
    
    # Caso nenhuma palavra-chave corresponda, retorna a resposta padrão
    return default_response

# Loop principal do chatbot
def chatbot():
    print("Chatbot: Hi! I am here to help you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

# Iniciar o chatbot
if __name__ == "__main__":
    chatbot()

