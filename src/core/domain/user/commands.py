from .services import UserService


class GetUsers:
    def __init__(self, service: UserService):
        self.service = service

    
    async def __call__(self):
        return self.service.get_all_users()
