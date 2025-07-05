#!/bin/bash

# 🚀 PDF to Portfolio Generator - Local Setup Script
# This script automates the setup process for running the project locally

echo "🚀 Setting up PDF to Portfolio Generator..."
echo "============================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

echo "✅ Python and Node.js are installed"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install backend dependencies
echo "📚 Installing backend dependencies..."
cd backend
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "🔑 Creating .env file..."
    echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
    echo "⚠️  IMPORTANT: Please add your Gemini API key to backend/.env file"
    echo "   Get your API key from: https://aistudio.google.com/app/apikey"
fi

cd ..

# Install frontend dependencies
echo "🎨 Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the application:"
echo ""
echo "1. Add your Gemini API key to backend/.env file"
echo "2. Start the backend:"
echo "   cd backend && uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "3. In a new terminal, start the frontend:"
echo "   cd frontend && npm start"
echo ""
echo "4. Open http://localhost:3000 in your browser"
echo ""
echo "Happy portfolio building! 🎉" 