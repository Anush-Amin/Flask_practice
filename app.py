## Create a simple flask application
from flask import Flask, render_template, request, redirect, url_for

## create flask app
app = Flask(__name__)

# create app decorator
## whenever the / in url is triggered it will perform home()
## example for local host http://127.0.0.1:5000/ will perform welcome()
@app.route('/')
def home():
    return '<h1>Hello World</h1>'

## whenever /welcome in url is triggered it will perform welcome()
## example for local host http://127.0.0.1:5000/welcome will perform welcome()
@app.route('/welcome')
def welcome():
    return '<h1>Welcome to flask tutorial</h1>'

@app.route('/index')
def index():
    ## render_template will check for templates folder
    ## hence naming convention should be maintained
    return render_template('index.html')

@app.route('/success/<int:score>')
## if we give url http://127.0.0.1:5000/success/24
## it will display The person has passed and score is 24
def success(score):
    return "The person has passed and score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and score is "+str(score)

@app.route('/calculate', methods=["POST", "GET"])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths_score = float(request.form['maths'])
        science_score = float(request.form['science'])
        history_score = float(request.form['history'])

        average_marks = (maths_score+science_score+history_score)/3

        result=""
        if average_marks>=50:
            result="success"
        else:
            result="fail"
        #return redirect(url_for(result, score=average_marks)) # this is to redirect to success and fail functions
        return render_template('result.html', results=average_marks)

## Assignment: Try for loop
    

## This is the entry point
if __name__ == '__main__':
    ## dont do debug=True in production
    ## for debug=True whenever we do changes and save, the page will reload
    app.run(debug=True) 
