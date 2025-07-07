from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/datosabiertos/api/legislacion-consolidada/id/{boe_id}/texto/bloque/{bloque_id}")
def obtener_articulo_legislacion(boe_id: str, bloque_id: str):
    url = f"https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{boe_id}/texto/bloque/{bloque_id}"
    headers = {"Accept": "application/json"}
    try:
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
