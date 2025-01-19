from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to render the map page
@app.route('/')
def map_page():
    # Dummy data points for heatmap (latitude, longitude, and weight)
    heatmap_data = [
        {"lon": 75.231870, "lat": 12.240140, "weight": 0.8},  # College of Engineering Trikaripur
        {"lon": 75.233870, "lat": 12.242140, "weight": 0.6},  # Nearby point 1
        {"lon": 75.229870, "lat": 12.238140, "weight": 0.9},  # Nearby point 2
        {"lon": 75.235870, "lat": 12.241140, "weight": 0.7},  # Nearby point 3
    ]
    return render_template('map.html', heatmap_data=heatmap_data)

if __name__ == '__main__':
    app.run(debug=True)
