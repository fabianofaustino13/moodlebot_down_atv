import time
from moodlebot.plugin import CheckPlugin

class CheckEnquete(CheckPlugin):
    """Validando as configurações da Atividade Enquete."""
    def handle(self, page, context):
        results = []
        print("Enquete")
        #return results
        
        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity questionnaire modtype_questionnaire "]')
            time.sleep(0.5)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity questionnaire modtype_questionnaire "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper questionnaire modtype_questionnaire hasinfo dropready draggable"]')
            
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True
            
            total = cont.count()
            for x in range(total):          
                time.sleep(0.5)
                print(f'Enquete {x+1}/{total}')
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
                print(f'Enquete {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                time.sleep(0.5)
                if exp_all.count() != 0:        
                    if exp_all.get_attribute('aria-expanded') == 'false':
                        exp_all.click()
                        time.sleep(0.5)
                
                #Geral- NOME
                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator("input[id='id_name']").input_value()
                print("Nome da Atividade: %s" % nome_atividade)

                time.sleep(0.5)
                if id_geral.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)
            
                #GERAL - FORMATO - Padrão (automático)
                if (id_geral.locator('select[id="menuintroeditorformat"]').input_value()) != '0':
                    geral_formato_padrao = 'Formato Automático'
                    geral_formato = id_geral.locator('select[id="menuintroeditorformat"] > option[selected]').inner_text()
                    #id_geral.locator('select[id="menuintroeditorformat"]').select_option('0')
                    results+= [f"{nome_atividade} ==> Geral'Formato' é '{geral_formato} e deve ser atualizado para '{geral_formato_padrao}' atendendo ao Padrão."]
                
                #GERAL - EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO - Padrão (desmarcado)
                if id_geral.locator('input[id="id_showdescription"]').is_checked():
                    #id_geral.locator('input[id="id_showdescription"]').click()
                    results+= [f"{nome_atividade} ==> Geral'Exibir descrição na página do curso' deve ser desmarcado atendendo ao Padrão."]

                #TEMPO - PERMITIR RESPOSTAS DE - Padrão (desmarcado)
                id_tempo = page.locator('fieldset[id="id_availabilityhdr"]')
                time.sleep(0.5)
                if id_tempo.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = id_tempo.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)
                #time.sleep(1)
                #if id_tempo.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                #    page.locator('a:has-text("Expandir tudo")').click()

                if id_tempo.locator('input[id="id_opendate_enabled"]').is_checked():
                    #id_tempo.locator('input[id="id_useopendate"]').click()
                    results+=  [f"{nome_atividade} ==> Tempo 'Permitir respostas de' deve ser desmarcado atendendo ao Padrão."]
                
                #TEMPO - DATA DE ENCERRAMENTO - Padrão (desmarcado)
                if id_tempo.locator("input[id='id_closedate_enabled']").is_checked():
                    #id_tempo.locator('input[id="id_useclosedate"]').click()
                    results+=  [f"{nome_atividade} ==> Tempo 'Permitir respostas de' deve ser desmarcado atendendo ao Padrão."]
                    
                #OPÇÕES DE RESPOSTAS - TIPO - Padrão (responder uma única vez)
                id_opcoes_respostas = page.locator('fieldset[id="id_questionnairehdr"]')
                time.sleep(0.5)
                if id_opcoes_respostas.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_opcoes_respostas.locator("select[id='id_qtype']").input_value()) != '1':
                    opcoes_resp_tipo_padrao = 'Responder uma única vez'
                    opcoes_resp_tipo = id_opcoes_respostas.locator('select[id="id_qtype"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_qtype"]').select_option('1')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Tipo' é '{opcoes_resp_tipo} e deve ser atualizado para '{opcoes_resp_tipo_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - TIPO DE RESPONDENTE - Padrão (anônimo)
                if (id_opcoes_respostas.locator("select[id='id_respondenttype']").input_value()) != 'anonymous':
                    opcoes_resp_respondente_padrao = 'Anônimo'
                    opcoes_resp_respondente = id_opcoes_respostas.locator('select[id="id_respondenttype"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_respondenttype"]').select_option('anonymous')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Tipo do respondente' é '{opcoes_resp_respondente} e deve ser atualizado para '{opcoes_resp_respondente_padrao}' atendendo ao Padrão."]
            
                #OPÇÕES DE RESPOSTAS - ESTUDANTES PODEM VISUALIZAR TODAS AS RESPOSTAS - Padrão (depois de responder a enquete)
                if (id_opcoes_respostas.locator("select[id='id_resp_view']").input_value()) != '1':
                    opcoes_resp_estudante_padrao = 'Depois de responder a enquete'
                    opcoes_resp_estudante = id_opcoes_respostas.locator('select[id="id_resp_view"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_resp_view"]').select_option('1')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Estudantes podem visualizar TODAS as respostas' é '{opcoes_resp_estudante} e deve ser atualizado para '{opcoes_resp_estudante_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - ENVIAR NOTIFICAÇÕES DE SUBMISSÃO - Padrão (não)
                if (id_opcoes_respostas.locator("select[id='id_notifications']").input_value()) != '0':
                    opcoes_resp_enviar_padrao = 'Não'
                    opcoes_resp_enviar = id_opcoes_respostas.locator('select[id="id_notifications"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_notifications"]').select_option('0')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Enviar notificações de submissão' é '{opcoes_resp_enviar} e deve ser atualizado para '{opcoes_resp_enviar_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - SALVAR/RETOMAR RESPOSTAS - Padrão (sim)
                if (id_opcoes_respostas.locator("select[id='id_resume']").input_value()) != '1':
                    opcoes_resp_salvar_padrao = 'Sim'
                    opcoes_resp_salvar = id_opcoes_respostas.locator('select[id="id_resume"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_resume"]').select_option('1')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Salvar/Retomar respostas' é '{opcoes_resp_salvar} e deve ser atualizado para '{opcoes_resp_salvar_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - PERMITIR QUESTÕES DE RAMIFICAÇÃO - Padrão (sim)
                if (id_opcoes_respostas.locator("select[id='id_navigate']").input_value()) != '1':
                    opcoes_resp_permitir_padrao = 'Sim'
                    opcoes_resp_permitir = id_opcoes_respostas.locator('select[id="id_navigate"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_navigate"]').select_option('1')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Permitir questões de ramificação' é '{opcoes_resp_permitir} e deve ser atualizado para '{opcoes_resp_permitir_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - NUMERAÇÃO AUTOMÁTICA - Padrão (Numerar automaticamente páginas e questões)
                if (id_opcoes_respostas.locator("select[id='id_autonum']").input_value()) != '3':
                    opcoes_resp_numero_padrao = 'Numerar automaticamente páginas e questões'
                    opcoes_resp_numero = id_opcoes_respostas.locator('select[id="id_autonum"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_autonum"]').select_option('3')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Permitir questões de ramificação' é '{opcoes_resp_numero} e deve ser atualizado para '{opcoes_resp_numero_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - ESCALA DE NOTAS - Padrão (nenhuma nota)
                if (id_opcoes_respostas.locator("select[id='id_grade']").input_value()) != '0':
                    opcoes_resp_escala_padrao = 'Nenhuma nota'
                    opcoes_resp_escala = id_opcoes_respostas.locator('select[id="id_grade"] > option[selected]').inner_text()
                    #id_opcoes_respostas.locator('select[id="id_grade"]').select_option('0')
                    results+= [f"{nome_atividade} ==> Opções de respostas 'Permitir questões de ramificação' é '{opcoes_resp_escala} e deve ser atualizado para '{opcoes_resp_escala_padrao}' atendendo ao Padrão."]
                
                #OPÇÕES DE RESPOSTAS - MOSTRAR BARRA DE PROGRESSO - Padrão (desmarcado)
                if id_opcoes_respostas.locator("input[id='id_progressbar']").is_checked():
                    #id_tempo.locator('input[id="id_useclosedate"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de respostas 'Mostrar barra de progresso' deve ser desmarcado atendendo ao Padrão."]

                #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                if (id_conf_comuns_modulos.locator("select[id='id_visible']").input_value()) != '1':
                    conf_com_mod_padrao = 'Mostrar na página do curso'
                    conf_com_mod = id_conf_comuns_modulos.locator("select[id='id_visible'] > option[selected]").inner_text()
                    #id_conf_comuns_modulos.locator('select[id="id_visible"]').select_option('1')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod}' e deve ser atualizado para '{conf_com_mod_padrao}' atendendo ao Padrão."]

                #CONFIGURAÇÕES COMUNS DE MÓDULOS - MODALIDADE GRUPO - Padrão (nenhum grupo)
                if (id_conf_comuns_modulos.locator("select[id='id_groupmode']").input_value()) != '0':
                    conf_com_mod_grupo_padrao = 'Nenhum grupo'
                    conf_com_mod_grupo = id_conf_comuns_modulos.locator("select[id='id_groupmode'] > option[selected]").inner_text()
                    #id_conf_comuns_modulos.locator('select[id="id_groupmode"]').select_option('0')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Modalidade grupo' é '{conf_com_mod_grupo}' e deve ser atualizado para '{conf_com_mod_grupo_padrao}' atendendo ao Padrão."]

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
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' e deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                            
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionsubmit']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionsubmit']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]

                except:
                    #DESBLOQUEAR OPÇÃO DE CONCLUSÃO
                    id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click()
                    time.sleep(1)
                    
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_acom_conc_padrao = 'Mostrar atividade como concluída quando as condições forem satisfeitas'
                        conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator('select[id="id_completion"]').select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' e deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                            
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionsubmit']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionsubmit']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]

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
            print('Enquete concluída')
        except Exception as err:
            results+=  [f"Não foi possível validar Enquete. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
