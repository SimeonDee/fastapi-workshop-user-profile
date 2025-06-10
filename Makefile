# Variable names
APP_NAME = app
APP_MODULE_NAME = main
VENV_NAME = .venv
HOST = 0.0.0.0
PORT = 8000

# Create a virtual env
venv:
	uv venv $(VENV_NAME)

# Activate virtual env (for unix systems e.g. Linux, MacOS)
activate:
	source $(VENV_NAME)/bin/activate

# Deactivate virtual env
deactivate:
	deactivate

# Activate virtual env (for unix systems e.g. Linux, MacOS)
activate-windows:
	$(VENV_NAME)/Scripts/activate.bat

# Install dependencies
install:
	uv pip install -r requirements.txt

# Run the FastAPI app in PROD env
run:
	uvicorn $(APP_MODULE_NAME):$(APP_NAME) --host $(HOST)

# Run the FastAPI app in Dev env
run-dev:
	uvicorn $(APP_MODULE_NAME):$(APP_NAME) --port $(PORT) --reload

# Clean up
clean:
	rm -rf $(VENV_NAME)
	rm -rf __pycache__