from fastapi import FastAPI,HTTPException,status
from database import supabase

app = FastAPI(
    title="Supabase Products API", 
    description="Fetch product records from Supabase using FastAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "Message": "fastApi with supabase is running"
    }
    
@app.get("/products")
def get_products():
    try :
        response = supabase.table("Products").select('*').order("id").execute()
        return response.data
    except Exception as error:
        print(f"Error : {error}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Table details not found"
        )