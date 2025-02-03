class Settings:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage: Both settings1 and settings2 are the SAME object
settings1 = Settings()
settings2 = Settings()

print(settings1 is settings2)