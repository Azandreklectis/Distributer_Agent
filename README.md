# Distributor Agent (LangChain + Gemini)

Simple web app for your distributor AI concept:
- Shows a **product catalog** on a local site.
- Lets you **ask questions directly** to a Gemini-powered sales assistant grounded in your product data.

## 1) Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set your Gemini key in `.env`. You can also set `EMBEDDING_MODEL` if your account supports a different embeddings model.

## 2) Run the site

```bash
python main.py
```

Open `http://localhost:8000`.

## 3) What you can do

1. View product cards from `data/sample_products.json`.
2. Ask pricing/margin/offer questions in the text box.
3. Get grounded responses using vector search + Gemini.

## 4) Replace with your own catalog

Update `data/sample_products.json` using this structure per product:

```json
{
  "sku": "BIS-001",
  "name": "Crispy Butter Biscuits 200g",
  "category": "Biscuits",
  "mrp": 40,
  "distributor_price": 31,
  "retailer_margin_percent": 22.5,
  "moq": 24,
  "shelf_life_days": 180,
  "benefits": ["High repeat purchase"],
  "offers": ["Buy 10 boxes get 1 free"],
  "source": "launch-sheet-july"
}
```

Restart the app after editing data.

## 5) GitHub sync checklist (if repo looks outdated)

If changes are visible locally but not on GitHub, verify:

```bash
git log --oneline -n 5
git remote -v
```

If `git remote -v` is empty, add your GitHub repo remote first:

```bash
git remote add origin <your-github-repo-url>
```

Then push your current branch:

```bash
git push -u origin HEAD
```

If remote exists but GitHub still looks old, run:

```bash
git fetch origin
git status
```

and confirm you are on the branch you actually pushed.
