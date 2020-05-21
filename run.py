import uvicorn
import sys
sys.path.append("./app")
from app.main import app


def run_server():
	uvicorn.run('app.main:app', host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
	run_server()
