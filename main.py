class KitForge:
    def __init__(self):
        self.tools = {
            "1": ("System Info", self.system_info),
            "2": ("Say Hello", self.say_hello),
            "3": ("Exit", self.exit_tool)
        }
        self.running = True

    def menu(self):
        print("=== KitForge Tool Suite ===")
        for key, (name, _) in self.tools.items():
            print(f"{key}. {name}")

    def run(self):
        while self.running:
            self.menu()
            choice = input("Choose a tool (1-3): ").strip()
            tool = self.tools.get(choice)
            if tool:
                tool[1]() 
            else:
                print("Invalid choice. Please try again.\n")

    def system_info(self):
        import platform
        print("\n--- System Info ---")
        print(f"Platform: {platform.system()}")
        print(f"Release: {platform.release()}")
        print(f"Processor: {platform.processor()}\n")

    def say_hello(self):
        name = input("Enter your name: ")
        print(f"Hello, {name}! Welcome to KitForge.\n")

    def exit_tool(self):
        print("Exiting KitForge. Goodbye!")
        self.running = False



kitforge = KitForge()
kitforge.run()

