# property-data-ai-agent
An AI Agent prototype using Azure OpenAI to extract structured property data from unstructured messages (WhatsApp/Email)

# 🧠 Property Data AI Agent (Azure OpenAI + Azure Functions)

An AI-powered agent that extracts structured property details from unstructured WhatsApp/email-style messages using Azure OpenAI — designed to solve real-world bottlenecks in property data entry for the real estate domain.

---

## 📌 Problem Statement

Real estate field agents and property owners often share property details informally via WhatsApp or email, making it tedious and error-prone for admins to manually extract, clean, and input this data into listing platforms or CRMs.

---

## 🎯 Goal

Build an AI Agent that:
- Accepts unstructured property text input
- Extracts structured data like location, price, area, contact, etc.
- Saves the result to Azure Table Storage / Blob / Cosmos DB
- Optionally exposes an API for downstream use (CRM, website)

---

## 👤 Target Users

- Field Agents / Brokers
- Property Admin / Operations Teams
- Real Estate Product Managers (MVP testing)
- AI/Automation Enthusiasts

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Agent LLM | Azure OpenAI (GPT-4 Turbo or GPT-3.5) |
| Function Logic | Azure Functions (Python) |
| Data Storage | Azure Table Storage or Blob Storage |
| Input | HTTP Trigger (simulates WhatsApp/email message) |
| Optional | Azure API Management, Power Apps for UI |

---

## 🧱 Architecture

```text
[Unstructured Message]
       ⬇️
Azure Function (HTTP Trigger)
       ⬇️
Azure OpenAI (Prompt Completion or Function Calling)
       ⬇️
Structured JSON Output
       ⬇️
Azure Table / Blob / Cosmos DB
       ⬇️
(Optional) Expose via API
