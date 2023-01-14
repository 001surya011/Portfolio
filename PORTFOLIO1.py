from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

print(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<string:page_name>') # Dynamically One Liner For Working.
def html_page(page_name):
    return render_template(page_name)


# @app.route('/home.html')
# def home():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/thankyou.html')
# def thank():
#     return render_template('thankyou.html')

def write_to_file(data):
    with open('Database.txt', mode='a') as database1:
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        file = database1.write(f'\n Email :{email}; Subject :{subject}; Message:{message}')

def write_to_csv(data): # csv --> Comma Separated Values
    with open('Database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # csv_writer.writeheader()
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message]) # List Format Is Important


@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # print(data)
        return redirect('/thankyou.html')
    # return render_template('login.html', error = error)
    else:
        return 'Invalid Submission'
if __name__ == '__main__':
    app.run(debug=True)