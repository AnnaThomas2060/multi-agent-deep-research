# Autonomous Multi-Agent Deep Research System

This repository contains the implementation of a multi-agent system designed to perform complex research tasks, drawing inspiration from Anthropic's multi-agent workflows and SFR-DeepResearch.

## Features
- **Orchestrator-Worker Architecture**: Uses CrewAI to manage specialized agents.
- **Free Web Search**: Integrated DuckDuckGo search without API keys.
- **Web Browsing**: Custom scraping tool for HTML to Markdown conversion.
- **Colab Ready**: Includes a Jupyter Notebook designed for execution on a Google Colab Pro A100 instance.

## Setup
1. Clone the repository.
2. Install dependencies: \pip install -r requirements.txt\`n3. Run the tests: \pytest tests/ -v\`n4. Run the main pipeline: \python src/main.py\`n
