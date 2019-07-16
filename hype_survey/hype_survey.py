import json
#
# def create_file():
#     responses = collect_responses()
#     my_json = json.dumps(responses)
#     f = open("responses.json", "w")
#     f.write(my_json)
#     f.close()

def collect_responses():
    questions = ["What is your name?",
                 "What is your date of birth? (MM/DD/YYYY)",
                 "What is your age?",
                 "How many people live in your home more than 50% of the time?",
                 "How many hours per week do you spend on the phone?",
                 "Name the app,  program or website that you use most frequently?",
                 "What has been your favorite thing to learn so far?",
                 "Continue collecting responses?"]
    responses = []

    collecting_responses = True
    while collecting_responses:
        response = {}
        for num in range(len(questions)):
            answer = input(questions[num])
            if num == len(questions) - 1:
                if answer == 'False':
                    collecting_responses = False
            else:
                response[num] = answer

        responses.append(response)

    return responses


if __name__ == '__main__':
    collect_responses()


