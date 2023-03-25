import tkinter as tk

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def check_prime():
    n = int(entry.get())
    if is_prime(n):
        result.configure(text=f"{n} is a prime number.")
    else:
        result.configure(text=f"{n} is not a prime number.")

# Create the main window
window = tk.Tk()
window.title("Prime Number Checker")

# Create the entry widget
entry = tk.Entry(window)
entry.pack()

# Create the check button
button = tk.Button(window, text="Check", command=check_prime)
button.pack()

# Create the result label
result = tk.Label(window, text="")
result.pack()

# Start the main event loop
window.mainloop()

