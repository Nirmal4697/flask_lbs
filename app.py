from flask import Flask,render_template, request
import weight_p
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method=='POST':
        height=request.form['height']
        print(height)
        weight=weight_p.prediction([[float(height)]])
        return render_template("index.htm",hei=height,wei=weight)
    return render_template("index.htm")



if __name__ =="__main__":
    app.run(port=2005)


