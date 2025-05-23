from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)


bot = ChatBot("chatbot", read_only=True)  
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Route for main page
@app.route("/")
def home():
    return render_template("index.html")

# Route to get bot response
@app.route("/get")
def get_bot_response():
    user_text = request.args.get("userMessage") 
    if user_text:
        return str(bot.get_response(user_text))
    return "Sorry, I didn't get that."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


