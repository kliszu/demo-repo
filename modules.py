class student:

   def __init__(self, name, major, gpa, is_on_probation):
       self.name = name
       self.major = major
       self.gpa = gpa
       self.is_on_probation = is_on_probation
   def on_honor_roll(self):
       if self.gpa >= 3.5:
           return True
       else:
           return False


class question:
    def __init__(self,prompt, answer):
        self.prompt = prompt
        self.answer = answer