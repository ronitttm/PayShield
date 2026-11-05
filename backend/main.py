from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from collections import Counter, defaultdict

app = FastAPI(
    title="PayShield AI",
    description="Autonomous Payment Intelligence API",
    version="1.0.0"
)


class TransactionAnalysisRequest(BaseModel):
    gateway: Optional[str] = None

class LogAnalysisRequest(BaseModel):
    gateway: Optional[str] = None

class MetricsAnalysisRequest(BaseModel):
    gateway: str

class FraudAnalysisRequest(BaseModel):
    gateway: str

# syntheic transaction logs
TRANSACTIONS = [
    {"id": "TXN001", "gateway": "BANK_ALPHA", "status": "SUCCESS"},
    {"id": "TXN002", "gateway": "BANK_ALPHA", "status": "FAILED"},
    {"id": "TXN003", "gateway": "BANK_ALPHA", "status": "FAILED"},
    {"id": "TXN004", "gateway": "BANK_BETA", "status": "SUCCESS"},
    {"id": "TXN005", "gateway": "BANK_BETA", "status": "SUCCESS"},
    {"id": "TXN006", "gateway": "BANK_ALPHA", "status": "FAILED"},
]

# Synthetic application logs
APPLICATION_LOGS = [
    {
        "log_id": "LOG001",
        "gateway": "BANK_ALPHA",
        "level": "ERROR",
        "error_code": "GATEWAY_TIMEOUT",
        "message": "Payment gateway request timed out after 30 seconds",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:01:12"
    },
    {
        "log_id": "LOG002",
        "gateway": "BANK_ALPHA",
        "level": "ERROR",
        "error_code": "GATEWAY_TIMEOUT",
        "message": "Payment gateway request timed out after 30 seconds",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:02:18"
    },
    {
        "log_id": "LOG003",
        "gateway": "BANK_ALPHA",
        "level": "ERROR",
        "error_code": "CONNECTION_RESET",
        "message": "Connection reset while communicating with gateway",
        "service": "gateway-adapter",
        "timestamp": "2026-11-05T10:03:05"
    },
    {
        "log_id": "LOG004",
        "gateway": "BANK_ALPHA",
        "level": "ERROR",
        "error_code": "GATEWAY_TIMEOUT",
        "message": "Payment gateway request timed out after 30 seconds",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:04:22"
    },
    {
        "log_id": "LOG005",
        "gateway": "BANK_ALPHA",
        "level": "WARNING",
        "error_code": "HIGH_LATENCY",
        "message": "Gateway response latency exceeded threshold",
        "service": "gateway-adapter",
        "timestamp": "2026-11-05T10:05:30"
    },
    {
        "log_id": "LOG006",
        "gateway": "BANK_ALPHA",
        "level": "ERROR",
        "error_code": "ISSUER_DECLINED",
        "message": "Transaction declined by issuing bank",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:06:11"
    },
    {
        "log_id": "LOG007",
        "gateway": "BANK_BETA",
        "level": "INFO",
        "error_code": "PAYMENT_SUCCESS",
        "message": "Payment processed successfully",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:01:45"
    },
    {
        "log_id": "LOG008",
        "gateway": "BANK_BETA",
        "level": "INFO",
        "error_code": "PAYMENT_SUCCESS",
        "message": "Payment processed successfully",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:02:30"
    },
    {
        "log_id": "LOG009",
        "gateway": "BANK_BETA",
        "level": "INFO",
        "error_code": "PAYMENT_SUCCESS",
        "message": "Payment processed successfully",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:03:15"
    },
    {
        "log_id": "LOG010",
        "gateway": "BANK_BETA",
        "level": "WARNING",
        "error_code": "RETRY_ATTEMPT",
        "message": "Payment retry initiated",
        "service": "payment-service",
        "timestamp": "2026-11-05T10:04:00"
    }
]

#synthetic metrics
METRICS_DATA = []

# BANK_ALPHA: Healthy performance followed by degradation
alpha_metrics = [
    (100, 98, 2, 120, 180, 250),
    (105, 103, 2, 125, 190, 260),
    (110, 107, 3, 130, 200, 280),
    (100, 98, 2, 115, 175, 240),
    (108, 105, 3, 125, 190, 270),
    (112, 109, 3, 130, 195, 275),
    (105, 102, 3, 120, 185, 260),
    (110, 107, 3, 125, 190, 270),

    # Performance degradation begins
    (115, 90, 25, 450, 1200, 2500),
    (120, 75, 45, 850, 2200, 4000),
    (118, 65, 53, 1100, 3000, 5500),
    (125, 60, 65, 1400, 4000, 7000)
]

# BANK_BETA: Stable performance throughout
beta_metrics = [
    (100, 99, 1, 110, 160, 220),
    (105, 103, 2, 115, 170, 230),
    (110, 108, 2, 120, 175, 240),
    (100, 99, 1, 110, 165, 225),
    (108, 106, 2, 115, 170, 235),
    (112, 110, 2, 120, 180, 245),
    (105, 103, 2, 115, 170, 230),
    (110, 108, 2, 120, 175, 240),
    (115, 113, 2, 125, 185, 250),
    (120, 118, 2, 120, 180, 245),
    (118, 116, 2, 125, 185, 255),
    (125, 123, 2, 120, 180, 245)
]


def generate_metrics(gateway, dataset):
    for index, values in enumerate(dataset):
        requests, successes, failures, avg, p95, p99 = values

        METRICS_DATA.append({
            "gateway": gateway,
            "timestamp": f"2026-11-05T10:{index * 5:02d}:00",
            "request_count": requests,
            "successful_requests": successes,
            "failed_requests": failures,
            "average_latency_ms": avg,
            "p95_latency_ms": p95,
            "p99_latency_ms": p99
        })


generate_metrics("BANK_ALPHA", alpha_metrics)
generate_metrics("BANK_BETA", beta_metrics)

#synthetic fraudulent behaviour
FRAUD_EVENTS = [
    # BANK_ALPHA: Suspicious activity
    {
        "transaction_id": "TXN101",
        "gateway": "BANK_ALPHA",
        "amount": 1200,
        "status": "failed",
        "device_id": "DEVICE_X",
        "ip_address": "192.168.1.10"
    },
    {
        "transaction_id": "TXN102",
        "gateway": "BANK_ALPHA",
        "amount": 1500,
        "status": "failed",
        "device_id": "DEVICE_X",
        "ip_address": "192.168.1.10"
    },
    {
        "transaction_id": "TXN103",
        "gateway": "BANK_ALPHA",
        "amount": 1800,
        "status": "failed",
        "device_id": "DEVICE_X",
        "ip_address": "192.168.1.10"
    },
    {
        "transaction_id": "TXN104",
        "gateway": "BANK_ALPHA",
        "amount": 75000,
        "status": "success",
        "device_id": "DEVICE_X",
        "ip_address": "192.168.1.10"
    },
    {
        "transaction_id": "TXN105",
        "gateway": "BANK_ALPHA",
        "amount": 2500,
        "status": "failed",
        "device_id": "DEVICE_Y",
        "ip_address": "192.168.1.10"
    },
    {
        "transaction_id": "TXN106",
        "gateway": "BANK_ALPHA",
        "amount": 900,
        "status": "success",
        "device_id": "DEVICE_Z",
        "ip_address": "192.168.1.20"
    },

    # BANK_BETA: Relatively normal activity
    {
        "transaction_id": "TXN201",
        "gateway": "BANK_BETA",
        "amount": 1200,
        "status": "success",
        "device_id": "DEVICE_A",
        "ip_address": "192.168.2.10"
    },
    {
        "transaction_id": "TXN202",
        "gateway": "BANK_BETA",
        "amount": 2500,
        "status": "success",
        "device_id": "DEVICE_B",
        "ip_address": "192.168.2.11"
    },
    {
        "transaction_id": "TXN203",
        "gateway": "BANK_BETA",
        "amount": 1800,
        "status": "failed",
        "device_id": "DEVICE_C",
        "ip_address": "192.168.2.12"
    },
    {
        "transaction_id": "TXN204",
        "gateway": "BANK_BETA",
        "amount": 3200,
        "status": "success",
        "device_id": "DEVICE_D",
        "ip_address": "192.168.2.13"
    },
    {
        "transaction_id": "TXN205",
        "gateway": "BANK_BETA",
        "amount": 900,
        "status": "success",
        "device_id": "DEVICE_E",
        "ip_address": "192.168.2.14"
    }
]


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PayShield AI"
    }


@app.post("/tools/transactions/analyze")
def analyze_transactions(request: TransactionAnalysisRequest):

    transactions = TRANSACTIONS

    if request.gateway:
        transactions = [
            txn for txn in transactions
            if txn["gateway"] == request.gateway
        ]

    total = len(transactions)

    if total == 0:
        return {
            "total_transactions": 0,
            "message": "No transactions found"
        }

    successful = sum(
        txn["status"] == "SUCCESS"
        for txn in transactions
    )

    failed = total - successful

    return {
        "gateway": request.gateway or "ALL",
        "total_transactions": total,
        "successful_transactions": successful,
        "failed_transactions": failed,
        "success_rate": round(successful / total * 100, 2),
        "failure_rate": round(failed / total * 100, 2)
    }

@app.post("/tools/logs/analyze")
def analyze_logs(request: LogAnalysisRequest):

    logs = APPLICATION_LOGS

    gateway = request.gateway

    if gateway:
        logs = [
            log for log in logs
            if log["gateway"] == gateway
        ]

    if not logs:
        return {
            "gateway": gateway,
            "total_logs": 0,
            "error_count": 0,
            "warning_count": 0,
            "error_groups": [],
            "message": "No logs found"
        }

    errors = [
        log for log in logs
        if log["level"] == "ERROR"
    ]

    warnings = [
        log for log in logs
        if log["level"] == "WARNING"
    ]

    error_counter = Counter(
        log["error_code"] for log in errors
    )

    error_groups = [
        {
            "error_code": error_code,
            "count": count
        }
        for error_code, count in error_counter.most_common()
    ]

    return {
        "gateway": gateway or "ALL",
        "total_logs": len(logs),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "error_groups": error_groups,
        "recent_errors": errors[-5:],
        "recent_warnings": warnings[-5:]
    }

@app.post("/tools/metrics/analyze")
def analyze_metrics(request: MetricsAnalysisRequest):

    gateway = request.gateway.upper()

    metrics = [
        item for item in METRICS_DATA
        if item["gateway"] == gateway
    ]

    if not metrics:
        return {
            "gateway": gateway,
            "status": "no_data",
            "message": "No metrics available for this gateway."
        }

    total_requests = sum(m["request_count"] for m in metrics)
    total_successes = sum(m["successful_requests"] for m in metrics)
    total_failures = sum(m["failed_requests"] for m in metrics)

    success_rate = round(
        (total_successes / total_requests) * 100, 2
    )

    failure_rate = round(
        (total_failures / total_requests) * 100, 2
    )

    avg_latency = round(
        sum(
            m["average_latency_ms"] * m["request_count"]
            for m in metrics
        ) / total_requests,
        2
    )

    first_half = metrics[:len(metrics) // 2]
    second_half = metrics[len(metrics) // 2:]

    def calculate_failure_rate(data):
        requests = sum(m["request_count"] for m in data)
        failures = sum(m["failed_requests"] for m in data)

        return round((failures / requests) * 100, 2)

    first_half_failure_rate = calculate_failure_rate(first_half)
    second_half_failure_rate = calculate_failure_rate(second_half)

    failure_rate_change = round(
        second_half_failure_rate - first_half_failure_rate, 2
    )

    return {
        "gateway": gateway,
        "status": "success",
        "time_intervals": len(metrics),
        "total_requests": total_requests,
        "successful_requests": total_successes,
        "failed_requests": total_failures,
        "success_rate": success_rate,
        "failure_rate": failure_rate,
        "average_latency_ms": avg_latency,

        "latency": {
            "latest_p95_ms": metrics[-1]["p95_latency_ms"],
            "latest_p99_ms": metrics[-1]["p99_latency_ms"],
            "peak_p95_ms": max(m["p95_latency_ms"] for m in metrics),
            "peak_p99_ms": max(m["p99_latency_ms"] for m in metrics)
        },

        "trend": {
            "first_half_failure_rate": first_half_failure_rate,
            "second_half_failure_rate": second_half_failure_rate,
            "failure_rate_change_percentage_points": failure_rate_change
        },

        "time_series": metrics
    }

@app.post("/tools/fraud/analyze")
def analyze_fraud(request: FraudAnalysisRequest):

    gateway = request.gateway.upper()

    transactions = [
        txn for txn in FRAUD_EVENTS
        if txn["gateway"] == gateway
    ]

    if not transactions:
        return {
            "gateway": gateway,
            "status": "no_data",
            "message": "No transaction data available."
        }

    device_activity = defaultdict(list)
    ip_activity = defaultdict(list)

    for txn in transactions:
        device_activity[txn["device_id"]].append(txn)
        ip_activity[txn["ip_address"]].append(txn)

    risk_indicators = []

    # Rule 1: Device velocity
    for device, records in device_activity.items():
        if len(records) >= 3:
            risk_indicators.append({
                "indicator": "HIGH_DEVICE_VELOCITY",
                "device_id": device,
                "transaction_count": len(records),
                "description": (
                    "Multiple transactions originated from the same device."
                ),
                "affected_transaction_ids": [
                    txn["transaction_id"] for txn in records
                ]
            })

    # Rule 2: IP velocity
    for ip, records in ip_activity.items():
        if len(records) >= 4:
            risk_indicators.append({
                "indicator": "HIGH_IP_VELOCITY",
                "ip_address": ip,
                "transaction_count": len(records),
                "description": (
                    "Multiple transactions originated from the same IP address."
                ),
                "affected_transaction_ids": [
                    txn["transaction_id"] for txn in records
                ]
            })

    # Rule 3: Repeated failed attempts
    for device, records in device_activity.items():

        failed_attempts = [
            txn for txn in records
            if txn["status"] == "failed"
        ]

        if len(failed_attempts) >= 3:
            risk_indicators.append({
                "indicator": "REPEATED_PAYMENT_FAILURES",
                "device_id": device,
                "failed_attempts": len(failed_attempts),
                "description": (
                    "Multiple failed payment attempts "
                    "originated from the same device."
                ),
                "affected_transaction_ids": [
                    txn["transaction_id"] for txn in failed_attempts
                ]
            })

    # Rule 4: High-value transactions
    for txn in transactions:
        if txn["amount"] > 50000:
            risk_indicators.append({
                "indicator": "HIGH_VALUE_TRANSACTION",
                "transaction_id": txn["transaction_id"],
                "amount": txn["amount"],
                "description": (
                    "Transaction exceeded the configured "
                    "high-value threshold."
                ),
                "affected_transaction_ids": [
                    txn["transaction_id"]
                ]
            })

    # Summary statistics
    total_transactions = len(transactions)

    failed_transactions = [
        txn for txn in transactions
        if txn["status"] == "failed"
    ]

    flagged_transactions = set()
    for indicator in risk_indicators:
        flagged_transactions.update(
        indicator["affected_transaction_ids"]
    )

    

    return {
        "gateway": gateway,
        "status": "success",
        "total_transactions": total_transactions,
        "failed_transactions": len(failed_transactions),
        "flagged_transaction_count": len(flagged_transactions),
        "risk_indicator_count": len(risk_indicators),
        "risk_indicators": risk_indicators,
        "flagged_transaction_ids": sorted(flagged_transactions),
        "transactions_analyzed": [
            {
                "transaction_id": txn["transaction_id"],
                "amount": txn["amount"],
                "status": txn["status"]
            }
            for txn in transactions
        ]
    }