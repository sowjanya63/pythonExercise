from flask import Flask
app=Flask(__name__)
count=0
@app.route("/")
def route():
    global count
    count=count+1
    return "you hit the url this "+str(count)+" times"
if __name__ =="__main__":
    app.run(debug=True)
