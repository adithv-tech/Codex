interface Props { params: { ticker: string } }
export default function Dashboard({ params }: Props) {
  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 p-6 grid grid-cols-3 gap-4">
      <section className="col-span-2 border border-zinc-800 p-4 rounded">Live Prompt Stream: {params.ticker}</section>
      <aside className="border border-zinc-800 p-4 rounded">Debate Panel + Thesis Timeline</aside>
      <section className="border border-zinc-800 p-4 rounded">Valuation Heatmap</section>
      <section className="border border-zinc-800 p-4 rounded">Risk Meter</section>
      <section className="border border-zinc-800 p-4 rounded">TradingView Widget Placeholder</section>
    </div>
  );
}
