amounts = [1200, 1300, 1250, 9800, 1100]

average = sum(amounts) / len(amounts)

print("Average invoice amount:", average)
for amt in amounts:
    if amt > average * 2:
        print("⚠️ Suspicious invoice detected:", amt)
