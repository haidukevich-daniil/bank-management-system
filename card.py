class Card:
    def __init__(self, card_number, account, pin):
        self.card_number = card_number
        self.account = account
        self.pin = pin
        self.is_blocked = False
        self.failed_attempts = 0


    def __str__(self):
        return f"Card number: {self.card_number}\nAccount ID: {self.account.account_id}"

    def authorize(self, code):
        if self.is_blocked:
            raise ValueError("Card is blocked")

        if code != self.pin:
            self.failed_attempts += 1 

            if self.failed_attempts == 3:
                self.is_blocked = True
                raise ValueError("Card is blocked")
            
            raise ValueError("Wrong PIN")

        self.failed_attempts = 0
        print("You are authorized")


    def to_dict(self):
        return {
            "card_number": self.card_number,
            "account_id": self.account.account_id,
            "pin": self.pin,
            "is_blocked": self.is_blocked,
            "failed_attempts": self.failed_attempts
        }

    @classmethod
    def from_dict(cls, data, account):
        card = cls(data["card_number"], account, data["pin"])
        card.is_blocked = data["is_blocked"]
        card.failed_attempts = data["failed_attempts"]
        return card