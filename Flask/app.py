from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods =['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',  methods = ['POST'])
def math_operation():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0
        if ops == 'add':
            r = num1 + num2
            result = 'The sum of {} and {} is {}'.format(num1,num2,r)
            
        elif ops == 'subtract':
            r = num1 - num2
            result = 'The subtraction of {} and {} is {}'.format(num1,num2,r)
            
        elif ops == 'multiply':
            r = num1 * num2
            result = 'The multiplication of {} and {} is {}'.format(num1,num2,r)
            
        
        else:
            r = num1 / num2
            result = 'The division of {} and {} is {}'.format(num1,num2,r)
        
        return render_template('results.html',result = result)


#checking api with postman for validation
@app.route('/postman_data',  methods = ['POST'])
def math_operation2():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = 0
        if ops == 'add':
            r = num1 + num2
            result = 'The sum of {} and {} is {}'.format(num1,num2,r)
            
        elif ops == 'subtract':
            r = num1 - num2
            result = 'The subtraction of {} and {} is {}'.format(num1,num2,r)
            
        elif ops == 'multiply':
            r = num1 * num2
            result = 'The multiplication of {} and {} is {}'.format(num1,num2,r)
            
        
        else:
            r = num1 / num2
            result = 'The division of {} and {} is {}'.format(num1,num2,r)
        
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
