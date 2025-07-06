
import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import './App.css';

function App() {
  const [htmlContent, setHtmlContent] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [fileName, setFileName] = useState('');

  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) {
      return;
    }

    setFileName(file.name);
    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      const response = await fetch(`${apiUrl}/upload-pdf/`, {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const html = await response.text();
        setHtmlContent(html);
      } else {
        console.error('Failed to upload file');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
    }
    setIsLoading(false);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, accept: '.pdf' });

  const handleDownload = () => {
    const blob = new Blob([htmlContent], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'portfolio.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="header-content">
          <div className="logo-section">
            <div className="logo-icon">P</div>
            <div>
              <h1 className="header-title">Portfolio Generator</h1>
              <p className="header-subtitle">Transform your resume into a professional portfolio</p>
            </div>
          </div>
        </div>
      </header>
      
      <main className="main-content">
        <div className="upload-section">
          <h2 className="section-title">Create Your Portfolio</h2>
          <p className="section-subtitle">
            Upload your PDF resume and we'll generate a beautiful, professional portfolio website for you
          </p>
          
          <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''}`}>
            <input {...getInputProps()} />
            <div className="dropzone-content">
              <div className="upload-icon">
                📄
              </div>
              {fileName ? (
                <div className="file-name">{fileName}</div>
              ) : (
                <>
                  <p className="dropzone-text">Drag & drop your PDF resume here</p>
                  <p className="dropzone-subtext">or click to browse files</p>
                </>
              )}
            </div>
          </div>
        </div>
        
        {isLoading && (
          <div className="loading">
            <div className="loading-spinner"></div>
            <p className="loading-text">Generating your portfolio...</p>
          </div>
        )}
        
        {htmlContent && (
          <div className="preview-container">
            <div className="preview-header">
              <h2 className="preview-title">Your Portfolio Preview</h2>
              <button className="download-btn" onClick={handleDownload}>
                ⬇️ Download Portfolio
              </button>
            </div>
            <iframe srcDoc={htmlContent} title="Portfolio Preview" className="preview-iframe" />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
