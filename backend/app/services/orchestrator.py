from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from app.prompts.stages import PROMPT_PIPELINE, PromptTask
from app.schemas.research import DebateInput, ResearchThreadResponse


class PromptOrchestrator:
    def __init__(self, base_dir: Path = Path("stocks")) -> None:
        self.base_dir = base_dir
        self.threads: dict[str, dict] = {}

    def create_thread(self, ticker: str) -> ResearchThreadResponse:
        thread_id = str(uuid.uuid4())
        normalized_ticker = ticker.upper().strip()
        self.threads[thread_id] = {
            "thread_id": thread_id,
            "ticker": normalized_ticker,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "events": [],
            "thesis": "initiated",
        }
        self._ensure_folder_tree(normalized_ticker)
        self._save_thread_memory(thread_id)
        return ResearchThreadResponse(thread_id=thread_id, ticker=normalized_ticker, status="running")

    def run_full_pipeline(self, thread_id: str) -> None:
        thread = self.threads[thread_id]
        for task in PROMPT_PIPELINE:
            filled_prompt = task.prompt.replace("[TICKER]", thread["ticker"])
            response = self._run_task(thread_id, task, filled_prompt)
            self._save_task_output(thread["ticker"], task, response)
            thread["events"].append({"task": task.id, "stage": task.stage, "status": "completed"})
            thread["thesis"] = f"updated_after_prompt_{task.id}"
            self._save_thread_memory(thread_id)

    def process_debate_input(self, thread_id: str, debate_input: DebateInput) -> None:
        thread = self.threads[thread_id]
        thread["events"].append(
            {
                "type": "debate",
                "source": debate_input.source_label,
                "text": debate_input.text,
                "at": datetime.now(timezone.utc).isoformat(),
            }
        )
        thread["thesis"] = "reweighted_after_user_challenge"
        self._save_thread_memory(thread_id)

    def _run_task(self, thread_id: str, task: PromptTask, prompt: str) -> dict:
        return {
            "thread_id": thread_id,
            "task": task.id,
            "stage": task.stage,
            "prompt": prompt,
            "analysis": "Model execution placeholder. Integrate Claude Opus 4.7 + tool adapters here.",
            "sources": ["sec_edgar", "yahoo_finance", "polygon", "finnhub"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def _ensure_folder_tree(self, ticker: str) -> None:
        folders = [
            "research_foundation", "valuation", "financials", "risk_analysis", "technicals", "sentiment",
            "competitors", "sec_filings", "final_verdict", "uploads", "chat_memory", "business_model", "moat",
            "catalysts", "historical_multiples", "ownership", "bear_case", "10k_risks", "dilution",
            "customer_concentration", "short_interest", "volatility", "investment_rating", "scenario_models"
        ]
        for folder in folders:
            (self.base_dir / ticker / folder).mkdir(parents=True, exist_ok=True)

    def _save_task_output(self, ticker: str, task: PromptTask, response: dict) -> None:
        destination = self.base_dir / ticker / task.folder / f"prompt_{task.id}.json"
        destination.write_text(json.dumps(response, indent=2))

    def _save_thread_memory(self, thread_id: str) -> None:
        thread = self.threads[thread_id]
        memory_path = self.base_dir / thread["ticker"] / "chat_memory" / f"{thread_id}.json"
        memory_path.write_text(json.dumps(thread, indent=2))


orchestrator = PromptOrchestrator()
