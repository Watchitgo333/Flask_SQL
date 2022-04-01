from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', num_blocks1 = 8, num_blocks2 = 8, color1 = "red", color2 = "black")

@app.route('/<int:num>')
def byFour(num):
    return render_template('index.html', num_blocks1 = num, num_blocks2 = 8, color1 = "red", color2 = "black")

@app.route('/<int:num1>/<int:num2>')
def numByNum(num1, num2):
    return render_template('index.html', num_blocks1 = num1, num_blocks2 = num2, color1 = "red", color2 = "black")

@app.route('/<int:num1>/<int:num2>/<string:newColor1>')
def numByNumNewColor(num1, num2, newColor1):
    return render_template('index.html', num_blocks1 = num1, num_blocks2 = num2, color1 = newColor1, color2 = "black")

@app.route('/<int:num1>/<int:num2>/<string:newColor1>/<string:newColor2>')
def numByNumNewColor2(num1, num2, newColor1, newColor2):
    return render_template('index.html', num_blocks1 = num1, num_blocks2 = num2, color1 = newColor1, color2 = newColor2)

if __name__ == "__main__":
    app.run(debug=True)