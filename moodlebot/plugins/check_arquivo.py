import time
from moodlebot.plugin import CheckPlugin

class CheckArquivo(CheckPlugin):
    """Validando as configurações do Recurso Arquivo."""
    def handle(self, page, context):
        results = []
        print("Arquivo")
        #return results
        
        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity resource modtype_resource "]')
            time.sleep(1)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity resource modtype_resource "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper resource modtype_resource hasinfo dropready draggable"]')
                    
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True
            total = cont.count()
            for x in range(total):
                time.sleep(0.5)
                print(f'Arquivo {x+1}/{total}')
                atividade = cont.nth(x).locator('xpath=//div[@class="activity-actions align-self-start"]')
                atividade.click()
                time.sleep(0.5)
                editar_configuracao = atividade.locator('xpath=//a[@class="dropdown-item editing_update menu-action cm-edit-action" and @data-action="update"]')
                editar_configuracao.click()
                #editar = cont.nth(x).locator('a:has-text("Editar configurações")')
                #editar.click()
                time.sleep(1) 
                        
                #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
                #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
                print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
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
            
                #GERAL - EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO - Padrão (desmarcado)
                if id_geral.locator('input[id="id_showdescription"]').is_checked():
                    #id_geral.locator('input[id="id_showdescription"]').click()
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição na página do curso' deve ser desmarcado atendendo ao Padrão."]

                #APARÊNCIA - EXIBIR - Padrão (Forçar o download)
                id_aparencia = page.locator('fieldset[id="id_optionssection"]')
                time.sleep(0.5)
                if id_aparencia.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if (id_aparencia.locator('select[id="id_display"]').input_value()) != '4':
                    apa_exibir_padrao = 'Forçar o download'
                    apa_exibir = id_aparencia.locator("select[id='id_display'] > option[selected]").inner_text()
                    #id_aparencia.locator('select[id="id_display"]').select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Exibir' é '{apa_exibir}' e deve ser atualizado para '{apa_exibir_padrao}' atendendo ao Padrão."]
                
                #APARÊNCIA - MOSTAR TAMANHO - Padrão (desmarcado)
                if id_aparencia.locator("input[id='id_showsize']").is_checked():
                    #id_aparencia.locator("input[id='id_showsize']").click()
                    results+= [f"{nome_atividade} ==> Aparência 'Mostrar tamanho' deve ser desmarcado atendendo ao Padrão."]

                #APARÊNCIA - MOSTAR TIPO - Padrão (desmarcado)
                if id_aparencia.locator("input[id='id_showtype']").is_checked():
                    #id_aparencia.locator("input[id='id_showtype']").click()
                    results+= [f"{nome_atividade} ==> Aparência 'Mostrar tipo' deve ser desmarcado atendendo ao Padrão."]

                #APARÊNCIA - EXIBIR DATA DE ENVIO/MODIFICAÇÃO - Padrão (desmarcado)
                if id_aparencia.locator("input[id='id_showdate']").is_checked():
                    #id_aparencia.locator("input[id='id_showdate']").click()
                    results+= [f"{nome_atividade} ==> Aparência 'Exibir data de envio/modificação' deve ser desmarcado atendendo ao Padrão."]
                
                #APARÊNCIA - USAR FILTROS NO CONTEÚDO DO ARQUIVO - Padrão (nenhum)
                time.sleep(0.5)
                if id_aparencia.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                    id_aparencia.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                    time.sleep(0.5)

                if (id_aparencia.locator("select[id='id_filterfiles']").input_value()) != '0':
                    apa_exibir_filtro_padrao = 'Nenhum'
                    apa_exibir_filtro = id_aparencia.locator("select[id='id_filterfiles'] > option[selected]").inner_text()
                    #id_aparencia.locator('select[id="id_filterfiles"]').select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Usar filtros no conteúdo do arquivo' é '{apa_exibir_filtro}' e deve ser atualizado para '{apa_exibir_filtro_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - EXIBIR A DESCRIÇÃO DOS RECURSOS - Padrão (marcado)
                try:
                    if id_aparencia.locator("input[id='id_printintro']").is_checked() == False:
                        #id_aparencia.locator("input[id='id_printintro']").click()
                        results+= [f"{nome_atividade} ==> Aparência 'Exibir a descrição dos recursos' deve ser marcado atendendo ao Padrão."]
                except:
                    results+= [f"{nome_atividade} ==> Aparência 'Exibir a descrição dos recursos' deve ser marcado atendendo ao Padrão."]
                
                #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                time.sleep(0.5)
                if id_conf_comuns_modulos.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = id_conf_comuns_modulos.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
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
                    exp_all = id_conclusao_atividade.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
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
            print('Arquivo concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Arquivo. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
