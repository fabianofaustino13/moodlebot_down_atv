import time
from moodlebot.plugin import CheckPlugin

class CheckLivro(CheckPlugin):
    """Validando as configurações do Recurso Livro."""
    def handle(self, page, context):
        results = []
        print("Livro")
        #return results
        
        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity book modtype_book "]')
            time.sleep(0.5)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity book modtype_book "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper book modtype_book hasinfo dropready draggable"]')
            
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True

            total = cont.count()
            for x in range(total):
                time.sleep(0.5)
                print(f'Livro {x+1}/{total}')
                """ cont.locator('xpath=//div[@class="activity-actions align-self-start"]').nth(x).click()
                time.sleep(1)
                cont.nth(x).locator('a:has-text("Editar configurações")').click() """ 

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
                print(f'Livro {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                time.sleep(0.5)
                if exp_all.count() != 0:
                    if exp_all.get_attribute('aria-expanded') == 'false':
                        exp_all.click()
                        time.sleep(0.5)

                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator("input[id='id_name']").input_value()
                print("Nome do Recurso: %s" % nome_atividade)
                time.sleep(0.5)
                if id_geral.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)
            
                #GERAL - EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO - Padrão (desmarcado)
                if id_geral.locator("input[id='id_showdescription']").is_checked():
                    #id_geral.locator("input[id='id_showdescription']").click()
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição na página do curso' deve ser desabilitado atendendo ao Padrão."]
                    
                #APARÊNCIA - FORMATAÇÃO DE CAPÍTULO - Padrão (Números)
                id_aparencia = page.locator('fieldset[id="id_appearancehdr"]')
                time.sleep(0.5)
                if id_aparencia.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_aparencia.locator("select[id='id_numbering']").input_value()) != '1':
                    apa_form_cap_padrao = 'Números'
                    apa_form_cap = id_aparencia.locator("select[id='id_numbering'] > option[selected]").inner_text()
                    #id_aparencia.locator('select[id="id_numbering"]').select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Formatação de capítulo' é '{apa_form_cap}' e deve ser atualizado para '{apa_form_cap_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - ESTILO DE NAVEGAÇÃO - Padrão (Imagens)
                #if (id_aparencia.locator("select[id='id_navstyle']").input_value()) != '1':
                #    apa_est_nav_padrao = 'Imagens'
                #    apa_est_nav = id_aparencia.locator("select[id='id_navstyle'] > option[selected]").inner_text()
                    #id_aparencia.locator('select[id="id_navstyle"]').select_option('1')
                #    results+=  [f"{nome_atividade} ==> Aparência 'Formatação de capítulo' é '{apa_est_nav}' e deve ser atualizado para '{apa_est_nav_padrao}' atendendo ao Padrão."]
            
                #APARÊNCIA - TÍTULOS PERSONALIZADOS - Padrão (desmarcado)
                if id_aparencia.locator("input[id='id_customtitles']").is_checked():
                    #id_aparencia.locator("input[id='id_customtitles']").click()
                    results+= [f"{nome_atividade} ==> Aparência 'Títulos personalizados' deve ser desmarcado atendendo ao Padrão."]

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
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod}' e deve ser atualizado para '{conf_com_mod_padrao}' atendendo ao Padrão."]
            
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
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' foi marcado atendendo ao Padrão."]
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
                            
                #CONCLUSÃO DE ATIVIDADE - CONCLUSÃO ESPéDA EM - Padrão (desmarcado)
                if id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").is_checked():
                    #id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").click()
                    results+= [f"{nome_atividade} ==> Conclusão de atividade 'Conclusão espéda em' deve ser desmarcado atendendo ao Padrão."]
                
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
            print('Livro concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Livro. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
