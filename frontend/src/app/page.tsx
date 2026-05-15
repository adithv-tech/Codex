export default function HomePage() {
  return (
    <main className="min-h-screen bg-zinc-950 text-zinc-100 p-8">
      <h1 className="text-3xl font-semibold">Autonomous Stock Research OS</h1>
      <p className="mt-3 text-zinc-400">Bloomberg x Apple inspired institutional dashboard scaffold.</p>
      <section className="mt-8 grid gap-4 md:grid-cols-3">
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-4">Ticker Input + Run Button</div>
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-4">Thesis Timeline Widget</div>
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-4">AI Debate Panel</div>
      </section>
    </main>
  );
}
