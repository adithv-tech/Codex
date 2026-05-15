from pathlib import Path

BASE = Path("stocks")
REQUIRED_DIRS = [
    "research_foundation", "valuation", "financials", "risk_analysis", "technicals",
    "sentiment", "competitors", "sec_filings", "final_verdict", "uploads", "chat_memory",
    "business_model", "moat", "catalysts", "historical_multiples", "ownership", "bear_case",
    "10k_risks", "dilution", "customer_concentration", "volatility", "short_interest",
    "investment_rating", "scenario_models"
]

def ensure_ticker_dirs(ticker: str) -> Path:
    root = BASE / ticker.upper()
    for d in REQUIRED_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)
    return root

def save_stage_output(ticker: str, folder: str, prompt_id: int, text: str) -> str:
    root = ensure_ticker_dirs(ticker)
    path = root / folder / f"prompt_{prompt_id:02d}.md"
    path.write_text(text)
    return str(path)
