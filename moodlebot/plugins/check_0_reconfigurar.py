import time
from moodlebot.plugin import CheckPlugin

class CheckReconfigurarCurso(CheckPlugin):
    """Limpando o curso para iniciar as validações - Reconfigurando o curso."""
    def handle(self, page, context):
        results = []
        print("Reconfigurar")
        #return results

        print("Reconfigurando o Curso") #Funcionalidade para remover as tentativas existentes
        #print(page)
        link = str(page)
        #print(link)
        #print(len(link))
        tam = link.find(".escolavirtual.gov.br/course/view.php?id=")
        id_curso = link[71:len(link)-2]
        print(f"ID do curso: {id_curso}")
        try: 
            navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
            time.sleep(0.5)
            navegacao_secundaria.locator('a:has-text("Mais")').click()
            time.sleep(0.5)
            navegacao_secundaria.locator('a:has-text("Reutilizar curso")').click()
            time.sleep(1)
            page.locator('select[name="jump"]').click()
            time.sleep(1)
            page.locator('select[name="jump"]').select_option(f'/course/reset.php?id={id_curso}')
            time.sleep(3)
            
            #time.sleep(1)
            #GERAL: DATA DE INÍCIO DO CURSO - Padrão (marcado)
            id_date_start = page.locator('fieldset[id="id_reset_start_date"]')
            if id_date_start.locator('input[id="id_reset_start_date_enabled"]').is_checked():
                id_date_start.locator('input[id="id_reset_start_date_enabled"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]
            
            #GERAL: DATA DE TÉRMINO DO CURSO - Padrão (desmarcado)
            id_date_end = page.locator('fieldset[id="id_reset_end_date"]')
            if id_date_end.locator('input[id="id_reset_end_date_enabled"]').is_checked():
                id_date_end.locator('input[id="id_reset_end_date_enabled"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]
            
            id_geral = page.locator('fieldset[id="id_generalheader"]')
            #GERAL: EXCLUIR EVENTO - Padrão (marcado)
            if id_geral.locator('input[id="id_reset_events"]').is_checked() == False:
                id_geral.locator('input[id="id_reset_events"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]

            #GERAL: EXCLUIR TODAS AS ANOTAÇÕES - Padrão (marcado)
            if id_geral.locator('input[id="id_reset_notes"]').is_checked() == False:
                id_geral.locator('input[id="id_reset_notes"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]

            #GERAL: EXCLUIR TODOS OS COMENTÁRIOS - Padrão (marcado)
            if id_geral.locator('input[id="id_reset_comments"]').is_checked() == False:
                id_geral.locator('input[id="id_reset_comments"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]

            #GERAL: EXCLUIR DADOS DE CONCLUSÃO - Padrão (marcado)
            if id_geral.locator('input[id="id_reset_completion"]').is_checked() == False:
                id_geral.locator('input[id="id_reset_completion"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]

            #GERAL: APAGAR ASSOCIAÇÕES DE BLOG - Padrão (marcado)
            if id_geral.locator('input[id="id_delete_blog_associations"]').is_checked() == False:
                id_geral.locator('input[id="id_delete_blog_associations"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]

            #GERAL: APAGAR ASSOCIAÇÕES DE BLOG - Padrão (marcado)
            if id_geral.locator('input[id="id_reset_competency_ratings"]').is_checked() == False:
                id_geral.locator('input[id="id_reset_competency_ratings"]').click()
                #results+= ["Geral: 'Data de inínio do curso' deve ser desmarcado atendendo ao Padrão."]

            #SALVAR MUDANÇAS
            time.sleep(1)
            page.locator("#id_submitbutton").click()
            time.sleep(1)
            continuar = page.locator('xpath=//div[@class="continuebutton"]')
            continuar.locator('xpath=//button[@class="btn btn-primary"]').click()
            time.sleep(1) 
            print('Reconfigurar concluído')

        except Exception as err:
            results+=  [f"Não foi possível validar Reconfiguração do Curso. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results