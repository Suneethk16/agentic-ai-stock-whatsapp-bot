#  Agentic AI Stock Analysis Bot (LLM-Powered)

An **autonomous Agentic AI system** that analyzes stock market data daily and delivers **WhatsApp-ready insights at 9:00 AM**, without any human prompts.

The system combines **rule-based agents** with an **LLM-powered reasoning agent (Google Gemini)** and runs in a **Docker + cron** setup for full automation and cloud portability.

---

## Key Features

- **Fully Autonomous** – runs daily via cron (no manual prompts)
- **Agentic Architecture** – multiple specialized agents working together
- **LLM-Powered Reasoning** – uses **Google Gemini** for natural-language insights
- **Graceful Fallback** – switches to rule-based logic if LLM is unavailable
- **Market Intelligence**
  - Stock price trend analysis (7 / 30 / 90 days)
  - News sentiment analysis
- 📲 **WhatsApp Delivery** – sends concise daily summaries
- 🐳 **Dockerized** – reproducible, cloud-safe deployment

---

## Agent Architecture
Scheduler (Cron)<br>
↓<br>
DataAgent → Fetches stock prices & news<br>
↓<br>
SentimentAgent → Analyzes market news sentiment<br>
↓<br>
TrendAgent → Computes short / mid / long-term trends<br>
↓<br>
GeminiReasoningAgent (LLM)<br>
↓<br>
WhatsAppAgent → Sends daily insight to WhatsApp<br>


---

##  Tech Stack

- Python 3.11
- Google Gemini API (LLM reasoning)
- Alpha Vantage (stock news & sentiment)
- yFinance (historical price data)
- VADER Sentiment Analysis
- Twilio WhatsApp API
- Docker
- Cron


---

## Learning Outcomes

- Designed a true **agentic AI system**
- Integrated **LLM reasoning** into autonomous workflows
- Built **fault-tolerant AI pipelines**
- Deployed using **Docker + cron**
- Delivered real-world value via WhatsApp automation

---

## Disclaimer

This project is for **educational purposes only**.  
It does **not** constitute financial or investment advice.

---

## Future Enhancements

- Multi-stock portfolio summaries
- Confidence scoring
- SQLite / PostgreSQL storage
- Open-source LLM (Ollama + LLaMA)
- Cloud deployment (AWS / Railway)
- Web dashboard (FastAPI + React)

---

## Author

**Suneeth Kokala**  
Built with curiosity, discipline and real-world engineering principles.





