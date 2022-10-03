from flask import Flask,redirect,url_for,render_template,request




app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


@app.route('/',methods=['GET','POST'])
def radiomain():
    return render_template('radiomain.html')

@app.route('/radiomain2',methods=['GET','POST'])
def radiomain2():
   return render_template('radiomain2.html')


@app.route('/radio',methods=['GET','POST'])
def radio():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('radio.html')
    return render_template('radio.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)