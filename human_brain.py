class Human:
    def __init__(self,name):
        print('Human Object creation....')
        self.name = name
        self.head = self.Head()
    def info(self):
        print('Hello Myself', self.name)
        print('I am full busy with,')
        self.head.talk()
        self.head.brain.think()
    class Head:
        def __init__(self):
            print('Head object cration...')
            self.brain = self.Brain
        def talk(self):
            print('Talking...')
        class Brain:
            def __init__(self):
                print('Brain object creayion......')
            def think():
                print('Thinking....')
human = Human('Sdbisht')
human.info()