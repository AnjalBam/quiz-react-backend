# Quiz App Backend
Hello there fellas, this is the Backend for the quiz app that I have built
. This repo consists of a simple setup for the api to list all the questions
 and also to create the question with answers.
 
 The endpoints are:
 
 `api/list/` It only accepts the get method
 
`api/create/` It only accepts the POST method

#####Note:
the data format for the create api is as follows:
```json
{
        "id": 1,
        "q_title": "",
        "answers": [
            {
                "answer_no": 1,
                "choice_answer": "",
                "is_correct": false
            },
            {
                "answer_no": 2,
                "choice_answer": "",
                "is_correct": true
            },
            {
                "answer_no": 3,
                "choice_answer": "",
                "is_correct": false
            },
            {
                "answer_no": 4,
                "choice_answer": "",
                "is_correct": false
            }
        ]
    }
```
Only set true for the true answer only...

### How to setup this project locally &rarr;
1. Create your virtual environment and activate your virtual env
2. Install the requirements with command  `pip install -r requirements.txt`
3. Run the server using command `./manage.py runserver`

##### Note
There's an `example.env.py` file in the settings package in the Quiz directory
. Copy the settings in the example.env file in a new env.py file and also put
 your
  security key as well as database credentials if you have any, however they
   aren't required for the `sqlite3`.
   