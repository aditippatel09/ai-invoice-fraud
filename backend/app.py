import pandas as pd

# Load invoice data
data = pd.read_csv("data/invoice.csv")

print("INVOICE FRAUD REPORT\n")

# Rule 1: Duplicate invoice numbers
dup_invoice_numbers = data[data.duplicated(subset="invoice_number", keep=False)]
print("Duplicate invoice numbers:")
print(dup_invoice_numbers if not dup_invoice_numbers.empty else "None")
print()

# Rule 2: Same vendor + same amount
dup_vendor_amount = data[data.duplicated(subset=["vendor_name", "total_amount"], keep=False)]
print("Duplicate vendor & amount:")
print(dup_vendor_amount if not dup_vendor_amount.empty else "None")
print()

# Rule 3: Abnormally high invoice amount
average_amount = data["total_amount"].mean()
threshold = average_amount * 2

high_amounts = data[data["total_amount"] > threshold]
print("Abnormally high invoices:")
print(high_amounts if not high_amounts.empty else "None")