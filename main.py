import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet as wn
from difflib import get_close_matches
from nltk import pos_tag

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

def get_synonyms(word):
    synonyms = set(lemma.name() for syn in wn.synsets(word, lang='por') for lemma in syn.lemmas('por'))
    return synonyms

def semantic_similarity(user_input, keywords):
    user_words = word_tokenize(user_input)
    for word in user_words:
        close_matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if close_matches:
            return True
        synonyms = get_synonyms(word)
        if any(get_close_matches(syn, keywords, n=1, cutoff=0.8) for syn in synonyms):
            return True
    return False

def identify_intention(user_input):
    intentions = {
        'cidade favorita': ['paris', 'cidade favorita', 'cidade dos sonhos'],
        'moradia': ['são paulo', 'vive', 'moradia', 'mora', 'reside'],
        'trabalho': ['designer','trabalha', 'profissão', 'trabalho', 'emprego', 'carreira'],
        'hobbies': ['hobbies','diversao', 'finais de semana', 'cozinhar', 'passatempo', 'atividades'],
        'cachorro': ['cachorro','bichinho', 'pet', 'animal de estimação', 'max'],
        'música': ['música','escuta','escutar', 'concerto', 'música clássica', 'instrumento'],
        'viagem': ['viagem', 'viagens', 'turismo', 'destino favorito'],
        'família': ['família', 'pais', 'parentes', 'unida', 'família dela'],
        'filmes': ['filmes','assistir', 'cinema', 'suspense', 'hitchcock', 'diretor'],
        'comida favorita': ['comida favorita','comer', 'prato favorito', 'lasanha', 'receita', 'culinária'],
        'esportes': ['esportes', 'tênis', 'futebol', 'atividade física', 'jogar'],
        'livros': ['livros','ler', 'leitura', 'autores favoritos', 'agatha christie', 'gabriel garcía márquez'],
        'tecnologia': ['tecnologia', 'inovações', 'novidades tecnológicas', 'ferramentas digitais', 'design gráfico'],
        'arte': ['arte','cultura', 'galeria', 'pintura', 'expressionismo', 'desenho', 'artista'],
    }

    for intention, keywords in intentions.items():
        if semantic_similarity(user_input, keywords):
            return intention
    return None

def decision_tree(intention):
    responses = {
        'cidade favorita': "Maria adora Paris. Ela passou um mês lá explorando museus e cafés.",
        'moradia': "Maria vive em São Paulo, uma das cidades mais vibrantes do Brasil.",
        'trabalho': "Maria trabalha como designer gráfica e ama arte moderna.",
        'hobbies': "Nos finais de semana, Maria gosta de fazer caminhadas e experimentar novas receitas na cozinha.",
        'cachorro': "Maria tem um cachorro chamado Max, que adora correr no parque.",
        'música': "Maria é uma grande fã de música clássica e vai frequentemente a concertos com sua família.",
        'viagem': "Maria é apaixonada por viagens, e seu destino favorito foi Paris.",
        'família': "Maria tem uma família muito unida e gosta de passar tempo com eles aos domingos.",
        'filmes': "Maria adora filmes de suspense, especialmente os dirigidos por Alfred Hitchcock.",
        'comida favorita': "O prato favorito de Maria é lasanha, e ela adora preparar para seus amigos.",
        'esportes': "Maria joga tênis aos finais de semana e é muito competitiva.",
        'livros': "Maria é uma ávida leitora, e seus autores favoritos são Agatha Christie e Gabriel García Márquez.",
        'tecnologia': "Maria está sempre antenada com as últimas novidades em tecnologia, especialmente no design gráfico digital.",
        'arte': "Maria ama visitar galerias de arte e desenha nas horas vagas. Seu estilo preferido é o expressionismo."
    }
    
    return responses.get(intention, "Desculpe, não entendi sua pergunta.")

def chatbot():
    print("Olá! Eu sou o chatbot. Pergunte-me sobre Maria e eu tentarei responder com base na história dela.")
    
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input in ['sair', 'exit', 'quit']:
            print("Chatbot: Até mais!")
            break

        intention = identify_intention(user_input)
        
        response = decision_tree(intention)
        print(f"Chatbot: {response}")

chatbot()
