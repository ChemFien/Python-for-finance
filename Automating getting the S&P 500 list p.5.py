import bs4 as bs # for parsing HTML and XML data
import pickle # serilises any python object to be saved so as not having to go online again
import requests #


def save_sp500_tickers():
    # Collect information to parse NOT source
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    #Option+Command+U to view source
    soup = bs.BeautifulSoup(resp.text, 'lxml') #the text of the source code;Python library which allows for easy handling of XML and HTML files, and can also be used for web scraping.
    table = soup.find('table', {'class': 'wikitable sortable'})# select table you are interested iin
    tickers = []
    for row in table.findAll('tr')[1:]:  # start afte the header of the table roe
        ticker = row.findAll('td')[0].text # find the table data from the first column, index 0 as a text format
        tickers.append(ticker) # append ticker into tickers list

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f) # dumping tickers into file f
    print(tickers)
    return tickers


save_sp500_tickers()