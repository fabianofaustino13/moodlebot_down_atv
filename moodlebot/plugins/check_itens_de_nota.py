import time
from moodlebot.plugin import CheckPlugin

class CheckItensDeNota(CheckPlugin):
    """Validando as configurações dos Itens de Nota."""

    def handle(self, page, context):
        results = []
        print("Itens de Nota")
        #return results
        try: 
            navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
            #time.sleep(0.5)
            navegacao_secundaria.locator('a:has-text("Notas")').click()
            time.sleep(1)
            id_tipo = page.locator('xpath=//div[@class="container-fluid tertiary-navigation full-width-bottom-border"]')
            time.sleep(0.5)
            nota = id_tipo.locator('xpath=//nav[@class="tertiary-navigation-selector"]')
            nota.click()
            time.sleep(1)
            livro_notas = nota.locator('xpath=//li[@class="dropdown-item"]')
            print(livro_notas.count())
            for w in range(livro_notas.count()):
                print(livro_notas.nth(w).inner_text().strip())
                time.sleep(0.5)
                if livro_notas.nth(w).inner_text().strip() == 'Configuração do Livro de Notas':
                    time.sleep(0.5)
                    livro_notas.nth(w).click()
                    time.sleep(0.5)
                    break
            
            categoria_curso = page.locator('xpath=//tr[@class="coursecategory category"]')
            valor = categoria_curso.get_attribute('data-category')
            print(f'Categoria: {valor}')
            time.sleep(1)
            total_atv = page.locator(f'xpath=//tr[@class="item  {valor}"]')
            tabela_itens = page.locator('xpath=//table[@id="grade_edit_tree_table"]')
            total_itens_notas = tabela_itens.locator('xpath=//td[@class="cell column-range level2 leveleven cell c2"]')
            total_itens_editar = tabela_itens.locator('xpath=//td[@class="cell column-actions level2 leveleven cell c3 lastcol"]')
            #print(total_atv.count())
            #total = total_atv.count()
            total = total_itens_editar.count()
            print(total)
            for x in range(total):
                time.sleep(0.5)
                print(f'Item de nota {x+1}/{total}')
                print(total_atv)
                #PROCURA PELO VALOR DA ATIVIDADE, SE ESTIVER SEM NOTA, A ATIVIDADE DEVERÁ ESTAR OCULTA
                #valor_atv = total_atv.nth(x).locator('xpath=//td[@class="cell column-range level2 leveleven cell c2"]').inner_text()
                time.sleep(0.5)
                valor_atv = total_itens_notas.nth(x).inner_text()
                #print(valor_atv)
                time.sleep(0.5)
                mostrar_mais = False
                if valor_atv != '0,00':
                    #teste1 = total_atv.nth(x).get_attribute('data-itemid')
                    time.sleep(0.5)
                    #total_atv.locator('xpath=//div[@class="action-menu moodle-actionmenu"]').nth(x).click()
                    #itens_nota_editar = total_atv.nth(x).locator('xpath=//div[@class="action-menu moodle-actionmenu" and @data-enhance="moodle-core-actionmenu"]')
                    itens_nota_editar = total_itens_editar.nth(x).locator('xpath=//div[@class="action-menu moodle-actionmenu" and @data-enhance="moodle-core-actionmenu"]')
                    editar_in = itens_nota_editar.locator('xpath=//a[@class=" dropdown-toggle icon-no-margin" and @role="button"]')
                    editar_in.click()
                    time.sleep(1)
                    #editar_configuracao = atividade.locator('a:has-text("Editar configurações")')
                    #editar.click()
                    editar_configuracao_in = itens_nota_editar.locator('span:has-text("Editar configurações")')
                    editar_configuracao_in.click()
                    time.sleep(1)    
                    
                    #ITEM DE NOTA - NOTA PARA APROVAÇÃO - Padrão 0,00
                    id_item_nota = page.locator('fieldset[id="id_general"]')
                    #MOSTRAR MAIS
                    mostrar_mais_item_nota = id_item_nota.locator('xpath=//a[@class="moreless-toggler" and @role="button"]')
                    time.sleep(0.5)
                    if mostrar_mais_item_nota.get_attribute('aria-expanded') == 'false':
                        mostrar_mais_item_nota.click()     
                        mostrar_mais = True
                        time.sleep(0.5)                       
                    
                    nomeAtividade = id_item_nota.locator('#id_itemname').input_value()
                    if id_item_nota.locator('#id_gradepass').input_value() != "0,00":
                        item_aprov_padrao = '0,00'
                        item_aprov = id_item_nota.locator('#id_gradepass').input_value()
                        #id_item_nota.locator('#id_gradepass').fill('0,00')
                        results+= [f"Item de Notas 'Nota para aprovação' da '{nomeAtividade}' é '{item_aprov}' deve ser atualizado para '{item_aprov_padrao}' atendendo ao Padrão."]
                    
                    #MOSTRAR MAIS                
                    time.sleep(0.5)
                    if mostrar_mais == False:
                        mostrar_mais_item_nota = id_item_nota.locator('xpath=//a[@class="moreless-toggler" and @role="button"]')
                        time.sleep(0.5)
                        if mostrar_mais_item_nota.get_attribute('aria-expanded') == 'false':
                            mostrar_mais_item_nota.click()     
                            mostrar_mais = True
                            time.sleep(0.5)

                    #ITEM DE NOTA - MULTIPLICADOR - Padrão 1,000
                    if id_item_nota.locator('#id_multfactor').input_value() != "1,0000":
                        item_mult_padrao = '1,0000'
                        item_mult = id_item_nota.locator('#id_multfactor').input_value()
                        #id_item_nota.locator('#id_multfactor').fill('1,0000')
                        results+= [f"Item de Notas 'Multiplicador' da '{nomeAtividade}' é '{item_mult}' deve ser atualizado para '{item_mult_padrao}' atendendo ao Padrão."]

                    #ITEM DE NOTA - COMPENSAÇÃO - Padrão 0,0000
                    if id_item_nota.locator('#id_plusfactor').input_value() != "0,0000":
                        item_comp_padrao = '0,0000'
                        item_comp = id_item_nota.locator('#id_plusfactor').input_value()
                        #id_item_nota.locator('#id_plusfactor').fill('0,0000')
                        results+= [f"Item de Notas 'Compensação' da '{nomeAtividade}' é '{item_comp}' deve ser atualizado para '{item_comp_padrao}' atendendo ao Padrão."]
                    
                    #ITEM DE NOTA - TIPO DE APRESENTAÇÃO DA NOTA - Padrão (Real) 
                    if id_item_nota.locator('select[id="id_display"]').input_value() != "0":
                        item_apres_padrao = 'Padrão (Real)'
                        item_apres = id_item_nota.locator('select[id="id_display"] > option[selected]').inner_text()
                        #id_item_nota.locator('select[id="id_display"]').select_option('0')
                        results+= [f"Item de Notas 'Tipo de apresentação da nota' da '{nomeAtividade}' é '{item_apres}' deve ser atualizado para '{item_apres_padrao}' atendendo ao Padrão."]
                                
                    #ITEM DE NOTA - PONTOS DECIMAIS GERAL - Padrão (2)
                    if id_item_nota.locator('select[id="id_decimals"]').input_value() != "-1":
                        item_dec_geral_padrao = 'Padrão (2)'
                        item_dec_geral = id_item_nota.locator('select[id="id_decimals"] > option[selected]').inner_text()
                        #id_item_nota.locator('select[id="id_decimals"]').select_option('-1')
                        results+= [f"Item de Notas 'Pontos decimais geral' da '{nomeAtividade}' é '{item_dec_geral}' deve ser atualizado para '{item_dec_geral_padrao}' atendendo ao Padrão."]
                                        
                    #ITEM DE NOTA - TRAVADO - Padrão (desmarcado)
                    if id_item_nota.locator('input[id="id_locked"]').is_checked():
                        #id_item_nota.locator('input[id="id_locked"]').click()
                        results+= [f"Categorias de Notas 'Travado' da '{nomeAtividade}' deve ser 'Desmarcado' atendendo ao Padrão."]
                    
                    #ITEM DE NOTA - TRAVAR DEPOIS DE - Padrão (desmarcado)
                    if id_item_nota.locator('input[id="id_locktime_enabled"]').is_checked():
                        #id_item_nota.locator('input[id="id_locktime_enabled"]').click()
                        results+= [f"Categorias de Notas 'Travar depois de:' da '{nomeAtividade}' deve ser 'Desmarcado' atendendo ao Padrão."]
                    
                    #CATEGORIA PAI - PESO AJUSTADO - Padrão (desmarcado)
                    id_categoria_pai = page.locator('fieldset[id="id_headerparent"]')
                    if id_categoria_pai.locator('input[id="id_weightoverride"]').is_checked():
                        #id_categoria_pai.locator('input[id="id_weightoverride"]').click()
                        results+= [f"Categorias de Notas 'Peso ajustado' da '{nomeAtividade}' deve ser 'Desmarcado' atendendo ao Padrão."]
                    
                    #CATEGORIA PAI - CRÉDITO EXTRA - Padrão (desmarcado)
                    if id_categoria_pai.locator('input[id="id_aggregationcoef"]').is_checked():
                        #id_categoria_pai.locator('input[id="id_aggregationcoef"]').click()
                        results+= [f"Categorias de Notas 'Crédito extra' da '{nomeAtividade}' deve ser 'Desmarcado' atendendo ao Padrão."]

                    #SALVAR MUDANÇAS
                    time.sleep(0.5)            
                    page.locator('#id_cancel').click()
                    time.sleep(1)
                else:
                    results+= [f"Exite(m) Item(ns) no Quadro de Notas que a Nota Máxima está 0 (zero) e por isso, deve estar Oculto para o Participante."]

            # Total do quadro de notas
            text_content = " ".join(
                page.locator(
                    ".courseitem > td.cell.column-range.level1.levelodd.cell.c2"
                ).all_text_contents()
                
            )
            if not "100" in text_content:
                results.append("Quadro de notas não apresenta total 100,00")

            print('Itens de nota concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Itens de nota. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
