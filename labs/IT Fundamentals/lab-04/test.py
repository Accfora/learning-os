from pathlib import Path
current_directory = Path.cwd()
print("Current directory: ", current_directory)
file_path = Path("data") / "measurements.txt"
print(file_path.exists())
logs_dir = Path("logs")
print(logs_dir)
# logs_dir.mkdir(exist_ok=True)

import os
print(os.getcwd())
print(os.environ.get("USERNAME"))

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Программа запущена")
logging.warning("Предупреждение")
logging.error("Произошла ошибка")
