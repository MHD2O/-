from pathlib import Path

BASE_DIR = Path(__file__).parent

TEMPLATE_FOLDER = BASE_DIR / "templates"
OUTPUT_FOLDER = BASE_DIR / "output"

OUTPUT_FOLDER.mkdir(exist_ok=True)
