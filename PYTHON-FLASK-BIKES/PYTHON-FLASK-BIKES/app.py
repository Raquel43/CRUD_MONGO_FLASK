from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from flask_paginate import Pagination, get_page_args
import database as dbase  
from classes import *


db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    bikes = db['bikes']
    bikesReceived = bikes.find()
    return render_template('index.html', bikes = bikesReceived)

#Method Post
@app.route('/bikes', methods=['POST'])
def addBike():
    bikes = db['bikes']
    _id = request.form['_id']
    model = request.form['model']
    brand = request.form['brand']
    features = request.form['features']
    year = request.form['year']
    size = request.form['size']
    availability = request.form['availability']
    Price_day = request.form['Price_day']


    if _id and model and brand and features and year and size and availability and Price_day:
        bike = Bike(int(_id), model, brand, features, year, size, availability, Price_day)
        bikes.insert_one(bike.toDBCollection())
        response = jsonify({
            '_id' : int(_id),
            'model' : model,
            'brand' : brand,
            'features' : features,
            'year' : year,
            'size' : size,
            'availability' : availability,
            'Price_day' : Price_day,


        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<_id>', methods=['GET'])
def delete(_id):
    bikes = db['bikes']
    bikes.delete_one({'_id' : int(_id)})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<_id>', methods=['POST'])
def edit(_id):
    bikes = db['bikes']
    _id = request.form['_id']
    model = request.form['model']
    brand = request.form['brand']
    features = request.form['features']
    year = request.form['year']
    size =request.form['size']
    availability =request.form['availability']
    Price_day =request.form['Price_day']

    if _id and model and brand and features and year and size and availability and Price_day:
        bikes.update_one({'_id' :int(_id)}, {'$set' : {'model' : model, 'brand' : brand, 'features' : features, 'year' : year, 'size' : size, 'availability': availability, 'Price_day': Price_day}})
        response = jsonify({'message' : 'Bike '+ str(_id) + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()






@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(debug=True, port=4000)