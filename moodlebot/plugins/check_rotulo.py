import time
from moodlebot.plugin import CheckPlugin

class CheckRotulo(CheckPlugin):
    """Validando as configurações dos Rótulos."""
    def handle(self, page, context):
        results = []
        print("Rótulo")
        return results

        #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
        board = False
        board_chave = page.locator('xpath=//li[@class="activity label modtype_label "]')
        time.sleep(0.5)
        if board_chave.count() != 0:
            cont = page.locator('xpath=//li[@class="activity label modtype_label "]')
            board = True
        else:
            cont = page.locator('xpath=//li[@class="activity activity-wrapper label modtype_label hasinfo dropready draggable"]')
        
        #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
        formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
        #print(formato_tiles.count())
        tiles = False
        if formato_tiles.count() != 0:
            tiles = True

        total = cont.count()
        for x in range(total):
            time.sleep(0.5)
            print(f'Rótulo {x+1}/{total}')
            atividade = cont.nth(x).locator('xpath=//div[@class="activity-actions align-self-start"]')
            atividade.click()
            #time.sleep(1)
            editar_configuracao = atividade.locator('xpath=//a[@class="dropdown-item editing_update menu-action cm-edit-action" and @role="menuitem"]')
            editar_configuracao.click()
            time.sleep(1)  
            
            #GERAL - TEXTO DO RÓTULO
            id_geral = page.locator('fieldset[id="id_generalhdr"]')
            nome_atividade = id_geral.locator("div[id='id_introeditoreditable']").inner_text()
            #nome = nome_atividade.locator('xpath=//i[@class="fa fa-graduation-cap"]').inner_text()
            print("Nome do Recurso: %s" % nome_atividade)

            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
            #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
            #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
            print(f'Rótulo {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
            if exp_all.get_attribute('aria-expanded') == 'false':
                exp_all.click()
            
            #if expandir_tudo.count() != 0:
            #    expandir_tudo.click()
            #time.sleep(0.5)

            #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
            id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
            if (id_conf_comuns_modulos.locator("select[id='id_visible']").input_value()) != '1':
                conf_com_mod_disp_padrao = 'Mostrar na página do curso'
                conf_com_mod_disp = id_conf_comuns_modulos.locator("select[id='id_visible'] > option[selected]").inner_text()
                #id_conf_comuns_modulos.locator("select[id='id_visible']").select_option('1')
                results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod_disp}' e deve ser atualizado para '{conf_com_mod_disp_padrao}' atendendo ao Padrão."]

            #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
            id_conclusao_atividade = page.locator('fieldset[id="id_activitycompletionheader"]')
            try:
                #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Não indicar a conclusão de atividade)
                if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '0':
                    conc_atv_acom_conc_padrao = 'Não indicar a conclusão de atividade'
                    conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                    #id_conclusao_atividade.locator("select[id='id_completion']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' e deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
            except:
                #DESBLOQUEAR OPÇÃO DE CONCLUSÃO
                id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click() 
                time.sleep(1)   
                if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '0':
                    conc_atv_acom_conc_padrao = 'Não indicar a conclusão de atividade'
                    conc_atv_acom_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                    #id_conclusao_atividade.locator("select[id='id_completion']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_acom_conc}' e deve ser atualizado para '{conc_atv_acom_conc_padrao}' atendendo ao Padrão."]
    
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
        print('Rótulo concluído')
        return results
