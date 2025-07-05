# 🚀 PDF to Portfolio Generator

Transform your PDF resume into a beautiful, professional HTML portfolio with AI-powered parsing.

![Portfolio Generator](https://img.shields.io/badge/Status-Ready-brightgreen)
![LinkedIn Theme](https://img.shields.io/badge/Theme-LinkedIn-0a66c2)
![License](https://img.shields.io/badge/License-MIT-blue)

## 📋 **Overview**

This project uses AI (Google Gemini) to extract structured data from PDF resumes and generates beautiful HTML portfolios with a LinkedIn-inspired design.

### **Tech Stack**
- **Frontend:** React.js with modern UI
- **Backend:** FastAPI (Python)
- **AI:** Google Gemini API
- **PDF Processing:** pdfplumber
- **Styling:** Custom CSS (LinkedIn-inspired)

---

## 🚀 **Quick Start - Run Locally**

### **Prerequisites**
- Python 3.8+ installed
- Node.js 16+ installed
- Google Gemini API key ([Get it here](https://aistudio.google.com/app/apikey))

### **1. Clone & Setup**
```bash
# Clone the repository
git clone <your-repo-url>
cd linkedin

# Create Python virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### **2. Backend Setup**
```bash
# Navigate to backend
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create environment file
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env

# Start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### **3. Frontend Setup** (New Terminal)
```bash
# Navigate to frontend
cd frontend

# Install Node.js dependencies
npm install

# Start the development server
npm start
```

### **4. Access the Application**
- **Frontend:** http://localhost:3000 (or 3001/3002 if 3000 is busy)
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

---

## 📁 **Project Structure**
```
linkedin/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── pdf_parser.py        # PDF parsing with Gemini AI
│   ├── portfolio_generator.py # HTML portfolio generation
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
├── frontend/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # LinkedIn-inspired styling
│   │   └── index.js        # React entry point
│   ├── package.json        # Node.js dependencies
│   └── public/             # Static assets
├── deployment-guide.md     # Deployment instructions
└── README.md              # This file
```

---

## 🔧 **Detailed Setup Instructions**

### **Backend Dependencies** (`backend/requirements.txt`)
```
fastapi==0.104.1
uvicorn==0.24.0
pdfplumber==0.10.3
python-multipart==0.0.6
python-dotenv==1.0.0
langchain-google-genai==1.0.10
langchain==0.1.0
pydantic==2.5.0
```

### **Frontend Dependencies** (`frontend/package.json`)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-dropzone": "^14.2.3"
  }
}
```

### **Environment Variables** (`.env`)
```bash
# Backend environment variables
GEMINI_API_KEY=your_gemini_api_key_here
CORS_ORIGINS=http://localhost:3000,http://localhost:3001,http://localhost:3002
```

---

## 🎯 **How to Use**

1. **Start both servers** (backend on :8000, frontend on :3000)
2. **Open** http://localhost:3000 in your browser
3. **Upload** a PDF resume by dragging & dropping or clicking
4. **Wait** for AI processing (usually 10-30 seconds)
5. **Preview** the generated portfolio
6. **Download** the HTML file

---

## 🐛 **Troubleshooting**

### **Common Issues & Solutions**

#### **Backend Issues**
```bash
# Port already in use
ERROR: [Errno 98] Address already in use
# Solution: Kill existing process or use different port
pkill -f uvicorn
# or
uvicorn main:app --reload --port 8001

# Missing dependencies
ModuleNotFoundError: No module named 'fastapi'
# Solution: Install requirements
pip install -r requirements.txt

# API key error
ValueError: GEMINI_API_KEY not found in .env file
# Solution: Add your API key to .env file
echo "GEMINI_API_KEY=your_api_key" > .env
```

#### **Frontend Issues**
```bash
# Node modules missing
npm ERR! Cannot resolve dependency
# Solution: Clean install
rm -rf node_modules package-lock.json
npm install

# Port conflicts
Port 3000 is already in use
# Solution: Use different port
npm start -- --port 3001

# CORS errors in browser
Access to fetch blocked by CORS policy
# Solution: Ensure backend CORS is configured (already done)
```

#### **PDF Processing Issues**
```bash
# Large PDF files
Processing timeout or memory issues
# Solution: Optimize PDF or reduce file size

# Unsupported PDF format
Text extraction failed
# Solution: Ensure PDF has selectable text (not scanned images)
```

---

## 🔄 **Development Workflow**

### **Making Changes**
```bash
# Backend changes (auto-reload enabled)
cd backend
# Edit files, server automatically restarts

# Frontend changes (hot reload enabled)
cd frontend
# Edit files, browser automatically refreshes

# Install new dependencies
# Backend:
pip install new-package
pip freeze > requirements.txt

# Frontend:
npm install new-package
```

### **Testing**
```bash
# Test backend API
curl -X GET http://localhost:8000/docs

# Test file upload
curl -X POST -F "file=@sample.pdf" http://localhost:8000/upload-pdf/

# Frontend testing
npm test
```

---

## 📱 **Features**

- ✅ **AI-Powered Parsing** - Extracts structured data from any resume PDF
- ✅ **Beautiful UI** - LinkedIn-inspired professional design
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile
- ✅ **Real-time Preview** - See your portfolio as it's generated
- ✅ **One-Click Download** - Get your portfolio as an HTML file
- ✅ **Professional Templates** - Clean, modern portfolio layouts
- ✅ **Fast Processing** - Typically processes in 10-30 seconds

---

## 🌐 **API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/upload-pdf/` | Upload PDF and get HTML portfolio |
| `GET` | `/docs` | API documentation |
| `GET` | `/` | Health check |

---

## 🚀 **Next Steps**

1. **Run locally** using this guide
2. **Test** with your own PDF resume
3. **Deploy** using `deployment-guide.md`
4. **Customize** the portfolio templates
5. **Share** with friends and colleagues!

---

## 📞 **Support**

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Verify your Gemini API key is valid
4. Check that both servers are running

---

## 📄 **License**

MIT License - feel free to use and modify for your projects!

---

**Happy Portfolio Building! 🎉** 