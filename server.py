from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# @app.route('/')
# def home_page():
#     return render_template('index.html')    


@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)  

def write_to_db_text(data):
    with open('database.txt', mode='a') as database_text:
        email = data['email']
        subject = data['subject']
        message = data['message']
        text_writer = database_text.write(f'\nEmail:{email}, Subject:{subject}, Message:{message}')

def write_to_db_csv(data):
    with open('database.csv', newline='', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_db_text(data)
            write_to_db_csv(data)
            # print(data)
            return redirect('/thank_you.html')
        except:
            return 'Did not save to DB!!'
    else:
        return 'Something went wrong! Try again.'









# @app.route('/<username>/<int:post_id>')
# def username(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)