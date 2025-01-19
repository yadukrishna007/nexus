import pymysql
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Establish databaseconnection
con = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    port=3307,
    db='smartcitydb',
    charset='utf8'
)

# Route to render the map page
@app.route('/')
def map_page():
    # Fetch heatmap data from the database as a dictionary
    cmd = con.cursor(pymysql.cursors.DictCursor)
    cmd.execute("SELECT temp, hum, gas, noise, lat, long FROM readings")
    heatmap_data = cmd.fetchall()
    con.close()
    return render_template('map.html', heatmap_data=heatmap_data)

if __name__ == '__main__':
    app.run(debug=True)
