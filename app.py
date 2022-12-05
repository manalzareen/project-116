# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Manal zareen" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father_webpage():
    name = "Mohammed Majid"
    return render_template("father.html",father_name = name)
# define the route to mother webpage
@app.route("/mother")
def mother_webpage():
    name = "Asiya Fatima"
    return render_template("mother.html",mother_name = name)

# define the route to friends webpage
@app.route("/friend")
def friend_webpage():
    name = "Alina Anwar"
    return render_template("friend.html",friend_name = name)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
