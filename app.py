# =[Modules dan Packages]========================
from flask import Flask,render_template,request,jsonify

# =[Variabel Global]=============================
app = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def index():
	return render_template("index.html")

# =[Main]========================================
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)