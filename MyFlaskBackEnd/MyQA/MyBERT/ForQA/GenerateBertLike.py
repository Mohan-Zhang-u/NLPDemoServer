import json
import codecs

# The structure looks like this:
# SQuAD:https://rajpurkar.github.io/SQuAD-explorer/
#
# file.json
# ├── "data"
# │   └── [i]
# │       ├── "paragraphs"
# │       │   └── [j]
# │       │       ├── "context": "paragraph text"
# │       │       └── "qas"
# │       │           └── [k]
# │       │               ├── "answers"
# │       │               │   └── [l]
# │       │               │       ├── "answer_start": N
# │       │               │       └── "text": "answer"
# │       │               ├── "id": "<uuid>"
# │       │               └── "question": "paragraph question?"
# │       └── "title": "document id"
# └── "version": 1.1


# data=[]
# version="my_ver"
#
# # now, things inside data: (multiple elements)
# title=""
# paragraphs=[]
#
# # now, things inside paragraphs: (multiple elements)
# context=""
# qas=[]
#
# # now, things inside qas: (multiple elements)
# answers=[]
# id=""
# question=""
#
# # now, things inside answers: (multiple elements)
# answer_start=-1
# text=""


def get_paragraph(filename):
    with codecs.open('Paragraphs/'+filename, 'r',encoding='utf8') as fp:
        paragraph = fp.read()
        paragraph = paragraph.replace('\r\n', '\n')
        paragraph = paragraph.replace('\n', '\n')
        # paragraph.replace('\'', ' ')
        paragraph = paragraph.replace('\'', '\\\'')
        paragraph = paragraph.replace('\"', '\\\"')
        return paragraph

def generate_multi_test_cases(list_of_paragraphs, list_of_questions, name_of_file):
    assert len(list_of_paragraphs) == len(list_of_questions)
    length_of_them = len(list_of_paragraphs)

    data = []
    version = "my_ver"

    # now, things inside data: (multiple elements)
    title = ""
    paragraphs = []

    # now, things inside paragraphs: (multiple elements)
    context = ""
    qas = []

    # now, things inside qas: (multiple elements)
    answers = []
    id = ""
    question = ""

    # now, things inside answers: (multiple elements)
    answer_start = -1
    text = ""

    jsondict={}
    jsondict["data"]=data
    jsondict["version"]=version

    for j in range(length_of_them):
        new_paragraph = {}
        new_paragraph["context"]=list_of_paragraphs[j]
        new_paragraph["qas"]=[{"answers": [{"answer_start": -1, "text": ""}], "question":list_of_questions[j], "id":list_of_questions[j]}]
        data.append({"title": "", "paragraphs":[new_paragraph]}) # here we can have multiple paragraph in paragraphs

    with open('Data/'+name_of_file+'.json', 'w') as fp:
        json.dump(jsondict, fp)


if __name__ == "__main__":
    # list_of_paragraphs=["Super Bowl 50 was an American football game to determine the champion of the National Football League (NFL) for the 2015 season. The American Football Conference (AFC) champion Denver Broncos defeated the National Football Conference (NFC) champion Carolina Panthers 24\u201310 to earn their third Super Bowl title. The game was played on February 7, 2016, at Levi's Stadium in the San Francisco Bay Area at Santa Clara, California. As this was the 50th Super Bowl, the league emphasized the \"golden anniversary\" with various gold-themed initiatives, as well as temporarily suspending the tradition of naming each Super Bowl game with Roman numerals (under which the game would have been known as \"Super Bowl L\"), so that the logo could prominently feature the Arabic numerals 50."]
    # list_of_questions = ["hich NFL team represented the AFC at Super Bowl 50?"]
    # list_of_paragraphs.append(get_paragraph("dota2.txt"))
    # list_of_questions.append("what is Dota 2?")
    # list_of_paragraphs.append(get_paragraph("dota2.txt"))
    # list_of_questions.append("what is The International?")
    # list_of_paragraphs.append(get_paragraph("dota2.txt"))
    # list_of_questions.append("When did Dota 2 support VR?")
    # list_of_paragraphs.append(get_paragraph("dota2.txt"))
    # list_of_questions.append("Who developed Dota 2?")
    # list_of_paragraphs.append(get_paragraph("dota2.txt"))
    # list_of_questions.append("How many teams are there in one game of Dota 2?")
    # list_of_paragraphs.append(get_paragraph("dota2.txt"))
    # list_of_questions.append("How can a team win a game of Dota 2?")
    list_of_paragraphs=[]
    list_of_questions=[]
    list_of_paragraphs.append(get_paragraph("imperial_short.txt"))
    list_of_questions.append("Imperial's income is growing or decreasing?")
    list_of_paragraphs.append(get_paragraph("imperial_short.txt"))
    list_of_questions.append("How many barrels of petroleum product does Imperial sale each day during its highest quarterly sales?")
    list_of_paragraphs.append(get_paragraph("imperial_short.txt"))
    list_of_questions.append("How many barrels of Refinery throughput does Imperial sale per day during its highest quarterly sales?")


    generate_multi_test_cases(list_of_paragraphs, list_of_questions, "imperial_short")

    list_of_paragraphs = []
    list_of_questions = []
    list_of_paragraphs.append(get_paragraph("imperial_long.txt"))
    list_of_questions.append("How much is Bitumen realizations average barrel price for the second quarter of 2018?")
    list_of_paragraphs.append(get_paragraph("imperial_long.txt"))
    list_of_questions.append("How is the quarterly chemical net income?")
    list_of_paragraphs.append(get_paragraph("imperial_short.txt"))
    list_of_questions.append("Imperial's income is growing or decreasing?")

    generate_multi_test_cases(list_of_paragraphs, list_of_questions, "imperial_long")

    list_of_paragraphs = []
    list_of_questions = []
    list_of_paragraphs.append(get_paragraph("beeshort.txt"))
    list_of_questions.append("How do traditional beekeepers feel about GM bees?")

    generate_multi_test_cases(list_of_paragraphs, list_of_questions, "beeshort")

    list_of_paragraphs = []
    list_of_questions = []
    list_of_paragraphs.append(get_paragraph("bee.txt"))
    list_of_questions.append("What leads bees to abandon their hive?")
    list_of_paragraphs.append(get_paragraph("bee.txt"))
    list_of_questions.append("How do traditional beekeepers feel about GM bees?")
    list_of_paragraphs.append(get_paragraph("bee.txt"))
    list_of_questions.append("When will the bee's egg pop when injecting to it?")
    list_of_paragraphs.append(get_paragraph("bee.txt"))
    list_of_questions.append("What is already threatening crops worldwide?")
    list_of_paragraphs.append(get_paragraph("bee.txt"))
    list_of_questions.append("From when do people start to consuming honey?")

    generate_multi_test_cases(list_of_paragraphs, list_of_questions, "bee")


