
#This line imports tools from Flask that we need:
# Flask is the core framework
# render_template helps show HTML pages
# request handles web requests
# jsonify helps send data back to the webpage

from flask import Flask, render_template, request, jsonify, redirect, Response
from functools import wraps
import csv
import os

app = Flask(__name__)

def init_csv():
    if not os.path.exists('workers.csv'):
        # The 'w' mode means "write" - it will create a new file or overwrite an existing one.
        with open('workers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'wage'])  # Simplified headers

def get_workers():
    workers = []
    try:

        # Opens the CSV file in read mode ('r')
        # Checks if the file is empty by trying to read the first character
        # If empty, returns an empty list
        with open('workers.csv', 'r', encoding='utf-8', newline='') as file:
            # First, check if the file is empty
            first_char = file.read(1)
            if not first_char:
                print("Warning: CSV file is empty")
                return []
            
            # Reset file pointer to beginning
            file.seek(0)
            
            # Read the CSV file
            csv_reader = csv.reader(file)
            next(csv_reader, None)  # Skip the header row
            
            for row in csv_reader:
                # Make sure we have exactly 2 values (name and wage)
                if len(row) != 2:
                    print(f"Warning: Skipping invalid row: {row}")
                    continue
                
                name, wage_str = row
                
                # Clean the wage string and convert to float
                try:
                    wage = float(wage_str.strip())
                    workers.append({
                        'name': name.strip(),
                        'wage': wage
                    })
                except ValueError as e:
                    print(f"Warning: Invalid wage value '{wage_str}' for worker '{name}'")
                    
    except FileNotFoundError:
        print(f"Error: Could not find workers.csv file")
    except Exception as e:
        print(f"Error reading workers: {str(e)}")
        
    return workers


def add_worker(name, wage):
    # Data to append
    new_data = [name, wage]

    # open the csv file in append mode 'a'
    with open('workers.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)

        #append the new data
        csv_writer.writerow(new_data)


def remove_worker(name):
    workers = get_workers()
    # filter out the worker to remove
    updated_workers = [worker for worker in workers if worker["name"] != name]

    #write the updated list bacl to the csv
    with open('workers.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "wage"])
        writer.writeheader()
        writer.writerows(updated_workers)


# Flask sees the request for the homepage ("/")
# Calls get_workers() to get the list of workers from the CSV
# Uses render_template to show the 'index.html' page, passing the worker data to it
# This is where Python connects to the HTML/JavaScript we looked at earlier. The {% for worker in workers %} in your HTML 
# is using the worker data that Python just read from the CSV file. Each worker's name and wage from the CSV becomes 
# available in the HTML template, which then creates those worker cards we discussed earlier.
@app.route("/")
def index():
    workers = get_workers()
    return render_template('index.html', workers=workers)


@app.route("/add_worker", methods=['POST'])
def handle_add_worker():
    name = request.form['name']
    wage = request.form['wage']
    
    add_worker(name, wage)
    return redirect('/')


@app.route("/remove_worker", methods=['POST'])
def handle_remove_worker():
    name = request.form['name']

    remove_worker(name)
    return redirect('/')

if __name__ == '__main__':
    init_csv()
    app.run(debug=True)
