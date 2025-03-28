# chapters/ch2.py

def get_content():
    return {
        "paragraphs": [
            "In de tandartspraktijk werken meerdere mensen samen.",
            "Er is een tandarts, een assistent, soms een mondhygiënist en een baliemedewerker.",
            "De assistent helpt bij behandelingen, de hygiënist richt zich op schoonmaken van het gebit.",
            "De baliemedewerker ontvangt patiënten en plant afspraken."
        ],
        "vocab": {
            "Assistent": "assistant",
            "Mondhygiënist": "dental hygienist",
            "Baliemedewerker": "receptionist",
            "Afspraak": "appointment",
            "Behandeling": "treatment"
        },
        "questions": [
            "Wat is het verschil tussen een tandarts en een mondhygiënist?",
            "Wie plant meestal de afspraken?"
        ],
        "quiz": {
            "question": "Wie helpt de tandarts tijdens een behandeling?",
            "options": ["De patiënt", "De assistent", "De baliemedewerker"],
            "answer": "De assistent",
            "explanation": "De assistent helpt actief mee in de behandelkamer."
        }
    }
