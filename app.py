from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/index')
def index_alias():
    """兼容模板中误写的 /index，重定向到站点首页。"""
    return redirect(url_for('index'), code=301)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/city')
def city():
    return render_template('city.html')

# 修改这里：/route 或 /featured-routes 都可以
@app.route('/route')
def featured_routes():
    return render_template('route.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/map-simple')
def map_simple_page():
    return render_template('map-simple.html')

@app.route('/guide')
def guide_page():
    return render_template('guide.html')

# Vercel WSGI handler
handler = app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)