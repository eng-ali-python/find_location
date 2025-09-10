from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/automatic_save', methods=['POST'])
def automatic_save():
    try:
        data = request.json
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        with open('coordinates.txt', 'a') as f:
            f.write(f'Latitude: {latitude}, Longitude: {longitude}\n')
        return jsonify({'message': 'تم حفظ الموقع بنجاح.'}), 200
    except Exception as e:
        return jsonify({'message': f'حدث خطأ أثناء محاولة حفظ الموقع: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)