import time
from moodlebot.plugin import CheckPlugin

class CheckPasta(CheckPlugin):
    """Validando as configurações do Recurso Pasta."""
    def handle(self, page, context):
        results = []
        print("Pasta")
        #return results

        try:            
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity folder modtype_folder "]')
            time.sleep(1)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity folder modtype_folder "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper folder modtype_folder hasinfo dropready draggable"]')
            
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True

            total = cont.count()
            for x in range(total):
                time.sleep(0.5)
                print(f'Pasta {x+1}/{total}')
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
                print(f'Pasta {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                time.sleep(0.5)
                if exp_all.count() != 0:
                    if exp_all.get_attribute('aria-expanded') == 'false':
                        exp_all.click()
                        time.sleep(0.5)

                #GERAL - NOME
                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator("input[id='id_name']").input_value()
                print("Nome do Recurso: %s" % nome_atividade)
            
                #GERAL - EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO - Padrão (desmarcado)
                time.sleep(0.5)
                if id_geral.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

            
                if id_geral.locator("input[id='id_showdescription']").is_checked():
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição na página do curso' deve ser desmarcado atendendo ao Padrão."]
                    #id_geral.locator("input[id='id_showdescription']").click()

                #CONTEÚDO - EXIBIR O CONTEÚDO DA PASTA - Padrão (Em uma página separada)
                id_conteudo = page.locator('fieldset[id="id_content"]')
                time.sleep(0.5)
                if id_conteudo.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)


                if (id_conteudo.locator("select[id='id_display']").input_value()) != '0':
                    cont_exib_cont_padrao = 'Em uma página separada'
                    cont_exib_cont = id_conteudo.locator("select[id='id_display'] > option[selected]").inner_text()
                    #id_conteudo.locator("select[id='id_display']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Conteúdo 'Exibir o conteúdo da pasta' é '{cont_exib_cont}' deve ser atualizado para '{cont_exib_cont_padrao}' atendendo ao Padrão."]
                
                #CONTEÚDO - MOSTAR SUBPASTAS EXPANDIDAS - Padrão (marcado)
                if id_conteudo.locator("input[id='id_showexpanded']").is_checked() == False:
                    #id_conteudo.locator("input[id='id_showexpanded']").click()
                    results+= [f"{nome_atividade} ==> Conteúdo 'Mostrar subpastas expandidas' deve ser marcado atendendo ao Padrão."]

                #CONTEÚDO - EXIBIR BOTÃO DE DOWNLOAD DA PASTA - Padrão (marcado)
                if id_conteudo.locator("input[id='id_showdownloadfolder']").is_checked() == False:
                    #id_conteudo.locator("input[id='id_showdownloadfolder']").click()
                    results+= [f"{nome_atividade} ==> Conteúdo 'Exibir botão de download da pasta' deve ser marcado atendendo ao Padrão."]
                
                #CONTEÚDO - FORÇAR DOWNLOAD DE ARQUIVOS - Padrão (marcado)
                if id_conteudo.locator("input[id='id_forcedownload']").is_checked() == False:
                    #id_conteudo.locator("input[id='id_forcedownload']").click()
                    results+= [f"{nome_atividade} ==> Conteúdo 'Forçar download de arquivos' deve ser marcado atendendo ao Padrão."]
                    
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
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod_disp}' deve ser atualizado para '{conf_com_mod_disp_padrao}' atendendo ao Padrão."]

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
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]

                except:
                    #DESBLOQUEAR OPÇÃO DE CONCLUSÃO
                    id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click()
                    time.sleep(1)
                    
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_acom_conc_padrao = 'Mostrar atividade como concluída quando as condições forem satisfeitas'
                        conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator("select[id='id_completion']").select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
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
            print('Pasta concluída')
        except Exception as err:
            results+=  [f"Não foi possível validar Pasta. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
