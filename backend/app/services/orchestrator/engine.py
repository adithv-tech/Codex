from collections.abc import AsyncGenerator
from app.models.research import StageResult
from app.prompts.stages import STAGES
from app.services.storage.filesystem import save_stage_output

class PromptOrchestrator:
    async def run(self, ticker: str) -> AsyncGenerator[StageResult, None]:
        thread_summary = []
        for stage, prompts in STAGES.items():
            for prompt in prompts:
                content = self._simulate_agent_output(ticker, prompt.text, thread_summary)
                output_path = save_stage_output(ticker, prompt.folder, prompt.id, content)
                thread_summary.append(f"P{prompt.id}: {content[:120]}")
                yield StageResult(
                    stage=stage,
                    prompt_id=prompt.id,
                    agent=prompt.agent,
                    output_path=output_path,
                    status="completed",
                    content=content,
                )

    def _simulate_agent_output(self, ticker: str, prompt: str, memory: list[str]) -> str:
        return (
            f"# {ticker} Prompt Execution\n\n"
            f"Prompt: {prompt.replace('[TICKER]', ticker)}\n\n"
            f"Context used: {len(memory)} prior findings\n"
            "- Sources required: SEC EDGAR, Yahoo Finance, Polygon, Finnhub, Reddit, Stocktwits\n"
            "- Hallucination policy: require citation-backed claims and confidence tagging\n"
            "- Thesis update: compare with prior stage outputs and revise probabilities\n"
        )
