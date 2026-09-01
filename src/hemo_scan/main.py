from fastapi import FastAPI

from hemo_scan.api.routes import health

app = FastAPI(title="hemo-scan")
app.include_router(health.router)