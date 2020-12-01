"""Load in the excel file created from the scraper
    script and make it into JSON data
    """
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

file = '/home/daniel/python_web/site/Car_list.xls'


def loadAndPreprocess(url):

    df = pd.read_excel(file)

    # Load Name into seperate variable
    df_name = df['Name']
    df_name = np.asarray(df_name)
    df_name = [i.split()[0] for i in df_name]

    # Preprocess price into seperate variable
    df_price = df['Price']
    df_price = df_price.str.replace('$', '')
    df_price = np.array([v.replace(',', '')
                         for v in df_price], dtype=np.float32)
    df_price = np.divide(df_price, 1000)

    return df_name, df_price
