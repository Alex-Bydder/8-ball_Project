import random

# Responses to said usr_question
random_responses = ['Certainly', 'Likely', 'Possibly', 'Unlikely', 'Not going to happen', 'Most likely']
ran_num_response = random.randint(0, len(random_responses))

# What user asks
usr_question = (input('Ask a question: '))

# Ensuring that it is actually a question
if ("?" not in usr_question):
    usr_question = (input('(No question Mark) Ask a question: '))

if (usr_question != ""):
    print (random_responses[ran_num_response])

