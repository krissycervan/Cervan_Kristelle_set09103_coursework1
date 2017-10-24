from flask import Flask, render_template, url_for, abort, json
app = Flask(__name__)
#routes to pages
@app.route('/')
@app.route('/index')
def index():
 return render_template('index.html'), 200

@app.route('/tops')
def tops():
 return render_template('tops.html'), 200
 
 
@app.route('/tops')
@app.route('/tops/floral')
def tops_floral():
 start = '<img src="'
 url = url_for('static', filename='img/tops/floral-top.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/tops')
@app.route('/tops/croptop')
def tops_croptop():
 start = '<img src="'
 url = url_for('static', filename='img/tops/croptop.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/tops')
@app.route('/tops/chokersweater')
def tops_chokersweater():
 start = '<img src="'
 url = url_for('static', filename='img/tops/chokersweater.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/tops')
@app.route('/tops/poncho')
def tops_poncho():
 start = '<img src="'
 url = url_for('static', filename='img/tops/poncho.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/bottoms')
def bottoms():
 return render_template('bottoms.html'), 200

@app.route('/botoms')
@app.route('/bottoms/whitetrouser')
def bottoms_whitetrouser():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/white-trouser.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/bottoms')
@app.route('/bottoms/jeans')
def bottoms_jeans():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/jeans.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/bottoms')
@app.route('/bottoms/shorts')
def bottoms_shorts():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/blueshorts.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/bottoms')
@app.route('/bottoms/leggings')
def bottoms_leggings():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/blackleggings.jpg')
 end = '">'
 return start+url+end, 200
 


@app.route('/shoes')
def shoes():
 return render_template('shoes.html'), 200

@app.route('/shoes')
@app.route('/shoes/pinkshoes')
def shoes_pinkshoes():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/pinkshoes.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/shoes')
@app.route('/shoes/sandals')
def shoes_sandals():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/sandals.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/shoes')
@app.route('/shoes/ankleboots')
def shoes_ankleboots():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/ankleboots.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/shoes')
@app.route('/shoes/longboots')
def shoes_longboots():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/longboots.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/accessories')
def accessories():
 return render_template('accessories.html'), 200
 
@app.route('/accessories')
@app.route('/accessories/hairaccessory')
def accessories_hairaccessory():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/hairacc.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/accessories')
@app.route('/accessories/sunglasses')
def accessories_sunglasses():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/sunglasses.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/accessories')
@app.route('/accessories/scarf')
def accessories_scarf():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/scarf.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/accessories')
@app.route('/accessories/hatgloves')
def accessories_hatgloves():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/hatgloves.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/all')
def all():
 return render_template('all.html'), 200

@app.route('/all')
@app.route('/all/springstyle')
def springstyle():
 return render_template('springstyle.html'), 200
 
@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/top')
def all_springstyle_top():
 start = '<img src="'
 url = url_for('static', filename='img/tops/floral-top.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/bottom')
def all_springstyle_bottom():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/white-trouser.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all/springstyle/shoes')
def all_springstyle_shoes():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Pink Shoes":
       print item
       p = item

 return render_template('pinkshoes.html', pinkshoes=p), 200


@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/accessory')
def all_springstyle_accessory():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/hairacc.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/all')
@app.route('/all/summerstyle')
def summerstyle():
 return render_template('summerstyle.html'), 200
 
@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/top')
def all_summerstyle_top():
 start = '<img src="'
 url = url_for('static', filename='img/tops/croptop.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/bottom')
def all_summerstyle_bottom():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/blueshorts.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/shoes')
def all_summerstyle_shoes():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/sandals.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/accessory')
def all_summerstyle_accessory():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/sunglasses.jpg')
 end = '">'
 return start+url+end, 200
 
@app.route('/all')
@app.route('/all/fallstyle')
def fallstyle():
 return render_template('fallstyle.html'), 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/top')
def all_fallstyle_top():
 start = '<img src="'
 url = url_for('static', filename='img/tops/chokersweater.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/bottom')
def all_fallstyle_bottom():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/jeans.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/shoes')
def all_fallstyle_shoes():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/ankleboots.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/accessory')
def all_fallstyle_accessory():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/scarf.jpg')
 end = '">'
 return start+url+end, 200
 

@app.route('/all')
@app.route('/all/winterstyle')
def winterstyle():
 return render_template('winterstyle.html'), 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/top')
def all_winterstyle_top():
 start = '<img src="'
 url = url_for('static', filename='img/tops/poncho.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/bottom')
def all_winterstyle_bottom():
 start = '<img src="'
 url = url_for('static', filename='img/bottoms/blackleggings.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/shoes')
def all_winterstyle_shoes():
 start = '<img src="'
 url = url_for('static', filename='img/shoes/longboots.jpg')
 end = '">'
 return start+url+end, 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/accessory')
def all_winterstyle_accessory():
 start = '<img src="'
 url = url_for('static', filename='img/accessories/hatgloves.jpg')
 end = '">'
 return start+url+end, 200
 
#Error Notice (wrong url)
@app.errorhandler (404)
def page_not_found(error):
 return " <h1><em>Sorry! <p>Couldn't find the page you requested.</p><em></h1>", 404



 

#allows the website to run on python
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)



