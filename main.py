"""Write a program to scrape prices from a website and graph the prices to the web in JSON format"""
from flask import Flask, render_template, Response
import json
import html
from converter import loadAndPreprocess
import matplotlib.pyplot as plt
import names
import random
import io
import base64
from converter import loadAndPreprocess

app = Flask(__name__)
url = '/home/daniel/python_web/site/Car_list.xls'
y = '/home/daniel/python_web/site/plot.png'


@app.route("/jsonFile")
def getJSONFile():
    """Read from JSON file and deploy to web in JSON format

    Returns:
        [JSON, html page]: [description]
    """

    return render_template('index.html')


@app.route("/plot")
def plot_png():
    img = io.BytesIO()

    x = loadAndPreprocess(url)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(x[0], x[1], color='maroon', width=0.4)
    plt.xlabel('Car Brands')
    plt.ylabel('Cost in Dollars')
    plt.title('Cost of Cars from scraped site')
    # plt.show()
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plot_url), render_template('plot.html')


@app.route("/")
def route():
    return render_template("content.html")


if __name__ == "__main__":
    app.run(debug=True)
