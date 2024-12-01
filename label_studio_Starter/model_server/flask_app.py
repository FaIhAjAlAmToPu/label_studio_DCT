from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io

# Load the YOLO model
model = YOLO("epoch692.pt")  # Replace with your model path

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['file']
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Run the YOLO model for detection
    results = model(img)

    # Format the predictions to return as JSON
    predictions = []
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            conf = float(box.conf[0])  # Confidence score
            cls = int(box.cls[0])  # Class ID
            predictions.append({
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "confidence": conf,
                "class": cls
            })

    return jsonify(predictions)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "up"}), 200

@app.route('/setup', methods=['POST'])
def setup():
    """Endpoint for Label Studio to setup the ML backend."""
    # This is a placeholder response.
    # You can add custom initialization logic here if needed.
    return jsonify({"status": "setup complete"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
