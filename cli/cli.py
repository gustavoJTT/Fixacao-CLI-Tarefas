from cmd import ProjectsCMD 


class ProjectsCLI:
    def __init__(self):
        self.run : bool
        self.user : dict = {}
        self.cmd = ProjectsCMD()
        
    def start(self):
        self.is_running = True
        print("\n🚀 Projects CLI initialized.\n")

        while self.is_running:
            self._show_menu()
            self._handle_option()

    def stop(self):
        self.is_running = False
        print("\n👋 Exiting Projects CLI. Goodbye!\n")

    def _show_menu(self):
        if not self.user:
            menu = """
        ------- LOGIN -------
        1 > Sign In
        2 > Sign Up
        0 > Exit
        
            """
        else:
            menu = f"""
        ------- PROJECTS CLI -------
        Logged as: {self.user.get("username", "Unknown")}
        
        1 > New Project
        2 > All Projects
        3 > New Task
        4 > All Tasks
        0 > Logout
         
            """
        print(menu)

    def _handle_option(self):
        try:
            option = int(input(" > ").strip())
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")

        if not self.user:
            self._handle_auth_option(option)
        else:
            self._handle_project_option(option)

    #=============== Options ===================#
    def _handle_auth_option(self, option: int):
        match option:
            case 1:
                user = self.cmd.sign_in()
                if user:
                    self.user = user
                    print(f"🗸 Logged in as {user.get('username', 'user')} \n")
            case 2:
                user = self.cmd.sign_up()
                if user:
                    self.user = user
                    print(f"🗸 Account created and logged in as {user.get('username', 'user')}\n")
            case 0:
                self.stop()
            case _:
                print("❌ Invalid option. Try again.")

    def _handle_project_option(self, option: int):
        match option:
            case 1:
                project = self.cmd.new_project(self.user)
                if project:
                    print(f"🗸 New project created: {project} \n")
            case 2:
                projects = self.cmd.all_projects(self.user)
                if not projects:
                    print("⚠ No projects registered. \n")
                else:
                    print("\n📂 Projects:")
                    for p in projects:
                        print(f"  • {p}")
            case 3:
                task = self.cmd.new_task(self.user)
                if task:
                    print(f"🗸 New task created: {task} \n")
            case 4:
                tasks = self.cmd.all_task(self.user)
                if not tasks:
                    print("⚠ No tasks registered. \n")
                else:
                    print("\n🗒 Tasks:")
                    for t in tasks:
                        print(f"  • {t}")
            case 0:
                print("🔒 Logged out. \n")
                self.user = {}
            case _:
                print("❌ Invalid option. Try again. \n")

cli = ProjectsCLI()
cli.start()