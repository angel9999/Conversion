from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    number =float( request.args['number'])
    a = number * 0.45359237
    reply = str(a) + ' kg'
    return render_template('response.html', response = reply)

@app.route("/Page2")
def render_main1():
    return render_template('Page2.html')

@app.route("/response2")
def render_response2():
    number =float( request.args['number'])
    a = number % 28.35
    reply = str(a) + ' oz'
    return render_template('response2.html', response = reply)

@app.route("/Page3")
def render_main3():
    return render_template('Page3.html')

@app.route("/response3")
def render_response3():
    number =float( request.args['number'])
    a = number * 453.592
    reply = str(a) + ' g'
    return render_template('response3.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
