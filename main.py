import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords

# Baixar os recursos necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

# Texto que conta a história de alguém
text = """
Maria é uma jovem que vive em São Paulo. Ela adora viajar e conhecer novos lugares. Sua cidade favorita é Paris, onde ela passou um mês explorando museus e cafés. Maria trabalha como designer gráfica e tem um amor especial por arte moderna. Ela gosta de passar os finais de semana fazendo caminhadas e experimentando novas receitas na cozinha. Além disso, Maria é uma grande fã de música clássica e frequentemente vai a concertos com sua família. Ela tem um cachorro chamado Max que adora correr no parque.
"""

# Função para processar o texto
def process_text(text):
    # Tokenização em sentenças
    sentences = sent_tokenize(text)

    # Tokenização em palavras
    words = word_tokenize(text)

    # Remover stop words
    stop_words = set(stopwords.words('portuguese'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Stemming
    stemmer = RSLPStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    return {
        'sentences': sentences,
        'words': words,
        'filtered_words': filtered_words,
        'stemmed_words': stemmed_words
    }

# Função do chatbot
def chatbot():
    print("Olá! Eu sou o chatbot. Pergunte-me sobre Maria e eu tentarei responder com base na história dela.")
    
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input in ['sair', 'exit', 'quit']:
            print("Chatbot: Até mais!")
            break

        # Árvore de decisão simples para responder às perguntas
        if 'são paulo' in user_input:
            response = "Maria vive em São Paulo."
        elif 'paris' in user_input:
            response = "Maria adora Paris. Ela passou um mês lá explorando museus e cafés."
        elif 'trabalho' in user_input or 'design' in user_input:
            response = "Maria trabalha como designer gráfica e ama arte moderna."
        elif 'final de semana' in user_input:
            response = "Nos finais de semana, Maria gosta de fazer caminhadas e experimentar novas receitas."
        elif 'música clássica' in user_input:
            response = "Maria é uma grande fã de música clássica e vai frequentemente a concertos."
        elif 'cachorro' in user_input:
            response = "Maria tem um cachorro chamado Max que adora correr no parque."
        elif 'história' in user_input:
            response = "Maria é uma jovem que vive em São Paulo. Ela adora viajar e tem um amor especial por arte moderna e música clássica."
        else:
            response = "Desculpe, não entendi sua pergunta. Pode perguntar sobre a história de Maria, seus gostos ou onde ela vive?"

        print(f"Chatbot: {response}")

# Iniciar o chatbot
chatbot()
