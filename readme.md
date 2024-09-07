# Projeto: Chatbot Baseado em Semântica - História de Maria

## Descrição

Este projeto consiste em um **chatbot** capaz de responder perguntas sobre a história fictícia de Maria, com base em um texto previamente fornecido. O chatbot utiliza técnicas de **processamento de linguagem natural (NLP)** e **similaridade semântica** para identificar palavras-chave nas perguntas do usuário e fornecer respostas relevantes sobre a vida de Maria, seus hobbies, preferências e outros aspectos de sua biografia.

O projeto usa bibliotecas da **NLTK (Natural Language Toolkit)** para tokenização, remoção de stopwords, e busca de sinônimos, além de utilizar a função `get_close_matches` da biblioteca `difflib` para identificar correspondências aproximadas de palavras.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **NLTK (Natural Language Toolkit)**: Biblioteca para processamento de linguagem natural.
  - `nltk.tokenize.word_tokenize`: Para tokenização de palavras.
  - `nltk.corpus.stopwords`: Para eliminação de palavras irrelevantes.
  - `nltk.corpus.wordnet`: Para busca de sinônimos.
  - `nltk.download`: Para baixar pacotes necessários (stopwords, wordnet, etc).
- **Difflib**: Usado para encontrar correspondências aproximadas de palavras (fuzzy matching).

## Instalação

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/usuario/chatbot-maria.git
   ```

2. Instale as dependências do projeto (certifique-se de que tem o Python instalado):
   ```bash
   pip install nltk
   ```

3. Baixe os recursos necessários da biblioteca NLTK:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('rslp')
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   ```

## Estrutura do Código

- **Texto da história**: Um texto detalhado sobre Maria é usado como a base de conhecimento do chatbot. As perguntas dos usuários são relacionadas a este texto.

- **Função `get_synonyms(word)`**: Busca sinônimos em português utilizando o WordNet. Para cada palavra fornecida, a função retorna um conjunto de sinônimos.

- **Função `semantic_similarity(user_input, keywords)`**: Verifica se a entrada do usuário contém palavras-chave ou seus sinônimos utilizando uma abordagem de similaridade semântica. Ela faz correspondência aproximada (fuzzy matching) para garantir que variações de palavras ainda sejam compreendidas pelo chatbot.

- **Chatbot (`chatbot()`)**: Função principal do chatbot que processa a entrada do usuário, analisa se as perguntas estão relacionadas às informações do texto e responde adequadamente. O chatbot segue um loop que pode ser encerrado com os comandos `sair`, `exit`, ou `quit`.

## Exemplo de Uso

1. **Iniciar o chatbot**:
   Após executar o código, o chatbot iniciará, e você verá o prompt:
   ```
   Olá! Eu sou o chatbot. Pergunte-me sobre Maria e eu tentarei responder com base na história dela.
   ```

2. **Entrada do usuário**:
   Digite sua pergunta, como:
   ```
   Você: Qual é a cidade favorita de Maria?
   ```

3. **Resposta do chatbot**:
   O chatbot responderá com base na semântica da pergunta:
   ```
   Chatbot: Maria adora Paris. Ela passou um mês lá explorando museus e cafés.
   ```

4. Para sair, basta digitar `sair`, `exit` ou `quit`.

## Funcionalidades

- **Processamento semântico**: O chatbot é capaz de identificar perguntas com diferentes variações semânticas, como sinônimos e correspondências aproximadas.
- **Suporte ao idioma português**: O chatbot foi projetado para funcionar em português, utilizando pacotes do NLTK específicos para a língua.

## Licença

Este projeto está sob a licença [MIT License](LICENSE).

## Contato

Para perguntas ou feedback, entre em contato através de [email@example.com](mailto:email@example.com).