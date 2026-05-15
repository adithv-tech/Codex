from dataclasses import dataclass

@dataclass(frozen=True)
class PromptSpec:
    id: int
    agent: str
    folder: str
    text: str

STAGES: dict[int, list[PromptSpec]] = {
    1: [
        PromptSpec(1, "Foundation Research Agent", "research_foundation", "I am starting a dedicated research thread for [TICKER]..."),
        PromptSpec(2, "Foundation Research Agent", "business_model", "Generate a comprehensive Deep Research Report on [TICKER]..."),
        PromptSpec(3, "Foundation Research Agent", "catalysts", "Search recent news for [TICKER]. Identify top 3 upcoming catalysts..."),
    ],
    2: [
        PromptSpec(4, "Valuation Agent", "valuation", "Create a relative valuation table for [TICKER] vs top competitors..."),
        PromptSpec(5, "Valuation Agent", "financials", "Using management guidance calculate forward P/S..."),
        PromptSpec(6, "Valuation Agent", "financials", "Calculate Rule of 40 for the last 4 quarters."),
        PromptSpec(7, "Valuation Agent", "historical_multiples", "Pull historical P/S ratios for last 3 years..."),
        PromptSpec(8, "Valuation Agent", "ownership", "Analyze insider ownership and SBC as percentage of revenue."),
    ],
    3: [
        PromptSpec(9, "Bear Thesis Agent", "risk_analysis", "Act as a skeptic. Write a 3-point risk assessment..."),
        PromptSpec(10, "Bear Thesis Agent", "bear_case", "Act as a short seller. Write a 3-point short report."),
        PromptSpec(11, "Sentiment Agent", "risk_analysis", "Summarize top retail investor tail risks from Reddit and Stocktwits."),
        PromptSpec(12, "SEC Filing Agent", "10k_risks", "Summarize the most unusual company-specific 10-K risk factors."),
        PromptSpec(13, "SEC Filing Agent", "customer_concentration", "Analyze customer revenue concentration."),
        PromptSpec(14, "SEC Filing Agent", "dilution", "Analyze dilution and ATM offerings."),
        PromptSpec(15, "Bear Thesis Agent", "bear_case", "Critique the bull case."),
        PromptSpec(16, "Foundation Research Agent", "risk_analysis", "Find the last earnings miss and explain cause + stock reaction."),
    ],
    4: [
        PromptSpec(17, "Technical Analysis Agent", "technicals", "Analyze weekly support and resistance levels."),
        PromptSpec(18, "Technical Analysis Agent", "technicals", "Analyze 200-day MA slope and Golden/Death Cross status."),
        PromptSpec(19, "Technical Analysis Agent", "technicals", "Analyze Relative Strength vs SPY."),
        PromptSpec(20, "Technical Analysis Agent", "short_interest", "Analyze short interest and days to cover."),
        PromptSpec(21, "Sentiment Agent", "sentiment", "Analyze retail sentiment."),
        PromptSpec(22, "Technical Analysis Agent", "volatility", "Analyze implied volatility vs historical volatility."),
        PromptSpec(23, "Technical Analysis Agent", "technicals", "Analyze recent price-volume patterns."),
    ],
    5: [
        PromptSpec(24, "Final Verdict Agent", "final_verdict", "Based on everything in this thread about [TICKER]..."),
        PromptSpec(25, "Final Verdict Agent", "final_verdict", "Analyze asymmetry: downside risk, upside requirements..."),
        PromptSpec(26, "Final Verdict Agent", "investment_rating", "Generate final investment rating..."),
        PromptSpec(27, "Final Verdict Agent", "scenario_models", "Generate probability-weighted scenarios..."),
    ],
}
