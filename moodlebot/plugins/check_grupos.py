import time
from moodlebot.plugin import CheckPlugin

class CheckGrupos(CheckPlugin):
    """Validando a existência de grupos no Curso."""
    def handle(self, page, context):
        results = []
        print("Grupos")
        #return results
        link = str(page)
        #print(link)
        #print(len(link))
        tam = link.find(".escolavirtual.gov.br/course/view.php?id=")
        #print(tam)
        id_curso = link[71:len(link)-2]
        #print(f"ID do curso: {id_curso}")
        print("Pesquisando existência de grupos")
        #Clicar em Edição para localizar o Editar configurações
        navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
        #time.sleep(1)
        navegacao_secundaria.locator('a:has-text("Participantes")').click()
        time.sleep(1)
        
        try:                
            #print(page.locator('select[class="custom-select urlselect"]').input_value())
            page.locator('select[class="custom-select urlselect"]').click()
            if page.locator('select[class="custom-select urlselect"]').input_value() != f'/group/index.php?id={id_curso}':
                page.locator('select[class="custom-select urlselect"]').select_option(f'/group/index.php?id={id_curso}')
                time.sleep(1)
                total_grupos = page.locator('select[id="groups"] > option')
                print(f'Total de grupos neste curso: {total_grupos.count()}')
                if total_grupos.count() > 0:
                    results+= [f"Este curso possui {total_grupos.count()} grupo(s)."]
              
            time.sleep(0.5)
            navegacao_secundaria2 = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
            #time.sleep(1)
            navegacao_secundaria2.locator('xpath=//li[@class="nav-item" and @data-key="coursehome"]').click()
            time.sleep(0.5)
            print('Verificação de Grupos do curso concluído')  
              
        except Exception as err:
            results+=  [f"Não foi possível validar grupos. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results