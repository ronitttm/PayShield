# 🛡️ PayShield AI

### Multi-Agent AI System for Payment Monitoring & Incident Investigation

PayShield AI is an AI-powered payment intelligence platform that uses specialized AI agents to investigate payment failures, application errors, infrastructure degradation, and suspicious transaction behaviour.

Built using **Python, FastAPI, n8n, and OpenAI**, it coordinates four specialist agents through an Incident Commander and consolidates their findings using a Root Cause Analyst.

## 🚀 Key Features

- Multi-agent incident investigation.
- Parallel execution of four specialist agents.
- Transaction and payment failure analysis.
- Application log investigation.
- Infrastructure metrics analysis.
- Fraud and risk detection.
- AI-powered root cause analysis.
- Structured incident reports.
- Webhook-based orchestration.

## 🏗️ Architecture

```text
             INCIDENT WEBHOOK
                    |
                    v
             INCIDENT COMMANDER
                    |
          +---------+-------------------+
          |         |         |         |
          v         v         v         v
     Transaction  Log      Metrics   Fraud & Risk
      Analyst   Investigator Analyst  Analyst
          |         |         |         |
          +---------+-------------------+
                    |
                    |
                    v
           COLLECT ALL RESULTS
                    |
                    v
           ROOT CAUSE ANALYST
                    |
                    v
          FINAL INCIDENT REPORT
                    |
                    v
             WEBHOOK RESPONSE


              WEBHOOK TRIGGER
                      |
                      v
               INCIDENT COMMANDER
                      |
               DISTRIBUTE TASKS
                      |
          +-----------+--------------------+
          |           |           |        |
          v           v           v        v
     TRANSACTION    LOGS       METRICS    FRAUD
       AGENT       AGENT        AGENT     AGENT
          |           |           |        |
          +-----------+--------------------+
                      |
                      v
              COLLECT RESPONSES
                      |
                      v
             ROOT CAUSE ANALYST
                      |
                      v
               FINAL RESPONSE
```

## 🤖 Multi-Agent Architecture

| Agent | Responsibility |
|---|---|
| Transaction Analyst | Payment failures, success rates, gateway performance |
| Log Investigator | Application errors, exceptions, timeouts |
| Metrics Analyst | API latency, request volume, error rates |
| Fraud & Risk Analyst | Suspicious transactions and fraud indicators |
| Incident Commander | Coordinates specialist investigations |
| Root Cause Analyst | Correlates findings and generates incident reports |

## ⚙️ Technology Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| AI | OpenAI API, LLM-powered agents |
| Orchestration | n8n, Webhooks, HTTP Request Nodes |
| Infrastructure | Docker, Docker Desktop |
| Database | SQLite (planned) |
| Frontend | React, JavaScript (planned) |

## 🔄 Current Workflow

1. Receive an incident through an n8n webhook.
2. Incident Commander initiates four specialist investigations.
3. Agents independently analyze their respective domains.
4. Collect and consolidate investigation results.
5. Root Cause Analyst correlates findings.
6. Generate and return the final incident report.

## 🔮 Future Architecture

The next phase will introduce automated payment simulation and monitoring.

```text
                 REACT DASHBOARD
                       |
                START SIMULATION
                       |
                       v
                 FASTAPI BACKEND
                       |
                       v
                SIMULATION ENGINE
                       |
                GENERATE EVENTS
                       |
          +------------+------------+
          |            |            |
          v            v            v
     TRANSACTIONS     LOGS        FRAUD FLAGS
          |            |            |
          +------------+------------+
                       |
                       v
                  SQLITE DATABASE
                       |
                       v
                MONITORING ENGINE
                       |
                EVALUATE THRESHOLDS
                       |
                ANOMALY DETECTED?
                       |
                      YES
                       |
                       v
                 CREATE INCIDENT
                       |
                       v
                WEBHOOK TO n8n
                       |
                       v
               INCIDENT COMMANDER
                       |
          +------------+--------------------+
          |            |            |       |
          v            v            v       v  
     TRANSACTION     LOGS        METRICS    FRAUD
       ANALYST    INVESTIGATOR    ANALYST  ANALYST
          |            |            |       |
          +------------+--------------------+
                       |
                       |
                       v
                ROOT CAUSE ANALYST
                       |
                       v
                 INCIDENT REPORT
                       |
                       v
                 FASTAPI BACKEND
                       |
                       v
                  SQLITE DATABASE
                       |
                       v
                 REACT DASHBOARD
```

### Planned Features

- Payment event simulation.
- Centralized SQLite storage.
- Automated threshold-based monitoring.
- Automatic incident creation and triggering.
- React operations dashboard.
- Incident history and analytics.
- AI-generated resolution recommendations.
- Human-in-the-loop approval and remediation.

## 🛣️ Development Roadmap

| Feature | Status |
|---|---|
| FastAPI backend | ✅ Implemented |
| n8n orchestration (Docker) | ✅ Implemented |
| Four specialist agents | ✅ Implemented |
| Incident Commander | ✅ Implemented |
| Parallel agent execution | ✅ Implemented |
| Root Cause Analyst | ✅ Implemented |
| Incident reports and webhook response | ✅ Implemented |
| SQLite database | 🔄 Planned |
| Payment simulation engine | 🔄 Planned |
| Automated monitoring and anomaly detection | 🔄 Planned |
| Automatic incident creation | 🔄 Planned |
| React dashboard | 🔄 Planned |
| Resolution and remediation agents | 🔮 Future Scope |

## 💡 Project Objective

Build an intelligent payment operations platform that goes beyond anomaly detection by automatically investigating incidents, correlating operational signals, identifying potential root causes, and recommending corrective actions.

## 👨‍💻 Author

**Ronit Murpani**

AI Engineer | Backend Developer | Multi-Agent AI Systems

[GitHub](https://github.com/ronitttm) · [LinkedIn](https://www.linkedin.com/in/ronitttm/)

## 📄 License

Currently under development.