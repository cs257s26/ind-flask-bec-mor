'''Replace me with your flask app'''
from flask import *
import dotenv
import csv

app = Flask(__name__)

data = []

def load_data():
    '''Loads data from weather.csv into data global variable'''
    if len(data) == 0:
        with open('./productioncode/llmenergy.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

@app.route('/')
def homepage():
    return "Hello, this is the homepage of LLM Energy Route Assignment"

''' Function returns a specified column '''
@app.route('/<int:neutral_row>/<string:col_name>/')
def get_column(neutral_row: int, col_name: str) -> str: 
    col_names = data[neutral_row] 
    col_num = 0
    spec_col = []

    for i in range(len(col_names)):
        if (col_names[i] == col_name): 
            break
        else: 
            col_num += 1 
    
    if (col_num == len(col_names)): 
        return []

    for i in range(len(data)): 
        spec_col.append(data[i][col_num])

    return str(spec_col)

''' Function returns a specified row '''
@app.route('/<string:row_name>/')
def get_row(row_name: str) -> str: 
    name_col_num = 0
    for i in range(len(data)): 
        if (data[i][name_col_num] == row_name): 
            return str(data[i])
        
    abort(404, description="Row not found") 
        
@app.errorhandler(404)
def page_not_found(page: str):
    return "Page not found error: " + str(page)

if __name__ == '__main__':
    load_data()
    app.run(port=5100)