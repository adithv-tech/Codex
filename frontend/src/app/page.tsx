'use client';
import { useState } from 'react';

export default function Home() {
  const [ticker, setTicker] = useState('NVDA');
  return (
    <main className="min-h-screen bg-black text-green-200 p-8">
      <h1 className="text-3xl font-bold mb-6">Autonomous Hedge Fund Research OS</h1>
      <form action={`/dashboard/${ticker.toUpperCase()}`}>
        <input className="bg-zinc-900 border border-zinc-700 px-4 py-2 mr-3" value={ticker} onChange={(e)=>setTicker(e.target.value)} />
        <button className="bg-green-700 px-4 py-2">Launch Research Thread</button>
      </form>
    </main>
  );
}
