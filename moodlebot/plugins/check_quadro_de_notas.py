import time
from moodlebot.plugin import CheckPlugin

class CheckQuadroDeNotas(CheckPlugin):
    """Validando as configurações do Quadro de Notas."""
    def handle(self, page, context):
        results = []
        print("Quadro de Notas")
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

            time.sleep(1) #usando para fazer o entrar no click abaixo
            categoria_curso = page.locator('xpath=//td[@class="cell column-actions level1 levelodd cell c4 lastcol"]')
            #atv = categoria_curso.locator('xpath=//div[@class="action-menu moodle-actionmenu" and @data-enhance="moodle-core-actionmenu"]')
            atividade = categoria_curso.locator('xpath=//a[@class=" dropdown-toggle icon-no-margin" and @role="button"]')
            time.sleep(0.5)
            atividade.click()
            time.sleep(0.5)
            #editar_configuracoes = categoria_curso.locator('span:has-text("Editar configurações")')
            editar_configuracoes = categoria_curso.locator('span[id="actionmenuaction-1"]')
            time.sleep(0.5)
            editar_configuracoes.click()
            time.sleep(0.5)
            #ABRIR TODOS OS BOTÕES EXPANDIR TUDO - OBSERVAÇÃO: ESTE QUADRO SEMPRE ABRE EXPANDIDO
            #expandir_tudo = page.locator('xpath=//a[@class="btn btn-link p-1 collapseexpand collapsemenu collapsed" and @role="button"]')
            #if expandir_tudo.count() > 0:
            #    print(f"Total de Expandir tudo: {expandir_tudo.count()}")
            #    expandir_tudo.click()
        
            #CATEGORIA DE NOTAS - FORMA DE AGREGAÇÃO DAS NOTAS - Padrão (Soma das notas (Natural))
            id_categoria_notas = page.locator('fieldset[id="id_headercategory"]')
            time.sleep(1)
            if id_categoria_notas.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                id_categoria_notas.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                time.sleep(1)
                
            if (id_categoria_notas.locator('select[id="id_aggregation"]').input_value()) != "13": #VALOR 0 = MÉDIA DAS NOTAS; 13 = SOMA DAS NOTAS (NATURAL)
                cat_agre_padrao = 'Soma das notas (Natural)'
                cat_agre = id_categoria_notas.locator('select[id="id_aggregation"] > option[selected]').inner_text()
                #id_categoria_notas.locator('select[id="id_aggregation"]').select_option('13')
                results+= [f"Categorias de Notas 'Forma de agregação das notas' é '{cat_agre}' deve ser atualizado para '{cat_agre_padrao}' atendendo ao Padrão."]
            
            #CATEGORIA DE NOTAS - DESCONSIDERAR NOTAS VAZIAS - Padrão (desmarcado)
            if id_categoria_notas.locator("input[id='id_aggregateonlygraded']").is_checked():
                #id_categoria_notas.locator("input[id='id_aggregateonlygraded']").click()
                results+= ["Categorias de Notas 'Desconsiderar notas vazias' deve ser desmarcado atendendo o Padrão."]

            #TOTAL DA CATEGORIA - NOTA PARA APROVAÇÃO - Padrão (0,00)
            id_total_categoria = page.locator('fieldset[id="id_general"]')
            #id_total_categoria.locator('a:has-text("Mostrar mais ...")').click()
            time.sleep(1)
            if id_total_categoria.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').get_attribute('aria-expanded') == 'false':
                id_total_categoria.locator('xpath=//a[@class="moreless-toggler" and @role="button"]').click()
                time.sleep(0.5)
            #time.sleep(0.5)
            if id_total_categoria.locator('#id_grade_item_gradepass').input_value() != "0,00":
                tot_aprov_padrao = '0,00'
                tot_aprov = id_total_categoria.locator('#id_grade_item_gradepass').input_value()
                #id_total_categoria.locator('#id_grade_item_gradepass').fill('0,00')
                results+= [f"Categorias de Notas 'Nota para aprovação' é '{tot_aprov}' deve ser atualizado para '{tot_aprov_padrao}' atendendo ao Padrão."]
                    
            #TIPO DE APRESENTAÇÃO DA NOTA - Padrão (Real) 
            if id_total_categoria.locator("select[id='id_grade_item_display']").input_value() != "0":
                tot_tipo_padrao = 'Padrão (Real)'
                tot_tipo = id_total_categoria.locator('select[id="id_grade_item_display"] > option[selected]').inner_text()
                #id_total_categoria.locator('select[id="id_grade_item_display"]').select_option('0')
                results+= [f"Categorias de Notas 'Tipo de apresentação da nota' é '{tot_tipo}' deve ser atualizado para '{tot_tipo_padrao}' atendendo ao Padrão."]
            
            #PONTOS DECIMAIS GERAL - Padrão (2)
            if id_total_categoria.locator("select[id='id_grade_item_decimals']").input_value() != "-1":
                tot_pontos_padrao = 'Padrão (Real)'
                tot_pontos = id_total_categoria.locator('select[id="id_grade_item_decimals"] > option[selected]').inner_text()
                #id_total_categoria.locator('select[id="id_grade_item_decimals"]').select_option('-1')
                results+= [f"Categorias de Notas 'Pontos decimais geral' é '{tot_pontos}' deve ser atualizado para '{tot_pontos_padrao}' atendendo ao Padrão."]
                    
            #OCULTO - Padrão (desmarcado)
            if id_total_categoria.locator("input[id='id_grade_item_hidden']").is_checked():
                #id_total_categoria.locator("input[id='id_grade_item_hidden']").click()
                results+= ["Categorias de Notas 'Oculto' deve ser desmarcado atendendo o Padrão."]
                
            #OCULTO ATÉ - Padrão (desmarcado)
            if id_total_categoria.locator("input[id='id_grade_item_hiddenuntil_enabled']").is_checked():
                #id_total_categoria.locator("input[id='id_grade_item_hiddenuntil_enabled']").click()
                results+= ["Categorias de Notas 'Oculto até:' deve ser desmarcado atendendo o Padrão."]
            
            #TRAVADO - Padrão (desmarcado)
            if id_total_categoria.locator("input[id='id_grade_item_locked']").is_checked():
                #id_total_categoria.locator("input[id='id_grade_item_locked']").click()
                results+= ["Categorias de Notas 'Travado' deve ser desmarcado atendendo o Padrão."]
                
            #TRAVAR DEPOIS DE - Padrão (desmarcado)
            if id_total_categoria.locator("input[id='id_grade_item_locktime_enabled']").is_checked():
                #id_total_categoria.locator("input[id='id_grade_item_locktime_enabled']").click()
                results+= ["Categorias de Notas 'Travar depois de:' deve ser desmarcado atendendo o Padrão."]
            
            #SALVAR MUDANÇAS
            time.sleep(1)
            page.locator("#id_cancel").click()
            time.sleep(0.5)
            
            # Total do quadro de notas
            text_content = " ".join(
                page.locator(
                    ".courseitem > td.cell.column-range.level1.levelodd.cell.c2"
                ).all_text_contents()
            )
            if not "100" in text_content:
                results.append("Quadro de notas não apresenta total 100,00")
            print('Quadro de notas concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Quadro de notas. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
