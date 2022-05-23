from bs4 import BeautifulSoup as bs


def parse_xml(path):
    infile = open(path, 'r', encoding='utf-8')
    contents = infile.read()
    soup = bs(contents, 'xml')
    currencies = soup.find_all('Code')
    rates = soup.find_all('Mid')
    currencies_dict = {currency.get_text(): eval(rate.get_text()) for currency, rate in zip(currencies, rates)}
    currencies_dict['PLN'] = 1
    return currencies_dict
