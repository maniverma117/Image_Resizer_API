# Image Resizer API

A simple Flask-based API for dynamically resizing images. This application fetches an image from a provided URL, resizes it to the specified dimensions, and returns the resized image as a response.

---

## Features
- Resize images dynamically based on width and height query parameters.
- Fetch images directly from a given URL.
- Lightweight and containerized for deployment using Docker.
- Error handling for invalid inputs or failed requests.

---

## Requirements
- Python 3.9+
- Dependencies listed in `requirements.txt`:
  - Flask
  - Pillow
  - Requests
- Docker (optional, for containerized deployment)

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/maniverma117/Image_Resizer_API.git
cd image-resizer-api
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Application Locally
Run the Flask application:
```bash
python app.py
```
By default, the app runs on `http://127.0.0.1:3000`. You can change the port by editing the `app.run()` call in `app.py`.

---

## Using Docker

### 1. Build the Docker Image
```bash
docker build -t image-resizer .
```

### 2. Run the Docker Container
```bash
docker run -d -p 3000:3000 --name image-resizer image-resizer
```

### 3. Run the Docker Container Already Dockerised 
```bash
docker run -d -p 3000:3000 --name image-resizer maniverma/image-resizer:latest
```
The app will now be accessible at `http://127.0.0.1:3000`.

---

## API Usage

### Endpoint
`GET /resize-image`

### Query Parameters
| Parameter  | Type   | Description                         | Required |
|------------|--------|-------------------------------------|----------|
| `url`      | string | The URL of the image to resize.     | Yes      |
| `width`    | int    | The desired width of the image.     | Yes      |
| `height`   | int    | The desired height of the image.    | Yes      |

### Example Request
```plaintext
http://127.0.0.1:3000/resize-image?url=https://d2lo0tepqt73yr.cloudfront.net/migProductImages/O-8560118%20001-01.jpg&width=300&height=300
```

### Example Response
The API returns the resized image directly. You can download it using tools like `curl`:
```bash
curl -o resized_image.jpg "http://127.0.0.1:3000/resize-image?url=https://d2lo0tepqt73yr.cloudfront.net/migProductImages/O-8560118%20001-01.jpg&width=300&height=300"
```

---

## Development and Debugging

### Enable Debug Mode
The app runs in debug mode by default. To disable it, set `debug=False` in `app.py`:
```python
app.run(host="0.0.0.0", port=3000, debug=False)
```

---

## Error Handling
The API provides clear error messages for invalid inputs:
1. **Missing Parameters**:
   ```json
   {
       "error": "Image URL (url) is required"
   }
   ```

2. **Invalid URL or Network Issues**:
   ```json
   {
       "error": "Invalid URL or image not found"
   }
   ```

3. **Other Errors**:
   ```json
   {
       "error": "Detailed error message here"
   }
   ```

---

## File Structure
```plaintext
.
├── app.py               # Main Flask application
├── Dockerfile           # Dockerfile for containerized deployment
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Notes
- **Production Use**: Disable debug mode before deploying the application in production.
- **Security**: Avoid exposing the app directly to the internet without authentication or rate-limiting mechanisms.
- **Limitations**: Only supports JPEG images for now. Extend the `Pillow` functionality to handle other formats like PNG or GIF.

---
