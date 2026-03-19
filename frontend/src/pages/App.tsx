import React, { useState } from 'react'

export default function App() {
  const [log, setLog] = useState('Failed login attempts detected from 185.220.101.1 followed by PowerShell execution and possible CVE-2024-3094 exploitation.')
  const [result, setResult] = useState<any>(null)

  const analyze = async () => {
    const res = await fetch('http://localhost:8000/api/v1/analyze-log', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ source: 'EDR', raw_log: log })
    })
    const data = await res.json()
    setResult(data)
  }

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: 24, maxWidth: 1000, margin: '0 auto' }}>
      <h1>GenAI Cybersecurity Cloud SOC Copilot</h1>
      <p>Analyze security alerts, prompt quality, and incident playbooks.</p>
      <textarea
        rows={10}
        value={log}
        onChange={(e) => setLog(e.target.value)}
        style={{ width: '100%', marginTop: 12, padding: 12 }}
      />
      <br />
      <button onClick={analyze} style={{ marginTop: 12, padding: '10px 16px', cursor: 'pointer' }}>
        Analyze Log
      </button>
      {result && (
        <div style={{ marginTop: 24, border: '1px solid #ddd', padding: 16, borderRadius: 8 }}>
          <h2>Analysis Result</h2>
          <p><strong>Summary:</strong> {result.summary}</p>
          <p><strong>Severity:</strong> {result.severity}</p>
          <p><strong>Risk Score:</strong> {result.risk_score}</p>
          <p><strong>IOCs:</strong> {result.iocs?.join(', ')}</p>
          <p><strong>Patterns:</strong> {result.attack_patterns?.join(', ')}</p>
          <p><strong>Prompt:</strong> {result.analyst_prompt}</p>
        </div>
      )}
    </div>
  )
}
