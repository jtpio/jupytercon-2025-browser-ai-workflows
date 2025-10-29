---
marp: true
paginate: true
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .center {
    text-align: center;
  }
  .center-table {
    display: flex;
    justify-content: center;
  }
---

<style>
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
}
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
iframe {
  border: none;
}
.prompt-box {
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 12px;
  margin: 10px 0;
  position: relative;
  font-family: monospace;
  font-size: 14px;
  color: #333;
}
.copy-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: #007acc;
  color: white;
  border: none;
  border-radius: 3px;
  padding: 4px 8px;
  cursor: pointer;
  font-size: 12px;
}
.copy-btn:hover {
  background: #005a9e;
}
</style>

<div class="center">

# Browser-based AI workflows in Jupyter

## JupyterCon 2025

### 2025-11-04

Jeremy Tuloup

</div>

---

# About

- Jeremy Tuloup
- QuantStack
- JupyterLab, Jupyter Notebook, JupyterLite

![bg fit right:33%](images/qs.svg)

---

# The AI space is moving (very) fast

- New models
- IDE integrations
- CLI, TUI
- Background agents

---

# End-user products for AI in Jupyter

## The state in 2025

- Jupyter AI: https://github.com/jupyterlab/jupyter-ai
  - Incubating under JupyterLab
  - Stable (v2) - code completions, chat, magics
  - Beta (v3) - personas (agents), MCP, RTC
- Notebook Intelligence: https://github.com/notebook-intelligence/notebook-intelligence
  - Independent project
  - GitHub copilot, agents, MCP

---

# AI integration in the browser?

- What about JupyterLite?
- Using AI models in the browser?

---

# Forward-looking view on AI in Jupyter

*One of the possible views for what AI in Jupyter can look like*.

---

# Agenda

- **JupyterLite**
- **Remote AI Models**
- **Agent Mode**
- **Model Context Protocol**
- **In-Browser LLMs**
- **Built-in AI**
- **Privacy & Limitations**
- **What's Next?**

---

# What is JupyterLite?

![bg fit right:33%](https://raw.githubusercontent.com/jupyterlite/jupyterlite/main/docs/_static/icon.svg)

> JupyterLite is a JupyterLab distribution that runs entirely in the web browser, backed by in-browser language kernels.

---

# Lightweight Jupyter running in the browser

- ✅ can be hosted as a static website
- ✅ no need to install Python and other packages on the user machine
- ✅ kernels run in the browser via WebAssembly (Pyodide, Emscripten Forge)
- ✅ easy to embed a live Python console on your website

![center h:400px](images/numpy-org.png)

---

# How to integrate AI in JupyterLite?

https://github.com/jupyterlite/ai

---

# Chat with Remote Models

Connect to AI providers, directly from your browser (without a Python server)

- Anthropic
- OpenAI
- Mistral
- Ollama
- More via extensions

---

<div class="prompt-box">
  Give me the Python code to print the Fibonacci sequence
  <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.firstChild.textContent.trim())">
    Copy
  </button>
</div>

---

# Code completion

![](images/completions.png)

---

![bg fit](images/completions-demo.png)

---

# Agent Mode

- Create new notebooks
- Tool calling
- Approve or reject tool calls

---

<div class="prompt-box">
  Create a demo notebook about pandas and matplotlib
  <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.firstChild.textContent.trim())">
    Copy
  </button>
</div>

<div class="prompt-box">
  Now clear all the outputs and run all the cells in the notebook
  <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.firstChild.textContent.trim())">
    Copy
  </button>
</div>

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/e33d7d84-53ca-4835-a034-b6757476c98b">
</video>

---

# Accept / Reject Diffs

`jupyterlab-diff` provides commands to display diffs:

- Split (side-by-side) diffs
- Unified cell diffs
- Unified file diffs

https://github.com/jupyter-ai-contrib/jupyterlab-diff

---

![a screenshot showing the diff view](images/diffs.png)

---

<div class="prompt-box">
  Use `polars` instead of `pandas` in the current notebook
  <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.firstChild.textContent.trim())">
    Copy
  </button>
</div>

<div class="prompt-box">
  Remove all comments from the current file
  <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.firstChild.textContent.trim())">
    Copy
  </button>
</div>

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/329af10f-b602-4be6-9adf-636c2fa7de94">
</video>

---

# Execute JupyterLab Commands

- Expose JupyterLab commands as `tools` to the agent:
- `discover_commands(query)` to find available commands
- `execute_command(id, args)` to execute a command

---

# Control JupyterLab with natural language

- "toggle the right area"
- "show the about dialog"
- "create a new chess pawn in jupytercad"

---

<div class="prompt-box">
  Create an empty .jcad file. Once opened, build a chess pawn, step by step, using the available jupytercad commands
  <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.firstChild.textContent.trim())">
    Copy
  </button>
</div>

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/1bebdc78-c26f-4b63-9b7c-24bf14cc6a21">
</video>

---

# AI Proxies and Gateways

- Use LiteLLM or Portkey as a proxy server
- Maintain a gateway server with secrets
- Lightweight client in the browser
  - Low friction
  - No configuration needed

---

TODO: screencast of LiteLLM

---

# Model Context Protocol (MCP)

- Open-source standard for connecting AI applications to external systems:
  - Tools
  - Resources
  - Prompts

> Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

https://modelcontextprotocol.io

![bg fit right:20%](images/mcp.png)

---

# Remote MCP Servers

- The server is hosted somewhere else
- Available from any MCP client with an internet connection
- Ideal for web-based AI applications

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/b0c6f37c-9dc8-493d-9fe8-4ef53ab77fd8">
</video>

---

# LLMs in the Browser

- Run models directly in the browser
- No server dependencies
- Privacy-focused: no requests to external servers

---

# In-Browser AI libraries

<div class="center-table">

<table>
  <tr>
    <td style="text-align: center;"><img src="images/webllm.jpg" alt="WebLLM"></td>
    <td style="text-align: center;"><a href="https://webllm.mlc.ai">WebLLM</a></td>
  </tr>
  <tr>
    <td style="text-align: center;"><img src="images/huggingface.svg" alt="Hugging Face"></td>
    <td style="text-align: center;"><a href="https://huggingface.co/docs/transformers.js/index">Transformers.js</a></td>
  </tr>
</table>

</div>

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/c9dd79c2-99bf-4c4e-b4b8-9b1cf76fc165">
</video>

---

# Built-in AI

- Chrome: Gemini Nano
- Edge: Phi-4-mini

---

![bg fit](images/chromeai.png)

---

![bg fit](images/chromeai-api-status.png)

---

![bg fit](images/chromeai-flags.png)

---

# Not just about code

- ChromeAI multimodal capabilities:
  - Generate alt text for images
  - Transcribe audio to text
- New Browser APIs:
  - Proofreader API
  - Summarizer API

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/da53a662-af35-4302-b72f-dcf9eecefb45">
</video>

---

<video
  controls
  width="100%"
  height="600px"
  src="https://github.com/user-attachments/assets/1ffab2d6-94f3-4b53-abac-374f0adc33b7">
</video>

---

TODO: Proofreader API demo

---

TODO: Summarizer API demo

---

# The Case of Privacy

- Data stays in the browser
- No server round-trips
- Enhanced privacy protection

---

# Limitations of browser-based AI

- Model size (300MB - 1GB - 22GB)
- The model must be downloaded before use
- Performance (requires good hardware, GPU)
- Browser, flags and hardware compatibility
- MCP:
  - Some remote MCP servers can work
  - https://github.com/webmachinelearning/webmcp

---

# Secrets Management

- Store secrets via the settings (in the browser with JupyterLite)
- Or use the secrets manager with custom connectors:
  - https://github.com/jupyterlab-contrib/jupyter-secrets-manager
- Proxy server (LiteLLM, Portkey)

---

# What's Next?

- AI CLI tool via `jupyterlite-terminal`
- Real Time Collaboration and chat
- Tool calls with built-in AI models (ChromeAI, EdgeAI)

---

TODO: AI in `jupyterlite-terminal` screencast

---

# Building blocks for AI in Jupyter

- Towards modular and extensible components:
  - https://github.com/orgs/jupyter-ai-contrib/discussions/1
  - "AI in Jupyter" Community Workshop
- Extension authors can extend functionality via JupyterLab commands
- Hybrid workflows (server + browser)

---

# Join us at the sprints!

---

# References

- Presentation: https://github.com/jtpio/jupytercon-2025-browser-ai-workflows
- Live version: https://jtpio.github.io/jupytercon-2025-browser-ai-workflows/files/index.html
