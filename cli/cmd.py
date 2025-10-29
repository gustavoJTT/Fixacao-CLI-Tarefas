

class ProjectsCMD:
    
    def sign_in(self):
        user = input("username: ")
        password = input("password: ")
        return {"username": user, "password": password}
    
    def sign_up(self):
        user = input("username: ")
        password = input("password: ")
        return {"username": user, "password": password}
    
    def new_project(self, user):
        name = input("project name: ")
        owner = user.get("username")
        
        return {"name": name}
    
    def all_projects(self, user):
        return []
    
    def new_task(self, user):
        return {}
    
    def all_task(self, user):
        return []