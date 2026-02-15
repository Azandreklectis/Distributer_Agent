from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict

LEADS_FILE = Path("data/leads.ndjson")


def create_order_lead(shopkeeper_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)

    lead = {
        "created_at": datetime.utcnow().isoformat(),
        "shopkeeper_id": shopkeeper_id,
        "payload": payload,
        "status": "new",
    }

    with LEADS_FILE.open("a", encoding="utf-8") as fp:
        fp.write(json.dumps(lead, ensure_ascii=False) + "\n")

    return lead
