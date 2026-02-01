# Day 2 – Invoice Fraud Detection Logic

## Purpose
This document explains the fraud detection rules implemented on Day 2.
These rules operate on structured invoice data (CSV format) and form the
core backend logic of the Invoice Fraud Detection System.

---

## Input Data
The system uses invoice data stored in CSV format with the following columns:

- invoice_number
- vendor_name
- invoice_date
- total_amount

Each row in the CSV represents one invoice.

---

## Fraud Detection Rules Implemented

### Rule 1: Duplicate Invoice Number
If the same invoice number appears more than once, it may indicate
duplicate billing or fraud.

**Logic Used:**
- Check repeated values in the `invoice_number` column.
- Flag all repeated entries.

---

### Rule 2: Same Vendor and Same Amount
If the same vendor submits multiple invoices with the exact same amount,
it may indicate suspicious or repeated billing.

**Logic Used:**
- Check duplicates using a combination of `vendor_name` and `total_amount`.

---

### Rule 3: Abnormally High Invoice Amount
Invoices that are significantly higher than normal are flagged.

**Logic Used:**
- Calculate the average invoice amount.
- Any invoice with amount greater than 2 × average is flagged as suspicious.

---

## Output
The backend script prints a fraud report containing:

- Duplicate invoice numbers (if any)
- Duplicate vendor and amount combinations
- Abnormally high invoice amounts

This output is currently printed in the terminal and will later be
returned via an API and displayed on the web dashboard.

---

## Notes
- These rules are rule-based (not machine learning).
- They form the foundation for future AI/ML-based fraud scoring.
- The logic implemented here will be reused in the website backend.
