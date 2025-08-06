# 📝 Product Requirements Document (PRD)

## 📌 Project Name
**Property Data AI Agent**

---

## 1. 🎯 Problem Statement

Real estate field agents and property owners often share property details informally through WhatsApp messages or emails. These messages are unstructured, inconsistent, and require manual effort to convert into a format suitable for listing or CRM systems. This process is time-consuming, error-prone, and inefficient.

---

## 2. 🧑‍💼 Target Users

| Persona | Role | Pain Point |
|--------|------|------------|
| Field Agent | Sends property details via mobile or WhatsApp | No structured way to submit data |
| Property Admin | Manually inputs property data into system | Time-consuming, repetitive work |
| Listing Manager | Reviews data before publishing | Delays due to manual bottlenecks |

---

## 3. 🌟 Product Goals

- Accept unstructured text input (WhatsApp/email-style)
- Extract structured fields like property type, location, price, area, contact
- Store data in Azure Storage (Blob or Table)
- (Optional) Expose the data via an API for further integration

---

## 4. 📦 MVP Scope

### ✅ In Scope (Phase 1)
- Azure Function with HTTP trigger
- Integration with Azure OpenAI to extract fields from input text
- Save output to Azure Blob (CSV) or Table Storage
- Sample input/output files
- GitHub repo with README, PRD, and architecture diagram

### ❌ Out of Scope (for now)
- Web interface or chatbot
- Bi-directional communication (e.g., agent replies)
- CRM/website integration

---

## 5. ⚙️ Functional Requirements

| Feature | Description |
|---------|-------------|
| Input Interface | HTTP endpoint to receive raw property text |
| AI Processing | Use GPT to extract structured fields |
| Data Storage | Save results in CSV/JSON format in Azure |
| Logging | Log each request and response for debugging |

---

## 6. 🔐 Non-Functional Requirements

- Should work with Azure OpenAI (GPT-4 or GPT-3.5)
- Fast response time (<3s for extraction)
- Secure API access (future enhancement)
- Scalable and stateless design

---

## 7. 📊 Success Metrics

| Metric | Target |
|--------|--------|
| Extraction Accuracy | ≥ 90% field accuracy |
| Time Saved per Entry | ≥ 80% vs. manual process |
| First Response Latency | ≤ 3 seconds |
| Setup Time | ≤ 30 minutes for developer setup |

---

## 8. 🔭 Future Enhancements

- Support for images (OCR extraction from flyers)
- Integration with real estate CRM systems
- Power Apps UI for data entry and search
- Send confirmation back to agent

---

## ✍️ Created By

**Sakthiyendran Arunachalam**  
Principal Product Manager (SETHU PROPERTIES) | AI + API + Automation  
📅 August 2025

