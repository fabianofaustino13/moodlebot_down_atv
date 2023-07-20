import time
from moodlebot.plugin import CheckPlugin

class CheckNomeDoCurso(CheckPlugin):
    """Pegando o nome do curso."""
    def handle(self, page, context):
        #results = []
        #return results
        print("Nome do curso")
                
        #VERIFICAR SE O FORMATO DO CURSO É TÓPICO CONTRAÍDO - SE SIM, CLICA PARA EXPANDIR OS TÓPICOS
        formato_topico_contraido = page.locator('xpath=//span[@id="toggles-all-opened"]')
        print(formato_topico_contraido.count())
        if formato_topico_contraido.count() != 0:
            formato_topico_contraido.click()
            time.sleep(1)

        navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
        time.sleep(0.5)
        navegacao_secundaria.locator('a:has-text("Configurações")').click()
        
        #Clicar em Editar configurações
        time.sleep(1)
        
        nome_curso = page.locator('input[id="id_fullname"]').input_value()
        print(nome_curso)
        #SALVAR MUDANÇAS
        page.locator("#id_cancel").click()
        time.sleep(0.5)
        print('Nome do curso concluído')
        return nome_curso
