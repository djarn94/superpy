from datetime import date
import csv
import itertools
from rich.table import Table
from rich.console import Console
from collections import Counter

#Generates a bought ID
def bought_id():
    with open('bought.csv', 'r', newline = '') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        for row in rows:      
            id_list = row['id']
        try:
            last_id = int(id_list[-1]) + 1
        except:
            last_id = 1
        return last_id
    
#generates a sold ID
def sold_id():
    with open('sold.csv', 'r', newline = '') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        for row in rows:
            id_list = row['id']
        try:
            last_id = int(id_list[-1]) + 1
        except:
            last_id = 1
        return last_id
    
def inventory_list():
     
     today = date.today

     with open('bought.csv', 'r', newline = '') as file:
         csv_reader = csv.DictReader(file)
         product_list = []
         id_list = []


         for id in csv_reader:
            id_list.append(id['id'])
            if id_list not in get_bought_id():
                for col in csv_reader:
                    product_list.append(col['product_name'])
            print('Current inventory: ')        
            print(Counter(product_list))

def bought_list():
     
     today = date.today

     with open('bought.csv', 'r', newline = '') as file:
         next
         csv_reader = csv.DictReader(file)
         rows = list(csv_reader)

         for row in rows:
            print(row)

#Gets a list of bought_id's in the sold.csv file
def get_bought_id():
         
    with open('sold.csv', 'r', newline = '') as sold_file:
         next
         sold_reader = csv.DictReader(sold_file)
         sold_rows = list(sold_reader)

    for row in sold_rows:
        return list(row['bought_id'])


####  test  ####
def inventory_now():
    today = date.today
    
    with open('bought.csv', 'r', newline = '') as file:

        table = table(title = 'inventory')

        table.add_column('product_name', style = 'white')
        table.add_column('amount', style = 'white')
        table.add_column('expiry_date', style = 'white')

    for row in inventory_list:
        table.add_row(row)


     
    
    

    
