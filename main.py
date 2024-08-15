import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet as wn
from difflib import get_close_matches

# Baixar os recursos necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Texto que conta a história de alguém
text = """
Maria é uma jovem que vive em São Paulo. Ela adora viajar e conhecer novos lugares. Sua cidade favorita é Paris, onde ela passou um mês explorando museus e cafés. Maria trabalha como designer gráfica e tem um amor especial por arte moderna. Ela gosta de passar os finais de semana fazendo caminhadas e experimentando novas receitas na cozinha. Além disso, Maria é uma grande fã de música clássica e frequentemente vai a concertos com sua família. Ela tem um cachorro chamado Max que adora correr no parque.
"""

# Função para encontrar sinônimos em português
def get_synonyms(word):
    synonyms = set(lemma.name() for syn in wn.synsets(word, lang='por') for lemma in syn.lemmas('por'))
    return synonyms

# Função de similaridade semântica e correspondência de palavras próximas
def semantic_similarity(user_input, keywords):
    user_words = word_tokenize(user_input)
    for word in user_words:
        # Verificar correspondências aproximadas e sinônimos
        close_matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if close_matches:
            return True
        synonyms = get_synonyms(word)
        if any(get_close_matches(syn, keywords, n=1, cutoff=0.8) for syn in synonyms):
            return True
    return False

# Função do chatbot aprimorado
def chatbot():
    print("Olá! Eu sou o chatbot. Pergunte-me sobre Maria e eu tentarei responder com base na história dela.")
    
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input in ['sair', 'exit', 'quit']:
            print("Chatbot: Até mais!")
            break

        if 'cidade favorita' in user_input or semantic_similarity(user_input, ['paris', 'frança', 'cidade', 'favorita']):
            response = "Maria adora Paris. Ela passou um mês lá explorando museus e cafés."
        elif 'moradia' in user_input or semantic_similarity(user_input, ['são paulo', 'cidade', 'moradia', 'mora', 'vive']):
            response = "Maria vive em São Paulo, uma das cidades mais vibrantes do Brasil."
        elif 'trabalho' in user_input or 'design' in user_input or semantic_similarity(user_input, ['trabalho', 'profissão', 'designer']):
            response = "Maria trabalha como designer gráfica em uma agência de publicidade em São Paulo e ama arte moderna."
        elif 'finais de semana' in user_input or semantic_similarity(user_input, ['finais de semana', 'final de semana', 'atividade', 'hobby']):
            response = "Nos finais de semana, Maria gosta de fazer caminhadas em trilhas e experimentar novas receitas na cozinha."
        elif 'música clássica' in user_input or semantic_similarity(user_input, ['música', 'clássica', 'concerto']):
            response = "Maria é uma grande fã de música clássica e vai frequentemente a concertos com sua família."
        elif 'cachorro' in user_input or semantic_similarity(user_input, ['cachorro', 'animal', 'pet']):
            response = "Maria tem um cachorro chamado Max, um golden retriever que adora correr no parque."
        elif 'história' in user_input or semantic_similarity(user_input, ['história', 'biografia']):
            response = "Maria é uma jovem que vive em São Paulo. Ela adora viajar, ama arte moderna e música clássica, e tem um cachorro chamado Max."
        elif 'viagens' in user_input or semantic_similarity(user_input, ['viagens', 'viajar', 'turismo']):
            response = "Maria é apaixonada por viagens e seu destino favorito até hoje foi Paris, onde passou um mês inteiro."
        elif 'família' in user_input or semantic_similarity(user_input, ['família', 'pais', 'irmã']):
            response = "Maria é muito próxima de sua família, especialmente de sua irmã mais nova, Clara, que é sua melhor amiga."
        elif 'voluntariado' in user_input or semantic_similarity(user_input, ['voluntariado', 'social', 'ajuda']):
            response = "Maria dedica parte de seu tempo livre ao voluntariado em um abrigo para mulheres vítimas de violência doméstica."
        elif 'futuro' in user_input or semantic_similarity(user_input, ['futuro', 'sonhos', 'planos']):
            response = "No futuro, Maria sonha em abrir seu próprio estúdio de design e conhecer mais lugares ao redor do mundo."
        elif 'livros' in user_input or semantic_similarity(user_input, ['livros', 'leitura', 'literatura']):
            response = "Maria adora ler e seus gêneros favoritos são ficção científica e romances históricos."
        elif 'cozinhar' in user_input or semantic_similarity(user_input, ['cozinhar', 'culinária', 'receitas']):
            response = "Maria gosta de cozinhar pratos internacionais e experimentar receitas novas."
        elif 'arte' in user_input or semantic_similarity(user_input, ['arte', 'pintura', 'escultura']):
            response = "Maria é apaixonada por arte moderna e frequentemente visita galerias e museus."
        elif 'esportes' in user_input or semantic_similarity(user_input, ['esportes', 'atividade física', 'ginástica']):
            response = "Maria gosta de praticar yoga e corridas leves para manter-se saudável."
        elif 'filmes' in user_input or semantic_similarity(user_input, ['filmes', 'cinema', 'séries']):
            response = "Maria é fã de filmes de suspense e adora maratonar séries na Netflix."
        elif 'tecnologia' in user_input or semantic_similarity(user_input, ['tecnologia', 'gadgets', 'inovações']):
            response = "Maria está sempre atualizada com as últimas tendências em tecnologia e gadgets."
        elif 'natureza' in user_input or semantic_similarity(user_input, ['natureza', 'ambiental', 'ecologia']):
            response = "Maria aprecia a natureza e gosta de fazer trilhas em parques naturais."
        elif 'viagem dos sonhos' in user_input or semantic_similarity(user_input, ['viagem dos sonhos', 'destino dos sonhos']):
            response = "Maria sonha em visitar o Japão para conhecer a cultura e a culinária local."
        elif 'festivais' in user_input or semantic_similarity(user_input, ['festivais', 'eventos', 'celebrações']):
            response = "Maria gosta de participar de festivais de música e eventos culturais em São Paulo."
        elif 'estilo de vida' in user_input or semantic_similarity(user_input, ['estilo de vida', 'rotina']):
            response = "Maria leva um estilo de vida equilibrado, combinando trabalho, lazer e atividades ao ar livre."
        elif 'séries' in user_input or semantic_similarity(user_input, ['séries', 'programas de TV']):
            response = "Maria adora séries de mistério e drama, e sempre tem uma nova recomendação."
        elif 'hobbies' in user_input or semantic_similarity(user_input, ['hobbies', 'passatempos']):
            response = "Além de cozinhar e ler, Maria gosta de jardinagem e fotografia."
        elif 'café' in user_input or semantic_similarity(user_input, ['café', 'cafeteria']):
            response = "Maria é fã de café e costuma visitar novas cafeterias em São Paulo."
        elif 'educação' in user_input or semantic_similarity(user_input, ['educação', 'formação', 'estudos']):
            response = "Maria tem uma formação em design gráfico e continua estudando para aprimorar suas habilidades."
        elif 'compras' in user_input or semantic_similarity(user_input, ['compras', 'lojas']):
            response = "Maria gosta de fazer compras em boutiques locais e lojas de design."
        elif 'sol' in user_input or semantic_similarity(user_input, ['sol', 'tempo', 'clima']):
            response = "Maria aprecia dias ensolarados e costuma aproveitar o clima para passeios ao ar livre."
        elif 'música pop' in user_input or semantic_similarity(user_input, ['música pop', 'pop']):
            response = "Maria também curte música pop e costuma acompanhar as últimas tendências no gênero."
        elif 'passeios' in user_input or semantic_similarity(user_input, ['passeios', 'explorar']):
            response = "Maria adora explorar novos lugares e descobrir atrações turísticas locais."
        elif 'filmes de animação' in user_input or semantic_similarity(user_input, ['filmes de animação', 'animação']):
            response = "Maria é fã de filmes de animação e gosta de assistir tanto produções clássicas quanto novas."
        elif 'história de vida' in user_input or semantic_similarity(user_input, ['história de vida', 'biografia']):
            response = "Maria tem uma trajetória inspiradora, combinando carreira criativa com atividades altruístas."
        elif 'organização' in user_input or semantic_similarity(user_input, ['organização', 'planejamento']):
            response = "Maria é bastante organizada e planeja suas atividades para manter um bom equilíbrio entre trabalho e lazer."
        elif 'mudanças' in user_input or semantic_similarity(user_input, ['mudanças', 'transformações']):
            response = "Maria está aberta a mudanças e sempre busca novas oportunidades de crescimento pessoal e profissional."
        elif 'relacionamentos' in user_input or semantic_similarity(user_input, ['relacionamentos', 'amizades']):
            response = "Maria valoriza muito seus relacionamentos e está sempre em contato com amigos e familiares."
        elif 'praia' in user_input or semantic_similarity(user_input, ['praia', 'litoral']):
            response = "Maria gosta de visitar a praia nos fins de semana para relaxar e tomar sol."
        elif 'leitura' in user_input or semantic_similarity(user_input, ['leitura', 'livros']):
            response = "Maria gosta de leitura, especialmente de ficção e biografias inspiradoras."
        elif 'natureza' in user_input or semantic_similarity(user_input, ['natureza', 'ambiental']):
            response = "Maria aprecia a natureza e gosta de fazer caminhadas em parques e reservas naturais."
        elif 'trabalho voluntário' in user_input or semantic_similarity(user_input, ['trabalho voluntário', 'serviço']):
            response = "Maria realiza trabalho voluntário em várias causas sociais, ajudando a comunidade local."
        elif 'férias' in user_input or semantic_similarity(user_input, ['férias', 'descanso']):
            response = "Maria usa suas férias para viajar e explorar novos destinos ao redor do mundo."
        elif 'fotografia' in user_input or semantic_similarity(user_input, ['fotografia', 'câmera']):
            response = "Maria é apaixonada por fotografia e adora capturar momentos especiais com sua câmera."
        elif 'museus' in user_input or semantic_similarity(user_input, ['museus', 'exposições']):
            response = "Maria frequentemente visita museus e exposições para se inspirar e aprender mais sobre arte."
        elif 'música ao vivo' in user_input or semantic_similarity(user_input, ['música ao vivo', 'shows']):
            response = "Maria gosta de assistir a shows e eventos de música ao vivo sempre que pode."
        elif 'teatro' in user_input or semantic_similarity(user_input, ['teatro', 'drama']):
            response = "Maria aprecia peças de teatro e costuma ir a produções dramáticas e comédias."
        else:
            response = "Desculpe, não entendi sua pergunta. Pode perguntar sobre a história de Maria, seus gostos ou onde ela vive?"
            
        print(f"Chatbot: {response}")

# Iniciar o chatbot
chatbot()
