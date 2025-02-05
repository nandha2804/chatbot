from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import products, suppliers, chatbot

app = FastAPI(title="AI-Powered Chatbot for Supplier and Product Information")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(products.router, prefix="/api", tags=["Products"])
app.include_router(suppliers.router, prefix="/api", tags=["Suppliers"])
app.include_router(chatbot.router, prefix="/api", tags=["Chatbot"])

@app.get("/")
def root():
    return {"message": "Welcome to the AI-Powered Chatbot API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
