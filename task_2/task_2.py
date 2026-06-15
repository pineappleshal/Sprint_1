class Tester:

    def __init__(self, name):
        self.name = name
        self.deadline = True

    def work_hard(self):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')


tester_1 = Tester('tester_1')
tester_1.deadline = False
tester_1.work_hard()

tester_2 = Tester('tester_2')
tester_2.work_hard()