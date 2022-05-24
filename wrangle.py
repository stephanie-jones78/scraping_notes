# Module for wrangling data

# importing libraries
import requests
import pandas as pd

def get_html(url):
    '''
    This function takes in a web url and returns the html text of that url.
    '''
    html = requests.get(url).text
    return html

def scrape_data(html, target):
    '''
    This function takes in html text of a webpage and a substring of text to target for scraping and returns
    a list of each line of html text containing the target substring.

    ARGS:
    - html: (str) html text
    - target: (str) text to target 
    Returns:
    list: list of strings, with lines containing target substring
    '''
    # initalizing empty list to store html lines in
    list = []
    for line in html.split('\n'):
        if target in line:
            list.append(line)
    return list

def clean_list():

def cache_list():


# def scrape_data(file_name, html, url_str_remove, ):
#     '''
    
#     '''
#     with open(file_name, 'w') as store_data:
#         for line in html.split('\n'):
#             if 'keyword' in line:
#                 line = line.replace('<meta class="keywords" itemprop="keywords" content="', '')\
#                     .replace('" /    >', '').replace(',', ' ')
#                 store_data.write(line)
#                 store_data.write('\n')