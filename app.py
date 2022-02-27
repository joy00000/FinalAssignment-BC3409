#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template
import joblib
from sklearn.preprocessing import StandardScaler


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        selected_model = request.form.get("model")
        if selected_model == "LR":
            model = joblib.load("LR")
            pred = model.predict([[age, loan]])
        elif selected_model == "MLP":
            model = joblib.load("MLP")
            scaler = StandardScaler()
            norm = scaler.fit_transform([[age, loan, income]])
            pred = model.predict(norm)
        else:
            print(selected_model)
            model = joblib.load(selected_model)
            pred = model.predict([[age, loan, income]])
        
        
        pred = pred[0]
        
        if pred == 1:
            res = "Will default!"
        else:
            res = "Will not default!"
        m = ("Selected model: " + selected_model)
        s = ("Result is: " + res)
        return (render_template("index.html", result = s, model = m))
    else: 
        return (render_template("index.html", result = "Predict default"))


# In[5]:


if __name__ == "__main__":
    app.run()


# In[ ]:




