class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class FaqatBittaInstans(Singleton):
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"FaqatBittaInstans: {self.nom}"

# Test
instans1 = FaqatBittaInstans("Instans 1")
instans2 = FaqatBittaInstans("Instans 2")

print(instans1)  # FaqatBittaInstans: Instans 1
print(instans2)  # FaqatBittaInstans: Instans 1
```

Kodda `Singleton` metaklassi faqat bitta instans yaratish uchun ishlatiladi. `FaqatBittaInstans` klassi `Singleton` metaklassidan meros oladi va faqat bitta instans yaratish uchun ishlatiladi. `instans1` va `instans2` ni yaratishda, faqat bitta instans yaratiladi va u `instans1` va `instans2` uchun bir xildir.
