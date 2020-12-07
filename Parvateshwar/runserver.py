import os
from src import app

if __name__ == "__main__":
	HOST = os.environ.get("SERVER_HOST","localhost")
	try:
		PORT = int(os.environ.get("SERVER_PORT", "1324"))
	except ValueError:
		PORT = 1234
	app.run(HOST, PORT, debug=True)