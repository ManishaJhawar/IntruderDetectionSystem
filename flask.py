import pandas as pd
import time
import Combo2 as cb

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    s = cb.main()
    print "In hello flask ",s
    print "s = ",s
    return s
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

