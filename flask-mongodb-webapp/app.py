from flask import Flask, request, jsonify, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from db_setup import Data, Base

app = Flask(__name__)

DATABASE_URL = "sqlite:///data.db"
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def add_data():
    name = request.json['name']
    value = request.json['value']
    new_data = Data(name=name, value=value)
    session.add(new_data)
    session.commit()
    return jsonify({'message': 'Data added successfully!'}), 201

@app.route('/data', methods=['GET'])
def get_data():
    data = session.query(Data).all()
    data_list = [{'name': d.name, 'value': d.value} for d in data]
    return jsonify(data_list)

@app.route('/analysis', methods=['GET'])
def analyze_data():
    data = session.query(Data).all()
    data_list = [{'name': d.name, 'value': d.value} for d in data]
    data_values = [d['value'] for d in data_list]
    np_data = np.array(data_values)
    mean = np.mean(np_data)
    median = np.median(np_data)
    df = pd.DataFrame(data_list)
    summary = df.describe().to_dict()
    return jsonify({
        'mean': mean,
        'median': median,
        'summary': summary
    })

if __name__ == '__main__':
    app.run(debug=True)
