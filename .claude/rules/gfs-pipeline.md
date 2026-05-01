# Claude Rules - GFS Pipeline

Use these rules when editing this repository with Claude Code.

- Keep the pipeline focused on local execution, not cloud deployment.
- Preserve the three-map scope: surface wind, 2m temperature, and 500 hPa geopotential height.
- Preserve the short 72h portfolio run with five forecast steps.
- Treat `README.md` as the human-facing source of truth.
- Prefer small, reviewable commits that explain both the code change and the agent-operation reason.
- Never add `.github/workflows/` unless the project scope explicitly changes away from local-only execution.

