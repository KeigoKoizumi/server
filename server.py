from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
my_port = 16043
@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/dust', methods=['POST'])
def update_dust():
    time = request.form["time"]
    lux = request.form["dust"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + dust)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()
@app.route('/dust', methods=['GET'])
def get_dust():
    try:
        f = open(file_path, 'r')
        for row in f:
            dust = row
        return dust
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=my_port)