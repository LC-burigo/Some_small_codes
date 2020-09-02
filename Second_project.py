import requests
from bs4 import BeautifulSoup
from csv import writer

films_per_year = {1950: [], 1951: [], 1952: [], 1953: [], 1954: [], 1955: [], 1956: [], 1957: [], 1958: [], 1959: [], 1960: [], 1961: [], 1962: [], 1963: [], 1964: [], 1965: [], 1966: [], 1967: [], 1968: [], 1969: [], 1970: [], 1971: [], 1972: [], 1973: [], 1974: [], 1975: [], 1976: [], 1977: [], 1978: [], 1979: [], 1980: [], 1981: [], 1982: [], 1983: [], 1984: [], 1985: [], 1986: [], 1987: [], 1988: [], 1989: [], 1990: [], 1991: [], 1992: [], 1993: [], 1994: [], 1995: [], 1996: [], 1997: [], 1998: [], 1999: [], 2000: [], 2001: [], 2002: [], 2003: [], 2004: [], 2005: [], 2006: [], 2007: [], 2008: [], 2009: [], 2010: [], 2011: [], 2012: [], 2013: [], 2014: [], 2015: [], 2016: [], 2017: [], 2018: [], 2019: [], 2020: []}

# fazer a conexão com a página
connection_url = requests.get("http://serieszoiudo.blogspot.com/p/lista-de-filmes_4.html")
# Acessar a parte html da página
html_content = BeautifulSoup(connection_url.text, "html.parser")
# pegar as etiquetas onde estão contidas as listas de filmes e colocá-las em uma variável
html_films = html_content.find_all(id="post-body-3825210740813673476")
#gerar uma lista somente com os textos das etiquetas pegas (os filmes) e colocá-los em uma lista.
for html_film in html_films:
    string_of_films = html_film.get_text()
    list_of_films = string_of_films.split("\n")
    list_of_films.pop(0)
    list_of_films.pop(1)
#adicionar os filmes em um dicionário, onde o critério de separação é o ano do filme.
for element in list_of_films:
    for key in films_per_year.keys():
        if element[-5:-1] == str(key):
            films_per_year[key].append(element[0:-6])
print(films_per_year[2019])






# with open("films_zoiudo.csv", "w") as csv_file:
#     headers = ["Title"]
#     csv_write = writer(csv_file, Fieldnames=headers)
#     csv_write.writerow({"Title": films})

# films.append(film.get_text())
        








