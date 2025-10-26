# 🧠 PolyMind

<div align="center">

**A Multi-Agent Retrieval-Augmented Generation (RAG) System for Collective Reasoning**

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

</div>

---

## 📖 Overview

**PolyMind** is a multi-agent Retrieval-Augmented Generation (RAG) system designed to explore collective reasoning and bias interplay within AI decision-making. Instead of relying on a single model's output, PolyMind simulates a **society of minds**, where each agent embodies a unique cognitive bias and perspective.

### 🎭 The Agent Society

The system includes five specialized agents, each with distinct reasoning patterns:

| Agent | Role | Perspective |
|-------|------|-------------|
| 🌟 **OptimistAgent** | Optimistic Interpreter | Interprets context through best-case outcomes and opportunities |
| 🔍 **SkepticAgent** | Critical Analyzer | Challenges assumptions, verifies sources, and identifies risks |
| 📚 **HistorianAgent** | Historical Context | Grounds reasoning in past data, precedent, and lessons learned |
| 🔮 **ForecasterAgent** | Future Predictor | Predicts future outcomes using trend-based retrieval and analysis |
| ⚖️ **JudgeAgent** | Consensus Builder | Evaluates all reasoning chains and synthesizes final decisions |

### �� How It Works

1. **Independent Retrieval**: Each agent retrieves context independently from a shared vector database
2. **Diverse Reasoning**: Agents form their own reasoning traces based on their unique perspectives
3. **Collaborative Debate**: Agents debate and challenge each other's conclusions
4. **Consensus Building**: The JudgeAgent synthesizes insights into a final answer
5. **Self-Audit Loop**: The system reviews its own quality and confidence, creating metacognitive awareness

### 🎯 Key Features

- **🤖 Multi-Agent Orchestration**: Powered by LangGraph for complex agent workflows
- **🗄️ Vector Database**: LanceDB for efficient similarity search and retrieval
- **🔗 RAG Pipeline**: Advanced retrieval-augmented generation with multiple perspectives
- **🎭 Bias-Aware AI**: Explicit modeling of cognitive biases in decision-making
- **📊 Self-Evaluation**: Built-in evaluation using RAGAS and DeepEval metrics
- **🌐 REST API**: FastAPI backend for easy integration
- **💻 Interactive UI**: User interface for exploring agent interactions
- **🔭 Observability**: Telemetry and monitoring for transparency

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         User Query                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Vector Database (LanceDB)                 │
│                  Shared Knowledge Repository                 │
└─────┬─────────┬─────────┬─────────┬─────────┬──────────────┘
      │         │         │         │         │
      ▼         ▼         ▼         ▼         ▼
   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐
   │ 🌟 │   │ 🔍 │   │ 📚 │   │ 🔮 │   │ ⚖️ │
   └─┬──┘   └─┬──┘   └─┬──┘   └─┬──┘   └─┬──┘
     │        │        │        │        │
     └────────┴────────┴────────┴────────┘
                      │
                      ▼
           ┌──────────────────────┐
           │   Debate & Synthesis  │
           └──────────┬────────────┘
                      │
                      ▼
           ┌──────────────────────┐
           │    Final Answer      │
           └──────────┬────────────┘
                      │
                      ▼
           ┌──────────────────────┐
           │    Self-Audit Loop   │
           └──────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gksaurabh/PolyMind.git
   cd PolyMind
   ```

2. **Install dependencies using uv** (recommended)
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Create virtual environment and install dependencies
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -e ".[dev]"
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

   Required environment variables:
   ```env
   # LLM Provider API Keys
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   
   # Vector Database
   LANCEDB_PATH=./data/lancedb
   
   # Redis (optional, for caching)
   REDIS_URL=redis://localhost:6379
   
   # Telemetry
   AGNO_API_KEY=your_agno_key  # Optional
   ```

### Quick Start

1. **Run the API server**
   ```bash
   uvicorn src.api.main:app --reload
   ```

2. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Interactive UI: http://localhost:8000

3. **Run the UI (optional)**
   ```bash
   cd src/ui
   npm install
   npm run dev
   ```

---

## 📚 Usage

### Python API

```python
from src.agents import PolyMindSystem

# Initialize the system
polymind = PolyMindSystem()

# Ask a question
result = await polymind.query(
    question="What are the potential impacts of AI on healthcare?",
    context_docs=["doc1.pdf", "doc2.txt"]
)

# Access agent perspectives
for agent_name, reasoning in result.agent_perspectives.items():
    print(f"{agent_name}: {reasoning}")

# Get final consensus
print(f"Final Answer: {result.consensus}")
print(f"Confidence: {result.confidence}")
```

### REST API

```bash
# Query the system
curl -X POST "http://localhost:8000/api/v1/query" \\
  -H "Content-Type: application/json" \\
  -d '{
    "question": "What are the risks of quantum computing?",
    "include_reasoning": true
  }'
```

### CLI (Coming Soon)

```bash
polymind query "Your question here" --verbose
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_agents.py

# Run with verbose output
pytest -v
```

---

## 📊 Evaluation

PolyMind includes built-in evaluation metrics:

- **RAGAS Metrics**: Faithfulness, Answer Relevancy, Context Precision
- **DeepEval Metrics**: Hallucination detection, Bias detection
- **Custom Metrics**: Inter-agent agreement, Confidence calibration

```python
from src.utils.evaluation import evaluate_system

metrics = await evaluate_system(
    questions=test_questions,
    ground_truth=ground_truth_answers
)
```

---

## 🗂️ Project Structure

```
PolyMind/
├── src/
│   ├── agents/              # Agent implementations
│   │   ├── optimist/        # Optimistic reasoning agent
│   │   ├── skeptic/         # Critical analysis agent
│   │   ├── historian/       # Historical context agent
│   │   ├── forecaster/      # Future prediction agent
│   │   └── judge/           # Consensus building agent
│   ├── api/                 # FastAPI backend
│   └── ui/                  # User interface
├── utils/
│   ├── retrieval/           # RAG and vector DB utilities
│   ├── evaluation/          # Evaluation metrics
│   ├── prompts/             # Agent prompts and templates
│   ├── graph/               # LangGraph workflows
│   └── telemetry/           # Monitoring and logging
├── tests/                   # Test suite
├── data/                    # Data storage
│   ├── raw/                 # Raw input documents
│   ├── processed/           # Processed embeddings
│   └── ingest/              # Data ingestion scripts
├── docs/                    # Documentation
├── scripts/                 # Utility scripts
├── config/                  # Configuration files
└── pyproject.toml          # Project configuration
```

---

## 🛠️ Development

### Code Quality

This project uses modern Python tooling:

- **Ruff**: Fast linting and formatting
- **Black**: Code formatting
- **MyPy**: Static type checking
- **Pytest**: Testing framework

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
mypy src/

# Run all quality checks
./scripts/check.sh  # Coming soon
```

### Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🔬 Research & Motivation

PolyMind explores several key research questions:

1. **Collective Intelligence**: How do diverse AI agents collaborate to produce better decisions?
2. **Bias Interplay**: How do different cognitive biases interact in multi-agent systems?
3. **Reasoning Transparency**: Can we make AI decision-making more interpretable?
4. **Metacognition**: Can AI systems evaluate their own reasoning quality?
5. **RAG Enhancement**: How does multi-perspective retrieval improve RAG systems?

### Related Work

- Multi-Agent Systems (MAS)
- Retrieval-Augmented Generation (RAG)
- Cognitive Bias in AI
- Metacognitive AI
- Collective Intelligence

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph)
- Vector storage powered by [LanceDB](https://github.com/lancedb/lancedb)
- Evaluation frameworks: [RAGAS](https://github.com/explodinggradients/ragas) and [DeepEval](https://github.com/confident-ai/deepeval)
- LLM providers: OpenAI and Anthropic

---

## 📧 Contact

For questions, suggestions, or collaboration:

- **GitHub Issues**: [Report bugs or request features](https://github.com/gksaurabh/PolyMind/issues)
- **Email**: [Your contact email]
- **Twitter**: [@yourusername]

---

<div align="center">

**Built with ❤️ by the PolyMind Team**

⭐ Star this repo if you find it interesting!

</div>
