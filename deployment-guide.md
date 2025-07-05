# 🚀 Free Deployment Guide - PDF to Portfolio Generator

## 📋 **Overview**
Deploy your PDF to Portfolio generator for FREE using modern cloud platforms.

## 🎯 **Best Free Deployment Strategy**

### **Frontend: Vercel** (FREE)
- ✅ Unlimited static deployments
- ✅ Custom domains
- ✅ Automatic HTTPS
- ✅ GitHub integration

### **Backend: Railway** (FREE)
- ✅ $5/month free credit
- ✅ PostgreSQL database
- ✅ Automatic deployments
- ✅ Custom domains

---

## 🔧 **Step-by-Step Deployment**

### **1. Prepare Your Code**

#### Backend Changes:
```bash
# Add to backend/requirements.txt
fastapi==0.104.1
uvicorn==0.24.0
pdfplumber==0.10.3
python-multipart==0.0.6
python-dotenv==1.0.0
langchain-google-genai==1.0.10
langchain==0.1.0
pydantic==2.5.0
```

#### Environment Variables:
```bash
# Create backend/.env
GEMINI_API_KEY=your_gemini_api_key_here
```

### **2. Deploy Backend on Railway**

1. **Sign up**: Go to [railway.app](https://railway.app)
2. **Connect GitHub**: Link your repository
3. **Create Project**: 
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Select the `backend` folder
4. **Configure**:
   - Add environment variable: `GEMINI_API_KEY`
   - Railway will auto-detect FastAPI
5. **Deploy**: Railway will build and deploy automatically

### **3. Deploy Frontend on Vercel**

1. **Sign up**: Go to [vercel.com](https://vercel.com)
2. **Import Project**: 
   - Click "New Project"
   - Import from GitHub
   - Select your repository
   - Choose the `frontend` folder
3. **Configure**:
   - Build Command: `npm run build`
   - Output Directory: `build`
   - Install Command: `npm install`
4. **Environment Variables**:
   ```
   REACT_APP_API_URL=https://your-railway-backend-url.railway.app
   ```
5. **Deploy**: Vercel will build and deploy

### **4. Update Frontend API URL**

```javascript
// In frontend/src/App.js, update the fetch URL:
const response = await fetch(`${process.env.REACT_APP_API_URL}/upload-pdf/`, {
  method: 'POST',
  body: formData,
});
```

---

## 🌟 **Alternative FREE Options**

### **Option 2: Netlify + Render**
- **Frontend**: Netlify (FREE)
- **Backend**: Render (FREE tier)

### **Option 3: GitHub Pages + Heroku**
- **Frontend**: GitHub Pages (FREE)
- **Backend**: Heroku (FREE dynos)

### **Option 4: All-in-One Solutions**
- **Streamlit Cloud**: Convert to Streamlit app (FREE)
- **Hugging Face Spaces**: Deploy as Gradio app (FREE)

---

## 📝 **Production Checklist**

### **Security**
- [ ] Add rate limiting
- [ ] Validate file types
- [ ] Limit file sizes
- [ ] Add API authentication

### **Performance**
- [ ] Add caching
- [ ] Optimize images
- [ ] Minify CSS/JS
- [ ] Use CDN

### **Monitoring**
- [ ] Add error tracking
- [ ] Set up logging
- [ ] Monitor API usage
- [ ] Add health checks

---

## 🔐 **Environment Variables**

### **Backend (.env)**
```
GEMINI_API_KEY=your_api_key
CORS_ORIGINS=https://your-frontend-url.vercel.app
```

### **Frontend (.env)**
```
REACT_APP_API_URL=https://your-backend-url.railway.app
```

---

## 📱 **Custom Domain Setup**

### **Vercel (Frontend)**
1. Go to Project Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed

### **Railway (Backend)**
1. Go to Project Settings → Domains
2. Add custom domain
3. Update DNS CNAME record

---

## 🚨 **Common Issues & Solutions**

### **CORS Errors**
```python
# Update backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-frontend-url.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### **API Key Issues**
- Store API keys in platform environment variables
- Never commit API keys to Git
- Use different keys for development/production

### **Build Failures**
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Check for missing environment variables

---

## 💰 **Cost Breakdown**

| Platform | Service | FREE Tier | Paid Tier |
|----------|---------|-----------|-----------|
| Vercel | Frontend | Unlimited | $20/month |
| Railway | Backend | $5 credit | $5/month |
| Netlify | Frontend | 100GB | $19/month |
| Render | Backend | 750 hours | $7/month |

**Total Monthly Cost: $0** (using free tiers)

---

## 🎯 **Quick Deploy Commands**

```bash
# 1. Prepare backend
cd backend
pip freeze > requirements.txt
echo "web: uvicorn main:app --host 0.0.0.0 --port $PORT" > Procfile

# 2. Prepare frontend
cd frontend
npm run build

# 3. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

---

## 🌐 **Live Example**
Once deployed, your app will be available at:
- **Frontend**: https://your-app.vercel.app
- **Backend API**: https://your-app.railway.app/docs

Users can upload PDFs and get beautiful portfolios instantly! 🎉 