from scraper import Scraper
from injector import Injector

urls = {'Stratocaster': 'https://www.thomann.de/gb/st_models.html?ls=100&pg=', 
        'Telecaster': 'https://www.thomann.de/gb/t_models.html?ls=100&pg=', 
        'Les Paul': 'https://www.thomann.de/gb/lp_models.html?ls=100&pg='
}
db_url = 'bolt://localhost:7687'

def main():
    injector = Injector(db_url)
    injector.connect()

    for guitar_type, url in urls.items():
        scraper = Scraper(url)
        scraper.connect()
        guitars = scraper.parse_guitars(guitar_type)
        injector.inject_guitars(guitars)

if __name__ == '__main__':
    main()