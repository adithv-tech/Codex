from dataclasses import dataclass

@dataclass(frozen=True)
class PromptSpec:
    id: int
    stage: str
    agent: str
    prompt_template: str
    save_dir: str

PROMPTS = [
    PromptSpec(1, "research_foundation", "Foundation Research Agent", "I am starting a dedicated research thread for {ticker}. Retain all context in this chat. Search Yahoo Finance: summarize the last 3 major news events and the most recent earnings top-line numbers for {ticker}. Do not hallucinate.", "research_foundation"),
    PromptSpec(2, "research_foundation", "Foundation Research Agent", "Generate a comprehensive Deep Research Report on {ticker}. Cover: 1. Business Model 2. Moat and Competition 3. Catalysts 4. Asymmetry Check", "business_model"),
    PromptSpec(3, "research_foundation", "Catalyst Agent", "Search recent news for {ticker}. Identify the top 3 upcoming catalysts for the next 12 months. Rate each Critical, High, or Strategic.", "catalysts"),
    PromptSpec(4, "valuation_financials", "Valuation Agent", "Create a relative valuation table for {ticker} vs top competitors including: P/S, Forward P/S, EV/EBITDA, Gross Margin, Revenue Growth, Value/Growth Score", "valuation"),
    PromptSpec(5, "valuation_financials", "Valuation Agent", "Using management guidance calculate forward P/S and compare to TTM P/S.", "financials"),
    PromptSpec(6, "valuation_financials", "Valuation Agent", "Calculate Rule of 40 for the last 4 quarters.", "financials"),
    PromptSpec(7, "valuation_financials", "Valuation Agent", "Pull historical P/S ratios for last 3 years. Report min, max, average, and current position.", "historical_multiples"),
    PromptSpec(8, "valuation_financials", "SEC Filing Agent", "Analyze insider ownership and SBC as percentage of revenue.", "ownership"),
    PromptSpec(9, "risk_red_team", "Bear Thesis Agent", "Act as a skeptic. Write a 3-point risk assessment focusing on: accounting irregularities, customer concentration, competitive threats", "risk_analysis"),
    PromptSpec(10, "risk_red_team", "Bear Thesis Agent", "Act as a short seller. Write a 3-point short report.", "bear_case"),
    PromptSpec(11, "risk_red_team", "Sentiment Agent", "Summarize top retail investor tail risks from Reddit and Stocktwits.", "risk_analysis"),
    PromptSpec(12, "risk_red_team", "SEC Filing Agent", "Summarize the most unusual company-specific 10-K risk factors.", "10k_risks"),
    PromptSpec(13, "risk_red_team", "SEC Filing Agent", "Analyze customer revenue concentration.", "customer_concentration"),
    PromptSpec(14, "risk_red_team", "SEC Filing Agent", "Analyze dilution and ATM offerings.", "dilution"),
    PromptSpec(15, "risk_red_team", "Bear Thesis Agent", "Critique the bull case.", "bear_case"),
    PromptSpec(16, "risk_red_team", "Foundation Research Agent", "Find the last earnings miss and explain the cause and stock reaction.", "risk_analysis"),
    PromptSpec(17, "technicals", "Technical Analysis Agent", "Analyze weekly support and resistance levels.", "technicals"),
    PromptSpec(18, "technicals", "Technical Analysis Agent", "Analyze 200-day MA slope and Golden/Death Cross status.", "technicals"),
    PromptSpec(19, "technicals", "Technical Analysis Agent", "Analyze Relative Strength vs SPY.", "technicals"),
    PromptSpec(20, "technicals", "Technical Analysis Agent", "Analyze short interest and days to cover.", "short_interest"),
    PromptSpec(21, "technicals", "Sentiment Agent", "Analyze retail sentiment.", "sentiment"),
    PromptSpec(22, "technicals", "Technical Analysis Agent", "Analyze implied volatility vs historical volatility.", "volatility"),
    PromptSpec(23, "technicals", "Technical Analysis Agent", "Analyze recent price-volume patterns.", "technicals"),
    PromptSpec(24, "final_verdict", "Final Verdict Agent", "Based on everything in this thread about {ticker}, give your honest assessment: Bull case, Bear case, Net view, What would change your mind?", "final_verdict"),
    PromptSpec(25, "final_verdict", "Final Verdict Agent", "Analyze asymmetry: downside risk, upside requirements, valuation floor, growth ceiling", "scenario_models"),
    PromptSpec(26, "final_verdict", "Final Verdict Agent", "Generate final investment rating: Strong Buy, Buy, Hold, Sell, Strong Sell", "investment_rating"),
    PromptSpec(27, "final_verdict", "Final Verdict Agent", "Generate probability-weighted scenarios: Bear, Base, Bull", "scenario_models"),
]
