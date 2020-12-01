from flask import Flask
import matplotlib.pyplot as plt
import io
import base64
from converter import loadAndPreprocess

x = '/home/daniel/python_web/site/Car_list.xls'
y = '/home/daniel/python_web/site/img/plot'


def create_figure(URLtoWebScrapeInfo):
    """Create figure from scraped info and save
    plot to local directory

    Args:
        URLtoWebScrapeInfo ([url]): [path to excel file made from web scraped info in scraper.py]
        URLtoSaveImageTo ([url]): [path to save plot image to in users local directory]
    """

    img = io.BytesIO()

    x = loadAndPreprocess(URLtoWebScrapeInfo)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(x[0], x[1], color='maroon', width=0.4)
    plt.xlabel('Car Brands')
    plt.ylabel('Cost in Dollars')
    plt.title('Cost of Cars from scraped site')
    # plt.show()
    plt.savefig(img, format='png')
    img.seek(0)

create_figure(x)
# https://stackoverflow.com/questions/41459657/how-to-create-dynamic-plots-to-display-on-flask