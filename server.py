""" This server.py and it is responsible for the rendering """
from flask import Flask, render_template, request
from EDetection import emotion_detection

app= Flask("Emotion Detector")

@app.route("/emotionDetection")
def sent_emotion():
    """This returns back the emotion"""
    test_to_analyze = request.args.get("testToAnalyze")
    response = emotion_detection.emotion_detector(test_to_analyze)

    if response is None:
        return "Invalid! Please try again"

    return f"the system response is {response}. Emotion is {max(response, key = response.get)}"

@app.route("/")
def render_index_page():
    """This renders back the index.html page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000)
    