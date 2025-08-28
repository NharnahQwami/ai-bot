from flask import Flask, render_template, request
from google import genai
import markdown

app = Flask(__name__)

client = genai.Client(api_key="AIzaSyBDQRIctzDb5Ve2BzRMX9Km6sg4gVoViC0")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        if user_prompt:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_prompt
            )
            # Convert Markdown to HTML
            response_text = markdown.markdown(response.text)
    
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
