import time
from moodlebot.plugin import CheckPlugin

class CheckGlossario(CheckPlugin):
    """Validando as configurações da Atividade Glossário."""
    def handle(self, page, context):
        results = []
        print("Glossário")
        #return results

        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity glossary modtype_glossary "]')
            time.sleep(0.5)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity glossary modtype_glossary "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper glossary modtype_glossary hasinfo dropready draggable"]')
            
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True
            
            total = cont.count()
            for x in range(total):  
                time.sleep(0.5)
                print(f'Glossário {x+1}/{total}')     
                """ cont.locator('xpath=//div[@class="activity-actions align-self-start"]').nth(x).click()
                time.sleep(0.5)           
                cont.nth(x).locator('a:has-text("Editar configurações")').click()            
                time.sleep(2) """

                atividade = cont.nth(x).locator('xpath=//div[@class="activity-actions align-self-start"]')
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
                print(f'Glossário {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                time.sleep(0.5)
                if exp_all.count() != 0:
                    if exp_all.get_attribute('aria-expanded') == 'false':
                        exp_all.click()
                        time.sleep(0.5)

                #GERAL - NOME
                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator("input[id='id_name']").input_value()
                print("Nome da Atividade: %s" % nome_atividade)
                time.sleep(0.5)
                if id_geral.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)           
    
            #GERAL - EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO - Padrão (desmarcado)
                if id_geral.locator('input[id="id_showdescription"]').is_checked():
                    #id_geral.locator('input[id="id_showdescription"]').click()
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição na página do curso' deve ser desmarcado atendendo ao Padrão."]

                #GERAL - SELECIONAR O BOX PARA DEFINIR O GLOSSÁRIO COMO GLOSSÁRIO GLOBAL - Padrão (desmarcado)
                if id_geral.locator('input[id="id_globalglossary"]').is_checked():
                    #id_geral.locator('input[id="id_globalglossary"]').click()
                    results+= [f"{nome_atividade} ==> Geral 'Selecionar o box para definir o glossário como glossário global' deve ser desmarcado atendendo ao Padrão."]

                #GERAL - TIPO DE GLOSSÁRIO - Padrão (Glossário principal)
                #if (id_geral.locator("select[id='id_mainglossary']").input_value()) != '1':
                #    geral_tipo_padrao = 'Glossário principal'
                #    geral_tipo = id_geral.locator("select[id='id_mainglossary'] > option[selected]").inner_text()
                    #id_geral.locator("select[id='id_mainglossary']").select_option('1')
                #    results+=  [f"{nome_atividade} ==> Geral 'Tipo de glossário' é '{geral_tipo}' deve ser atualizado para '{geral_tipo_padrao}' atendendo ao Padrão."]
                
                #ITENS - APROVAÇÃO IMEDIATA DE NOVOS ITENS - Padrão (Sim)
                id_itens = id_geral = page.locator('fieldset[id="id_entrieshdr"]')
                time.sleep(0.5)
                if id_itens.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = id_itens.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_itens.locator("select[id='id_defaultapproval']").input_value()) != '1':
                    itens_aprov_padrao = 'Sim'
                    itens_aprov = id_itens.locator("select[id='id_defaultapproval'] > option[selected]").inner_text()
                    #id_itens.locator("select[id='id_defaultapproval']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Itens 'Aprovação imediata de novos itens' é '{itens_aprov}' deve ser atualizado para '{itens_aprov_padrao}' atendendo ao Padrão."]
                
                #ITENS - SEMPRE PERMITIR EDIÇÃO - Padrão (Não)
                if (id_itens.locator("select[id='id_editalways']").input_value()) != '0':
                    itens_sempre_padrao = 'Não'
                    itens_sempre = id_itens.locator("select[id='id_editalways'] > option[selected]").inner_text()
                    #id_itens.locator("select[id='id_editalways']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Itens 'Sempre permitir edição' é '{itens_sempre}' deve ser atualizado para '{itens_sempre_padrao}' atendendo ao Padrão."]
                
                #ITENS - PERMITIR ITENS DUPLICADOS - Padrão (Não)
                if (id_itens.locator("select[id='id_allowduplicatedentries']").input_value()) != '0':
                    itens_duplicados_padrao = 'Não'
                    itens_duplicados = id_itens.locator("select[id='id_allowduplicatedentries'] > option[selected]").inner_text()
                    #id_itens.locator("select[id='id_allowduplicatedentries']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Itens 'Permitir itens duplicados' é '{itens_duplicados}' deve ser atualizado para '{itens_duplicados_padrao}' atendendo ao Padrão."]
                
                #ITENS - PERMITIR COMENTÁRIOS - Padrão (Não)
                if (id_itens.locator("select[id='id_allowcomments']").input_value()) != '0':
                    itens_comentarios_padrao = 'Não'
                    itens_comentarios = id_itens.locator("select[id='id_allowcomments'] > option[selected]").inner_text()
                    #id_itens.locator("select[id='id_allowcomments']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Itens 'Permitir comentários' é '{itens_comentarios}' deve ser atualizado para '{itens_comentarios_padrao}' atendendo ao Padrão."]
                
                #ITENS - FAZER O LINK AUTOMÁTICO DOS ITENS - Padrão (Sim)
                if (id_itens.locator("select[id='id_usedynalink']").input_value()) != '1':
                    itens_links_padrao = 'Sim'
                    itens_links = id_itens.locator("select[id='id_usedynalink'] > option[selected]").inner_text()
                    #id_itens.locator("select[id='id_usedynalink']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Itens 'Fazer o link automático dos itens' é '{itens_links}' deve ser atualizado para '{itens_links_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - FORMATO DE VISUALIZAÇÃO - Padrão (Simples, estilo dicionário)
                id_aparencia = page.locator('fieldset[id="id_appearancehdr"]')
                time.sleep(0.5)
                if id_aparencia.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_aparencia.locator("select[id='id_displayformat']").input_value()) != 'dictionary':
                    apa_visu_padrao = 'Simples, estilo dicionário'
                    apa_visu = id_aparencia.locator("select[id='id_displayformat'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_displayformat']").select_option('dictionary')
                    results+=  [f"{nome_atividade} ==> Aparência 'Formato de visualização' é '{apa_visu}' deve ser atualizado para '{apa_visu_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - FORMATO DA EXIBIÇÃO DE APROVAÇÃO - Padrão (Padrão para o mesmo formato de exibição)
                if (id_aparencia.locator("select[id='id_approvaldisplayformat']").input_value()) != 'default':
                    apa_exib_padrao = 'Padrão para o mesmo formato de exibição'
                    apa_exib = id_aparencia.locator("select[id='id_approvaldisplayformat'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_approvaldisplayformat']").select_option('default')
                    results+=  [f"{nome_atividade} ==> Aparência 'Formato da exibição de aprovação' é '{apa_exib}' deve ser atualizado para '{apa_exib_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - MOSTRAR ALFABETO EM LINKS - Padrão (Sim)
                if (id_aparencia.locator("select[id='id_showalphabet']").input_value()) != '1':
                    apa_alfa_padrao = 'Sim'
                    apa_alfa = id_aparencia.locator("select[id='id_showalphabet'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_showalphabet']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Mostrar alfabeto em links' é '{apa_alfa}' deve ser atualizado para '{apa_alfa_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - MOSTRA O LINK 'TODOS' - Padrão (Sim)
                if (id_aparencia.locator("select[id='id_showall']").input_value()) != '1':
                    apa_todos_padrao = 'Sim'
                    apa_todos = id_aparencia.locator("select[id='id_showall'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_showall']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Mostrar o link TODOS' é '{apa_todos}' deve ser atualizado para '{apa_todos_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - MOSTRA LINK ESPECIAL - Padrão (Sim)
                if (id_aparencia.locator("select[id='id_showspecial']").input_value()) != '1':
                    apa_especial_padrao = 'Sim'
                    apa_especial = id_aparencia.locator("select[id='id_showspecial'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_showspecial']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Mostrar link especial' é '{apa_especial}' deve ser atualizado para '{apa_especial_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - PERMITIR VISUALIZAR IMPRESSÃO - Padrão (Sim)
                if (id_aparencia.locator("select[id='id_allowprintview']").input_value()) != '1':
                    apa_impressao_padrao = 'Sim'
                    apa_impressao = id_aparencia.locator("select[id='id_allowprintview'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_allowprintview']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Permitir visualizar impressão' é '{apa_impressao}' deve ser atualizado para '{apa_impressao_padrao}' atendendo ao Padrão."]
                
                #AVALIAÇÕES - TIPO DE AGREGAÇÃO - Padrão (Nenhuma avaliação)
                id_avaliacoes = page.locator('fieldset[id="id_modstandardratings"]')
                if (id_avaliacoes.locator("select[id='id_assessed']").input_value()) != '0':
                    apa_impressao_padrao = 'Nenhuma avaliação'
                    apa_impressao = id_avaliacoes.locator("select[id='id_assessed'] > option[selected]").inner_text()
                    #id_avaliacoes.locator("select[id='id_assessed']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Avaliações 'Tipo de agregação' é '{apa_impressao}' deve ser atualizado para '{apa_impressao_padrao}' atendendo ao Padrão."]
                
                #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                time.sleep(0.5)
                if id_conf_comuns_modulos.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_conf_comuns_modulos.locator("select[id='id_visible']").input_value()) != '1':
                    conf_com_mod_padrao = 'Mostrar na página do curso'
                    conf_com_mod = id_conf_comuns_modulos.locator("select[id='id_visible'] > option[selected]").inner_text()
                    #id_conf_comuns_modulos.locator('select[id="id_visible"]').select_option('1')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod}' deve ser atualizado para '{conf_com_mod_padrao}' atendendo ao Padrão."]

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
                        #id_conclusao_atividade.locator('select[id="id_completion"]').select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                            
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]

                    #CONCLUSÃO DE ATIVIDADE - REQUER ENTRADAS - Padrão (desmarcado)
                    if id_conclusao_atividade.locator("input[id='id_completionentriesenabled']").is_checked():
                        #id_conclusao_atividade.locator("input[id='id_completionentriesenabled']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer entradas' deve ser desmarcado atendendo ao Padrão."]

                except:
                    #DESBLOQUEAR OPÇÃO DE CONCLUSÃO
                    id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click()
                    time.sleep(1)
                    
                #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_acom_conc_padrao = 'Mostrar atividade como concluída quando as condições forem satisfeitas'
                        conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator('select[id="id_completion"]').select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                            
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]

                    #CONCLUSÃO DE ATIVIDADE - REQUER ENTRADAS - Padrão (desmarcado)
                    if id_conclusao_atividade.locator("input[id='id_completionentriesenabled']").is_checked():
                        #id_conclusao_atividade.locator("input[id='id_completionentriesenabled']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer entradas' deve ser desmarcado atendendo ao Padrão."]

                #CONCLUSÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM - Padrão (desmarcado)
                if id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").is_checked():
                    #id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").click()
                    results+= [f"{nome_atividade} ==> Conclusão de atividade 'Conclusão esperada em' deve ser desmarcado atendendo ao Padrão."]
            
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
            print('Glossário concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Glossário. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
