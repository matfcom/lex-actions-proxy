from fastapi import FastAPI
import httpx

app = FastAPI(
    title="API Jurídica Española Completa",
    description="Consulta BOE, jurisprudencia, plazos, tasas y simuladores legales.",
    version="1.1.0"
)

@app.get("/datosabiertos/api/boe/sumario/{fecha}")
def obtener_sumario_boe(fecha: str):
    url = f"https://www.boe.es/datosabiertos/api/boe/sumario/{fecha}"
    headers = {"Accept": "application/json"}
    try:
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": {"code": 500, "text": "Error"}, "error": str(e)}

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

@app.get("/jurisprudencia/buscar")
def buscar_jurisprudencia(consulta: str):
    return {"resultados": [
        {"titulo": "Sentencia 1", "resumen": "Resumen 1", "enlace": "https://lexgpt.dev/fake1"},
        {"titulo": "Sentencia 2", "resumen": "Resumen 2", "enlace": "https://lexgpt.dev/fake2"}
    ]}

@app.get("/plazos-procesales/consulta")
def consultar_plazos_procesales(procedimiento: str):
    return {"plazo": "20 días hábiles"}

@app.get("/tasas-judiciales/calcular")
def calcular_tasas_judiciales(tipoProcedimiento: str):
    return {"importe": "135€"}

@app.get("/simuladores/indemnizacion")
def simular_indemnizacion(antiguedad: int, salarioMensual: float):
    indemnizacion = antiguedad * salarioMensual * 0.05
    return {"indemnizacion": indemnizacion}
