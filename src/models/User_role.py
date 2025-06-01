from enum import StrEnum

class RoleEnum(StrEnum):
    ADMIN = "admin"
    TENANT = "tenant"
    LANDLORD = "landlord"

    @classmethod
    def values(self):
        return [_.value for _ in list(self)]

    @classmethod
    def has(self, value):
        return value in self.values()