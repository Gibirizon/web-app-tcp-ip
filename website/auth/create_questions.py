from flask_login import current_user

from .. import db
from ..models import Answer, Question


def create_questions():
    questions = {
        "Na jakim porcie pracuje protokół DNS": [21, 22, 53, 69, 53],
        "Za co odpowiada warstwa internetowa": ["dodanie numerów portów aplikacji", "zapewnia interfejs usług sieciowych", "zapewnia dostęp do medium transmisyjnego", "adresowanie danych z wykorzystaniem adresów IP", "adresowanie danych z wykorzystaniem adresów IP"],
        "W której warstwie pracuje protokół ARP": ["w warstwie aplikacij", "w warstwie transportowej", "w warstwie internetowej", "w warstwie dostępu do sieci", "w warstwie dostępu do sieci"],
        "Za co odpowiada protokól ICMPv4": ["pozwala na przesłanie informacji zwrotnej o błędach w dostarczaniu pakietów", "adresuje pakiety w celu kompleksowego dostarczania przez sieć", "jest otwartym standardowym protokołem routingu wewnętrznego", "zapewnia dynamiczne odwzorowanie pomiędzy adresami IPv4 a adresami sprzętowymi", "pozwala na przesłanie informacji zwrotnej o błędach w dostarczaniu pakietów"],
        "Na jakim porcie pracuje protokół IMAP": [25, 143, 110, 443, 143]
    }
    print(
        f"Aktualne id usera, który tu wchodzi {current_user.id}, a jego nazwa to {current_user.login}")
    print(
        "Aktualne pytania danego usera {Question.query.filter_by(user_id=current_user.id).all()}")
    if not Question.query.filter_by(user_id=current_user.id).all():
        for question, answer in questions.items():
            quest = Question(
                question=question,
                user_id=current_user.id)
            db.session.add(quest)
            db.session.commit()

            ans = Answer(
                answer1=answer[0],
                answer2=answer[1],
                answer3=answer[2],
                answer4=answer[3],
                correct_answer=answer[4],
                question_id=quest.id
            )
            db.session.add(ans)
            db.session.commit()
