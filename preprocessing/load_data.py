import pandas as pd
import json
import sqlite3
import requests
from bs4 import BeautifulSoup
from datasets import load_dataset
import nltk

def load_text_file(filepath): # checked
    """ 
    Store the data as a list of lines. One line may contain multiple sentences and may also empty. 
    \n is placed at the end of each element indicating that the line has changed. 
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()

def load_csv_file(filepath): # checked
    """
    Make a list1 of list2. Text of each column is stored in separate list2. 
    Therefore, list1 encapsulates whole text contained in csv file.
    """
    df = pd.read_csv(filepath)
    return [df[i].tolist() for i in df.columns]
########################################################################################################
def load_json_file(filepath): # not checked
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_sqlite_data(db_path, query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def fetch_api_data(url):
    response = requests.get(url)
    return response.json()

def scrape_web_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [p.get_text() for p in soup.find_all('p')]

def load_nltk_data(corpus_name):
    nltk.download(corpus_name)
    if corpus_name == 'gutenberg':
        from nltk.corpus import gutenberg
        return gutenberg.raw('austen-emma.txt')
    # Add other NLTK corpora as needed

def load_huggingface_data(dataset_name):
    dataset = load_dataset(dataset_name)
    return [example['text'] for example in dataset['train']]

# Example usage
'''

if __name__ == "__main__":
    text_lines = load_text_file('data.txt')
    csv_texts = load_csv_file('data.csv')
    json_data = load_json_file('data.json')
    sqlite_texts = load_sqlite_data('database.db', "SELECT text_column FROM text_table")
    api_data = fetch_api_data('https://api.example.com/data')
    web_texts = scrape_web_data('https://www.example.com')
    nltk_text = load_nltk_data('gutenberg')
    hf_texts = load_huggingface_data('imdb')

    print(text_lines[:5])
    print(csv_texts[:5])
    print(json_data[:5])
    print(sqlite_texts[:5])
    print(api_data[:5])
    print(web_texts[:5])
    print(nltk_text[:1000])
    print(hf_texts[:5])

'''
