class SistemaExperto:
    def __init__(self):
        self.preguntas = {
            'asma': [
                '¿Tienes dificultad para respirar?',
                '¿Tienes tos?',
                '¿Sientes opresión en el pecho?',
                '¿Tienes sibilancias al respirar?',
                '¿Te despiertas por la noche debido a problemas respiratorios?',
                '¿Tienes sensación de falta de aire?',
                '¿Tus labios o uñas se ponen azules?',
                '¿Tienes dolor en el pecho al respirar?',
                '¿Tienes sensación de debilidad o cansancio?',
                '¿Tienes dificultad para hacer ejercicio físico?'
            ],
            'gripe': [
                '¿Tienes fiebre?',
                '¿Tienes dolor de garganta?',
                '¿Tienes congestión nasal?',
                '¿Tienes dolor de cabeza?',
                '¿Tienes dolores musculares?',
                '¿Tienes escalofríos?',
                '¿Tienes fatiga?',
                '¿Tienes pérdida de apetito?',
                '¿Tienes dificultad para respirar al acostarte?',
                '¿Tienes malestar general?'
            ],
            'gastritis': [
                '¿Tienes dolor abdominal?',
                '¿Tienes náuseas?',
                '¿Has vomitado?',
                '¿Sientes ardor en el estómago?',
                '¿Tienes eructos frecuentes?',
                '¿Tienes sensación de hinchazón?',
                '¿Tienes pérdida de apetito?',
                '¿Tienes pérdida de peso inexplicable?',
                '¿Tienes dolor en la parte superior del abdomen?',
                '¿Tienes gases excesivos?'
            ]
        }

        self.sintomas = {
            'asma': [0.9, 0.8, 0.7, 0.9, 0.8, 0.8, 0.7, 0.6, 0.7, 0.7],
            'gripe': [0.8, 0.7, 0.8, 0.7, 0.9, 0.7, 0.8, 0.7, 0.7, 0.7],
            'gastritis': [0.9, 0.8, 0.7, 0.8, 0.7, 0.8, 0.7, 0.6, 0.7, 0.6]
        }

    def preguntar(self, tipo):
        respuestas = []
        for i, pregunta in enumerate(self.preguntas[tipo]):
            respuesta = input(f"{pregunta} (si/no): ").strip().lower()
            if respuesta == 'si':
                respuestas.append(self.sintomas[tipo][i])
            else:
                respuestas.append(0)
        return respuestas

    def ejecutar_test(self, tipo):
        respuestas = self.preguntar(tipo)
        conteo_grado = sum(respuestas)
        print(f"El grado total de pertenencia para {tipo} es {conteo_grado:.2f}.")
        self.determinar_resultado(tipo, conteo_grado)

    def determinar_resultado(self, tipo, grado):
        if grado >= 6.0:
            print(f"Resultado: Probablemente tienes {tipo}")
        elif grado >= 3.0:
            print(f"Resultado: visita a tu médico para checar síntomas de {tipo}")
        else:
            print(f"Resultado: ¡No padeces {tipo}!")

    def probar(self):
        self.ejecutar_test('asma')
        self.ejecutar_test('gripe')
        self.ejecutar_test('gastritis')


if __name__ == "__main__":
    sistema_experto = SistemaExperto()
    sistema_experto.probar()

