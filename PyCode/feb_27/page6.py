class Teacher:
    def __init__(self):
        print('inside Teacher __init__')

class LabAssistant:
    def __init__(self):
        print('inside LabAssistant__init__')

class TeacherLabAssistant(Teacher, LabAssistant):
    def __init__(self):
        Teacher.__init__(self)
        LabAssistant.__init__(self)
        print('inside TeacherLabAssistant __init__')

