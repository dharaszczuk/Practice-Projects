#! python3
# randomQuizGenerator.py - tworzy quiz z losowo ułożonymi pytaniami i odpowiedziami

import random

# Dane quizu. Klucze to nazwy stanów, wartości to ich stolice.
capitals = {"Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas":"Little Rock", "Kalifornia":"Sacramento", "Kolorado":"Denver", "Connecticut":"Hartford",
            "Delaware":"Dover", "Floryda":"Tallahasse", "Georgia":"Atlanta", "Hawaje":"Honolulu", "Idaho":"Boise", "Illnois":"Springfield", "Indiana":"Indianapolis", "Iowa":"Des Moines",
            "Kansas":"Topeka", "Kentucky":"Frankfort", "Luizjana":"Baton Rouge", "Maine":"Augusta", "Maryland":"Annapolis", "Massachusetts":"Boston", "Michigan":"Lansing",
            "Minnesota":"Saint Paul", "Mississippi":"Jackson", "Missouri":"Jefferson City", "Montana":"Helena", "Nebraska":"Lincoln", "Nevada":"Carson City", "New Hampshire":"Concord",
            "New Jersey":"Trenton", "Nowy Meksyk":"Santa Fe", "Nowy Jork":"Albany", "Karolina Północna":"Raleigh", "Dakota Północna":"Bismarck", "Ohio":"Columbus",
            "Oklahoma":"Oklahoma City", "Oregon":"Salem", "Pensylwania":"Harrisburg", "Rhode Island":"Providence", "Karolina Południowa":"Columbia", "Dakota Południowa":"Pierre",
            "Tennessee":"Nashville", "Teksas":"Austin", "Utah":"Salt Lake City", "Vermont":"Montpelier", "Wirginia":"Richmond", "Waszyngton":"Olympia", "Wirginia Zachodnia":"Charleston",
            "Wisconsin":"Madison", "Wyoming":"Cheyenne"}

# Wygenerowanie 35 plików quizu
for quiz_num in range(3):
    # Utworzenie plików quizu i odpowiedzi na pytania
    quiz_file = open("capitalsquiz%s.txt" % (quiz_num + 1), "w")
    answer_key_file = open("capitalsquiz_answers%s.txt" % (quiz_num + 1), "w")

    # Zapis nagłówka quizu
    quiz_file.write("Imię i nazwisko:\n\nData:\n\nKlasa:\n\n")
    quiz_file.write((" "*20) + "Quiz stolic stanów (Quiz %s)" % (quiz_num + 1))
    quiz_file.write("\n\n")

    # Losowe ustalenie kolejności pytań
    states = list(capitals.keys())
    random.shuffle(states)

    #TODO: Iteracja przez 50 stanów i utworzenie pytania dotyczącego każdego z nich
    for question_num in range(50):
        #Przygotowanie prawidłowych i nieprawidłowych odpowiedzi
        correct_answer = capitals[states[question_num]]1
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_options = wrong_answer + [correct_answer]
        random.shuffle(answer_options)

        #Zapis pytania i odpowiedzi w pliku quizu
        quiz_file.write("%s. Co jest stolicą stanu %s?\n" % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write("    %s. %s\n" % ("ABCD"[i], answer_options[i]))
        quiz_file.write("\n")

        # Zapis odpowiedzi w pliku.
        answer_key_file.write("%s. %s\n" % (question_num + 1, "ABCD"[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()
