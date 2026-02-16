# 🌊 AI Flood Risk Detection API

A FastAPI-based backend service that evaluates flood risks from terrain images using Google’s Gemini AI. This API processes uploaded images, analyzes environmental features, and returns structured flood risk insights.


This backend provides an AI-powered solution for analyzing flood-prone areas using image data. It integrates Google Gemini for intelligent interpretation and includes fallback mechanisms to ensure reliability even during API failures.



## ✨ Features

* 🧠 **AI Image Analysis** – Uses Gemini model to analyze terrain images
* 📊 **Structured Risk Reports** – Returns risk level, elevation, and recommendations
* 🔁 **Retry Mechanism** – Automatically retries failed AI requests
* ⚠️ **Fallback System** – Generates simulated results if AI service is unavailable
* 📦 **FastAPI Backend** – High performance and async-ready
* 🌐 **CORS Enabled** – Easy integration with frontend apps

---

## 🛠️ Tech Stack

* **FastAPI** – API framework
* **Uvicorn** – ASGI server
* **Google Generative AI** – AI analysis engine
* **Pydantic** – Data validation
* **Pillow (PIL)** – Image processing
* **Python-dotenv** – Environment management

---

## 📂 Project Structure

```
backend/
├── main.py          # Main API logic
├── start.py         # Startup script
├── requirements.txt # Dependencies
├── .env             # Environment variables
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Project

```bash
git clone <your-repo-url>
cd backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
PORT=10000
```

---

### 5️⃣ Run the Server

```bash
python start.py
```

Or manually:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 10000
```

---

## 🌐 API Endpoints

### Root Endpoint

```http
GET /
```

Returns API status and metadata.

---

### Image Analysis Endpoint

```http
POST /api/analyze/image
```

#### Request

* Content-Type: `multipart/form-data`
* Body:

  * `file`: Image file (max 10MB)

#### Example

```bash
curl -X POST "http://localhost:10000/api/analyze/image" \
-H "Content-Type: multipart/form-data" \
-F "file=@image.jpg"
```

---

## 📥 Response Format

```json
{
  "success": true,
  "risk_level": "High",
  "description": "Detected terrain features indicating high flood risk.",
  "recommendations": [
    "Install flood barriers",
    "Monitor water levels",
    "Prepare evacuation plan"
  ],
  "elevation": 35.4,
  "distance_from_water": 800.2,
  "ai_analysis": "Detailed AI analysis...",
  "message": "Image analyzed successfully using Gemini AI."
}
```

---

## 🧠 How It Works

### 1. Image Upload

* Accepts user-uploaded terrain images
* Validates file type and size

---

### 2. Preprocessing

* Converts image to RGB format
* Ensures compatibility with AI model

---

### 3. AI Analysis

* Sends image + prompt to Gemini AI
* Extracts structured flood-related insights

---

### 4. Response Parsing

* Parses JSON from AI response
* Handles malformed responses gracefully

---

### 5. Fallback System

If AI fails:

* Generates simulated flood risk data
* Ensures API always returns a response

---

## 🔄 Retry Strategy

The system includes a retry mechanism:

* Maximum retries: **3**
* Uses **exponential backoff**
* Detects quota errors and delays accordingly

---

## ⚠️ Error Handling

* Invalid file type → `400 Bad Request`
* File too large → `400 Bad Request`
* Processing failure → `500 Internal Server Error`

---

## 🧪 Testing Tips

* Use small images (<10MB)
* Try different terrains (urban, rivers, fields)
* Test API using Swagger UI

---

## 📖 API Documentation

Once the server is running:

* Swagger UI → `http://localhost:10000/docs`
* ReDoc → `http://localhost:10000/redoc`
* OpenAPI JSON → `http://localhost:10000/openapi.json`

---

## 🚀 Deployment

### Environment Variables

```env
GEMINI_API_KEY=your_key
```



---

## 🌟 Advantages

* No need for complex computer vision models
* Fast implementation using AI
* Reliable fallback system
* Easy to extend with more endpoints

---

## 📌 Future Improvements

* Add coordinate-based analysis
* Store analysis history in database
* Real-time flood alerts
* Frontend dashboard integration

---

## 📜 License

This project is open-source and available for educational and commercial use.


