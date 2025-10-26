from fastapi import FastAPI
from supabase import create_client
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def home():
    return {"mensagem": "API de propostas está ativa!"}

@app.get("/propostas")
def listar_propostas():
    res = supabase.table("propostas").select("id_proposta").execute()
    return res.data

@app.get("/propostas/{id_proposta}")
def obter_proposta(id_proposta: str):
    res = supabase.table("propostas").select("*").eq("id_proposta", id_proposta).execute()
    if res.data:
        return res.data[0]
    return {"erro": "Proposta não encontrada"}
