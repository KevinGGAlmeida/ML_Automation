import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

class Request:
    def __init__(self,product_name):
        self.product_name = product_name
        self.request = requests.Session()
        self.response = None
        self.df = None
        self.filtered_list = []
    def get_list_of_products(self):
        self.response = self.request.get(f'https://lista.mercadolivre.com.br/{self.product_name}_NoIndex_True_PRICE*DESC_True').text
    def filtering_data(self):
        soup = BeautifulSoup(self.response,'html.parser')
        soup_json = json.loads(soup.find('script',type="application/ld+json").string.strip())
        for values in range(1,len(soup_json["@graph"])-1):
            self.filtered_list.append({"Numero":values,"Produto":soup_json["@graph"][values]["name"],"Preco":soup_json["@graph"][values]["offers"]["price"],"link":soup_json["@graph"][values]["offers"]["url"]})

    def creating_df(self):
        df = pd.DataFrame(self.filtered_list)
        df.to_excel(f"{self.product_name}.xlsx")
