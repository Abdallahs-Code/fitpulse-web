from .base_user import BaseUser, UserRole
from . import db

class Admin(BaseUser):
    role: UserRole = UserRole.Admin

    def __init__(self, email: str, first_name: str, last_name: str, *args, **kwargs):
        super().__init__(email, first_name, last_name, *args, **kwargs)

        
        
        
# a = Admin("ashraf@gmail.com","ashraf","hakimi")
# a.set_password("123")
# Admin.insert(a)
