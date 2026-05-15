from dataclasses import dataclass


@dataclass(frozen=True)
class PromptTask:
    id: int
    stage: str
    folder: str
    prompt: str


PROMPT_PIPELINE: list[PromptTask] = [
    PromptTask(1, "research_foundation", "research_foundation", "I am starting a dedicated research thread for [TICKER]. Retain all context in this chat. Search Yahoo Finance: summarize the last 3 major news events and the most recent earnings top-line numbers for [TICKER]. Do not hallucinate."),
    PromptTask(2, "research_foundation", "business_model", "Generate a comprehensive Deep Research Report on [TICKER]. Cover: 1. Business Model 2. Moat and Competition 3. Catalysts 4. Asymmetry Check"),
    PromptTask(3, "research_foundation", "catalysts", "Search recent news for [TICKER]. Identify the top 3 upcoming catalysts for the next 12 months. Rate each Critical, High, or Strategic."),
    PromptTask(4, "valuation_financials", "valuation", "Create a relative valuation table for [TICKER] vs top competitors including: P/S, Forward P/S, EV/EBITDA, Gross Margin, Revenue Growth, Value/Growth Score"),
    PromptTask(5, "valuation_financials", "financials", "Using management guidance calculate forward P/S and compare to TTM P/S."),
    PromptTask(6, "valuation_financials", "financials", "Calculate Rule of 40 for the last 4 quarters."),
    PromptTask(7, "valuation_financials", "historical_multiples", "Pull historical P/S ratios for last 3 years. Report min, max, average, and current position."),
    PromptTask(8, "valuation_financials", "ownership", "Analyze insider ownership and SBC as percentage of revenue."),
    PromptTask(9, "risk_red_teaming", "risk_analysis", "Act as a skeptic. Write a 3-point risk assessment focusing on: accounting irregularities, customer concentration, competitive threats"),
    PromptTask(10, "risk_red_teaming", "bear_case", "Act as a short seller. Write a 3-point short report."),
    PromptTask(11, "risk_red_teaming", "sentiment", "Summarize top retail investor tail risks from Reddit and Stocktwits."),
    PromptTask(12, "risk_red_teaming", "10k_risks", "Summarize the most unusual company-specific 10-K risk factors."),
    PromptTask(13, "risk_red_teaming", "customer_concentration", "Analyze customer revenue concentration."),
    PromptTask(14, "risk_red_teaming", "dilution", "Analyze dilution and ATM offerings."),
    PromptTask(15, "risk_red_teaming", "risk_analysis", "Critique the bull case."),
    PromptTask(16, "risk_red_teaming", "risk_analysis", "Find the last earnings miss and explain the cause and stock reaction."),
    PromptTask(17, "technical_analysis", "technicals", "Analyze weekly support and resistance levels."),
    PromptTask(18, "technical_analysis", "technicals", "Analyze 200-day MA slope and Golden/Death Cross status."),
    PromptTask(19, "technical_analysis", "technicals", "Analyze Relative Strength vs SPY."),
    PromptTask(20, "technical_analysis", "short_interest", "Analyze short interest and days to cover."),
    PromptTask(21, "technical_analysis", "sentiment", "Analyze retail sentiment."),
    PromptTask(22, "technical_analysis", "volatility", "Analyze implied volatility vs historical volatility."),
    PromptTask(23, "technical_analysis", "technicals", "Analyze recent price-volume patterns."),
    PromptTask(24, "final_verdict", "final_verdict", "Based on everything in this thread about [TICKER], give your honest assessment: Bull case, Bear case, Net view, What would change your mind?"),
    PromptTask(25, "final_verdict", "final_verdict", "Analyze asymmetry: downside risk, upside requirements, valuation floor, growth ceiling"),
    PromptTask(26, "final_verdict", "investment_rating", "Generate final investment rating: Strong Buy, Buy, Hold, Sell, Strong Sell"),
    PromptTask(27, "final_verdict", "scenario_models", "Generate probability-weighted scenarios: Bear, Base, Bull"),
]
