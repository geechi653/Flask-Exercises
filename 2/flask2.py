from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            if num % 2 == 0:
                result = f"{num} is an even number."
            else:
                result = f"{num} is an odd number."
            return render_template('result.html', result=result)
        except ValueError:
            error = "Invalid input. Please enter an integer."
            return render_template('error.html', error=error)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)