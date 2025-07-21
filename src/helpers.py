import subprocess
from time import sleep
import psutil


def is_mlflow_running(port=8080):
    for process in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
        try:
            cmdline = process.info["cmdline"]
            if cmdline and "mlflow" in cmdline and f"--port {port}" in " ".join(cmdline):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False


def start_mlflow_server():
    port = 8080
    if not is_mlflow_running(port):
        subprocess.Popen(
            ["uv", "run", "mlflow", "server", "--host", "127.0.0.1", "--port", str(port)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        sleep(3)
        print(f"MLflow server started at http://127.0.0.1:{port}")
    else:
        print(f"MLflow server is already running on port {port}")
