import re
import time
from moodlebot.plugin import CheckPlugin

class CheckObterCertificado(CheckPlugin):
    """Validando as configurações do Botão: Obter certificado."""
    def handle(self, page, context):
        results = []
        print("Obter certificado")
        #return results
        
        try:
            #PROCURARNDO PELA SEÇÃO PARA PEGAR A NOTA PARA APROVAÇÃO
            pagina_toda = page.locator('xpath=//div[@id="page-content"]').inner_text()
            #print(pagina_toda)
            nota_minima = pagina_toda.find('Nota mínima para aprovação:')
            #print(nota_minima)
            pontos = pagina_toda.find('pontos.')
            #print(pontos)
            if nota_minima != -1 and pontos != -1:
                nota_curso = (nota_minima + 28)
                nota_minima_aprovacao = pagina_toda[nota_curso:pontos].strip()
            else:
                nota_minima_aprovacao = '0'
                results+= [f"O texto 'Nota mínima para aprovação:' não encontrado."]
            if nota_minima_aprovacao[0:2] != '60' and nota_minima_aprovacao[0:2] != '70':
                    results+= [f"A 'Nota mínima para aprovação' é '{nota_minima_aprovacao}' e em geral, deve ser 60 ou 70 atendendo ao Padrão."]

            print(f'Nota para aprovação é: {nota_minima_aprovacao}')
            #Clicar em Edição para localizar o Conclusão de Curso
            time.sleep(0.5)
        
            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity label modtype_label "]')
            time.sleep(1)
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

            #INICIANDO O OBTÃO OBTER CERTIFICADO
            total_button = cont.count() #-1 PQ O LAÇO ABAIXO INICIA EM 0
            for w in range(cont.count()):
                time.sleep(0.5)
                cont_button = cont.nth(w).locator('xpath=//button[@type="button"]')
                #print(cont_button.count())
                if cont_button.count() != 0:
                    atividade = cont.nth(w).locator('xpath=//div[@class="activity-actions align-self-start"]')
                    atividade.click()
                    time.sleep(1)
                    editar_configuracao = atividade.locator('xpath=//a[@class="dropdown-item editing_update menu-action cm-edit-action" and @data-action="update"]')
                    editar_configuracao.click()
                    time.sleep(1)  
                                                        
                    #GERAL - TEXTO DO RÓTULO - Padrão ({GENERICO:type="certificate"})
                    texto = page.locator('xpath=//div[@id="id_introeditoreditable"]')
                    text_area = texto.inner_text().strip()
                
                    novo_text_area_portugues = text_area[0:32] #em português
                    novo_text_area_ingles = text_area[0:33] #em inglês
                    #print(novo_text_area_portugues)
                    #print(novo_text_area_ingles)
                    generico_portugues = '{GENERICO:type="certificate"}'
                    generico_ingles = '{GENERICO:type="certificate2"}'
                    #print(generico_portugues)
                    #print(generico_ingles)

                    #ABRIR TODOS OS BOTÕES EXPANDIR TUDO
                    expandir = page.locator("xpath=//div[@class='collapsible-actions']")
                    exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                    #expandir_tudo = expandir.locator('a:has-text("Expandir tudo")')
                    #print(f'Arquivo {x+1}/{total} - total de Expandir tudo: {expandir_tudo.count()}')
                    print(f'Botão obter certificado {w+1}/{total_button} - total de Expandir tudo: {exp_all.count()} e status: {exp_all.get_attribute("aria-expanded")}')
                    if exp_all.count() != 0:
                        if exp_all.get_attribute('aria-expanded') == 'false':
                            exp_all.click()
                    
                    if novo_text_area_portugues != generico_portugues and novo_text_area_ingles != generico_ingles:
                        results+= [f"Obter certificado ==> Geral 'Texto do rótulo' está fora do Padrão."]
                    
                    #CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE - Padrão (Mostrar na página do curso)
                    id_conf_comuns_modulos = page.locator('fieldset[id="id_modstandardelshdr"]')
                    time.sleep(0.5)
                    if id_conf_comuns_modulos.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                        if exp_all.count() != 0:
                            exp_all.click()
                            time.sleep(0.5)

                    #if id_conf_comuns_modulos.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                    #    page.locator('a:has-text("Expandir tudo")').click()
                        
                    if (id_conf_comuns_modulos.locator("select[id='id_visible']").input_value()) != '1':
                        conf_com_mod_disp_padrao = 'Mostrar na página do curso'
                        conf_com_mod_disp = id_conf_comuns_modulos.locator("select[id='id_visible'] > option[selected]").inner_text()
                        #id_conf_comuns_modulos.locator("select[id='id_visible']").select_option('1')
                        results+=  [f"Obter certificado ==> Configurações comuns de módulos 'Disponibilidade' é '{conf_com_mod_disp}' deve ser atualizado para '{conf_com_mod_disp_padrao}' atendendo ao Padrão."]

                    try:
                        id_restricao = page.locator('fieldset[id="id_availabilityconditionsheader"]')
                        time.sleep(0.5)
                        if id_restricao.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                            exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                            if exp_all.count() != 0:
                                exp_all.click()
                                time.sleep(0.5)

                        #RETRINGIR ACESSO - RESTRIÇÕES DE ACESSO - Padrão (estudante nota >= 60 ou 70 o valor está sendo retirado da seção do Participante)
                        if (id_restricao.locator('xpath=//select[@class="availability-neg custom-select mx-1" and @title="Tipo de restrição"]').input_value()) != '':
                            #id_restricao.locator('xpath=//select[@class="availability-neg custom-select mx-1" and @title="Tipo de restrição"]').select_option('')
                            results+=  [f"Obter certificado ==> Restringir acesso 'Estudante...' é 'Não deve' deve ser atualizado para 'Deve' atendendo ao Padrão."]
                        
                        #RETRINGIR ACESSO - NOTA - Padrão (Total do curso)
                        restricao = id_restricao.locator('xpath=//div[@class="d-inline-block form-inline availability_grade availability-plugincontrols"]')
                        nome = restricao.locator('select[class="custom-select"]').inner_html()
                        texto = nome.split("</option>")
                        for t in texto:
                            tam_total = len(t)
                            #print(len(t))
                            #print(t)
                            inicio = tam_total - 14 #14 é o tamanho do texto 'Total do curso'
                            #print(t[inicio:tam_total])
                            if t[inicio:tam_total] == 'Total do curso':
                                novo_tamanho = inicio - 2
                                valor = t[15:novo_tamanho] #15 é o tamanho do texto '<option value="' 
                                #print(valor)
                                restricao_nota = restricao.locator('select[class="custom-select"]').input_value()
                                #print(restricao_nota)
                                if valor != restricao_nota:
                                    results+=  [f"Obter certificado ==> Restringir acesso 'Nota' está fora do Padrão."]
                    
                        #RETRINGIR ACESSO - OCULTAR - Padrão (oculto)
                        restringir_oculto = id_restricao.locator('xpath=//div[@class="availability-item d-sm-flex align-items-center"]')
                        resgringir_ocutar = restringir_oculto.locator('xpath=//a[@class="availability-eye col-form-label"]').get_attribute('title')
                        if resgringir_ocutar != 'Ocultar totalmente se o estudante não atender essa condição • Clicar para exibir':
                            results+=  [f"Obter certificado ==> Restringir acesso 'Exibido em cinza se o usuário não atender a esta condição' está fora do Padrão."]   

                        #RETRINGIR ACESSO - DEVE SER - Padrão (marcado)
                        if id_restricao.locator('xpath=//input[@class="form-check-input mx-1" and @name="min"]').is_checked() == False:
                            results+=  [f"Obter certificado ==> Restringir acesso 'Deve ser >=' está fora do Padrão."]   

                        #RETRINGIR ACESSO - NOTA MÍNIMA - Padrão (60 ou 70 pontos)
                        restringir_nota_minima = id_restricao.locator('xpath=//input[@class="form-control mx-1" and @name="minval"]').input_value()
                        if restringir_nota_minima[0:2] != nota_minima_aprovacao[0:2]:
                            results+=  [f"Obter certificado ==> Restringir acesso 'Nota mínima' é {restringir_nota_minima[0:2]} e está diferente da 'Nota mínima para aprovação' {nota_minima_aprovacao[0:2]} do Guia do Participante."]   
                        
                        #RETRINGIR ACESSO - DEVE SER - Padrão (desmarcado)
                        if id_restricao.locator('xpath=//input[@class="form-check-input mx-1" and @name="max"]').is_checked():
                            results+=  [f"Obter certificado ==> Restringir acesso 'Deve ser <' está fora do Padrão."]   

                    except:
                        results+=  [f"Obter certificado ==> Não existe a condição para aprovação, sendo assim, está fora do Padrão."]   

                    #CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO - Padrão (não indicar a conclusão de atividade)
                    id_conclusao = page.locator('fieldset[id="id_activitycompletionheader"]')
                    time.sleep(0.5)
                    if id_conclusao.locator('xpath=//a[@class="btn btn-icon mr-1 icons-collapse-expand stretched-link fheader collapsed"]').count() != 0:
                        exp_all = expandir.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
                        if exp_all.count() != 0:
                            exp_all.click()
                            time.sleep(0.5)
                            
                    if (id_conclusao.locator("select[id='id_completion']").input_value()) != '0':
                        conc_atv_acom_conc_padrao = 'Não indicar a conclusão de atividade'
                        conc_atv_acom_conc = id_conclusao.locator("select[id='id_completion'] > option[selected]").inner_text()
                        #id_conclusao.locator("select[id='id_completion']").select_option('0')
                        results+=  [f"Obter certificado ==> Conclusão de atividade 'Acompanhamento de conclusão' é {conc_atv_acom_conc} deve ser atualizado para {conc_atv_acom_conc_padrao} atendendo ao Padrão."]

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
                else:
                    if w == total_button: #CONDIÇÃO SE NÃO EXISTIR UM BOTÃO OBTER CERTIFICADO, IRÁ INFORMAR.
                        results+=  [f"Obter certificado ==> Não existe o botão 'Obter certificado' neste curso."]   
            print('Botão obter certificado concluído')    
        except Exception as err:
            results+=  [f"Não foi possível validar Botão Obter certificado. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
