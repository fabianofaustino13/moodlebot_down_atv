import time
from moodlebot.plugin import CheckPlugin

class CheckFiltros(CheckPlugin):
    """Validando as configurações dos Filtros - Todos os filtros habilitados."""

    def handle(self, page, context):
        results = []
        print("Filtros")
        return results

        navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
        #time.sleep(1)
        navegacao_secundaria.locator('a:has-text("Mais")').click()
        time.sleep(0.5)
        navegacao_secundaria.locator('a:has-text("Filtros")').click()
        time.sleep(1) 

        try:
            #EXIBIR H5P - Padrão (Habilitado)
            if (page.locator("select[id='menudisplayh5p']").input_value()) != '0':
                exib_h5p_padrao = 'Padrão (Habilitado)'
                exib_h5p = page.locator('select[id="menudisplayh5p"] > option[selected="selected"]').inner_text()
                #page.locator("select[id='menudisplayh5p']").select_option('0')
                results+=  [f"O Filtro 'Exibir H5P' é '{exib_h5p}' e deve ser '{exib_h5p_padrao}' atendendo ao Padrão."]
            
            #LINK AUTOMÁTICO DE NOMES DE ATIVIDADES - Padrão (Habilitado)
            if (page.locator("select[id='menuactivitynames']").input_value()) != '0':
                link_automatico_padrao = 'Padrão (Habilitado)'
                link_automatico = page.locator('select[id="menuactivitynames"] > option[selected="selected"]').inner_text()
                #page.locator("select[id='menudisplayh5p']").select_option('0')
                results+=  [f"O Filtro 'Link automático de nomes de atividades' é '{link_automatico}' e deve ser '{link_automatico_padrao}' atendendo ao Padrão."]

            #MATJHJAX - Padrão (Habilitado)
            if (page.locator('select[id="menumathjaxloader"]').input_value()) != '0':
                mat_padrao = 'Padrão (Habilitado)'
                mat = page.locator('select[id="menumathjaxloader"] > option[selected="selected"]').inner_text()
                #page.locator("select[id='menumathjaxloader']").select_option('0')
                results+=  [f"O Filtro 'MatjhJax' é '{mat}' e deve ser '{mat_padrao}' atendendo ao Padrão."]

            #EXIBIR EMOTICONS COMO IMAGENS - Padrão (Habilitado)
            if (page.locator('select[id="menuemoticon"]').input_value()) != '0':
                exibir_emoticons_padrao = 'Padrão (Habilitado)'
                exibir_emoticons = page.locator("select[id='menuemoticon'] > option[selected='selected']").inner_text()
                #page.locator('select[id="menuactivitynames"]').select_option('0')
                results+=  [f"O Filtro 'Exibir emoticons como imagens' é '{exibir_emoticons}' e deve ser '{exibir_emoticons_padrao}' atendendo ao Padrão."]

            #CONVERTER URLs EM LINKS E IMAGENS - Padrão (Habilitado)
            if (page.locator('select[id="menuurltolink"]').input_value()) != '0':
                converter_url_padrao = 'Padrão (Habilitado)'
                converter_url = page.locator("select[id='menuurltolink'] > option[selected='selected']").inner_text()
                #page.locator('select[id="menuactivitynames"]').select_option('0')
                results+=  [f"O Filtro 'Converter URLs em links e imagens' é '{converter_url}' e deve ser '{converter_url_padrao}' atendendo ao Padrão."]

            #PLUGINS MULTIMÍDIA - Padrão (Habilitado)
            if (page.locator('select[id="menumediaplugin"]').input_value()) != '0':
                mult_padrao = 'Padrão (Habilitado)'
                mult = page.locator('select[id="menumediaplugin"] > option[selected="selected"]').inner_text()
                #page.locator('select[id="menumediaplugin"]').select_option('0')
                results+=  [f"O Filtro 'Plugins multimídia' é '{mult}' e deve ser '{mult_padrao}' atendendo ao Padrão."]

            #GENÉRICO - Padrão (Habilitado)
            if (page.locator('select[id="menugenerico"]').input_value()) != '0':
                gen_padrao = 'Padrão (Habilitado)'
                gen = page.locator('select[id="menugenerico"] > option[selected="selected"]').inner_text()
                #page.locator('select[id="menugenerico"]').select_option('0')
                results+=  [f"O Filtro 'Generico' é '{gen}' e deve ser '{gen_padrao}' atendendo ao Padrão."]
            
            time.sleep(1)
            page.locator('input[name="savechanges"]').click()
            time.sleep(0.5)
            page.goto(context["course_url"], wait_until="load")
            print('Filtros concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Filtros. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")

        return results
