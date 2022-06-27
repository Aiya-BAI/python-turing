# 民意调查
class AnonymousSurvey:
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷调查"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_response(self):
        """显示收集到的所有答卷"""
        print('Survey results:')
        for response in self.responses:
            print(f'-{response}')

