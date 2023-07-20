import time
from moodlebot.plugin import CheckPlugin

class CheckQuestionarioAvaliativo(CheckPlugin):
    """Validando as configurações do Questionário Avaliativo."""
    def handle(self, page, context):
        results = []
        print("Questionário")
        #return results
        
        try:
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity quiz modtype_quiz "]')
            time.sleep(0.5)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity quiz modtype_quiz "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper quiz modtype_quiz hasinfo dropready draggable"]')
            
            #VERIFICAR SE O FORMATO DO CURSO É DO TIPO TILES - SE SIM, ENTRAR ABAIXO E MARCAR COMO VERDADEIRO PQ NA HORA DE SAIR DA ATIVIDADE ELE DEVE VOLTAR PARA O HOME
            formato_tiles = page.locator('xpath=//ul[@class="tiles"]')
            #print(formato_tiles.count())
            tiles = False
            if formato_tiles.count() != 0:
                tiles = True
            
            total = cont.count()
            for x in range(total):
                time.sleep(0.5)
                print(f'Questionário {x+1}/{total}')
                atividade = cont.nth(x).locator('xpath=//div[@class="activity-actions align-self-start"]')
                atividade.click()
                time.sleep(0.5)
                editar_configuracao = atividade.locator('xpath=//a[@class="dropdown-item editing_update menu-action cm-edit-action" and @data-action="update"]')
                time.sleep(0.5)
                editar_configuracao.click()
                time.sleep(1)  

                #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
                #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
                print(f'Questionário {x+1}/{total} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                if exp_all.count() != 0:
                    if exp_all.get_attribute('aria-expanded') == 'false':
                        exp_all.click()
                                
                #GERAL - NOME
                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator('input[id="id_name"]').input_value()
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
                
                #DURAÇÃO - ENCERRAR QUESTIONÁRIO - Padrão (desmarcado)
                id_duracao = page.locator('fieldset[id="id_timing"]')
                time.sleep(0.5)
                if id_duracao.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                if id_duracao.locator('input[id="id_timeclose_enabled"]').is_checked():
                    #id_duracao.locator('input[id="id_timeclose_enabled"]').click()
                    results+= [f"{nome_atividade} ==> Duração 'Encerrar questionário' deve ser desmarcado atendendo ao Padrão."]
                
                #DURAÇÃO - ABRIR QUESTIONÁRIO - Padrão (desmarcado)
                if id_duracao.locator('input[id="id_timeopen_enabled"]').is_checked():
                    #id_duracao.locator('input[id="id_timeopen_enabled"]').click()
                    results+= [f"{nome_atividade} ==> Duração 'Abrir questionário' deve ser desmarcado atendendo ao Padrão."]
                
                #DURAÇÃO - LIMITE DE TEMPO - Padrão (desmarcado)
                if id_duracao.locator('input[id="id_timelimit_enabled"]').is_checked():
                    #id_duracao.locator('input[id="id_timelimit_enabled"]').clicK()
                    results+= [f"{nome_atividade} ==> Duração 'Limite de tempo' deve ser desmarcado atendendo ao Padrão."]

                #DURAÇÃO - QUANDO O TEMPO EXPIRAR - Padrão (as tentativas abertas são enviadas automaticamente)
                if (id_duracao.locator('select[id="id_overduehandling"]').input_value()) != 'autosubmit':
                    dur_expirar_padrao = 'As tentativas abertas são enviadas automaticamente'
                    dur_expirar = id_duracao.locator('select[id="id_overduehandling"] > option[selected]').inner_text()
                    #id_duracao.locator('select[id="id_overduehandling"]').select_option('autosubmit')
                    results+=  [f"{nome_atividade} ==> Duração 'Quando o tempo expirar' é '{dur_expirar}' e deve ser atualizado para '{dur_expirar_padrao}' atendendo ao Padrão."]
                
                #NOTA - CATEGORIA DE NOTAS - Padrão (não categorizado)
                id_nota = page.locator('fieldset[id="id_modstandardgrade"]')
                time.sleep(0.5)
                if id_nota.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    if exp_all.count() != 0:
                        exp_all.click()
                        time.sleep(0.5)

                    
                nota_categoria = id_nota.locator('select[id="id_gradecat"]').inner_html()
                texto = nota_categoria.split("</option>")
                #print(texto)
                for t in texto:
                    texto_sem_espaco = t.lstrip()
                    #print(f"Sem espaço: {texto_sem_espaco}")
                    tam_total = len(texto_sem_espaco)
                    #print(tam_total)
                    inicio = tam_total - 16 # 16 é o tamanho do texto 'Não categorizado'
                    #print(texto_sem_espaco[inicio:tam_total])
                    if texto_sem_espaco[inicio:tam_total] == 'Não categorizado':
                        novo_tamanho = inicio - 14
                        #print(novo_tamanho)
                        valor = texto_sem_espaco[15:novo_tamanho]
                        #print(f'Valor: {valor}')
                        categoria = page.locator('select[id="id_gradecat"]').input_value()
                        #print(categoria)
                        if valor != categoria:
                            results+=  [f"{nome_atividade} ==> Nota 'Categoria de notas' está fora do Padrão."]

                #NOTA - NOTA PARA APROVAÇÃO - Padrão (zero)
                if (id_nota.locator('input[id="id_gradepass"]').input_value()) != '0,00':
                    nota_aprov_padrao = 'Zero'
                    nota_aprov = id_nota.locator('input[id="id_gradepass"]').input_value()
                    #id_nota.locator('input[id="id_gradepass"]').fill('0,00')
                    results+=  [f"{nome_atividade} ==> Nota 'Nota para aprovação' é '{nota_aprov}' e deve ser atualizado para '{nota_aprov_padrao}' atendendo ao Padrão."]

                #NOTA - TENTATIVAS PERMITIDAS - Padrão (1)
                if (id_nota.locator('select[id="id_attempts"]').input_value()) != '1':
                    #results+=  [f"{nome_atividade} ==> Nota 'Tentativas permitidas' está fora do Padrão."]
                    
                    #MÉTODO DE AVALIAÇÃO - Padrão (Nota mais alta)
                    if (id_nota.locator('select[id="id_grademethod"]').input_value()) != '1':
                        nota_met_aval_padrao = 'Nota mais alta'
                        nota_met_aval = id_nota.locator('select[id="id_grademethod"] > option[selected]').inner_text()
                        #id_nota.locator('input[id="id_grademethod"]').select_option('1')
                        results+=  [f"{nome_atividade} ==> Nota 'Método de avaliação' é '{nota_met_aval}' e deve ser atualizado para '{nota_met_aval_padrao}' atendendo ao Padrão."]

                #LAYOUT - NOVA PÁGINA - Padrão (cada 5 questões) - é importante sempre organizar em 5. Função não gera informação
                id_layout = page.locator('fieldset[id="id_layouthdr"]')
                time.sleep(0.5)
                #id_layout.locator('a:has-text("Mostrar mais ...")').click()
                expandir_layout = id_layout.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                if id_layout.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                    if expandir_layout.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                    id_layout.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                    time.sleep(0.5)
                #time.sleep(0.5)
                    
                layout_nova_pagina = id_layout.locator('select[id="id_questionsperpage"]')
                if layout_nova_pagina.input_value() != "5":
                    layout_nova_pagina.select_option(value="5")
                    #results+=  [f"{nome_atividade} ==> Layout 'Nova página' está fora do Padrão."]
                
                #LAYOUT - REPAGINAR AGORA - Padrão (marcado) - é importante sempre repaginar. Função não gera informação
                layout_repaginar = id_layout.locator('input[id="id_repaginatenow"]')
                if layout_repaginar.is_checked() == False:
                    layout_repaginar.click()
                    time.sleep(0.5)
                    #results+=  [f"{nome_atividade} ==> Layout 'Repaginar agora' está fora do Padrão."]
                
                #LAYOUT - MÉTODO DE NAVEGAÇÃO - Padrão (Livre)
                if (id_layout.locator('select[id="id_navmethod"]').input_value()) != 'free':
                    layout_nav_padrao = 'Livre'
                    layout_nav = id_layout.locator('select[id="id_navmethod"] > option[selected]').inner_text()
                    #id_layout.locator('input[id="id_navmethod"]').select_option('free')
                    results+=  [f"{nome_atividade} ==> Nota 'Método de avaliação' é '{layout_nav}' e deve ser atualizado para '{layout_nav_padrao}' atendendo ao Padrão."]
                
                #COMPORTAMENTO DA QUESTÃO - MISTURAR ENTRE AS QUESTÕES - Padrão (Não)
                id_comportamento_questao = page.locator('fieldset[id="id_interactionhdr"]')
                time.sleep(0.5)
                #id_comportamento_questao.locator('a:has-text("Mostrar mais ...")').click()
                expandir_comportamento = id_comportamento_questao.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                if id_comportamento_questao.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                    if expandir_comportamento.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                    id_comportamento_questao.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                    time.sleep(0.5)

                if (id_comportamento_questao.locator('select[id="id_shuffleanswers"]').input_value()) != '0':
                    comp_ques_mist_padrao = 'Não'
                    comp_ques_mist = id_comportamento_questao.locator('select[id="id_shuffleanswers"] > option[selected]').inner_text()
                    #id_comportamento_questao.locator('select[id="id_shuffleanswers"]').select_option('0')
                    results+=  [f"{nome_atividade} ==> Comportamento da questão 'Misturar entre as questões' é '{comp_ques_mist}' e deve ser atualizado para '{comp_ques_mist_padrao}' atendendo ao Padrão."]
                            
                #COMPORTAMENTO DA QUESTÃO - COMO AS QUESTÕES SE COMPORTAM - Padrão (Feedback adiado)
                if (id_comportamento_questao.locator('select[id="id_preferredbehaviour"]').input_value()) != 'deferredfeedback':
                    comp_ques_comportam_padrao = 'Feedback adiado'
                    comp_ques_comportam = id_comportamento_questao.locator('select[id="id_preferredbehaviour"] > option[selected]').inner_text()
                    #id_comportamento_questao.locator('select[id="id_preferredbehaviour"]').select_option('deferredfeedback')
                    results+=  [f"{nome_atividade} ==> Comportamento da questão 'Como as questões se comportam' é '{comp_ques_comportam}' e deve ser atualizado para '{comp_ques_comportam_padrao}' atendendo ao Padrão."]
                    
                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - A TENTATIVA - Padrão (marcado)
                id_opcoes_revisao = page.locator('fieldset[id="id_reviewoptionshdr"]')
                if id_opcoes_revisao.locator('input[id="id_attemptimmediately"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_attemptimmediately"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - A tentativa' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - ACERTOS/ERROS - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_correctnessimmediately"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_correctnessimmediately"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Acertos/Erros' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - NOTAS - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_marksimmediately"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_marksimmediately"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Notas' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - FEEDBACK ESPECÍFICO - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_specificfeedbackimmediately"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_specificfeedbackimmediately"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Feedback específico' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - FEEDBACK GERAL - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_generalfeedbackimmediately"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_generalfeedbackimmediately"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Feedback geral' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - RESPOSTA CORRETA - Padrão (marcado para 1 tentativa e desmarcado se houver mais tentativas)
                if (id_nota.locator('select[id="id_attempts"]').input_value()) == '1':
                    if id_opcoes_revisao.locator('input[id="id_rightanswerimmediately"]').is_checked() == False:
                        #id_opcoes_revisao.locator('input[id="id_rightanswerimmediately"]').click()
                        results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Resposta correta' deve ser marcado atendendo ao Padrão."]
                else:
                    if id_opcoes_revisao.locator('input[id="id_rightanswerimmediately"]').is_checked():
                        #id_opcoes_revisao.locator('input[id="id_rightanswerimmediately"]').click()
                        results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Resposta correta' deve ser desmarcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - APÓS A TENTATIVA - FEEDBACK FINAL - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_overallfeedbackimmediately"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_overallfeedbackimmediately"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Após a tentativa - Feedback final' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - A TENTATIVA - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_attemptopen"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_attemptopen"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - A tentativa' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - ACERTOS/ERROS - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_correctnessopen"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_correctnessopen"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Acertos/Erros' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - NOTAS - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_marksopen"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_marksopen"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Notas' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - FEEDBACK ESPECÍFICO - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_specificfeedbackopen"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_specificfeedbackopen"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Feedback específico' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - FEEDBACK GERAL - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_generalfeedbackopen"]') == False:
                    #id_opcoes_revisao.locator('input[id="id_generalfeedbackopen"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Feedback geral' deve ser marcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - RESPOSTA CORRETA - Padrão (marcado para 1 tentativa e desmarcado se houver mais tentativas)
                if (id_nota.locator('select[id="id_attempts"]').input_value()) == '1':
                    if id_opcoes_revisao.locator('input[id="id_rightansweropen"]').is_checked() == False:
                        #id_opcoes_revisao.locator('input[id="id_rightansweropen"]').click()
                        results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Resposta correta' deve ser marcado atendendo ao Padrão."]
                else:
                    if id_opcoes_revisao.locator('input[id="id_rightansweropen"]').is_checked():
                        #id_opcoes_revisao.locator('input[id="id_rightansweropen"]').click()
                        results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Resposta correta' deve ser desmarcado atendendo ao Padrão."]

                #OPÇÕES DE REVISÃO - MAIS TARDE,... - FEEDBACK FINAL - Padrão (marcado)
                if id_opcoes_revisao.locator('input[id="id_overallfeedbackopen"]').is_checked() == False:
                    #id_opcoes_revisao.locator('input[id="id_overallfeedbackopen"]').click()
                    results+=  [f"{nome_atividade} ==> Opções de revisão 'Mais tarde,... - Feedback final' deve ser marcado atendendo ao Padrão."]

                #APARÊNCIA - MOSTRAR A FOTOGRAFIA DO USUÁRIO - Padrão (Nenhuma imagem)
                id_aparencia = page.locator('fieldset[id="id_display"]')
                time.sleep(0.5)
                #id_aparencia.locator('a:has-text("Mostrar mais ...")').click()
                expandir_aparencia = id_aparencia.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]')
                if id_aparencia.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                    if expandir_aparencia.count() != 0:
                        page.locator('a:has-text("Expandir tudo")').click()
                    id_aparencia.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                    time.sleep(0.5)

                if (id_aparencia.locator('select[id="id_showuserpicture"]').input_value()) != '0':
                    apa_foto_padrao = 'Nenhuma imagem'
                    apa_foto = id_aparencia.locator('select[id="id_showuserpicture"] > option[selected]').inner_text()
                    #id_aparencia.locator('select[id="id_showuserpicture"]').select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Mostrar a fotografia do usuário' é '{apa_foto}' e deve ser atualizado para '{apa_foto_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - CASAS DECIMAIS NAS NOTAS - Padrão (2)
                if (id_aparencia.locator('select[id="id_decimalpoints"]').input_value()) != '2':
                    apa_casas_padrao = '2'
                    apa_casas = id_aparencia.locator('select[id="id_decimalpoints"] > option[selected]').inner_text()
                    #id_aparencia.locator('select[id="id_decimalpoints"]').select_option('2')
                    results+=  [f"{nome_atividade} ==> Aparência 'Casas decimais nas notas' é '{apa_casas}' e deve ser atualizado para '{apa_casas_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - CASAS DECIMAIS NAS NOTAS DA QUESTÃO - Padrão (O mesmo que para as avaliações em geral)
                if (id_aparencia.locator('select[id="id_questiondecimalpoints"]').input_value()) != '-1':
                    apa_casas_questao_padrao = 'O mesmo que para as avaliações em geral'
                    apa_casas_questao = id_aparencia.locator('select[id="id_questiondecimalpoints"] > option[selected]').inner_text()
                    #id_aparencia.locator('select[id="id_questiondecimalpoints"]').select_option('-1')
                    results+=  [f"{nome_atividade} ==> Aparência 'Casas decimais nas notas da questão' é '{apa_casas_questao}' e deve ser atualizado para '{apa_casas_questao_padrao}' atendendo ao Padrão."]

                #APARÊNCIA - MOSTRAR BLOCOS DURANTE AS TENTATIVAS DO QUESTIONÁRIO - Padrão (Não)
                if (id_aparencia.locator('select[id="id_showblocks"]').input_value()) != '0':
                    apa_blocos_padrao = 'Não'
                    apa_blocos = id_aparencia.locator('select[id="id_showblocks"] > option[selected]').inner_text()
                    #id_aparencia.locator('select[id="id_showblocks"]').select_option('0')
                    results+=  [f"{nome_atividade} ==> Aparência 'Mostrar blocos durante as tentativas do questionário' é '{apa_blocos}' e deve ser atualizado para '{apa_blocos_padrao}' atendendo ao Padrão."]

                #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                if (id_conf_comuns_modulos.locator('select[id="id_visible"]').input_value()) != '1':
                    conf_com_mod_padrao = 'Mostrar na página do curso'
                    conf_com_mod = id_conf_comuns_modulos.locator('select[id="id_visible"] > option[selected]').inner_text()
                    #id_conf_comuns_modulos.locator('select[id="id_visible"]').select_option('1')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod}' e deve ser atualizado para '{conf_com_mod_padrao}' atendendo ao Padrão."]

                #CONFIGURAÇÕES COMUNS DE MÓDULOS - MODALIDADE GRUPO - Padrão (nenhum grupo)
                if (id_conf_comuns_modulos.locator('select[id="id_groupmode"]').input_value()) != '0':
                    conf_com_mod_grupo_padrao = 'Nenhum grupo'
                    conf_com_mod_grupo = id_conf_comuns_modulos.locator('select[id="id_groupmode"] > option[selected]').inner_text()
                    #id_conf_comuns_modulos.locator('select[id="id_groupmode"]').select_option('0')
                    results+=  [f"{nome_atividade} ==> Configurações comuns de módulos 'Modalidade grupo' é '{conf_com_mod_grupo}' e deve ser atualizado para '{conf_com_mod_grupo_padrao}' atendendo ao Padrão."]
                
                #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
                id_conclusao_atividade = page.locator('fieldset[id="id_activitycompletionheader"]')
                try:
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator('select[id="id_completion"]').input_value()) != '2':
                        conc_atv_conc_padrao = 'Mostrar atividade como concluída quando as condições forem sastisfeitas'
                        conc_atv_conc = id_conclusao_atividade.locator('select[id="id_completion"] > option[selected]').inner_text()
                        #id_conclusao_atividade.locator('select[id="id_completion"]').select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_conc}' e deve ser atualizado para '{conc_atv_conc_padrao}' atendendo ao Padrão."]
                
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (desmarcado)
                    if id_conclusao_atividade.locator('input[id="id_completionview"]').is_checked():
                        #id_conclusao_atividade.locator('input[id="id_completionview"]').click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser desmarcado atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - REQUER NOTA - Padrão (marcado)
                    if id_conclusao_atividade.locator('input[id="id_completionusegrade"]').is_checked() == False:
                        #id_conclusao_atividade.locator('input[id="id_completionusegrade"]').click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer nota' deve ser marcado atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - EXIGIR NOTA DE APROVAÇÃO - Padrão (desmarcado)
                    if id_conclusao_atividade.locator('input[id="id_completionpassgrade"]').is_checked():
                        #id_conclusao_atividade.locator('input[id="id_completionpass"]').click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Exigir nota de aprovação' deve ser desmarcado atendendo ao Padrão."]

                except:
                    #DESBLOQUEAR OPÇÃO DE CONCLUSÃO
                    id_conclusao_atividade.locator('xpath=//input[@id="id_unlockcompletion"]').click()
                    time.sleep(1)
                    
                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (Mostrar atividade como concluída quando as condições forem sastisfeitas)
                    if (id_conclusao_atividade.locator('select[id="id_completion"]').input_value()) != '2':
                        conc_atv_conc_padrao = 'Mostrar atividade como concluída quando as condições forem sastisfeitas'
                        conc_atv_conc = id_conclusao_atividade.locator('select[id="id_completion"] > option[selected]').inner_text()
                        #id_conclusao_atividade.locator('select[id="id_completion"]').select_option('2')
                        results+=  [f"{nome_atividade} ==> Conclusão de atividade 'Acompanhamento de conclusão' é '{conc_atv_conc}' e deve ser atualizado para '{conc_atv_conc_padrao}' atendendo ao Padrão."]
                
                    #CONCLUSÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO - Padrão (desmarcado)
                    if id_conclusao_atividade.locator('input[id="id_completionview"]').is_checked():
                        #id_conclusao_atividade.locator('input[id="id_completionview"]').click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer visualização' deve ser desmarcado atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - REQUER NOTA - Padrão (marcado)
                    if id_conclusao_atividade.locator('input[id="id_completionusegrade"]').is_checked() == False:
                        #id_conclusao_atividade.locator('input[id="id_completionusegrade"]').click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Requer nota' deve ser marcado atendendo ao Padrão."]
                    
                    #CONCLUSÃO DE ATIVIDADE - EXIGIR NOTA DE APROVAÇÃO - Padrão (desmarcado)
                    if id_conclusao_atividade.locator('input[id="id_completionpassgrade"]').is_checked():
                        #id_conclusao_atividade.locator('input[id="id_completionpass"]').click()
                        results+= [f"{nome_atividade} ==> Conclusão de atividade 'Exigir nota de aprovação' deve ser desmarcado atendendo ao Padrão."]

                #CONCLUSÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM - Padrão (desmarcado)
                if id_conclusao_atividade.locator('input[id="id_completionexpected_enabled"]').is_checked():
                    #id_conclusao_atividade.locator('input[id="id_completionexpected_enabled"]').click()
                    results+= [f"{nome_atividade} ==> Conclusão de atividade 'Conclusão esperada em' deve ser desmarcado atendendo ao Padrão."]
            

                #SE O FORMATO FOR TILES, RETORNAR PARA A PÁGINA INICIAL
                if tiles:
                    #RETORNAR PARA A PÁGINA INICIAL
                    page.goto(context["course_url"], wait_until="load")
                    time.sleep(0.5)
                else:
                    #SALVAR E VOLTAR AO CURSO    
                    page.locator('input[id="id_submitbutton2"]').click()
                    time.sleep(0.5)
            print('Questionário concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Questionário. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
