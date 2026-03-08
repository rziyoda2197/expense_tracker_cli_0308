import json
import os

FILE = "expenses.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def save(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    data = load()
    data.append({"name":name,"amount":amount})
    save(data)

def show_expenses():
    data = load()
    total = 0
    for e in data:
        print(e["name"], "-", e["amount"])
        total += e["amount"]
    print("Total:", total)

while True:
    print("\n1.Add expense")
    print("2.Show expenses")
    print("3.Exit")

    c = input("Choose: ")

    if c == "1":
        add_expense()
    elif c == "2":
        show_expenses()
    elif c == "3":
        break
