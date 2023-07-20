import time
from moodlebot.plugin import CheckPlugin

class CheckConclusaoDeCurso(CheckPlugin):
    """Validando as configurações da Conclusão de Curso."""
    def handle(self, page, context):
        results = []
        print("Conclusão do Curso")
        #return results
        
        pagina_toda = page.locator('xpath=//div[@id="page-content"]').inner_text()
        #print(pagina_toda)
        nota_minima = pagina_toda.find('Nota mínima para aprovação:')
        #print(nota_minima)
        pontos = pagina_toda.find('pontos.')
        #print(pontos)
        if nota_minima != -1 and pontos != -1:
            nota_curso = (nota_minima + 28)
            nota_minima_aprovacao = pagina_toda[nota_curso:pontos].strip()
        else:
            nota_minima_aprovacao = '0'
            results+= [f"O texto 'Nota mínima para aprovação:' não encontrado."]
        if nota_minima_aprovacao[0:2] != '60' and nota_minima_aprovacao[0:2] != '70':
                results+= [f"A 'Nota mínima para aprovação' é '{nota_minima_aprovacao}' e em geral, deve ser 60 ou 70 atendendo ao Padrão."]

        #Clicar em Edição para localizar o Conclusão de Curso
        time.sleep(0.5)
        page.locator('xpath=//input[@name="setmode"]').click() #ATIVAR EDIÇÃO DO CURSO
        time.sleep(1)
        navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
        time.sleep(0.5)
        navegacao_secundaria.locator('a:has-text("Mais")').click()
        time.sleep(0.5)
        navegacao_secundaria.locator('a:has-text("Conclusão de curso")').click()
        time.sleep(1)  
        
        try:
            #page.locator('a:has-text("Expandir tudo")').click()
            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
            #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
            #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
            print(f'Conclusão de curso 1/1 - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
            time.sleep(0.5)
            if exp_all.count() != 0:
                if exp_all.get_attribute('aria-expanded') == 'false':
                    exp_all.click()
                    time.sleep(0.5)
       
            try: 
                #GERAL - CONDIÇÕES DE CONCLUSÃO - Padrão (Curso concluído quando TODAS as condições forem atendidas)
                id_geral = page.locator('fieldset[id="id_overallcriteria"]')
                time.sleep(0.5)
                if id_geral.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    exp_all.click()
                    time.sleep(0.5)
                    
                if id_geral.locator('select[id="id_overall_aggregation"]').input_value() != '1':
                    condicao_conclusao_padrao = 'Curso concluído quando TODAS as condições forem atendidas'
                    results+=  [f"Geral 'Condições de conclusão' deve ser '{condicao_conclusao_padrao}' atendendo ao Padrão."]
                                    
                #CONDIÇÃO: CONCLUSÃO DE ATIVIDADE - Padrão (todos desmarcados)
                id_cond_conc_atv = page.locator('fieldset[id="id_activitiescompleted"]')
                time.sleep(0.5)
                if id_cond_conc_atv.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    page.locator('a:has-text("Expandir tudo")').click()
                    time.sleep(0.5)

                condicao_total = id_cond_conc_atv.locator('xpath=//div[@class="form-group row  fitem  checkboxgroup1"]')
                for x in range(condicao_total.count()):
                    #atv = condicao_total.nth(x).locator('input[class="form-check-input checkboxgroup1"]').is_checked()
                    if condicao_total.nth(x).locator('input[class="form-check-input checkboxgroup1"]').is_checked():  
                        nome_condicao = condicao_total.nth(x).locator('div[class="form-check d-flex"]').inner_text()
                        results+= [f"Condição: Conclusão de atividade '{nome_condicao}' deve ser 'Desmarcado' atendendo ao Padrão."]
                
                #CONDIÇÃO: CONCLUSÃO DE ATIVIDADE -  CONDIÇÃO REQUER - Padrão (TODAS as atividades selecionadas devem estar concluídas)
                if id_cond_conc_atv.locator('select[id="id_activity_aggregation"]').input_value() != '1':
                    cond_conc_atv_padrao = 'TODAS as atividades selecionadas devem estar concluídas'
                    results+=  [f"Condição: 'Condição requer' deve ser '{cond_conc_atv_padrao}' atendendo ao Padrão."]
                                    
                #CONDIÇÃO: CONCLUSÃO DE OUTROS CURSOS - CURSOS DISPONÍVEIS - Padrão (Sem seleção)
                id_cond_conc_outros = page.locator('fieldset[id="id_courseprerequisites"]') 
                condicao_outros_cursos_disponiveis = id_cond_conc_outros.locator('select[id="id_criteria_course"] > option[selected=""]')
                if condicao_outros_cursos_disponiveis.count() != 0:
                    results+= ["Condição: Conclusão de outros cursos 'Cursos disponíveis' deve ser 'Sem seleção' atendendo ao Padrão."]
                
                #CONDIÇÃO: DATA - HABILITAR - Padrão (desmarcado)
                id_cond_data = page.locator('fieldset[id="id_date"]')
                if id_cond_data.locator('input[id="id_criteria_date"]').is_checked():
                    results+= ["Condição: Data 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]
                
                #CONDIÇÃO: DURAÇÃO DA INSCRIÇÃO - HABILITAR - Padrão (desmarcado)
                id_cond_duracao = page.locator('fieldset[id="id_duration"]')
                if id_cond_duracao.locator('input[id="id_criteria_duration"]').is_checked():
                    results+= ["Condição: Duração da inscrição 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]
                
                #CONDIÇÃO: DESINSCRIÇÃO - HABILITAR - Padrão (desmarcado)
                id_cond_desinscricao = page.locator('fieldset[id="id_unenrolment"]')
                if id_cond_desinscricao.locator('input[id="id_criteria_unenrol"]').is_checked():
                    results+= ["Condição: Desinscrição 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]

                #CONDIÇÃO DE NOTA - Padrão (marcado)
                id_cond_nota = page.locator('fieldset[id="id_grade"]')
                if id_cond_nota.locator('input[id="id_criteria_grade"]').is_checked() == False:
                    results+= ["Condição: Nota do curso 'Habilitar' deve ser 'Marcado' atendendo ao Padrão."]
                
                #NOTA DE CURSO OBRIGATÓRIA - Padrão 60,00000 ?
                notaObrigatoria = id_cond_nota.locator("#id_criteria_grade_value").input_value()
                print(f"Nota Obrigatória: {notaObrigatoria[0:2]}")
                print(f"Nota mínima aprovação: {nota_minima_aprovacao[0:2]}")
                if (notaObrigatoria[0:2]) != (nota_minima_aprovacao[0:2]): # and notaObrigatoria != "70,00000":
                    #id_cond_nota.locator("#id_criteria_grade_value").fill(nota_minima_aprovacao)
                    results+= [f"Condição: Nota do curso 'Nota de curso obrigatória' era '{notaObrigatoria[0:2]}' e 'Nota mínima para aprovação' é '{nota_minima_aprovacao[0:2]}' estando fora do Padrão."]
                if notaObrigatoria[0:2] != '60' and notaObrigatoria[0:2] != '70':
                    results+= [f"Condição: Nota do curso 'Nota de curso obrigatória' é '{notaObrigatoria[0:2]}' e em geral, deve ser 60 ou 70 atendendo ao Padrão."]
                
                #CONDIÇÃO: CONCLUSÃO MANUAL POR SI MESMO - HABILITAR - Padrão (desmarcado)
                id_cond_conc_manual = page.locator('fieldset[id="id_manualselfcompletion"]')
                if id_cond_conc_manual.locator('input[id="id_criteria_self"]').is_checked():
                    results+= ["Condição: Conclusão manual por si mesmo 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]

                #CONDIÇÃO: CONCLUSÃO MANUAL POR OUTROS - Padrão (todos desmarcado)
                condicao_conclusao_manual_outros = page.locator('fieldset[id="id_roles"]')
                condicao_conclusao_total = condicao_conclusao_manual_outros.locator('xpath=//div[@class="form-group row  fitem  "]')
                for w in range(condicao_conclusao_total.count()):
                    perfil = condicao_conclusao_total.locator('input[class="form-check-input "]').nth(w)
                    if perfil.is_checked():
                        nome_perfil = condicao_conclusao_total.nth(w).inner_text()
                        results+= [f"Condição: Conclusão manual por outros '{nome_perfil}' deve ser 'Desmarcado' atendendo ao Padrão."]

            except:
                #CONFIGURAÇÃO DE CONCLUSÃO BLOQUEADAS - DESBLOQUEAR OPÇÕES DE CONCLUSÃO E APAGAR OS DADOS DE PROGRESSO DOS USUÁRIOS
                desbloquear = page.locator('xpath=//input[@id="id_settingsunlock"]')
                desbloquear.click()
                time.sleep(1)
                #GERAL - CONDIÇÕES DE CONCLUSÃO - Padrão (Curso concluído quando TODAS as condições forem atendidas)
                id_geral = page.locator('fieldset[id="id_overallcriteria"]')
                if id_geral.locator('select[id="id_overall_aggregation"]').input_value() != '1':
                    condicao_conclusao_padrao = 'Curso concluído quando TODAS as condições forem atendidas'
                    results+=  [f"Geral 'Condições de conclusão' deve ser '{condicao_conclusao_padrao}' atendendo ao Padrão."]
                                    
                #CONDIÇÃO: CONCLUSÃO DE ATIVIDADE - Padrão (todos desmarcados)
                id_cond_conc_atv = page.locator('fieldset[id="id_activitiescompleted"]')
                condicao_total = id_cond_conc_atv.locator('xpath=//div[@class="form-group row  fitem  checkboxgroup1"]')
                for x in range(condicao_total.count()):
                    #atv = condicao_total.nth(x).locator('input[class="form-check-input checkboxgroup1"]').is_checked()
                    if condicao_total.nth(x).locator('input[class="form-check-input checkboxgroup1"]').is_checked():                   
                        results+= [f"Condição: Conclusão de atividade deve ser 'Desmarcado' atendendo ao Padrão."]
                        #atv.click()
                
                #CONDIÇÃO: CONCLUSÃO DE ATIVIDADE -  CONDIÇÃO REQUER - Padrão (TODAS as atividades selecionadas devem estar concluídas)
                if id_cond_conc_atv.locator('select[id="id_activity_aggregation"]').input_value() != '1':
                    cond_conc_atv_padrao = 'TODAS as atividades selecionadas devem estar concluídas'
                    results+=  [f"Condição: 'Condição requer' deve ser '{cond_conc_atv_padrao}' atendendo ao Padrão."]
                                    
                #CONDIÇÃO: CONCLUSÃO DE OUTROS CURSOS - CURSOS DISPONÍVEIS - Padrão (Sem seleção)
                id_cond_conc_outros = page.locator('fieldset[id="id_courseprerequisites"]') 
                condicao_outros_cursos_disponiveis = id_cond_conc_outros.locator('select[id="id_criteria_course"] > option[selected=""]')
                if condicao_outros_cursos_disponiveis.count() != 0:
                    results+= ["Condição: Conclusão de outros cursos 'Cursos disponíveis' deve ser 'Sem seleção' atendendo ao Padrão."]
                
                #CONDIÇÃO: DATA - HABILITAR - Padrão (desmarcado)
                id_cond_data = page.locator('fieldset[id="id_date"]')
                if id_cond_data.locator('input[id="id_criteria_date"]').is_checked():
                    results+= ["Condição: Data 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]
                
                #CONDIÇÃO: DURAÇÃO DA INSCRIÇÃO - HABILITAR - Padrão (desmarcado)
                id_cond_duracao = page.locator('fieldset[id="id_duration"]')
                if id_cond_duracao.locator('input[id="id_criteria_duration"]').is_checked():
                    results+= ["Condição: Duração da inscrição 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]
                
                #CONDIÇÃO: DESINSCRIÇÃO - HABILITAR - Padrão (desmarcado)
                id_cond_desinscricao = page.locator('fieldset[id="id_unenrolment"]')
                if id_cond_desinscricao.locator('input[id="id_criteria_unenrol"]').is_checked():
                    results+= ["Condição: Desinscrição 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]

                #CONDIÇÃO DE NOTA - Padrão (marcado)
                id_cond_nota = page.locator('fieldset[id="id_grade"]')
                if id_cond_nota.locator('input[id="id_criteria_grade"]').is_checked() == False:
                    results+= ["Condição: Nota do curso 'Habilitar' deve ser 'Marcado' atendendo ao Padrão."]
                
                #NOTA DE CURSO OBRIGATÓRIA - Padrão 60,00000 ?
                notaObrigatoria = id_cond_nota.locator("#id_criteria_grade_value").input_value()
                print(f"Nota Obrigatória: {notaObrigatoria[0:2]}")
                print(f"Nota mínima aprovação: {nota_minima_aprovacao[0:2]}")
                if (notaObrigatoria[0:2]) != (nota_minima_aprovacao[0:2]): # and notaObrigatoria != "70,00000":
                    #id_cond_nota.locator("#id_criteria_grade_value").fill(nota_minima_aprovacao)
                    results+= [f"Condição: Nota do curso 'Nota de curso obrigatória' era '{notaObrigatoria[0:2]}' e 'Nota mínima para aprovação' é '{nota_minima_aprovacao[0:2]}' estando fora do Padrão."]
                if notaObrigatoria[0:2] != '60' and notaObrigatoria[0:2] != '70':
                    results+= [f"Condição: Nota do curso 'Nota de curso obrigatória' é '{notaObrigatoria[0:2]}' e em geral, deve ser 60 ou 70 atendendo ao Padrão."]
                
                #CONDIÇÃO: CONCLUSÃO MANUAL POR SI MESMO - HABILITAR - Padrão (desmarcado)
                id_cond_conc_manual = page.locator('fieldset[id="id_manualselfcompletion"]')
                if id_cond_conc_manual.locator('input[id="id_criteria_self"]').is_checked():
                    results+= ["Condição: Conclusão manual por si mesmo 'Habilitar' deve ser 'Desmarcado' atendendo ao Padrão."]

                #CONDIÇÃO: CONCLUSÃO MANUAL POR OUTROS - Padrão (todos desmarcado)
                condicao_conclusao_manual_outros = page.locator('fieldset[id="id_roles"]')
                condicao_conclusao_total = condicao_conclusao_manual_outros.locator('xpath=//div[@class="form-group row  fitem  "]')
                for w in range(condicao_conclusao_total.count()):
                    perfil = condicao_conclusao_total.locator('input[class="form-check-input "]').nth(w)
                    if perfil.is_checked():
                        nome_perfil = condicao_conclusao_total.nth(w).inner_text()
                        results+= [f"Condição: Conclusão manual por outros '{nome_perfil}' deve ser 'Desmarcado' atendendo ao Padrão."]

            #SALVAR MUDANÇAS
            time.sleep(1)
            page.locator("#id_cancel").click()
            time.sleep(0.5)
            print('Conclusão de curso concluído')

        except Exception as err:
            results+=  [f"Não foi possível validar Conclusão do Curso. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results