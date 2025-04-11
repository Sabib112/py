class bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")
    
    def fly(self):
        print("Fly faster")

class penguin(bird):
    def __init__(self):
        print("Penguin is ready")

    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("swim faster")
    
penggy=penguin()
penggy.whoisthis()
penggy.fly()
penggy.run()