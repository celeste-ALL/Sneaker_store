from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<name>')
def product_page(name):
    with open(f'static/configs/cfg{name}/text.txt', 'r') as file:
        lines = file.readlines()

    i1 = url_for('static', filename=f'configs/cfg{name}/1.webp')
    i2 = url_for('static', filename=f'configs/cfg{name}/2.webp')
    i3 = url_for('static', filename=f'configs/cfg{name}/3.webp')
    i4 = url_for('static', filename=f'configs/cfg{name}/4.webp')
    i5 = url_for('static', filename=f'configs/cfg{name}/5.webp')


    return render_template('product_page.html', i1=i1, i2=i2, i3=i3, i4=i4, i5=i5, t1=lines)




if __name__ == '__main__':
    app.run(debug=True,  port="5111")