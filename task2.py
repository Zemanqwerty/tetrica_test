import requests
from bs4 import BeautifulSoup as bs


def wiki_parser(start_word):
    repeat_count = 0
    error_count = 0
    start_word = start_word.replace(' ', '+')

    URL = f'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom={start_word}#mw-pages'
    response = requests.get(URL)

    soup = bs(response.text, 'html.parser')
    
    main_parse_block = soup.find('div', class_='mw-content-ltr')
    main_ul = main_parse_block.find_all('ul')

    articles = main_ul[-1].find_all('li')

    last_word = ''
    for article in articles:
        article_name = article.a['title']
        first_letter = article_name[0]

        if error_count <= 100 and repeat_count < 100:
            if first_letter in letters:
                if article_name not in words_list:
                    words_list.append(article_name)
                    last_word = article_name
                else:
                    repeat_count += 1
            else:
                error_count += 1
        else:
            return 'finally'
    
    wiki_parser(last_word)
        

def get_letters_count(words_list, letters):
    for letter in letters:
        count = 0
        for word in words_list:
            if word[0] == letter:
                count += 1
        print(f'{letter} -  {count}')


if __name__ == '__main__':
    start_word = 'Аардоникс'
    letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    words_list = []
    error_words_list = []


    wiki_parser(start_word)
    get_letters_count(words_list, letters)
