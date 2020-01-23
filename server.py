from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as myfile:
        myfile.write(f"\n{data['email']}|{data['subject']}|{data['message']}")
    myfile.close()


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
    database.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return "Something Went Wrong Please try again"
