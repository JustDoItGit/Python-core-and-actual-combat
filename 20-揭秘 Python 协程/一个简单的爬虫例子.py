import time


def cost_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('cost time: {}s'.format(end - start))
        return res

    return wrapper


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


@cost_time
def main(urls):
    for url in urls:
        crawl_page(url)


main(['url_1', 'url_2', 'url_3', 'url_4'])
