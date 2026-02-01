import pandas as pd
def detect_fraud(csv_path):
    data = pd.read_csv(csv_path, encoding="latin1")


    result = {}

    # Rule 1: Duplicate invoice numbers
    dup_invoice_numbers = data[data.duplicated(subset="invoice_number", keep=False)]
    result["duplicate_invoice_numbers"] = dup_invoice_numbers.to_dict(orient="records")

    # Rule 2: Same vendor + same amount
    dup_vendor_amount = data[data.duplicated(subset=["vendor_name", "total_amount"], keep=False)]
    result["duplicate_vendor_amount"] = dup_vendor_amount.to_dict(orient="records")

    # Rule 3: Abnormally high invoice amount
    average_amount = data["total_amount"].mean()
    threshold = average_amount * 2
    high_amounts = data[data["total_amount"] > threshold]
    result["high_amount_invoices"] = high_amounts.to_dict(orient="records")

    return result