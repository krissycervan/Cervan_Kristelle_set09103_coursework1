from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
 return render_template('index.html'), 200

@app.route('/tops.html')
def tops():
 return render_template('tops.html'), 200

@app.route('/bottoms.html')
def bottoms():
 return render_template('bottoms.html'), 200

@app.route('/shoes.html')
def shoes():
 return render_template('shoes.html'), 200

@app.route('/accessories.html')
def accessories():
 return render_template('accessories.html'), 200
 
@app.route('/all.html')
def all():
 return render_template('all.html'), 200
 
@app.route('/springstyle')
def springstyle():
 return render_template('springstyle.html'), 200
 
@app.route('/summerstyle')
def summerstyle():
 return render_template('summerstyle.html'), 200
 
@app.route('/fallstyle')
def fallstyle():
 return render_template('fallstyle.html'), 200

@app.route('/winterstyle')
def winterstyle():
 return render_template('winterstyle.html'), 200
 
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)
