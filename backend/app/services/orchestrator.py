from __future__ import annotations
from pathlib import Path
from typing import List
from app.core.prompts import PROMPTS
from app.schemas.research import StageResult

class PromptOrchestrator:
    def __init__(self, storage_root: str = "stocks") -> None:
        self.storage_root = Path(storage_root)

    def run_research(self, ticker: str) -> List[StageResult]:
        results: List[StageResult] = []
        for spec in PROMPTS:
            prompt = spec.prompt_template.format(ticker=ticker.upper())
            output = (
                f"[SIMULATED] {spec.agent} processed prompt {spec.id} for {ticker.upper()}. "
                "Integrate live model + data providers in production."
            )
            stage_result = StageResult(
                stage=spec.stage,
                prompt_id=spec.id,
                agent=spec.agent,
                prompt=prompt,
                output=output,
                sources=[],
            )
            self._persist_result(ticker.upper(), spec.save_dir, stage_result)
            results.append(stage_result)
        return results

    def _persist_result(self, ticker: str, save_dir: str, result: StageResult) -> None:
        base = self.storage_root / ticker.lower()
        for folder in [
            "research_foundation", "valuation", "financials", "risk_analysis", "technicals",
            "sentiment", "competitors", "sec_filings", "final_verdict", "uploads", "chat_memory",
            "business_model", "moat", "catalysts", "historical_multiples", "ownership", "bear_case",
            "10k_risks", "dilution", "customer_concentration", "short_interest", "volatility",
            "investment_rating", "scenario_models",
        ]:
            (base / folder).mkdir(parents=True, exist_ok=True)

        target = base / save_dir / f"prompt_{result.prompt_id}.md"
        target.write_text(
            f"# Prompt {result.prompt_id} - {result.agent}\n\n"
            f"## Prompt\n{result.prompt}\n\n"
            f"## Output\n{result.output}\n"
        )
