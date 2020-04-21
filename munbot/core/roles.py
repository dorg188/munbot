import enum


class Roles(str, enum.Enum):
    SecretaryGeneral = 'Secretary General'
    Advisor = 'Advisors'
    Chair = 'Chairs'
    Delegate = 'Delegates'
    Admin = 'Admins'
    VIP = 'VIPs'
    Observer = 'Observers'
