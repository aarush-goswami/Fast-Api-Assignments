import os
from dotenv import load_dotenv
from supabase import Client,create_client

load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_key or not supabase_url:
    raise RuntimeError(
        "SUPABASE_URL and SUPABASE_KEY are required"
    )
supabase:Client = create_client(supabase_url,supabase_key)