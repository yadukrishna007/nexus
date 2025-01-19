import pymysql
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Establish database connection
def get_connection():
    return pymysql.connect(
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
    con = get_connection()
    # error handling
    try:
        # Fetch heatmap data from the database as a dictionary
        with con.cursor(pymysql.cursors.DictCursor) as cmd:
            cmd.execute("SELECT temp, hum, gas, noise, lat, long FROM readings")
            heatmap_data = cmd.fetchall()
    finally:
        # Close the database connection
        con.close()

    # Render the map page with heatmap data
    return render_template('map.html', heatmap_data=heatmap_data)

if __name__ == '__main__':
    app.run(debug=True)

