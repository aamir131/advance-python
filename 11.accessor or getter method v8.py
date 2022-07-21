class Mobile:
    def __init__(self):
        self.modal = "Realme 5 Pro"     # Instance Variable
    
    def get_modal(self):                # ACCESSOR OR GETTER METHOD
        return self.modal

realme = Mobile()
m = realme.get_modal()                  # Calling Accessor OR Getter Method
print(m)
        