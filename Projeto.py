import json

class Trilha:

    # Construtor que recebe um objeto 'data' e 'final_file', que serão os objetos que 
    # serão lidos e o que terá o conteúdo escrito
    def __init__(self, data, final_file):
        self.final_file = final_file
        self.data = data

    # Função para separar o espaço e organizar as questões
    def espaco(self):
        self.final_file.write('\n\n' + '=' * 100 + '\n\n')

    def questao_1(self):
        self.final_file.write('Exibindo os nomes dos filmes presentes no arquivo:\n\n')

        # Itera sobre cada filme, acessando os termos do JSON
        for movie in self.data.get('data', {}).get('movies'):
            self.final_file.write(f"\tNome do filme: {movie.get('title')}")

        self.espaco()

    def questao_2(self):
        self.final_file.write('Exibindo os nomes das series presentes no arquivo:\n\n')

        for serie in self.data.get('data', {}).get('series'):
            self.final_file.write(f"\tNome da serie: {serie.get('title')}")

        self.espaco()

    def questao_3(self):
        self.final_file.write('Exibindo o elemento de maior rating:\n\n')

        maiorRate = ''
        rate = -1

        # Itera sobre os elementos iniciais do dicionário
        for ele in self.data.get('data').values():
            # E aqui itera sobre cada item do array do dicionário inicial
            for item in ele:
                if item.get('rating') > rate:
                    maiorRate = item.get('title')
                    rate = item.get('rating')

        self.final_file.write(f"\tNome do elemento: {maiorRate}\n")
        self.final_file.write(f"\tRating: {rate}")

        self.espaco()

    def questao_4(self):
        self.final_file.write('Exibindo os generos presentes no JSON:\n\n')

        genres = set()

        # Isso vai iterar sobre cada array de gêneros de cada elemento e então adicionará eles no set
        for ele in self.data['data'].values():
            for item in ele:
                genres.update(item['genres'])

        self.final_file.write(f'\t{", ".join(genres)}')

        self.espaco()

    def questao_5(self):
        self.final_file.write('Exibindo a quantidade de filmes e series no JSON:\n\n')

        num_film = 0
        num_serie = 0

        # Itera sobre cada elemento do dicionário e mede o tamanho do array, pra saber a quantidade de filmes e séries
        num_film = len(self.data.get('data').get('movies', []))
        num_serie = len(self.data.get('data').get('series', []))

        self.final_file.write(f"\tNumero de filmes: {num_film}\n")
        self.final_file.write(f"\tNumero de series: {num_serie}")

        self.espaco()

with open('movies_and_series.json', 'r') as read:

    with open('result.txt', 'w') as write:

        obj = Trilha(json.load(read), write)

        obj.questao_1()
        obj.questao_2()
        obj.questao_3()
        obj.questao_4()
        obj.questao_5()