from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

####################################################
# SETUP
####################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/fruitsDatabase"
mongo = PyMongo(app)

fruits_collection = mongo.db.fruits

####################################################
# ROUTES
####################################################

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/show_all_fruits')
def show_all_fruits():
  """Show all fruits in the database."""

  context = {
    # TODO: Put all fruits here by calling `find()` on the fruits_collection
    'list_of_fruits': ''
  }

  return render_template('show_fruits.html', **context)


@app.route('/fruits_search')
def fruits_search():
  """Show all fruits of a certain name in the database."""

  context = {
    # TODO: Get all fruits with the specified name by calling `find()`
    'list_of_fruits': ''
  }

  return render_template('show_fruits.html', **context)


@app.route('/add_fruit', methods=['POST'])
def add_fruit():
  """Add a new fruit to the database."""
  # TODO: Return an error message if the fruit doesn't have a name or a price

  # TODO: Add the fruit (with name and price) to the database using `insert_one()`

  # TODO: Return a success message
  return "Not Yet Implemented!"


@app.route('/update_fruit', methods=['POST'])
def update_fruit():
  """Update an existing fruit in the database."""
  # TODO: Return an error message if the fruit doesn't have a name or a price

  # TODO: Update the fruit to have the new price using `update_one()`

  # TODO: Return a success message
  return "Not Yet Implemented!"


@app.route('/delete_fruit', methods=['POST'])
def delete_fruit():
  """Delete an existing fruit from the database."""
  # TODO: Return an error message if the fruit doesn't have a name

  # TODO: Delete the fruit from the database

  # TODO: Return a success message
  return "Not Yet Implemented!"

app.run('0.0.0.0', debug=True)
