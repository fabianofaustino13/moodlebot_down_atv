import time
from moodlebot.plugin import CheckPlugin

class CheckEditarConfiguracoesDoCurso(CheckPlugin):
    """Validando as configurações do Curso."""
    def handle(self, page, context):
        results = []
        print("Configurações do Curso")
        #return results
        
        print("Editar configurações do curso")
        #Clicar em Edição para localizar o Editar configurações
        navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
        #time.sleep(1)
        navegacao_secundaria.locator('a:has-text("Configurações")').click()
        time.sleep(1)
        
        try:
            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
            #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
            #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
            print(f'Editar configurações 1/1 - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
            time.sleep(0.5)
            if exp_all.count() != 0:
                if exp_all.get_attribute('aria-expanded') == 'false':
                    exp_all.click()
                    time.sleep(0.5)
        
            #GERAL - DATA DE TÉRMINO DO CURSO - Padrão (desmarcado)
            if page.locator('input[id="id_enddate_enabled"]').is_checked():
                results+= ["Editar configurações do Curso 'Data de término do curso' deve ser 'Desmarcado' atendendo ao Padrão."]

            #GERAL - NÚMERO DE IDENTIFICAÇÃO DO CURSO - Padrão (NÚMERO-EVG)
            if page.locator("#id_idnumber").input_value() == '':
                results+= ["Editar configurações do Curso 'Número de identificação do curso' está vazio não atendendo ao Padrão."]

            #FORMATO DE CURSO - FORMATO - Padrão (BOARD OU TÓPICOS OU TÓPICOS CONTRATÍDOS)
            id_formato = page.locator('fieldset[id="id_courseformathdr"]')
            time.sleep(0.5)
            if id_formato.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                print(exp_all.count())
                if exp_all.count() != 0:
                    exp_all.click()
                    time.sleep(0.5)

            formato = page.locator('select[id="id_format"]').input_value()
            if (formato != 'board') and (formato != 'topics') and (formato != 'topcoll') and (formato != 'tiles'): 
                results+= ["Editar configurações do Curso 'Formato' deve ser: 'Formato Board, Tópicos, Tópicos Contraídos ou Tiles' atendendo ao Padrão."]

            #APARÊNCIA - FORÇAR IDIOMA - Padrão (não forçar)        
            if page.locator('select[id="id_lang"]').input_value() != '':
                results+= ["Editar configurações do Curso 'Forçar idioma' deve ser 'Não forçar' atendendo ao Padrão."]

            #APARÊNCIA - NÚMERO DE AVISOS - Padrão (0)
            if page.locator('select[id="id_newsitems"]').input_value() != "0":
                results+= ["Editar configurações do Curso 'Número de avisos' deve ser '0' atendendo ao Padrão."]
                
            #APARÊNCIA - MOSTRAR LIVRO DE NOTAS AOS ESTUDANTES - Padrão (1 - Sim)
            if page.locator('select[id="id_showgrades"]').input_value() != "1":
                results+= ["Editar configurações do Curso 'Mostrar livro de notas aos estudantes' deve ser 'Sim' atendendo ao Padrão."]
        
            #APARÊNCIA - MOSTRAR RELATÓRIO DAS ATIVIDADES - Padrão (1 - Sim)
            if page.locator('select[id="id_showreports"]').input_value() != "1":
                results+= ["Editar configurações do Curso 'Mostrar relatório das atividades' deve ser 'Sim' atendendo ao Padrão."]
                
            try:
                #ARQUIVOS E UPLOADS - ARQUIVOS DE CURSO LEGADOS - Padrão (1 - Não)
                if page.locator('select[id="id_legacyfiles"]').input_value() != "1":
                    results+= ["Editar configurações do Curso 'Arquivos de curso legados' deve ser 'Não' atendendo ao Padrão."]
            except:
                print("Curso não possue Arquivos legados")
        
            #ARQUIVOS E UPLOADS - TAMANHO MÁXIMO DE UPLOAD - Padrão (0 - 4Gb)
            if page.locator('select[id="id_maxbytes"]').input_value() != "0":
                results+= ["Editar configurações do Curso 'Tamanho máximo de upload' deve ser 4Gb atendendo ao Padrão."]

            #ACOMPANHAMENTO DE CONCLUSÃO - ATIVAR ACOMPANHAMENTO DE CONCLUSÃO - Padrão (1 - Sim)
            if page.locator('select[id="id_enablecompletion"]').input_value() != "1":
                results+= ["Editar configurações do Curso 'Ativar acompanhamento de conclusão' deve ser 'Sim' atendendo ao Padrão."]

            #GRUPOS - MODALIDADE GRUPO - Padrão (0 - Nenhum grupo)
            if page.locator('select[id="id_groupmode"]').input_value() != "0":
                results+= ["Editar configurações do Curso 'Modalidade grupo' deve ser 'Nenhum grupo' atendendo ao Padrão."]

            #GRUPOS - FORÇAR MODALIDADE GRUPO - Padrão (0 - Não)
            if page.locator('select[id="id_groupmodeforce"]').input_value() != "0":
                results+= ["Editar configurações do Curso 'Forçar modalidade grupo' deve ser 'Não' atendendo ao Padrão."]
                
            #GRUPOS - AGRUPAMENTO PADRÃO - Padrão (0 - Nenhum)
            if page.locator('select[id="id_defaultgroupingid"]').input_value() != "0":
                results+= ["Editar configurações do Curso 'Agrupamento padrão' deve ser 'Nenhum' atendendo ao Padrão."]

            time.sleep(1)
            #SALVAR MUDANÇAS       
            page.locator("#id_cancel").click()
            time.sleep(0.5)
            print('Configurações do curso concluída')  
              
        except Exception as err:
            results+=  [f"Não foi possível validar Editar configurações. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results