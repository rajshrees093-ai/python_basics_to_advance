def invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

invoice("Raj", 15,"19/05/2026")