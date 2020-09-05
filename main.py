from flask import Flask, render_template

app = Flask(__name__)
@app.route("/dashboard")

def dashboard():
  return render_parent("dashboard.html")

@app.route("/doubts")
def doubts():
  return render_parent("doubts.html")
@app.route("/index")

def index():
  return render_parent("index.html")
@app.route("/councel")

def councel():
  return render_parent("councel.html")
@app.route("/resources")

def resources():
  return render_parent("resources.html")
@app.route("/analysis")

def analysis():
  return render_parent("analysis.html")

if __name__ == "__main__":
  app.run(debug=True)
