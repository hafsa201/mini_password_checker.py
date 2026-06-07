class password_check:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.symbols = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/`~"

    def length_check(self):
        if len(self.password) >= 8:
            self.score += 1

    def symbol_check(self):
        if any(char in self.symbols for char in self.password):
            self.score += 1

    def space_check(self):
        if " " not in self.password:
            self.score += 1

    def confirmation_note(self):
        if self.score == 3:
            print("Password is strong and successfully saved!")
        elif self.score == 2:
            print("Password is medium strength.")
        else:
            print("Password is weak. Try adding symbols, increasing length, and removing spaces.")

    def ultimate_check(self):
        self.score = 0  # reset every run

        self.length_check()
        self.symbol_check()
        self.space_check()

        self.confirmation_note()


# example usage
user1 = password_check("hafsa123")
user1.ultimate_check()
