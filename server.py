from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
    
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read(all).html",users_from_controller=users)
            
# relevant code snippet from server.py
from user import User
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    #If values in html are same as in db we can use
    #@app.route('/friends/create', methods=['POST'])
    # def create_friend():
    #     Friend.save(request.form)
    #     return redirect('/')

    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/new_user')
def new_user():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
