export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 text-zinc-100 p-8">
      <h1 className="text-3xl font-semibold">Autonomous Stock Research OS</h1>
      <p className="mt-3 text-zinc-400">Institutional-grade multi-stage AI orchestration dashboard scaffold.</p>
      <section className="mt-8 grid grid-cols-3 gap-4">
        {[
          "Research Foundation",
          "Valuation & Financials",
          "Risk Red Team",
          "Technicals",
          "Final Verdict",
          "Live Debate"
        ].map((item) => (
          <div key={item} className="rounded-xl border border-zinc-800 p-4 bg-zinc-900">{item}</div>
        ))}
      </section>
    </main>
  );
}
