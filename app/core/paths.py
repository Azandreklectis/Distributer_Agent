from pathlib import Path

# /repo_root/app/core/paths.py -> repo root is parents[2]
REPO_ROOT = Path(__file__).resolve().parents[2]
APP_DIR = REPO_ROOT / "app"
DATA_DIR = REPO_ROOT / "data"
PROMPTS_DIR = APP_DIR / "prompts"
WEB_DIR = APP_DIR / "web"
WEB_STATIC_DIR = WEB_DIR / "static"
WEB_TEMPLATES_DIR = WEB_DIR / "templates"
