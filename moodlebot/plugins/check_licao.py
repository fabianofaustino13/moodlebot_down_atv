import time
from moodlebot.plugin import CheckPlugin

class CheckLicao(CheckPlugin):
    """Validando as configurações da Atividade Lição."""
    def handle(self, page, context):
        results = []
        print("Lição")
        #return results
        
        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity lesson modtype_lesson "]')
            time.sleep(1)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity lesson modtype_lesson "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper lesson modtype_lesson hasinfo dropready draggable"]')

            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True
            total = cont.count()
            for x in range(total):
                time.sleep(0.5)
                print(f'Lição {x+1}/{total}')
                """ cont.locator('xpath=//div[@class="activity-actions align-self-start"]').nth(x).click()
                time.sleep(1)
                editar = cont.locator('a:has-text("Editar configurações")').nth(x)
                editar.click() """      
                atividade = cont.nth(x).locator('xpath=//div[@class="activity-actions align-self-start"]')
                atividade.click()
                time.sleep(0.5)
                editar_configuracao = atividade.locator('xpath=//a[@class="dropdown-item editing_update menu-action cm-edit-action" and @data-action="update"]')
                editar_configuracao.click()      
                time.sleep(1)

                #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                print(f'Lição {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
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
                if id_geral.locator("input[id='id_showdescription']").is_checked():
                    #id_geral.locator("input[id='id_showdescription']").click()
                    results+= [f"{nome_atividade} ==> Geral 'Exibir descrição na página do curso' deve ser desmarcado atendendo ao Padrão."]

                #APARÊNCIA - BARRA DE PROGRESSO - Padrão (sim)
                id_aparencia = page.locator('fieldset[id="id_appearancehdr"]')
                expandir_aparencia = id_aparencia.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                time.sleep(0.5)
                mostrar_mais_aparencia = id_aparencia.locator('xpath=//a[@class="moreless-toggler" and @role="button"]')
                if mostrar_mais_aparencia.get_attribute('aria-expanded') == 'false':
                    if expandir_aparencia.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                        time.sleep(0.5)
                    mostrar_mais_aparencia.click()
                    time.sleep(0.5)

                if id_aparencia.locator("select[id='id_progressbar']").input_value() != '1':
                    apa_barra_padrao = 'Sim'
                    apa_barra = id_aparencia.locator("select[id='id_progressbar'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_progressbar']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Barra de progresso' é '{apa_barra}' deve ser atualizado para '{apa_barra_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - VISUALIZAR PONTUAÇÃO CORRENTE - Padrão (sim)
                if id_aparencia.locator("select[id='id_ongoing']").input_value() != '1':
                    apa_corrente_padrao = 'Sim'
                    apa_corrente = id_aparencia.locator("select[id='id_ongoing'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_ongoing']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Visualizar pontuação corrente' é '{apa_corrente}' deve ser atualizado para '{apa_corrente_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - MOSTRAR MENU - Padrão (não)
                if id_aparencia.locator("select[id='id_displayleft']").input_value() != '0':
                    apa_menu_padrao = 'Não'
                    apa_menu = id_aparencia.locator("select[id='id_displayleft'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_displayleft']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Mostrar menu' é '{apa_menu}' deve ser atualizado para '{apa_menu_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - NOTA MÍNIMA PARA A EXIBIÇÃO DO MENU - Padrão (0%)
                if id_aparencia.locator("select[id='id_displayleftif']").input_value() != '0':
                    apa_nota_minima_padrao = '0%'
                    apa_nota_minima = id_aparencia.locator("select[id='id_displayleftif'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_displayleftif']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Nota mínima para a exibição do menu' é '{apa_nota_minima}' deve ser atualizado para '{apa_nota_minima_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - APRESENTAÇÃO DE SLIDES - Padrão (não)
                if id_aparencia.locator("select[id='id_slideshow']").input_value() != '0':
                    apa_slides_padrao = 'Não'
                    apa_slides = id_aparencia.locator("select[id='id_slideshow'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_slideshow']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Apresentação de slides' é '{apa_slides}' deve ser atualizado para '{apa_slides_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - NÚMERO MÁXIMO DE RESPOSTAS - Padrão (não)
                if id_aparencia.locator("select[id='id_maxanswers']").input_value() != '10':
                    apa_max_resp_padrao = '10'
                    apa_max_resp = id_aparencia.locator("select[id='id_maxanswers'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_maxanswers']").select_option('5')
                    results+=  [f"{nome_atividade} ==> Aparência 'Número máximo de respostas' é '{apa_max_resp}' deve ser atualizado para '{apa_max_resp_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - USE O FEEDBACK PADRÃO - Padrão (não)
                if id_aparencia.locator("select[id='id_feedback']").input_value() != '0':
                    apa_feed_padrao = 'Não'
                    apa_feed = id_aparencia.locator("select[id='id_feedback'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_feedback']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Use o feedback padrão' é '{apa_feed}' deve ser atualizado para '{apa_feed_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - LINK PARA A PRÓXIMA ATIVIDADE - Padrão (nenhum)
                #if id_aparencia.locator("select[id='id_activitylink']").input_value() != '0':
                #    apa_prox_padrao = 'Nenhum'
                #    apa_prox = id_aparencia.locator("select[id='id_activitylink'] > option[selected]").inner_text()
                    #id_aparencia.locator("select[id='id_activitylink']").select_option('0')
                #    results+=  [f"{nome_atividade} ==> Aparência 'Link para a próxima atividade' é '{apa_prox}' deve ser atualizado para '{apa_prox_padrao}' atendendo ao Padrão."]

                #DISPONIBILIDAE - DISPONÍVEL A PARTIR DE - Padrão (desmarcado)
                id_disponibilidade = page.locator('fieldset[id="id_availabilityhdr"]')
                expandir_disponibilidade = id_disponibilidade.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                time.sleep(0.5)
                if expandir_disponibilidade.count() != 0:
                    page.locator('a:has-text("Expandir tudo")').click()
                    time.sleep(0.5)
                
                #time.sleep(0.5)
                #id_disponibilidade.locator('a:has-text("Mostrar mais ...")').click()
                mostrar_mais_disponibilidade = id_disponibilidade.locator('xpath=//a[@class="moreless-toggler" and @role="button"]')
                time.sleep(0.5)
                if mostrar_mais_disponibilidade.get_attribute('aria-expanded') == 'false':
                #if id_disponibilidade.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                    if expandir_disponibilidade.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                        time.sleep(0.5)
                    mostrar_mais_disponibilidade.click()
                    time.sleep(0.5)

                if id_disponibilidade.locator("input[id='id_available_enabled']").is_checked():
                    #id_disponibilidade.locator("input[id='id_available_enabled']").click()
                    results+=  [f"{nome_atividade} ==> Disponibilidade 'Disponível a partir de' deve ser desmarcado atendendo ao Padrão."]
                
                #DISPONIBILIDAE - PRAZO FINAL - Padrão (desmarcado)
                if id_disponibilidade.locator("input[id='id_deadline_enabled']").is_checked():
                    #id_disponibilidade.locator("input[id='id_deadline_enabled']").click()
                    results+=  [f"{nome_atividade} ==> Disponibilidade 'Prazo final' deve ser desmarcado atendendo ao Padrão."]
                
                #DISPONIBILIDAE - LIMITE DE TEMPO - Padrão (desmarcado)
                if id_disponibilidade.locator("input[id='id_timelimit_enabled']").is_checked():
                    #id_disponibilidade.locator("input[id='id_timelimit_enabled']").click()
                    results+=  [f"{nome_atividade} ==> Disponibilidade 'Limite de tempo' deve ser desmarcado atendendo ao Padrão."]
                
                #DISPONIBILIDAE - LIÇÃO PROTEGIDA POR SENHA - Padrão (não)
                if id_disponibilidade.locator("select[id='id_usepassword']").input_value() != '0':
                    disp_senha_padrao = 'Não'
                    disp_senha = id_disponibilidade.locator("select[id='id_usepassword'] > option[selected]").inner_text()
                    #id_disponibilidade.locator("select[id='id_usepassword']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Disponibilidade 'Lição protegida por senha' é '{disp_senha}' deve ser atualizado para '{disp_senha_padrao}' atendendo ao Padrão."]

                #DISPONIBILIDAE - PERMITIR QUE A LIÇÃO SEJA REALIZADA DE FORMA OFFLINE UTILIZANDO O APLICATIVO PARA DISPOSITIVOS MÓVEIS - Padrão (não)
                if id_disponibilidade.locator("select[id='id_allowofflineattempts']").input_value() != '0':
                    disp_offline_padrao = 'Não'
                    disp_offline = id_disponibilidade.locator("select[id='id_allowofflineattempts'] > option[selected]").inner_text()
                    #id_disponibilidade.locator("select[id='id_allowofflineattempts']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Disponibilidade 'Permitir que a lição seja realizada de forma offline utilizando o aplicativo para dispositivos móveis' é '{disp_offline}' deve ser atualizado para '{disp_offline_padrao}' atendendo ao Padrão."]

                #CONTROLE DE FLUXO - PERMITIR REVISAO PELO ESTUDANTE - Padrão (não)
                id_controle_fluxo = page.locator('fieldset[id="id_flowcontrol"]')
                #time.sleep(0.5)
                expandir_controle = id_controle_fluxo.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                if expandir_controle.count() != 0:
                    page.locator('a:has-text("Expandir tudo")').click()

                #id_controle_fluxo.locator('a:has-text("Mostrar mais ...")').click()
                mostrar_mais_controle = id_controle_fluxo.locator('xpath=//a[@class="moreless-toggler" and @role="button"]')
                if mostrar_mais_controle.get_attribute('aria-expanded') == 'false':
                    if expandir_controle.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                    mostrar_mais_controle.click()

                #if id_controle_fluxo.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                #    id_controle_fluxo.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                #    time.sleep(0.5)

                if id_controle_fluxo.locator("select[id='id_modattempts']").input_value() != '0':
                    cont_fluxo_estudante_padrao = 'Não'
                    cont_fluxo_estudante = id_controle_fluxo.locator("select[id='id_modattempts'] > option[selected]").inner_text()
                    #id_controle_fluxo.locator("select[id='id_modattempts']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Controle de fluxo 'Permitir revisão pelo estudante' é '{cont_fluxo_estudante}' deve ser atualizado para '{cont_fluxo_estudante_padrao}' atendendo ao Padrão."]

                #CONTROLE DE FLUXO - FORNECER UMA OPÇÃO PARA TENTAR UMA NOVA QUESTÃO DE NOVO - Padrão (não)
                if id_controle_fluxo.locator("select[id='id_review']").input_value() != '0':
                    cont_fluxo_opcao_padrao = 'Não'
                    cont_fluxo_opcao = id_controle_fluxo.locator("select[id='id_review'] > option[selected]").inner_text()
                    #id_controle_fluxo.locator("select[id='id_review']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Controle de fluxo 'Fornecer uma opção para tentar uma nova questão de novo' é '{cont_fluxo_opcao}' deve ser atualizado para '{cont_fluxo_opcao_padrao}' atendendo ao Padrão."]

                #CONTROLE DE FLUXO - NÚMERO MÁXIMO DE TENTATIVAS - Padrão (uma)
                if id_controle_fluxo.locator("select[id='id_maxattempts']").input_value() != '1':
                    cont_fluxo_max_padrao = 'Uma'
                    cont_fluxo_max = id_controle_fluxo.locator("select[id='id_maxattempts'] > option[selected]").inner_text()
                    #id_controle_fluxo.locator("select[id='id_maxattempts']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Controle de fluxo 'Número áximo de tentativas' é '{cont_fluxo_max}' deve ser atualizado para '{cont_fluxo_max_padrao}' atendendo ao Padrão."]

                #CONTROLE DE FLUXO - AÇÃO APÓS UMA RESPOSTA CORRETA - Padrão (Normal - seguir percurso da lição)
                if id_controle_fluxo.locator("select[id='id_nextpagedefault']").input_value() != '0':
                    cont_fluxo_correta_padrao = 'Normal, seguir percurso da lição'
                    cont_fluxo_correta = id_controle_fluxo.locator("select[id='id_nextpagedefault'] > option[selected]").inner_text()
                    #id_controle_fluxo.locator("select[id='id_nextpagedefault']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Controle de fluxo 'Ação após uma resposta correta' é '{cont_fluxo_correta}' deve ser atualizado para '{cont_fluxo_correta_padrao}' atendendo ao Padrão."]
                
                #CONTROLE DE FLUXO - NÚMERO DE PÁGINAS A SEREM MOSTRADAS - Padrão (uma)
                if id_controle_fluxo.locator("select[id='id_maxpages']").input_value() != '1':
                    cont_fluxo_pag_padrao = 'Uma'
                    cont_fluxo_pag = id_controle_fluxo.locator("select[id='id_maxpages'] > option[selected]").inner_text()
                    #id_controle_fluxo.locator("select[id='id_maxpages']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Controle de fluxo 'Número de páginas a serem mostradas' é '{cont_fluxo_pag}' deve ser atualizado para '{cont_fluxo_pag_padrao}' atendendo ao Padrão."]
                
                #NOTA - LIÇÃO PARA PRATICAR - Padrão (não)
                id_nota = page.locator('fieldset[id="id_modstandardgrade"]')
                #time.sleep(0.5)

                expandir_nota = id_nota.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                if expandir_nota.count() != 0:
                    page.locator('a:has-text("Expandir tudo")').click()

                mostrar_mais_nota = id_nota.locator('xpath=//a[@class="moreless-toggler" and @role="button"]')
                if mostrar_mais_nota.get_attribute('aria-expanded') == 'false':
                    if expandir_nota.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                    mostrar_mais_nota.click()

                """ #id_nota.locator('a:has-text("Mostrar mais ...")').click()
                if id_nota.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                    id_nota.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                    time.sleep(0.5) """

                #if id_nota.locator("select[id='id_practice']").input_value() != '0':
                #    nota_praticar_padrao = 'Não'
                #    nota_praticar = id_nota.locator("select[id='id_practice'] > option[selected]").inner_text()
                    #id_nota.locator("select[id='id_practice']").select_option('0')
                #    results+=  [f"{nome_atividade} ==> Nota 'Lição para praticar' é '{nota_praticar}' deve ser atualizado para '{nota_praticar_padrao}' atendendo ao Padrão."]
                
                #NOTA - PONTUAÇÃO PERSONALIZADA - Padrão (sim)
                if id_nota.locator("select[id='id_custom']").input_value() != '1':
                    nota_personalizada_padrao = 'Sim'
                    nota_personalizada = id_nota.locator("select[id='id_custom'] > option[selected]").inner_text()
                    #id_nota.locator("select[id='id_custom']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Nota 'Pontuação personalizada' é '{nota_personalizada}' deve ser atualizado para '{nota_personalizada_padrao}' atendendo ao Padrão."]
                
                #NOTA - PERMITE-SE RETOMAR A LIÇÃO - Padrão (não)
                if id_nota.locator("select[id='id_retake']").input_value() != '0':
                    nota_retomar_padrao = 'Não'
                    nota_retomar = id_nota.locator("select[id='id_retake'] > option[selected]").inner_text()
                    #id_nota.locator("select[id='id_retake']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Nota 'Permite-se retomar a lição' é '{nota_retomar}' deve ser atualizado para '{nota_retomar_padrao}' atendendo ao Padrão."]
                
                #NOTA - NÚMERO MÍNIMO DE QUESTÕES - Padrão (zero)
                if id_nota.locator("select[id='id_minquestions']").input_value() != '0':
                    nota_questoes_padrao = 'Zero'
                    nota_questoes = id_nota.locator("select[id='id_minquestions'] > option[selected]").inner_text()
                    #id_nota.locator("select[id='id_minquestions']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Nota 'Número mínimo de questões' é '{nota_questoes}' deve ser atualizado para '{nota_questoes_padrao}' atendendo ao Padrão."]
                
                #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                if (id_conf_comuns_modulos.locator("select[id='id_visible']").input_value()) != '1':
                    conf_com_mod_disp_padrao = 'Mostrar na página do curso'
                    conf_com_mod_disp = id_conf_comuns_modulos.locator("select[id='id_visible'] > option[selected]").inner_text()
                    #id_conf_comuns_modulos.locator("select[id='id_visible']").select_option('1')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod_disp}' deve ser atualizado para '{conf_com_mod_disp_padrao}' atendendo ao Padrão."]
                
                #CONFIGURAÇÕES COMUNS DE MÓDULOS - MODALIDADE GRUPO - Padrão (nenhum grupo)
                if (id_conf_comuns_modulos.locator("select[id='id_groupmode']").input_value()) != '0':
                    conf_com_mod_grupo_padrao = 'Nenhum grupo'
                    conf_com_mod_grupo = id_conf_comuns_modulos.locator("select[id='id_groupmode'] > option[selected]").inner_text()
                    #id_conf_comuns_modulos.locator("select[id='id_groupmode']").select_option('0')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Modalidade grupo' é '{conf_com_mod_grupo}' deve ser atualizado para '{conf_com_mod_grupo_padrao}' atendendo ao Padrão."]
                
                #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
                id_conclusao_atividade = page.locator('fieldset[id="id_activitycompletionheader"]')
                try:
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_conc_padrao = 'Mostrar atividade como concluída quando as condições forem sastisfeitas'
                        conc_atv_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator("select[id='id_completion']").select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_conc}' deve ser atualizado para '{conc_atv_conc_padrao}' atendendo ao Padrão."]
                
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - EXIBIR ALCANÇAR O FIM - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionendreached']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionendreached']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Exibir alcançar o fim' deve ser marcado atendendo ao Padrão."]

                    #CONCLUSÃO DE ATIVIDADE - EXIBIR TEMPO GASTO - Padrão (desmarcado)
                    if id_conclusao_atividade.locator("input[id='id_completiontimespentenabled']").is_checked():
                        #id_conclusao_atividade.locator("input[id='id_completiontimespentenabled']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Exibir tempo gasto' deve ser desmarcado atendendo ao Padrão."]

                except:
                    #DESBLOQUEAR OPÇÃO DE CONCLUSÃO
                    id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click()
                    time.sleep(1)

                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator("select[id='id_completion']").input_value()) != '2':
                        conc_atv_conc_padrao = 'Mostrar atividade como concluída quando as condições forem sastisfeitas'
                        conc_atv_conc = id_conclusao_atividade.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao_atividade.locator("select[id='id_completion']").select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_conc}' deve ser atualizado para '{conc_atv_conc_padrao}' atendendo ao Padrão."]
                
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionview']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionview']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser marcado atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - EXIBIR ALCANÇAR O FIM - Padrão (marcado)
                    if id_conclusao_atividade.locator("input[id='id_completionendreached']").is_checked() == False:
                        #id_conclusao_atividade.locator("input[id='id_completionendreached']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Exibir alcançar o fim' deve ser marcado atendendo ao Padrão."]

                    #CONCLUSÃO DE ATIVIDADE - EXIBIR TEMPO GASTO - Padrão (desmarcado)
                    if id_conclusao_atividade.locator("input[id='id_completiontimespentenabled']").is_checked():
                        #id_conclusao_atividade.locator("input[id='id_completiontimespentenabled']").click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Exibir tempo gasto' deve ser desmarcado atendendo ao Padrão."]

                #CONCLUSÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM - Padrão (desmarcado)
                if id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").is_checked():
                    #id_conclusao_atividade.locator("input[id='id_completionexpected_enabled']").clicl()
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
            print('Lição concluída')
        except Exception as err:
            results+=  [f"Não foi possível validar Lição. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
