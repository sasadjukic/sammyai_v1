# Common Installation & Setup Issues

This document outlines potential barriers users may encounter during the initial installation and configuration of SammyAI. Ensuring your environment meets these requirements is essential for a smooth experience.

## Hardware & System Requirements

### GPU & VRAM Constraints
Running local models like `Gemma 3:4B` via Ollama requires significant hardware resources.
*   **Recommendation:** A minimum of **8GB VRAM** is recommended for fluid local inference. 
*   **Symptoms:** If your system lacks sufficient VRAM, you may experience extreme latency (tokens per second), frequent model crashes, or failure to load the model entirely.

### RAM & Storage
*   **Disk Space:** Local models and the RAG (Retrieval-Augmented Generation) index database require significant disk space. Ensure at least **10GB of free space** for the base installation and local weights.
*   **System RAM:** A minimum of **16GB System RAM** is recommended to handle both the application UI and the underlying embedding processes.

## Dependency Management

### Python Environment (Source Installation)
When installing from source, missing or mismatched dependencies are common.
*   **Incomplete `requirements.txt`:** Always run `pip install -r requirements.txt` within a dedicated virtual environment (`venv`) to avoid system-wide library conflicts.
*   **Python Version:** SammyAI requires **Python 3.10+**. Earlier versions may lack support for newer asynchronous features or specific Type Hinting used in the codebase.

### Docker Environment
*   **GPU Pass-through:** If using Docker for local model execution, ensure you have the `nvidia-container-toolkit` installed and configured to allow the container to access your host's GPU.
*   **Port Conflicts:** By default, SammyAI may attempt to bind to specific ports for its UI or local API services. Ensure these ports are not occupied by other applications.

## Model Configuration & LLM Setup

### Local Model Initialization (Ollama)
*   **Missing Weights:** If `Gemma 3:4B` is selected but hasn't been "pulled" via Ollama, the application will return a runtime error. 
*   **Action Required:** Run `ollama pull gemma3:4b` in your terminal before launching SammyAI to ensure the weights are cached locally.

### Cloud Provider API Keys
Cloud models (Gemini-2.5-Flash, DeepSeek V3.2, etc.) require valid authentication tokens.
*   **Credential Errors:** Failure to provide an API key via the `API Key` icon in the toolbar will prevent communication with cloud providers.
*   **Quota Limits:** If your API key is valid but you receive "429 Too Many Requests" errors, you have likely reached the rate limit for your specific tier (especially common on free accounts).

## RAG & Database Initialization
*   **Empty Index:** Upon first launch, the RAG system will have no indexed documents. You must manually index local files (`Ctrl+Shift+I`) before features like "Conversation Context" or "Document Research" become functional.
*   **Embeddings Failures:** If the application cannot connect to the embedding service (often handled by the local Ollama instance), document indexing will fail silently or display a connection error in the status bar.
