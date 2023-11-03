from scraper import Scraper
from injector import Injector

strat_url = 'https://www.thomann.de/gb/st_models.html?ls=100&pg='
tele_url = 'https://www.thomann.de/gb/t_models.html?ls=100&pg='
les_paul_url = 'https://www.thomann.de/gb/lp_models.html?ls=100&pg='
db_url = 'bolt://localhost:7687'

def main():
    injector = Injector(db_url)
    injector.connect()

    scraper_strat = Scraper('https://www.thomann.de/gb/st_models.html?ls=100&pg=')
    scraper_strat.connect()
    stratocasters = scraper_strat.parse_guitars('Stratocaster')
    injector.inject_guitars(stratocasters)

    scraper_tele = Scraper('https://www.thomann.de/gb/t_models.html?ls=100&pg=')
    scraper_tele.connect()
    telecasters = scraper_tele.parse_guitars('Telecaster')
    injector.inject_guitars(telecasters)

    scraper_lp = Scraper('https://www.thomann.de/gb/lp_models.html?ls=100&pg=')
    scraper_lp.connect()
    les_pauls = scraper_lp.parse_guitars('Les Paul')
    injector.inject_guitars(les_pauls)

if __name__ == '__main__':
    main()