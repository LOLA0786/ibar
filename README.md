# 🍸 iBar — Regulated Alcohol Wallet & POS Authorization System

iBar is a **wallet-based alcohol consumption platform** that allows users to purchase and redeem alcohol **digitally and safely** across partnered restaurants, with **real-time authorization, fraud prevention, and compliance controls**.

Think of it as:
> **A payments-grade control plane for alcohol consumption**

---

## 🚀 Core Concepts

### 🧾 Alcohol Wallet (Bottle-as-Credit)
- Users purchase **virtual bottles** (e.g. 750ml)
- The bottle represents **entitled alcohol volume**
- Volume is redeemed incrementally (e.g. 30ml / 60ml pours)

### 🏪 POS Authorization (Not Inventory)
- Restaurants **do not own the bottle**
- They request authorization to pour
- The system decides **ALLOW / BLOCK** before alcohol is served

### 🔐 Pre-Execution Control
- No post-facto reconciliation
- Every pour is:
  - Authorized once
  - Idempotent
  - Replay-safe
  - Audit logged

---

## 🧠 Why iBar Is Different

| Problem | Traditional Systems | iBar |
|------|---------------------|------|
| Fraud | Manual checks | Cryptographic idempotency |
| Double pours | Possible | Impossible |
| Compliance | After-the-fact | Enforced before pour |
| Audit | Incomplete | Deterministic & replayable |
| Global expansion | Hard-coded rules | Policy-driven |

---

## 🏗️ Architecture Overview

Mobile App (User)
↓
QR Code (Time-bound)
↓
Restaurant POS
↓
/pos/authorize-pour
↓
iBar Core
├─ Wallet (Bottle)
├─ Ledger (Transactions)
├─ Fraud Controls
└─ Compliance Engine

yaml
Copy code

---

## 🔑 Key Features

### ✅ Authentication & Roles
- JWT-based auth
- Roles:
  - `USER`
  - `RESTAURANT`

### 🍾 Wallet / Bottles
- Create bottles with total volume
- Track remaining ml precisely
- Atomic balance updates

### 🍺 POS Authorization
- `/pos/authorize-pour`
- Idempotency via scan_id
- Row-level locking
- Time-bound QR validation

### 🛡️ Fraud Protection
- Double-scan prevention
- Replay attack protection
- Race-condition safe
- Evidence hash per transaction

### 📊 Analytics (Wrapped)
- Yearly drinking summary
- Total volume consumed
- Top brands
- Foundation for “Spotify Wrapped for Alcohol”

### 🌍 Compliance-Ready
- Country / state policy engine
- Prohibition support
- Time-of-day rules
- Daily consumption limits

---

## 🧪 Example Flows

### Create Bottle (User)
```bash
POST /bottles/create
Authorization: Bearer <USER_TOKEN>

{
  "brand": "Johnnie Walker Black",
  "total_ml": 750
}
Authorize Pour (Restaurant POS)
bash
Copy code
POST /pos/authorize-pour
Authorization: Bearer <RESTAURANT_TOKEN>
Idempotency-Key: scan-uuid

{
  "bottle_id": "<bottle_id>",
  "pour_ml": 60,
  "qr_issued_at": <unix_timestamp>
}
🧱 Tech Stack
Backend: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy + Alembic

Auth: JWT

Security: Idempotency, row locking, cryptographic evidence

Future: UAAL (Unified Authorization & Audit Layer)

🔮 Roadmap
 Auth & Wallet

 POS Authorization

 Fraud Protection

 Analytics (Wrapped)

 POS SDK (JS / Android)

 UAAL Shadow Mode

 Country/State Rule Packs

 Mobile App (iOS / Android)

 Enterprise Audit Exports

⚠️ Legal Note
iBar is a technology platform.
Alcohol sale, service, and consumption remain subject to local laws and licensing.
The system is designed to enforce compliance, not bypass it.

👤 Author
Built by LOLA0786
Focused on control planes, policy enforcement, and real-world AI systems.

⭐ Vision
Alcohol should be entitled, traceable, and responsibly controlled —
not anonymous, over-served, or unaccountable.

iBar is the infrastructure to make that possible.
