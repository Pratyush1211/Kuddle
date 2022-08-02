class UserService:
    def __init__(self):
        self.users = {}
        
        # dummy users for testing
        self.users["karan"] = "karan"
        self.users["shivansh"] = "shivansh"
        self.users["pratyush"] = "pratyush"
        self.users["dev"] = "dev"
        self.users["bharath"] = "bharath"
    
    def register(self, username):
        if username in self.users:
            return False
        return True
    
    def authenticate(self, username):
        if username not in self.users:
            return False
        return True