"""
Startup script for the flood detection backend API
"""

import os
import sys
import uvicorn
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

if __name__ == "__main__":
  port = int(os.getenv("PORT", 8000))
  host = os.getenv("HOST", "localhost")

  print(f"Starting Flood Analyzer API on {host}:{port}...")
  print("API Documentation available at:")
  print(f"  - Swagger UI: http://{host}:{port}/docs")
  print(f"  - ReDoc: http://{host}:{port}/redoc")
  print(f"  - OpenAPI JSON: http://{host}:{port}/openapi.json")

  uvicorn.run(
    'main:app', 
    host=host, 
    port=port, 
    reload=True, 
    log_level="info"
  )
