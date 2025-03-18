from flask import Flask, render_template, request, jsonify
from data_processor import DataProcessor

app = Flask(__name__)
processor = DataProcessor()

# Sample data for demonstration
SAMPLE_DATA = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "age": 28, "city": "New York"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "age": 34, "city": "Boston"},
    {"id": 3, "first_name": "Mike", "last_name": "Johnson", "age": 42, "city": "Chicago"},
    {"id": 4, "first_name": "Sara", "last_name": "Williams", "age": 19, "city": "New York"},
    {"id": 5, "first_name": "Robert", "last_name": "Brown", "age": 67, "city": "Los Angeles"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    # Process our sample data for display
    processed_data = [processor.transform_data(item) for item in SAMPLE_DATA]
    return render_template('data.html', data=processed_data)

@app.route('/stats')
def stats():
    # Extract ages for statistics
    ages = [person['age'] for person in SAMPLE_DATA]
    statistics = processor.calculate_statistics(ages)
    return render_template('stats.html', statistics=statistics)

@app.route('/filter')
def filter_view():
    city = request.args.get('city', '')
    if city:
        filtered_data = processor.filter_records(SAMPLE_DATA, 'city', city)
    else:
        filtered_data = SAMPLE_DATA
    
    cities = list(set(person['city'] for person in SAMPLE_DATA))
    return render_template('filter.html', data=filtered_data, cities=cities, selected_city=city)

# API Endpoints
@app.route('/api/data', methods=['GET'])
def api_data():
    return jsonify(SAMPLE_DATA)

@app.route('/api/stats', methods=['GET'])
def api_stats():
    ages = [person['age'] for person in SAMPLE_DATA]
    return jsonify(processor.calculate_statistics(ages))

@app.route('/api/filter', methods=['GET'])
def api_filter():
    field = request.args.get('field')
    value = request.args.get('value')
    
    if not field or value is None:
        return jsonify({"error": "Missing required parameters"}), 400
    
    filtered_data = processor.filter_records(SAMPLE_DATA, field, value)
    return jsonify(filtered_data)

@app.route('/api/transform', methods=['POST'])
def api_transform():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    transformed = processor.transform_data(data)
    return jsonify(transformed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
