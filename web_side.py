from flask import Flask, render_template, request
from ponsScrap2 import Scraper, Maker

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []  # To store the results

    if request.method == "POST":
        word = request.form["word"]
        results = Scraper(word)  # Call the Scraper function with the input word
        maker_results =Maker(word, results)

        # Read the results from the "dieFolgen.txt" file
        # with open("dieFolgen.txt", "r", encoding="utf-8") as f:
        #     results = f.read().splitlines()

        # for row in results:
        #     print(row)
        
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run()
