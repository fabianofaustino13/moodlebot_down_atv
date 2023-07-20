import time
from moodlebot.plugin import CheckPlugin

class CheckURL(CheckPlugin):
    """Validando as configurações do Recurso URL."""
    def handle(self, page, context):
        results = []
        print("URL")
        #return results

        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity url modtype_url "]')
            time.sleep(0.5)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity url modtype_url "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper url modtype_url hasinfo dropready draggable"]')
            
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True

            total = cont.count()
            for x in range(total):
                time.sleep(0.5)
                print(f'URL {x+1}/{total}')
                time.sleep(0.5)
                atividade = cont.nth(x).locator('xpath=//div[@class="activity-actions align-self-start"]')
                time.sleep(0.5)
                atividade.click()
                time.sleep(0.5)
                editar_configuracao = atividade.locator('xpath=//a[@class="dropdown-item editing_update menu-action cm-edit-action" and @data-action="update"]')
                editar_configuracao.click()       
                time.sleep(1)
                
                #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
                #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
                print(f'URL {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                time.sleep(0.5)
                if exp_all.count() != 0:
                    if exp_all.get_attribute('aria-expanded') == 'false':
                        exp_all.click()
                        time.sleep(0.5)
                
                #GERAL - NOME
                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator("input[id='id_name']").input_value()
                print("Nome do Recurso: %s" % nome_atividade)

                time.sleep(0.5)
                if id_geral.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                
                #GERAL - URL EXTERNA - Padrão (CDN)
                url_externa = id_geral.locator("input[id='id_externalurl']").input_value()
                if url_externa.find("https://cdn.evg.gov.br/") != 0:
                    results+= [f"{nome_atividade} ==> Geral 'URL externa' está diferente de um CDN. {url_externa}"]
                
                #GERAL - EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO - Padrão (desmarcado)
                if id_geral.locator("input[id='id_showdescription']").is_checked():
                    #id_geral.locator("input[id='id_showdescription']").click()
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição na página do curso' deve ser desmarcado atendendo ao Padrão."]

                #APARÊNCIA - EXIBIR - Padrão (Nova Janela)
                id_aparencia = page.locator('fieldset[id="id_optionssection"]')
                time.sleep(0.5)
                if id_aparencia.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_aparencia.locator("select[id='id_display']").input_value()) != '3':
                    apa_exibir_padrao = 'Nova janela'
                    apa_exibir = id_aparencia.locator("select[id='id_display'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_display']").select_option('3')
                    results+=  [f"{nome_atividade} ==> Aparência 'Exibir' é '{apa_exibir}' e deve ser atualizado para '{apa_exibir_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - EXIBIR DESCRIÇÃO DA URL- Padrão (marcado)
                if id_aparencia.locator("input[id='id_printintro']").is_checked() == False:
                    #id_geral.locator("input[id='id_showdescription']").click()
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição da URL' deve ser marcado atendendo ao Padrão."]            

                #VARIÁVEIS DE URL - &PARÂMETRO=VARIÁVEL - Padrão (automático)
                id_variaveis_url = page.locator('fieldset[id="id_parameterssection"]')
                time.sleep(0.5)
                if id_variaveis_url.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                    
                if id_variaveis_url.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    page.locator('a:has-text("Expandir tudo")').click()

                if (id_variaveis_url.locator("input[id='id_parameter_0']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Parâmetro 1' está fora do Padrão."]
                
                if (id_variaveis_url.locator("select[id='id_variable_0']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Variável 1' está fora do Padrão."]

                if (id_variaveis_url.locator("input[id='id_parameter_1']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Parâmetro 2' está fora do Padrão."]
                
                if (id_variaveis_url.locator("select[id='id_variable_1']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Variável 2' está fora do Padrão."]

                if (id_variaveis_url.locator("input[id='id_parameter_2']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Parâmetro 3' está fora do Padrão."]
                
                if (id_variaveis_url.locator("select[id='id_variable_2']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Variável 3' está fora do Padrão."]

                if (id_variaveis_url.locator("input[id='id_parameter_3']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Parâmetro 4' está fora do Padrão."]
                
                if (id_variaveis_url.locator("select[id='id_variable_3']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Variável 4' está fora do Padrão."]

                if (id_variaveis_url.locator("input[id='id_parameter_4']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Parâmetro 5' está fora do Padrão."]
                
                if (id_variaveis_url.locator("select[id='id_variable_4']").input_value()) != "":
                    results+=  [f"{nome_atividade} ==> Variáveis de URL 'Variável 5' está fora do Padrão."]
                
                #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                time.sleep(0.5)
                if id_conf_comuns_modulos.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)


                if (id_conf_comuns_modulos.locator("select[id='id_visible']").input_value()) != '1':
                    conf_com_mod_disp_padrao = 'Mostrar na página do curso'
                    conf_com_mod_disp = id_conf_comuns_modulos.locator("select[id='id_visible'] > option[selected]").inner_text()
                    #id_conf_comuns_modulos.locator("select[id='id_visible']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod_disp}' e deve ser atualizado para '{conf_com_mod_disp_padrao}' atendendo ao Padrão."]

                #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
                id_conclusao_atividade = page.locator('fieldset[id="id_activitycompletionheader"]')
                time.sleep(0.5)
                if id_conclusao_atividade.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                try:
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_acom_conc_padrao = 'Mostrar atividade como concluída quando as condições forem satisfeitas'
                        conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator("select[id='id_completion']").select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' e deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]
                    
                except:

                    id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click()
                    time.sleep(1)
                    
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_acom_conc_padrao = 'Mostrar atividade como concluída quando as condições forem satisfeitas'
                        conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator("select[id='id_completion']").select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' e deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]
                    
                #CONCLUSÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM - Padrão (desmarcado)
                if id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").is_checked():
                    #id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").click()
                    results+= [f"Recurso: {nome_atividade} ==> Conclusão de atividade 'Conclusão esperada em' deve ser desmarcado atendendo ao Padrão."]

                #SE O FORMATO FOR TILES, RETORNAR PARA A PÁGINA INICIAL
                if tiles:
                    #RETORNAR PARA A PÁGINA INICIAL
                    #page.locator('xpath=//li[@class="breadcrumb-item dimmed_text"]').click()
                    page.goto(context["course_url"], wait_until="load")
                    time.sleep(0.5)
                else:
                    #SALVAR E VOLTAR AO CURSO    
                    page.locator("input[id='id_cancel']").click()
                    time.sleep(0.5)
            print('URL concluída')    
        except Exception as err:
            results+=  [f"Não foi possível validar URL. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
