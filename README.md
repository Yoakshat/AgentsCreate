# AgentsCreate 🤖✨

**AI agents that collaborate to build useful software — judged by the only metric that matters: GitHub stars.**

## The Vision

What if AI agents could:
- **Decide** what's worth building
- **Collaborate** to write the code
- **Ship** real repositories to GitHub
- **Learn** from what resonates (stars, forks, usage)

This is natural selection for AI-generated software. Build, ship, let the market decide.

## How It Works

```
┌─────────────────────────────────────────────────────┐
│                   COORDINATOR                        │
│         Decides priorities, assigns tasks            │
└─────────────────────┬───────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │ Builder │   │ Builder │   │ Builder │
   │ Agent 1 │   │ Agent 2 │   │ Agent 3 │
   └────┬────┘   └────┬────┘   └────┬────┘
        │             │             │
        ▼             ▼             ▼
   [ GitHub Repos — Published & Public ]
                      │
                      ▼
              ┌──────────────┐
              │   Observer   │
              │ Tracks stars │
              │ Reports back │
              └──────────────┘
```

## Core Principles

1. **Real Output** — No mock projects. Real repos, real code, real users.
2. **Market Feedback** — Stars are the fitness function. Useful things get starred.
3. **Agent Autonomy** — Agents propose, debate, and decide what to build.
4. **Continuous Learning** — What worked? What flopped? Iterate.

## Tech Stack

Built with [OpenClaw](https://openclaw.ai) — AI agents with real tool access.

- **Multi-agent coordination** via `sessions_spawn` and `sessions_send`
- **GitHub integration** via `gh` CLI
- **Scheduled tasks** via cron jobs
- **Web research** to identify opportunities

## Status

🚧 **Early Development** — Building the foundation.

## Author

Created by [@Yoakshat](https://github.com/Yoakshat)

---

*Let the agents cook.* 🍳
