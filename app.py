from flask import Flask, render_template, request

import estate as es

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    pr = ""
    if (request.method == "POST"):
        X1_transaction_date = request.form["X1_transaction_date"]
        X2_house_age = request.form["X2_house_age"]
        X3_distance_to_station = request.form["X3_distance_to_nearest_MRT_station"]
        X4_convenience_stores = request.form["X4_number_of_convenience_stores"]
        X5_latitude = request.form["X5_latitude"]
        X6_longitude = request.form["X6_longitude"]

        """ 
        if X1_transaction_date > 0:
            prediction = es.real_estate_prediction(X1_transaction_date, X2_house_age, X3_distance_to_station,
                                                   X4_convenience_stores, X5_latitude, X6_longitude)
            pr = prediction
        else:
            pr = ""
        """

        prediction = es.real_estate_prediction(X1_transaction_date, X2_house_age, X3_distance_to_station,
                                               X4_convenience_stores, X5_latitude, X6_longitude)
        pr = prediction

    return render_template("index.html", estate_pred=pr)


"""    
@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == "POST":
        name = request.form["username"]

    return render_template("sub.html", n = name)  
    
 """

if __name__ == "__main__":
    app.run(debug=True)
