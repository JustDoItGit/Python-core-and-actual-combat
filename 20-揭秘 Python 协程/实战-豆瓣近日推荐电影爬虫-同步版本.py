import time
import requests
from bs4 import BeautifulSoup


def cost_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('cost time: {}s'.format(end - start))
        return res

    return wrapper


@cost_time
def main():
    url = 'https://movie.douban.com/cinema/later/beijing/'
    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, 'html.parser')

    all_movies = init_soup.find('div', id='showing-soon')
    for each_movie in all_movies.find_all('div', class_='item'):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch).content
        soup_item = BeautifulSoup(response_item, 'html.parser')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


main()
