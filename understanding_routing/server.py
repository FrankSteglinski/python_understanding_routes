#localhost:5000/

from flask import Flask  # Import Flask to allow us to create our app
#"From the module flask, import the class Flask"
#Note: flask, like django, is a third-party library that can be used as if it was standard,
    #which is why we do not see it in the directory to our left.
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          #Remember, a decorator is, simply put, a mechanism that will add functionality to the function directly underneath.
def hello_world():
    return 'Hello World!'  # Returns the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/hi/<string:name>/<int:num>')
def hi(name, num):
    return f"Hi {name * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. #Nothing- not even comments- must be below this block of code.