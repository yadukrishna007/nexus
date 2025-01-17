from flask import Flask, render_template, jsonify
from flask_cors import CORS  # To allow cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy data for heatmap (latitude, longitude, and intensity)
dummy_data = [
    {"latitude": 28.6139, "longitude": 77.2090, "intensity": 1.0},  # Delhi
    {"latitude": 19.0760, "longitude": 72.8777, "intensity": 0.8},  # Mumbai
    {"latitude": 12.9716, "longitude": 77.5946, "intensity": 0.6},  # Bangalore
    {"latitude": 13.0827, "longitude": 80.2707, "intensity": 0.4},  # Chennai
    {"latitude": 22.5726, "longitude": 88.3639, "intensity": 0.2},  # Kolkata
]

@app.route('/')
def index():
    # Render the map page (ensure map.html is inside the templates folder)
    return render_template('map.html')

@app.route('/get-heatmap-data', methods=['GET'])
def get_heatmap_data():
    # Return the dummy data as JSON
    return jsonify(dummy_data), 200

if __name__ == '__main__':
    app.run(debug=True)
