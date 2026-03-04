import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_settings():
    env = os.getenv("ENV", "qa")
    with open(f"config/envs/{env}.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    base_url = os.getenv("BASE_URL", data["base_url"])
    timeout = int(os.getenv("TIMEOUT_SECONDS", data.get("timeout_seconds", 15)))
    api_key = os.getenv("API_KEY", "")

    return {
        "env": env,
        "base_url": base_url.rstrip("/"),
        "timeout": timeout,
        "api_key": api_key,
    }
