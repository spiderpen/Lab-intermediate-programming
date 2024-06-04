class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("The numerator and denominator must be integers.")

        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            sign = -1 if (numerator < 0) ^ (denominator < 0) else 1
            a = abs(numerator)
            b = abs(denominator)
            gcd = self._gcd(a, b)
            self._numerator = sign * (a // gcd)
            self._denominator = b // gcd

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only add Fraction with Fraction.")

    # Similar methods for subtraction, multiplication, division, negation, equality check, string representation, repr, float conversion, and int conversion 

class BankAccount:
    _next_account_number = 1

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_account_number(self):
        return self.account_number

    def __str__(self):
        return f"Account({self.account_number}): {self.owner}, Balance: ${self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance}, account_number={self.account_number})"


class Family:
    def __init__(self, parents, *children):
        if len(parents) != 2:
            raise ValueError("Family must have exactly two parents.")

        self.parents = parents
        self.children = list(children)

    def add_child(self, child):
        self.children.append(child)

    def __iter__(self):
        return iter(self.children)

    def __str__(self):
        parents_str = f"Parents: {self.parents[0]} and {self.parents[1]}"
        children_str = ", ".join(self.children) if self.children else "No children"
        return f"{parents_str}\nChildren: {children_str}"

    def __repr__(self):
        return f"Family(parents={self.parents}, children={self.children})"
    
# Example usage for Fraction class:
f1 = Fraction(2, 3)
f2 = Fraction(4, 5)
print(f1 + f2) 
print(f1 - f2)  
print(f1 * f2)  
print(float(f1))  
print(int(f1))  

# Example usage for BankAccount class:
account1 = BankAccount("Steven", 1000)
account2 = BankAccount("Valerian", 500)
print(account1)  
print(account2)  
account1.deposit(200)
print(account1) 
account1.withdraw(300)
print(account1)  

# Example usage for Family class:
family = Family(("Steven", "Tepen"), "Stephen", "Stevie")
print(family)  
family.add_child("Valerian")
print(family)  
for child in family:
    print(child)

