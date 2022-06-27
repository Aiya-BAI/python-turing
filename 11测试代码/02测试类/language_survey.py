from survey import AnonymousSurvey as AS

# 定义一个问题，并创建一个调查
question = "What language did you first learn to speak"
my_survey = AS(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit\n")
while True:
    response = input('Language:')
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print('Thank you')
my_survey.show_response()





