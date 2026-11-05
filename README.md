# 🛡️ PayShield AI

### Multi-Agent AI System for Intelligent Payment Monitoring, Fraud Investigation & Incident Analysis

PayShield AI is an AI-powered payment intelligence and incident investigation platform designed to monitor payment systems, investigate operational anomalies, detect suspicious transaction behaviour, and identify potential root causes using a coordinated team of specialized AI agents.

Built around a multi-agent architecture, PayShield AI combines **FastAPI, Python, n8n, and Large Language Models (LLMs)** to automate the investigation of payment-related incidents.

Instead of relying on a single AI agent to analyze everything, PayShield distributes investigations across four specialized agents, each responsible for a different aspect of payment operations.

An Incident Commander coordinates these agents, collects their findings, and forwards the combined evidence to a Root Cause Analyst, which generates a unified incident investigation report.

The long-term goal is to evolve PayShield into an autonomous payment operations intelligence platform capable of continuously monitoring simulated payment infrastructure, identifying anomalies, initiating investigations, and recommending corrective actions.

---

## 🚀 Key Features

- **Multi-Agent Architecture:** Four specialized AI agents investigate different aspects of payment infrastructure.
- **Automated Incident Investigation:** An Incident Commander coordinates investigations through n8n workflows.
- **Transaction Intelligence:** Analyzes payment success rates, failures, gateway performance, and transaction patterns.
- **Application Log Investigation:** Investigates application logs to identify errors, exceptions, and operational issues.
- **Infrastructure Monitoring:** Evaluates latency, request volumes, error rates, and system performance.
- **Fraud & Risk Analysis:** Identifies suspicious transaction behaviour, unusual patterns, and potential fraud indicators.
- **Root Cause Analysis:** Correlates findings from all four agents to identify potential causes of incidents.
- **Unified Incident Reports:** Consolidates investigation results into a structured report.
- **API-Driven Architecture:** FastAPI provides the interface between payment intelligence services and the agent orchestration layer.

### Planned Features

- Real-time payment event simulation.
- Persistent storage using SQLite.
- Automated anomaly detection and threshold monitoring.
- Webhook-triggered incident investigations.
- React-based operations dashboard.
- Incident history and analytics.
- AI-generated resolution recommendations.
- Human-in-the-loop approval before executing corrective actions.

---

# 🏗️ System Architecture

PayShield follows a modular architecture that separates payment intelligence, agent orchestration, data storage, and presentation.

The system consists of four primary components:

| Component | Responsibility                                                            |
| --------- | ------------------------------------------------------------------------- |
| FastAPI   | Payment intelligence, analytics, data access, and backend APIs            |
| n8n       | Multi-agent orchestration and workflow execution                          |
| SQLite    | Planned persistent storage for transactions, logs, metrics, and incidents |
| React     | Planned frontend for monitoring and incident management                   |

## 1. High-Level Architecture

The initial implementation focuses on the backend intelligence and multi-agent orchestration layers.

```text
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

The Incident Commander distributes investigation tasks to four specialized agents. Their results are collected and passed to the Root Cause Analyst, which evaluates the combined findings.

---

# 🤖 Multi-Agent Architecture

PayShield uses a specialized multi-agent architecture where each agent has a clearly defined responsibility.

Rather than asking one LLM to investigate the entire payment infrastructure, the system separates the investigation into independent domains.

## 1. Transaction Analyst

**Responsibility:** Investigates payment transaction behaviour.

The Transaction Analyst examines transaction-level data to understand what happened to payments during an incident.

### What it investigates

- Total transaction volume.
- Successful and failed payments.
- Payment failure rates.
- Gateway-specific performance.
- Transaction status distribution.
- Unusual increases in payment failures.

### Example investigation

If a payment gateway suddenly experiences a high failure rate, the Transaction Analyst investigates the transaction records and determines whether the gateway is experiencing a payment degradation event.

---

## 2. Log Investigator

**Responsibility:** Investigates application-level errors and operational logs.

The Log Investigator examines application logs to identify errors and exceptions that could explain unexpected payment behaviour.

### What it investigates

- Application exceptions.
- API errors.
- Database connection failures.
- Timeout errors.
- Authentication failures.
- Repeated error patterns.
- Error frequency and distribution.

### Example investigation

If payment requests are failing because of repeated database connection timeouts, the Log Investigator identifies the corresponding errors and reports the evidence.

---

## 3. Metrics Analyst

**Responsibility:** Investigates infrastructure and application performance.

The Metrics Analyst evaluates operational metrics to determine whether system performance has degraded.

### What it investigates

- Request volume.
- API latency.
- Average response time.
- Payment failure rates.
- Error rates.
- Performance fluctuations.
- Gateway-specific metric patterns.

### Example investigation

If an API begins experiencing unusually high latency, the Metrics Analyst examines performance measurements across multiple monitoring intervals to determine whether there is evidence of system degradation.

---

## 4. Fraud & Risk Analyst

**Responsibility:** Identifies suspicious transaction behaviour and potential fraud indicators.

The Fraud & Risk Analyst examines transaction patterns to identify potentially malicious or unusual activity.

### What it investigates

- Repeated failed payment attempts.
- Suspicious transaction patterns.
- Unusual transaction frequency.
- Multiple attempts associated with suspicious activity.
- Fraud flags.
- Potential risk indicators.

### Example investigation

If a payment gateway experiences a sudden increase in suspicious payment attempts, the Fraud & Risk Analyst examines flagged transactions and identifies the indicators associated with the activity.

Importantly, suspicious activity does not automatically mean confirmed fraud. The agent reports evidence and potential risk rather than making unsupported conclusions.

---

# 🧠 Incident Commander

The Incident Commander is responsible for coordinating the entire investigation process.

It acts as the central orchestration agent within the n8n workflow.

### Responsibilities

1. Receive an incident investigation request through a webhook.
2. Understand the incident type and relevant context.
3. Identify the investigation requirements.
4. Trigger the four specialist agents.
5. Execute specialist investigations in parallel.
6. Collect their structured responses.
7. Consolidate the investigation findings.
8. Forward the findings to the Root Cause Analyst.
9. Return the final incident report.



# 🔍 Root Cause Analysis

After the specialist agents complete their investigations, their findings are consolidated and forwarded to the Root Cause Analyst.

The Root Cause Analyst evaluates the evidence collectively instead of relying on an isolated investigation.

### Responsibilities

- Correlate transaction failures with application errors.
- Compare system performance with transaction behaviour.
- Evaluate whether suspicious activity is related to the incident.
- Identify relationships between different operational signals.
- Distinguish confirmed observations from potential explanations.
- Determine whether sufficient evidence exists to establish a root cause.
- Generate a consolidated incident report.

### Example

Consider a payment gateway experiencing a sudden increase in failed transactions.

The investigation might produce the following findings:

| Agent                | Investigation Result                     |
| -------------------- | ---------------------------------------- |
| Transaction Analyst  | High payment failure rate detected       |
| Log Investigator     | Repeated application timeout errors      |
| Metrics Analyst      | Increased API latency detected           |
| Fraud & Risk Analyst | Suspicious transaction activity detected |

The Root Cause Analyst correlates these findings and determines whether the available evidence supports a common explanation.

It is also designed to distinguish unrelated events. For example, suspicious transaction activity may occur independently of an infrastructure degradation incident.

**The objective is evidence-based incident analysis, not simply generating an explanation for every anomaly.**

---

# ⚙️ Technology Stack

## Backend

| Technology | Purpose                                          |
| ---------- | ------------------------------------------------ |
| Python     | Core backend and payment intelligence logic      |
| FastAPI    | REST API development and investigation endpoints |
| Pydantic   | Structured request and response validation       |
| SQLite     | Planned persistent database                      |
| SQLAlchemy | Potential database abstraction layer             |

## AI & Agent Orchestration

| Technology         | Purpose                                                         |
| ------------------ | --------------------------------------------------------------- |
| n8n                | Workflow automation and multi-agent orchestration               |
| OpenAI API         | LLM-powered investigation and reasoning                         |
| AI Agents          | Specialized transaction, log, metrics, and fraud investigations |
| HTTP Request Nodes | Communication between agents and FastAPI services               |
| Webhooks           | Event-driven incident investigation                             |

## Infrastructure & Development

| Technology     | Purpose                                                            |
| -------------- | ------------------------------------------------------------------ |
| Docker         | Containerized n8n environment                                      |
| Docker Desktop | Local container management                                         |
| REST APIs      | Communication between backend services and orchestration workflows |
| JSON           | Structured communication between agents                            |

## Frontend (Planned)

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| React      | Operations dashboard               |
| JavaScript | Frontend application logic         |
| REST API   | Communication with FastAPI backend |

---

# 🔄 Current Incident Investigation Workflow

The current implementation follows an event-driven investigation workflow.

### Step 1: Incident Trigger

An incident investigation request is received through an n8n webhook.

The request contains information such as:

- Incident type.
- Payment gateway.
- Relevant investigation context.

### Step 2: Agent Orchestration

The Incident Commander processes the incoming request and invokes the four specialist investigation workflows.

### Step 3: Parallel Investigation

Each specialist agent investigates its respective domain.

The agents retrieve relevant information through FastAPI endpoints and return structured investigation results.

### Step 4: Result Collection

The Incident Commander collects the responses from all four agents.

The results are normalized and consolidated into a unified payload.

### Step 5: Root Cause Analysis

The consolidated findings are forwarded to the Root Cause Analyst.

The analyst evaluates the combined evidence and generates an incident assessment.

### Step 6: Incident Report

The final report is returned through the webhook response.

The report contains the investigation findings, agent observations, and root cause assessment.

---

# 📊 Planned Data Architecture

The next major development phase involves replacing temporary or prototype data sources with persistent storage.

PayShield will use a centralized SQLite database rather than maintaining separate databases for transactions, logs, metrics, and fraud information.

### Proposed Database Structure

| Table               | Description                                       |
| ------------------- | ------------------------------------------------- |
| `simulation_runs`   | Tracks individual payment simulation sessions     |
| `transactions`      | Stores generated payment transactions             |
| `application_logs`  | Stores application events, errors, and exceptions |
| `metrics_snapshots` | Stores performance metrics over time              |
| `fraud_flags`       | Stores suspicious transaction indicators          |
| `incidents`         | Stores detected incidents and their statuses      |
| `incident_reports`  | Stores AI-generated investigation reports         |
| `incident_events`   | Stores incident lifecycle events and updates      |

All records will be associated with relevant simulation runs, gateways, transactions, or incidents.

This centralized approach will make it easier to correlate information across different investigation domains.

---

# 🔮 Future Architecture

The next development phase will transform PayShield from a webhook-triggered investigation prototype into an automated payment monitoring and incident intelligence platform.

The objective is to simulate a payment infrastructure, continuously monitor its behaviour, detect anomalies, and automatically initiate AI-powered investigations.

## 1. Payment Simulation Engine

A simulation engine will generate realistic payment events.

Users will eventually be able to start and stop simulations through the React dashboard.

The simulation engine will generate:

- Successful transactions.
- Failed transactions.
- Payment gateway timeouts.
- Application errors.
- API latency fluctuations.
- Suspicious payment attempts.
- Fraud indicators.

Generated events will be stored in the centralized SQLite database.

## 2. Automated Monitoring Engine

A monitoring engine will continuously evaluate the generated payment and infrastructure data.

It will examine predefined thresholds and identify unusual system behaviour.

### Example Monitoring Conditions

| Metric               | Example Trigger Condition                        |
| -------------------- | ------------------------------------------------ |
| Payment Failure Rate | Failure rate exceeds 50%                         |
| API Latency          | Average latency exceeds the configured threshold |
| Error Rate           | Application errors increase significantly        |
| Fraud Activity       | Unusual increase in suspicious transactions      |
| Gateway Availability | Gateway becomes unavailable                      |

These values are illustrative configuration examples, not universal production thresholds.

## 3. Automatic Incident Creation

When the monitoring engine detects an anomaly, it will:

1. Identify the affected gateway or service.
2. Determine the anomaly type.
3. Create an incident record.
4. Store the relevant investigation context.
5. Trigger the n8n Incident Commander webhook.

This eliminates the need to manually trigger investigations through Postman or another API client.

The monitoring engine will also incorporate incident deduplication, cooldown periods, and recovery checks to prevent repeated alerts for the same ongoing issue.

## 4. Automated AI Investigation

Once an incident is created, the existing multi-agent architecture will automatically investigate it.

The specialist agents will retrieve relevant information from the centralized database and analyze the incident.

The Root Cause Analyst will correlate their findings and generate a structured report.

## 5. Incident Persistence

The generated report will be returned to FastAPI and persisted in the database.

This will enable incident history, investigation tracking, and historical analysis.

## 6. React Operations Dashboard

A React-based dashboard will provide a visual interface for monitoring payment operations.

### Planned Dashboard Features

**Simulation Controls**

- Start simulation.
- Stop simulation.
- View simulation status.
- Monitor generated payment events.

**Payment Monitoring**

- Total transactions.
- Successful transactions.
- Failed transactions.
- Payment success and failure rates.
- Gateway performance.

**Infrastructure Monitoring**

- API latency.
- Error rates.
- Request volume.
- Application logs.
- Performance trends.

**Fraud & Risk Monitoring**

- Suspicious transaction counts.
- Flagged payment attempts.
- Risk indicators.
- Gateway-specific fraud activity.

**Incident Management**

- Active incidents.
- Incident severity.
- Investigation status.
- Agent findings.
- Root cause analysis.
- Historical incident reports.

---

# 🏛️ Future End-to-End Architecture

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

---

# 🛣️ Development Roadmap

| Phase | Feature                                            | Status          |
| ----- | -------------------------------------------------- | --------------- |
| 1     | Local n8n environment using Docker                 | ✅ Completed     |
| 2     | FastAPI backend and initial API endpoints          | ✅ Completed     |
| 3     | Transaction Analyst                                | ✅ Implemented   |
| 4     | Log Investigator                                   | ✅ Implemented   |
| 5     | Metrics Analyst                                    | ✅ Implemented   |
| 6     | Fraud & Risk Analyst                               | ✅ Implemented   |
| 7     | Incident Commander                                 | ✅ Implemented   |
| 8     | Parallel specialist agent execution                | ✅ Implemented   |
| 9     | Root Cause Analyst                                 | ✅ Implemented   |
| 10    | Unified incident report and webhook response       | ✅ Implemented   |
| 11    | Centralized SQLite database                        | 🔄 Planned      |
| 12    | Payment simulation engine                          | 🔄 Planned      |
| 13    | Persistent transaction and log generation          | 🔄 Planned      |
| 14    | Automated monitoring engine                        | 🔄 Planned      |
| 15    | Threshold-based anomaly detection                  | 🔄 Planned      |
| 16    | Automatic incident creation and webhook triggering | 🔄 Planned      |
| 17    | Incident history and report persistence            | 🔄 Planned      |
| 18    | React operations dashboard                         | 🔄 Planned      |
| 19    | AI-generated resolution recommendations            | 🔄 Planned      |
| 20    | Human-in-the-loop approval                         | 🔄 Planned      |
| 21    | Automated remediation workflows                    | 🔄 Future Scope |

---

# 🎯 Project Objectives

PayShield AI is being developed to explore how multi-agent AI systems can improve the way payment infrastructure is monitored and investigated.

The primary objectives are:

- Build a practical multi-agent system using specialized AI agents.
- Explore event-driven architecture and webhook-based communication.
- Integrate LLM-powered reasoning with structured backend analytics.
- Automate incident investigation through workflow orchestration.
- Correlate transaction, application, infrastructure, and fraud-related signals.
- Develop an automated monitoring and incident management platform.
- Explore human-in-the-loop AI systems for operational decision-making.

---

# 💡 Why PayShield AI?

Traditional payment monitoring systems often rely on predefined alerts and manually performed investigations.

When an incident occurs, engineers may need to inspect transaction records, application logs, performance metrics, and fraud indicators separately.

PayShield explores a different approach.

By combining specialized AI agents with centralized payment intelligence and workflow orchestration, the system aims to automate the investigation process and provide a consolidated understanding of what happened.

The goal is not simply to detect that something went wrong, but to investigate **what happened, where it happened, why it might have happened, and what should be done next.**

---

# 👨‍💻 Author

**Ronit Murpani**

AI Engineer | Backend Developer | Multi-Agent AI Systems

[GitHub](https://github.com/ronitttm) · [LinkedIn](https://www.linkedin.com/in/ronitttm/)

---

# 📄 License

This project is currently under development. Licensing information will be added in a future release.
