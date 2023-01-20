from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<string:page_name>') # Dynamically One Liner For Working.
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data): # csv --> Comma Separated Values
    with open('Database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # csv_writer.writeheader()
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
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
