from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open(r'fetal_health1.pkl','rb'))
app=Flask(__name__)

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/inspect")
def inspect():
    return render_template("inspect.html")

# @app.route("/home", methods=["GET", "POST"])
# def home():
#     prolongued_decelerations = float(request.form['prolongued_decelerations'])
#     abnormal_short_term_variability = float(request.form['abnormal_short_term_variability'])
#     percentage_of_time_with_abnormal_long_term_variability = float(request.form['percentage_of_time_with_abnormal_long_term_variability'])
#     histogram_variance = float(request.form['histogram_variance'])
#     histogram_median = float(request.form['histogram_median'])
#     mean_value_of_long_term_variability = float(request.form['mean_value_of_long_term variability'])
#     histogram_mode = float(request.form['histogram_mode'])
#     accelerations = float(request.form['accelerations'])

#     X = [[prolongued_decelerations, abnormal_short_term_variability, percentage_of_time_with_abnormal_long_term_variability,
#           histogram_variance, histogram_median, mean_value_of_long_term_variability, histogram_mode, accelerations]] 
#     output = model.predict(X)

#     if int(output[0])==0:
#         output='Normal'
#     elif int(output[0])==1:
#         output='Pathological'
#     else:
#         output='Suspect'

#     return render_template('output.html', output=output)

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        input_data = request.form
        print(input_data)  # Debugging line

        # Access the form data and convert it to float
        feature1 = float(input_data.get('feature1', 0.0))
        feature2 = float(input_data.get('feature2', 0.0))
        feature3 = float(input_data.get('feature3', 0.0))
        feature4 = float(input_data.get('feature4', 0.0))
        feature5 = float(input_data.get('feature5', 0.0))
        feature6 = float(input_data.get('feature6', 0.0))
        feature7 = float(input_data.get('feature7', 0.0))
        feature8 = float(input_data.get('feature8', 0.0))
    
        # Make predictions using the loaded model
        input_features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]
        output = model.predict([input_features])

        # Process the output and return it
        res =  str(int(output[0]))
        result=''
        if res=="1":
            result="Normal"
        elif res=="2":
            result="Suspect"
        elif res=="3":
            result="Pathological"
        return render_template('output.html', output=result)


if __name__ == "__main__":
    app.run(debug=True)