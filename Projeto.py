import json

class Trilha:

    def __init__(self, data, final_file):
        self.final_file = final_file
        with open(data, 'r') as file:
            self.data = json.loads(file.read())


    # Exibindo os filmes presentes no arquivo:
    def questao_1(self):
        names_films = list()
        for movie in (self.data.get('data')).get('movies'):
            print(movie)
            names_films.append(movie)

        return names_films

    # Exibindo as séries presentes no arquivo:
    def questao_2(self):
        names_series = list()
        for serie in self.data['data']['series']:
            names_series.append(serie)

    def questao_3(self):
        maiorRate = ''
        rate = 0
        firstItem = True
        for ele in self.data['data'].values():
            for item in ele:
                if firstItem:
                    maiorRate = item['title']
                    rate = item['rating']
                    firstItem = False

                if item['rating'] > rate:
                    maiorRate = item['title']
                    rate = item['rating']

    # Listando os gêneros dos filmes e séries:
    def questao_4(self):
        genres = set()
        for ele in self.data['data'].values():
            for item in ele:
                genres.update(item['genres'])

    # Obtendo o número total de filmes e séries:

    def questao_5(self):
        num = 0
        for ele in self.data['data'].values():
            num += len(ele)