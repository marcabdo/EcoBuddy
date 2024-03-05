from flask import Flask,render_template, request 
from chatbot import bot
  
app = Flask(__name__,template_folder="templates") 
  
@app.route("/") 
def home(): 
    return render_template('index.html')
@app.route("/chatbot") 
def chat(): 
    return render_template('chatbot.html')
@app.route("/whyEco") 
def why(): 
    return render_template('whyus.html')


  
@app.route('/process', methods=['POST']) 
def process(): 
    data = request.form.get('data') 
    # process the data using Python code  
    return bot(data)
  
if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=5000) 