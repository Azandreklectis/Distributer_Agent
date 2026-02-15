# Distributor Agent (LangChain + Gemini)

A from-scratch starter project for building an AI distributor system:
- **Knowledge Agent**: creates and updates product KB.
- **Sales Agent**: chats with shopkeepers, resolves product questions, and nudges toward order intent.

## 1) Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set your Gemini API key in `.env`.

## 2) Run API

```bash
python main.py
```

Server: `http://localhost:8000`

## 3) Load product knowledge

```bash
curl -X POST http://localhost:8000/kb/products \
  -H "Content-Type: application/json" \
  -d @<(python - <<'PY'
import json
from pathlib import Path
print(json.dumps({"products": json.loads(Path('data/sample_products.json').read_text())}))
PY
)
```

## 4) Chat endpoint

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "shopkeeper_id": "shop-101",
    "message": "What margin do I get on BIS-001 and do you have any offer?",
    "language": "en"
  }'
```

## 5) Next upgrades

- Add WhatsApp connector
- Add CRM sync for lead/order creation
- Add multilingual prompting and regional scripts
- Add LangGraph state machine for robust multi-step sales flows
