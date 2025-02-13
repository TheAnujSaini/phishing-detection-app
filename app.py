from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the trained model
model = joblib.load("phishing_detection_model.pkl")

# Initialize Flask app
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    # Get the URL from the form
    url = request.form["url"]

    # Extract features from the URL (replace with your feature extraction logic)
    features = extract_features(url)

    # Convert features to a numpy array and reshape for prediction
    features_array = np.array(features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features_array)

    # Map prediction to result
    result = "Phishing" if prediction[0] == 1 else "Legitimate"

    # Render the result on the HTML page
    return render_template("index.html", result=result, url=url)

# Feature extraction function (replace with your actual logic)
def extract_features(url):
    # Example: Replace this with your feature extraction code
    features = [
        0,  # having_IP_Address
        1,  # URL_Length
        0,  # Shortening_Service
        0,  # having_At_Symbol
        0,  # double_slash_redirecting
        0,  # Prefix_Suffix
        1,  # having_Sub_Domain
        1,  # SSLfinal_State
        1,  # Domain_registeration_length
        0,  # Favicon
        0,  # port
        0,  # HTTPS_token
        1,  # Request_URL
        0,  # URL_of_Anchor
        0,  # Links_in_tags
        0,  # SFH
        0,  # Submitting_to_email
        0,  # Abnormal_URL
        0,  # Redirect
        0,  # on_mouseover
        0,  # RightClick
        0,  # popUpWidnow
        0,  # Iframe
        1,  # age_of_domain
        0,  # DNSRecord
        1,  # web_traffic
        1,  # Page_Rank
        1,  # Google_Index
        0,  # Links_pointing_to_page
        0,  # Statistical_report
    ]
    return features

# Run the app
if __name__ == "__main__":
    app.run(debug=True)