#Reto #7: EL SOMBRERO SELECCIONADOR
#Publicación: 13/02/23 | MEDIA

#Crea un programa que simule el comportamiento del sombrero selccionador del universo mágico de Harry Potter.
#- De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#- Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#- En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  coloque al alumno en una de las 4 casas de Hogwarts:
#  (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#- Ten en cuenta los rasgos de cada casa para hacer las preguntas
#  y crear el algoritmo seleccionador:
#  Por ejemplo, en Slytherin se premia la ambición y la astucia.

# gryffindor: valor
# hufflepuff: lealtad
# ravenclaw: sabiduría
# slytherin: ambición

from enum import Enum
import random

class HogwartsHouse(Enum):
    Gryffindor = 1
    Slytherin = 2
    Hufflepuff = 3
    Ravenclaw = 4

class AnswerOption:
    def __init__(self, number: int, name: str, house: HogwartsHouse) -> None:
        self.number = number
        self.name = name
        self.house = house
      
class Question:
    def __init__(self, question: str, options: list[AnswerOption]):
        self.question = question
        self.options = options
    
    def get_option_by_number(self, number: int) -> AnswerOption:
        found = [option for option in self.options if option.number == number]
        return found[0] if found else None

def get_questionnaire() -> list[Question]:
    return [Question("¿Cómo te definirías?", [
                            AnswerOption(1, "Valiente", HogwartsHouse.Gryffindor),
                            AnswerOption(2, "Leal", HogwartsHouse.Hufflepuff),
                            AnswerOption(3, "Sabio", HogwartsHouse.Ravenclaw),
                            AnswerOption(4, "Ambicioso", HogwartsHouse.Slytherin)]),
            Question("¿Cuál es tu clase favorita?", [
                            AnswerOption(1, "Vuelo", HogwartsHouse.Gryffindor),
                            AnswerOption(2, "Pociones", HogwartsHouse.Ravenclaw),
                            AnswerOption(3, "Defensa contra las artes oscuras", HogwartsHouse.Slytherin),
                            AnswerOption(4, "Animales fantásticos", HogwartsHouse.Hufflepuff)]),
            Question("¿Dónde pasarías más tiempo?", [
                            AnswerOption(1, "Invernadero", HogwartsHouse.Hufflepuff),
                            AnswerOption(2, "Biblioteca", HogwartsHouse.Ravenclaw),
                            AnswerOption(3, "En la sala común", HogwartsHouse.Slytherin),
                            AnswerOption(4, "Explorando", HogwartsHouse.Gryffindor)]),
            Question("¿Cuál es tu color favorito?", [
                            AnswerOption(1, "Rojo", HogwartsHouse.Gryffindor),
                            AnswerOption(2, "Azul", HogwartsHouse.Ravenclaw),
                            AnswerOption(3, "Verde", HogwartsHouse.Slytherin),
                            AnswerOption(4, "Amarillo", HogwartsHouse.Hufflepuff)]),
            Question("¿Cuál es tu mascota?", [
                            AnswerOption(1, "Sapo", HogwartsHouse.Ravenclaw),
                            AnswerOption(2, "Lechuza", HogwartsHouse.Gryffindor),
                            AnswerOption(3, "Gato", HogwartsHouse.Hufflepuff),
                            AnswerOption(4, "Serpiente", HogwartsHouse.Slytherin)])]

def get_input_answer():
    answer = input("Responde 1, 2, 3 o 4: ")
    if answer in ("1", "2", "3", "4"):
        return int(answer)
    return get_input_answer()

def get_random_answer():
    answer = random.choice([1, 2, 3, 4])
    print(f"Respuesta: {answer}")
    return answer

def start_questionnaire() -> list[AnswerOption]:
    print("Hola, soy el 'Sombrero Seleccionador' \nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.\n")
    questionnaire = get_questionnaire()
    answers = []
    for question in questionnaire:
        print(f'{question.question}')
        for option in question.options:
            print(f'\t{option.number}: {option.name}')
        answer_number = get_random_answer()
        option = question.get_option_by_number(answer_number)
        if option is not None:
            answers.append(option)
    return answers

def select_house(answers: list[AnswerOption]) -> HogwartsHouse:
    house_counters = dict.fromkeys(list(HogwartsHouse._member_names_), 0)
    for answer in answers:
        house_counters[answer.house.name] += 1 
    house_counters_sorted = sorted(house_counters.items(), key=lambda x:x[1], reverse=True)
    house_str, _ = house_counters_sorted[0]
    return getattr(HogwartsHouse, house_str)


def start_house_selection():
    answers = start_questionnaire()
    house = select_house(answers)
    print(f"Casa seleccionada: {house.name}")

start_house_selection()