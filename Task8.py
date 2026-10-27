
# Repeated Transaction Detection

transactions = []
suspicious = []
seen_ids = set()

n = int(input("Enter number of transactions: "))
threshold = float(input("Enter transaction amount threshold: "))

for i in range(n):
    print("\nTransaction", i + 1)

    tid = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))

    transactions.append((tid, amount))

for tid, amount in transactions:
    reasons = []

    if tid in seen_ids:
        reasons.append("Duplicate transaction ID")
    else:
        seen_ids.add(tid)

    if amount > threshold:
        reasons.append("Amount exceeds threshold")

    if reasons:
        suspicious.append((tid, amount, reasons))

print("\n----- TRANSACTION REPORT -----")

print("All Transactions:")
for transaction in transactions:
    print(transaction)

print("\nSuspicious Transactions:")
if suspicious:
    for tid, amount, reasons in suspicious:
        print("ID:", tid, "| Amount: Rs.", amount)
        print("Reason:", ", ".join(reasons))
else:
    print("No suspicious transactions found.")

print("\nTotal transactions:", len(transactions))
print("Suspicious entries:", len(suspicious))
