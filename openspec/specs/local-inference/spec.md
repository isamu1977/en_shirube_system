# local-inference Specification

## Purpose
TBD - created by archiving change use-local-mlx-server-for-tests. Update Purpose after archive.
## Requirements
### Requirement: Support for Apple MLX Inference Server

The backend MUST support connecting to a local Ollama server that exposes an OpenAI-compatible API for model inference.

#### Scenario: Switching to Ollama for testing

Given the `.env` configures `LLM_PROVIDER=ollama` and `OLLAMA_BASE_URL=http://localhost:11434/v1`
When the backend requests a chat completion
Then the request is routed to `http://localhost:11434/v1/chat/completions` using the model configured in `OLLAMA_MODEL` (e.g., `qwen3.5:9b`) without requiring real API key authentication.

