from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def yay():
    return str("success")

@app.route("/reply", methods=['GET', 'POST'])
def app():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if body == None:
        resp.message("Huh ?")
    else:
        try:
            resp.message(eval(body))
        except:
            resp.message("Operation not permitted !")            
            resp.message("Operation not permitted !")           
            resp.message("Operation not permitted !")           
            resp.message("Operation not permitted !")           
            resp.message("Operation not permitted !")           
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True) 
