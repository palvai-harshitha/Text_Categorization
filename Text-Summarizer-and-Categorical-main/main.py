# Prepare libraries
#from flask import Flask, render_template, request
#import flask
#app = flask.Flask(name)
from flask import Flask
import functions as func
import pickle
import warnings
from flask import Flask, redirect, url_for, render_template, request
# Stop not important warnings and define the main flask application
warnings.filterwarnings("ignore")
app= Flask(__name__)

# Application home page
@app.route("/")
def home():
    return render_template("home.html", page_title="Text Categorizer")

@app.route("/index.html")
def index():
    return render_template("index.html", page_title="Text Categorizer")

# Analyze URL page
# First we get the text from the input link
# Then get classifier and the number of sentences
# Get the language for calling the right model
# Get text summary and category
@app.route("/analyze_url", methods=['GET', 'POST'])
def analyze_url():
    if request.method == 'POST':
        input_language = request.form['url_language']
        input_url = request.form['url_input_text']
        input_text = func.fetch_data(input_url)
        classifier_model_name = request.form['url_classifier']
        sentences_number = request.form['url_sentences_number']
        classifier_model = pickle.load(open('models/en_' + classifier_model_name + '.pkl', 'rb'))
        text_summary, text_category = func.summarize_category(input_text, sentences_number, classifier_model, False)
    return render_template("index.html", page_title="Text Summarizer & Categorical", input_text=input_text, text_summary=text_summary, text_category=text_category)

# @app.route("/analyze_file", methods=['GET', 'POST'])
# def analyze_file():
#     if request.method == 'POST':
#         input_language = request.form['file_language']
#         input_file = request.files['file_input_text']
#         classifier_model_name = request.form['file_classifier']
#         sentences_number = request.form['file_sentences_number']
#         input_text = func.fetch_filedata(input_file)

@app.route("/analyze_text", methods=['GET', 'POST'])
def analyze_text():
    if request.method == 'POST':
        input_language = request.form['text_language']
        input_text = request.form['text_input_text']
        classifier_model_name = request.form['text_classifier']
        sentences_number = request.form['text_sentences_number']
        classifier_model = pickle.load(open('models/en_' + classifier_model_name + '.pkl', 'rb'))
        text_summary, text_category = func.summarize_category(input_text, sentences_number, classifier_model, False)
    return render_template("index.html", page_title="Text Summarizer & Categorical", input_text=input_text, text_summary=text_summary, text_category=text_category)


# Start the application on local server
if __name__ == "__main__":
    app.run()