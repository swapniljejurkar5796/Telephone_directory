from flask import Flask,render_template,request,redirect,url_for



app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


database={}
@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/search",methods=['GET','POST'])
def search():
    search=request.form.get('se')
    return render_template("search.html",database=database,search=search)


@app.route("/display")
def display():
    return render_template("display.html",database=database)


@app.route("/home",methods=['GET','POST'])
def home():
    #database={}
    name=request.form.get('Name')
    phone=request.form.get('phone')
    database[name]=phone

    return render_template("index.html",database=database)



if __name__ == '__main__':
    app.run(debug=True)
