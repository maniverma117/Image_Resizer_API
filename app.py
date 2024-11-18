from flask import Flask, request, jsonify, send_file
from PIL import Image
from io import BytesIO
import requests

app = Flask(__name__)

@app.route("/resize-image", methods=["GET"])
def resize_image():
    # Get query parameters
    image_url = request.args.get("url")
    new_width = request.args.get("width", type=int)
    new_height = request.args.get("height", type=int)

    # Validate parameters
    if not image_url:
        return jsonify({"error": "Image URL (url) is required"}), 400
    if not new_width or not new_height:
        return jsonify({"error": "Both width and height are required"}), 400

    try:
        # Fetch the image from the URL
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error for failed requests
        img = Image.open(BytesIO(response.content))

        # Resize the image
        img = img.resize((new_width, new_height))

        # Save the resized image to a buffer
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        buffer.seek(0)

        # Return the resized image as a response
        return send_file(buffer, mimetype="image/jpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Enable debug mode
    app.run(host="0.0.0.0", port=3000, debug=True)
