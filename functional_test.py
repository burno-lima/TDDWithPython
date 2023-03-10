from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online interessante
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o  título da página e o cabeçalho mencionam lista de 
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# Ela é convidada a inserir um item de tarefa imediatamente

# Ela digita "Buy peacock feathers" (Comprar de pavão) em uma caixa 
# de texto (o hobby de Edith é fazer iscas para pesca com fly)

# Quando ela tecla entar, a página é atualizada, e agora a página lista
# "1: Buy peacock feathers" como um item em uma lista de tarefas

# Ainda continua havendo uma caixa de texto convidado-a a acrescentar outro
# item. Ela insere "use peacock feathers to make a fly" (Usar penas de pavão
# para fazer um fly - Edith é bem metódica)

# A página é  atualizada novamente e agora mostra os dois itens em sua lista

# Edith se pergunta se o site lembrará de usa lista. Então ela nota
# texto explicativo para isso.

# Ela acessa esse URL - sua lista de tarefas continua lá.

# Satisfeita, ela volta a dormir
if __name__ == '__main__':
    unittest.main(warnings='ignore')
