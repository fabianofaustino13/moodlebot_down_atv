import re
import time
from moodlebot.plugin import CheckPlugin

class CheckQuestoesQuestionario(CheckPlugin):
    """Validando as configurações das Questões do Questionário."""
    def handle(self, page, context):
        results = []
        print("Questões do Questionário")
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
            
            total = cont.count()
            for x in range(total):
                #time.sleep(0.5) #SE NÃO TIVER, IRÁ APRESENTAR ERRO POR SER MUITO RÁPIDO
                #nome_atividade = cont.nth(x).locator('xpath=//span[@class="inplaceeditable inplaceeditable-text"]').get_attribute('data-value')
                #print(f'Nome do Questionário: {nome_atividade}')
                #cont.nth(x).locator('xpath=//span[@class="instancename"]').click()
                #time.sleep(0.5)

                time.sleep(0.5)
                print(f'Questões do Questionário {x+1}/{total}')
                cont.locator('xpath=//span[@class="inplaceeditable inplaceeditable-text"]').nth(x).click()
                time.sleep(0.5)
                navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
                time.sleep(0.5)
                navegacao_secundaria.locator('xpath=//li[@class="nav-item" and @data-key="modedit"]').click()
                time.sleep(1)
                #GERAL - NOME
                id_geral = page.locator('fieldset[id="id_general"]')
                nome_atividade = id_geral.locator('input[id="id_name"]').input_value()
                print("Nome da Atividade: %s" % nome_atividade)
                #GERAL - DESCRIÇÃO
                questionario_descricao = id_geral.locator('div[id="id_introeditoreditable"]').inner_text()
                print(questionario_descricao)
                
                #NOTA - TENTATIVAS PERMITIDAS
                id_nota = page.locator('fieldset[id="id_modstandardgrade"]')
                tentativa_permitida = id_nota.locator('select[id="id_attempts"]').input_value()
                print(tentativa_permitida)

                fixacao = True #Iniciando como verdadeiro, ou seja, existe o termo fixação na descrição da atividade
                tentativa_descricao = True
                metodo_avaliacao = True
                nome_questionario = True

                #questionario_descricao = page.locator('xpath=//div[@id="intro"]').inner_text()
                print('#######################')
                #print(questionario_descricao)
                termo_fixacao = questionario_descricao.find('fixação')
                #print(termo_fixacao)
                if termo_fixacao == -1: #and pontos != -1: #Não existe o termo procurado
                    fixacao = False
        
                termo_tentativa_descricao = questionario_descricao.find('Você terá apenas uma tentativa.')
                print(termo_tentativa_descricao)
                if termo_tentativa_descricao != -1: #Existe o termo procurado
                    tentativa_descricao = False

                questionario_descricao_metodo = page.locator('xpath=//div[@role="main"]').inner_text()
                termo_metodo_avaliacao = questionario_descricao_metodo.find('Método de avaliação')
                #print(termo_metodo_avaliacao)
                if termo_metodo_avaliacao == -1: #Não existe o termo procurado
                    #print('Na descrição desta atividade, NÃO Existe o termo: Método de avaliação')
                    #results+= [f"Este questionário é de Fixação e o número de tentativas está limitada a 1."]
                    metodo_avaliacao = False
            
                termo_nome_questionario = nome_atividade.find('fixação')
                #print(nome_questionario)
                if termo_nome_questionario == -1:
                    #print('No nome desta atividade, NÃO Existe o termo: fixação')
                    nome_questionario = False

                navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
                time.sleep(0.5)
                navegacao_secundaria.locator('xpath=//li[@class="nav-item" and @data-key="mod_quiz_edit"]').click()
                time.sleep(1)
                try:
                    #NOTA MÁXIMA
                    nota_maxima = page.locator('input[id="inputmaxgrade"]').input_value()
                    if nota_maxima == '0,00':
                        print(f'Nota máxima do Questionário: {nota_maxima}')
                        if nome_questionario == False:
                            results+= [f"Este questionário, {nome_atividade}, é de Fixação e em seu nome deveria constar a informação de que é uma atividade de fixação."]
                    
                        if fixacao == False:
                            results+= [f"Este questionário, {nome_atividade}, é de Fixação e não existe a informação na descrição da atividade."]

                        if tentativa_descricao == False:
                            if metodo_avaliacao:
                                results+= [f"Este questionário, {nome_atividade}, é de Fixação e está configurado para mais de 1 tentativa mas na descrição consta outra informação."]

                        if metodo_avaliacao == False: 
                            if tentativa_permitida == "1":
                                results+= [f"Este questionário, {nome_atividade}, é de Fixação e o número de tentativas está limitada a 1."]

                    #EDITANDO QUESTIONÁRIO - MISTURAR AS QUESTÕES? - Padrão (desmarcado)
                    if page.locator('input[data-action="shuffle_questions"]').is_checked():
                        #page.locator('input[data-action="shuffle_questions"]').click()
                        results+= [f"{nome_atividade} ==> Editando o questionário 'Misturar as opções?' deve ser desmarcado atendendo ao Padrão."]
            
                    cont_total_questoes = page.locator('xpath=//span[@class="slotnumber"]')
                    print(f'Total de questões do questionário: {cont_total_questoes.count()}')
                    cod_categoria = 0
                    time.sleep(0.5)
                    for w in range(cont_total_questoes.count()):
                        time.sleep(0.5)
                        t_questao = page.locator('xpath=//div[@class="activityinstance"]').nth(w)
                        tipo_questao = t_questao.locator('xpath=//img[@role="presentation"]')
                        #print(tipo_questao.get_attribute('title'))
                        tipo = tipo_questao.get_attribute('title')
                        time.sleep(0.5)                
                        if tipo_questao.get_attribute('title') == "Múltipla escolha":
                            time.sleep(0.5)
                            tipo_questao.click()
                            time.sleep(1)
                            nome_questao = page.locator('input[id="id_name"]').input_value()
                            print(f'{tipo} - {nome_questao}')

                            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                            time.sleep(0.5)
                            if exp_all.get_attribute('aria-expanded') == 'false':
                                exp_all.click()

                            time.sleep(0.5)
                            #GERAL - UMA OU MÚLTIPLAS RESPOSTAS - Padrão (apenas uma resposta)
                            id_geral_respostas_me = page.locator('fieldset[id="id_generalheader"]')
                        
                            #GERAL - MISTURAR AS OPÇÕES? - Padrão (desmarcado)
                            if id_geral_respostas_me.locator('input[id="id_shuffleanswers"]').is_checked():
                                #id_geral_respostas_me.locator('input[id="id_shuffleanswers"]').click()
                                results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Geral 'Misturar as opções?' deve ser desmarcado atendendo ao Padrão."]
                            
                            #SALVAR
                            page.locator('input[id="id_cancel"]').click()
                            time.sleep(0.5)
                        
                        elif tipo_questao.get_attribute('title') == "Verdadeiro/Falso":
                            time.sleep(0.5)
                            tipo_questao.click()
                            time.sleep(1)
                            nome_questao = page.locator('input[id="id_name"]').input_value()
                            print(f'{tipo} - {nome_questao}')

                            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                            time.sleep(0.5)
                            if exp_all.get_attribute('aria-expanded') == 'false':
                                exp_all.click()

                            time.sleep(0.5)
                            #GERAL - FEEDBACK VERDADEIRO - Padrão (feedback)
                            id_geral_respostas_vf = page.locator('fieldset[id="id_generalheader"]')
                            geral_feedback_verdadeiro = id_geral_respostas_vf.locator('div[id="id_feedbacktrueeditable"]')
                            if geral_feedback_verdadeiro.inner_html() == '':
                                results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Geral 'Feedback verdadeiro' está diferente do Padrão."]
                            
                            #GERAL - FEEDBACK FALSO - Padrão (feedback)
                            geral_feedback_falso = id_geral_respostas_vf.locator('div[id="id_feedbackfalseeditable"]')
                            if geral_feedback_falso.inner_html() == '':
                                results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Geral 'Feedback falso' está diferente do Padrão."]
                            
                            #SALVAR
                            page.locator('input[id="id_cancel"]').click()
                            time.sleep(0.5)

                        elif tipo_questao.get_attribute('title') == "Selecionar as palavras que faltam":
                            time.sleep(0.5)
                            tipo_questao.click()
                            time.sleep(1)
                            nome_questao = page.locator('input[id="id_name"]').input_value()
                            print(f'{tipo} - {nome_questao}')

                            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                            time.sleep(0.5)
                            if exp_all.get_attribute('aria-expanded') == 'false':
                                exp_all.click()

                            time.sleep(0.5)
                            #OPÇÕES - EMBARALHAR - Padrão (marcado)
                            id_opcoes_se = page.locator('fieldset[id="id_choicehdr"]')
                            if id_opcoes_se.locator('input[id="id_shuffleanswers"]').is_checked() == False:
                                #id_opcoes_se.locator('input[id="id_shuffleanswers"]').click()
                                results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Opções 'Embaralhar' deve ser marcado atendendo ao Padrão."]
                        
                            #SALVAR
                            page.locator('input[id="id_cancel"]').click()
                            time.sleep(0.5)
                        
                        elif tipo_questao.get_attribute('title') == "Arrastar e soltar sobre o texto":
                            time.sleep(0.5)
                            tipo_questao.click()
                            time.sleep(1)
                            nome_questao = page.locator('input[id="id_name"]').input_value()
                            print(f'{tipo} - {nome_questao}')

                            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                            time.sleep(0.5)
                            if exp_all.get_attribute('aria-expanded') == 'false':
                                exp_all.click()

                            time.sleep(0.5)
                            #OPÇÕES - EMBARALHAR - Padrão (desmarcado)
                            id_opcoes_ar = page.locator('fieldset[id="id_choicehdr"]')
                            if id_opcoes_ar.locator('input[id="id_shuffleanswers"]').is_checked():
                                #id_opcoes_ar.locator('input[id="id_shuffleanswers"]').click()
                                results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Opções 'Embaralhar' deve ser desmarcado atendendo ao Padrão."]

                            #SALVAR
                            page.locator('input[id="id_cancel"]').click()
                            time.sleep(0.5)

                        elif tipo_questao.get_attribute('title') == "Associação":
                            time.sleep(0.5)
                            tipo_questao.click()
                            time.sleep(1)
                            nome_questao = page.locator('input[id="id_name"]').input_value()
                            print(f'{tipo} - {nome_questao}')

                            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                            expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                            time.sleep(0.5)
                            if exp_all.get_attribute('aria-expanded') == 'false':
                                exp_all.click()

                            time.sleep(0.5)
                            #OPÇÕES - EMBARALHAR - Padrão (desmarcado)
                            id_geral_as = page.locator('fieldset[id="id_generalheader"]')
                            if id_geral_as.locator('input[id="id_shuffleanswers"]').is_checked():
                                #id_geral_as.locator('input[id="id_shuffleanswers"]').click()
                                results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Opções 'Embaralhar' deve ser desmarcado atendendo ao Padrão."]

                            #SALVAR
                            page.locator('input[id="id_cancel"]').click()
                            time.sleep(0.5)
                        
                        elif tipo_questao.get_attribute('title') == "Respostas embutidas (cloze)":
                            time.sleep(0.5)
                            tipo_questao.click()
                            time.sleep(1)
                            #SALVAR
                            page.locator('input[id="id_cancel"]').click()
                            time.sleep(0.5)

                        elif tipo_questao.get_attribute('title') == "Aleatório": #BANCO DE QUESTÕES
                            time.sleep(1)      
                            banco_questoes = t_questao.locator('xpath=//a[@class="mod_quiz_random_qbank_link"]')
                            time.sleep(0.5)
                            banco_questoes.click()
                            time.sleep(1)
                            #print(f'Código da categoria das questões: {cod_categoria}')
                            cod_cat = page.locator('select[id="id_selectacategory"]').input_value()
                            #print(f'Código da categoria das questões atuais: {cod_cat}')
                            #FAZ O TESTE PARA EVITAR CONFERIR A MESMA CATEGORIA DE QUESTÕES MAIS DE UMA VEZ.
                            if cod_cat != cod_categoria:
                                time.sleep(0.5)
                                cod_categoria = cod_cat
                                #print(f'Código da categoria: {cod_categoria} diferente da anterior, ou seja, um novo banco de questões')
                                questao = page.locator('xpath=//td[@class="qtype"]')
                                t_questao = questao.locator('xpath=//img[@class="icon "]')
                                cont_num_questoes = page.locator('xpath=//div[@class="action-menu moodle-actionmenu"]')
                                time.sleep(0.5)
                                for z in range(cont_num_questoes.count()):
                                    time.sleep(0.5)
                                    print(t_questao.nth(z).get_attribute('title'))
                                    time.sleep(1) 
                                    cont_num_questoes.nth(z).click()
                                    time.sleep(1)
                                    tipo =  t_questao.nth(z).get_attribute('title')
                                    time.sleep(0.5)
                                    if t_questao.nth(z).get_attribute('title') == "Múltipla escolha":
                                        time.sleep(0.5)
                                        cont_num_questoes.nth(z).locator('span:has-text("Editar questão")').click()
                                        time.sleep(1)
                                        nome_questao = page.locator('input[id="id_name"]').input_value()
                                        print(f'{tipo} - {nome_questao}')
                                        #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                                        expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                                        time.sleep(0.5)
                                        if exp_all.get_attribute('aria-expanded') == 'false':
                                            exp_all.click()
                                        time.sleep(0.5)
                                        #GERAL - UMA OU MÚLTIPLAS RESPOSTAS - Padrão (apenas uma resposta)
                                        id_geral_respostas_me = page.locator('fieldset[id="id_generalheader"]')
                                        
                                        #GERAL - MISTURAR AS OPÇÕES? - Padrão (desmarcado)
                                        if id_geral_respostas_me.locator('input[id="id_shuffleanswers"]').is_checked():
                                            #id_geral_respostas_me.locator('input[id="id_shuffleanswers"]').click()
                                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Geral 'Misturar as opções?' deve ser desmarcado atendendo ao Padrão."]
                                        
                                        #SALVAR
                                        page.locator('input[id="id_cancel"]').click()
                                        time.sleep(0.5)
                                
                                    elif t_questao.nth(z).get_attribute('title') == "Verdadeiro/Falso":
                                        time.sleep(0.5)
                                        cont_num_questoes.nth(z).locator('span:has-text("Editar questão")').click()
                                        time.sleep(1)
                                        nome_questao = page.locator('input[id="id_name"]').input_value()
                                        print(f'{tipo} - {nome_questao}')
                                        #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                                        expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                                        time.sleep(0.5)
                                        if exp_all.get_attribute('aria-expanded') == 'false':
                                            exp_all.click()
                                        time.sleep(0.5)
                                        #GERAL - FEEDBACK VERDADEIRO - Padrão (feedback)
                                        id_geral_respostas_vf = page.locator('fieldset[id="id_generalheader"]')
                                        geral_feedback_verdadeiro = id_geral_respostas_vf.locator('div[id="id_feedbacktrueeditable"]')
                                        if geral_feedback_verdadeiro.inner_html() == '':
                                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Geral 'Feedback verdadeiro' está diferente do Padrão."]
                                        
                                        #GERAL - FEEDBACK FALSO - Padrão (feedback)
                                        geral_feedback_falso = id_geral_respostas_vf.locator('div[id="id_feedbackfalseeditable"]')
                                        if geral_feedback_falso.inner_html() == '':
                                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Geral 'Feedback falso' está diferente do Padrão."]
                                        
                                        #SALVAR
                                        page.locator('input[id="id_cancel"]').click()
                                        time.sleep(0.5)

                                    elif t_questao.nth(z).get_attribute('title') == "Selecionar as palavras que faltam":
                                        time.sleep(0.5)
                                        cont_num_questoes.nth(z).locator('span:has-text("Editar questão")').click()
                                        time.sleep(1)
                                        nome_questao = page.locator('input[id="id_name"]').input_value()
                                        print(f'{tipo} - {nome_questao}')
                                        #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                                        expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                                        time.sleep(0.5)
                                        if exp_all.get_attribute('aria-expanded') == 'false':
                                            exp_all.click()
                                        time.sleep(0.5)
                                        #OPÇÕES - EMBARALHAR - Padrão (marcado)
                                        id_opcoes_se = page.locator('fieldset[id="id_choicehdr"]')
                                        if id_opcoes_se.locator('input[id="id_shuffleanswers"]').is_checked() == False:
                                            #id_opcoes_se.locator('input[id="id_shuffleanswers"]').click()
                                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Opções 'Embaralhar' deve ser marcado atendendo ao Padrão."]
                                    
                                        #SALVAR
                                        page.locator('input[id="id_cancel"]').click()
                                        time.sleep(0.5)
                                    
                                    elif t_questao.nth(z).get_attribute('title') == "Arrastar e soltar sobre o texto":
                                        time.sleep(0.5)
                                        cont_num_questoes.nth(z).locator('span:has-text("Editar questão")').click()
                                        time.sleep(1)
                                        nome_questao = page.locator('input[id="id_name"]').input_value()
                                        print(f'{tipo} - {nome_questao}')
                                        #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                                        expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                                        time.sleep(0.5)
                                        if exp_all.get_attribute('aria-expanded') == 'false':
                                            exp_all.click()
                                        time.sleep(0.5)
                                        #OPÇÕES - EMBARALHAR - Padrão (desmarcado)
                                        id_opcoes_ar = page.locator('fieldset[id="id_choicehdr"]')
                                        if id_opcoes_ar.locator('input[id="id_shuffleanswers"]').is_checked():
                                            #id_opcoes_ar.locator('input[id="id_shuffleanswers"]').click()
                                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Opções 'Embaralhar' deve ser desmarcado atendendo ao Padrão."]

                                        #SALVAR
                                        page.locator('input[id="id_cancel"]').click()
                                        time.sleep(0.5)

                                    elif t_questao.nth(z).get_attribute('title') == "Associação":
                                        time.sleep(0.5)
                                        cont_num_questoes.nth(z).locator('span:has-text("Editar questão")').click()
                                        time.sleep(1)
                                        nome_questao = page.locator('input[id="id_name"]').input_value()
                                        print(f'{tipo} - {nome_questao}')
                                        #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                                        expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                                        time.sleep(0.5)
                                        if exp_all.get_attribute('aria-expanded') == 'false':
                                            exp_all.click()
                                        time.sleep(0.5)
                                        #OPÇÕES - EMBARALHAR - Padrão (desmarcado)
                                        id_geral_as = page.locator('fieldset[id="id_generalheader"]')
                                        if id_geral_as.locator('input[id="id_shuffleanswers"]').is_checked():
                                            #id_geral_as.locator('input[id="id_shuffleanswers"]').click()
                                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} - Nome da questão {nome_questao} ==> Opções 'Embaralhar' deve ser desmarcado atendendo ao Padrão."]

                                        #SALVAR
                                        page.locator('input[id="id_cancel"]').click()
                                        time.sleep(0.5)
                                
                                    elif tipo_questao.get_attribute('title') == "Respostas embutidas (cloze)":
                                        time.sleep(0.5)
                                        tipo_questao.click()
                                        time.sleep(1)
                                        #SALVAR
                                        page.locator('input[id="id_cancel"]').click()
                                        time.sleep(0.5)

                                    else:
                                        results+= [f"{nome_atividade} é um questionário do tipo: {tipo} ==> Atividade não validada. Solicite este tipo para validação"]
                                                                        
                                #results+= [f"{nome_atividade} é um questionário com Banco de Questões e este tipo não está implementado."]
                            navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
                            time.sleep(0.5)
                            navegacao_secundaria.locator('xpath=//li[@class="nav-item" and @data-key="mod_quiz_edit"]').click()
                            time.sleep(1)

                        else:
                            results+= [f"{nome_atividade} é um questionário do tipo: {tipo} ==> Atividade não validada. Solicite este tipo para validação"]
                
                except: #BANCO DE QUESTÕES
                    results+= [f"{nome_atividade} erro neste questionário. Reportar a COSED"]
                    
                #HOME
                time.sleep(1)
                #page.locator('xpath=//li[@class="breadcrumb-item dimmed_text"]').click()
                page.goto(context["course_url"], wait_until="load")
                time.sleep(0.5)
            print('Questões do questionário concluído')    
        except Exception as err:
            results+=  [f"Não foi possível validar Questões do Questionário. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results       