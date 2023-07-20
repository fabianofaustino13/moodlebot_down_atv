import time
from moodlebot.plugin import CheckPlugin

class CheckGuiaParticipante(CheckPlugin):
    """Validando as configurações do Guia do Participante."""
    def handle(self, page, context):
        results = []
        print("Guia do Participante")
        return results
        
        try:
            pagina_toda = page.locator('xpath=//div[@id="page-content"]').inner_text()
            #print(pagina_toda)

            carga_horaria_valor = pagina_toda.find('Carga horária:')
            carga_horaria_hora = pagina_toda.find('horas.')
            if carga_horaria_valor != -1  and carga_horaria_hora != -1:
                valor_da_hora = pagina_toda[carga_horaria_valor+15:carga_horaria_hora].strip()
            else:
                results+= [f"O texto 'Carga horária: xxx horas.' não foi encontrado na página inicial deste curso."]

            nota_minima_valor = pagina_toda.find('Nota mínima para aprovação:')
            nota_minima_pontos = pagina_toda.find('pontos.')
            if nota_minima_valor != -1 and nota_minima_pontos != -1:
                nota_minima_aprovacao = pagina_toda[(nota_minima_valor+28):(nota_minima_pontos)].strip()
            else:
                nota_minima_aprovacao = '0'
                results+= [f"O texto 'Nota mínima para aprovação: xxx pontos.' não foi encontrada na página inicial deste curso."]
            if nota_minima_aprovacao[0:2] != '60' and nota_minima_aprovacao[0:2] != '70':
                results+= [f"A 'Nota mínima para aprovação' é '{nota_minima_aprovacao}' e em geral, deve ser 60 ou 70 atendendo ao Padrão."]

            #NOVA MOODLE 4.1 AS CHAVES SÃO ALTERADAS A DEPENDER DO FORMATO DO CURSO
            board = False
            board_chave = page.locator('xpath=//li[@class="activity book modtype_book "]')
            time.sleep(1)
            if board_chave.count() != 0:
                cont = page.locator('xpath=//li[@class="activity book modtype_book "]')
                board = True
            else:
                cont = page.locator('xpath=//li[@class="activity activity-wrapper book modtype_book hasinfo dropready draggable"]')
                
            total = cont.count()
            print(total)
            for y in range(total):
                #cont.nth(y).click()
                time.sleep(1)
                guia = cont.nth(y).locator('xpath=//span[@class="inplaceeditable inplaceeditable-text"]')
                print(guia.get_attribute('data-value'))
                time.sleep(1)
                if guia.get_attribute('data-value') == 'Guia do Participante':
                    guia.click()
                    time.sleep(1)
                    indice = page.locator('xpath=//div[@class="book_toc book_toc_numbered clearfix"]')

                    lista = indice.locator('xpath=//a[@class="text-truncate"]')
                    time.sleep(1)
                    for x in range(lista.count()):
                        time.sleep(0.5)
                        menu_oculto = page.locator('xpath=//div[@id="theme_boost-drawers-blocks"]')

                        if menu_oculto.get_attribute('aria-hidden') == "true":
                            menu_direito = page.locator('xpath=//div[@class="drawer-toggler drawer-right-toggle ml-auto d-print-none"]')
                            menu_direito.click()
                            time.sleep(1)
                        print(lista.nth(x).get_attribute('title'))
                        if lista.nth(x).get_attribute('title') == 'Carga horária e período de disponibilidade':
                            lista.nth(x).click()
                            time.sleep(1)
                            pagina_carga_horaria = page.locator('xpath=//div[@role="main"]').inner_text()
                            guia_carga_horaria_valor = pagina_carga_horaria.find('carga horária de')
                            guia_carga_horaria_horas = pagina_carga_horaria.find('horas.')
                            if guia_carga_horaria_valor != -1 and guia_carga_horaria_horas != -1:
                                val_horas = pagina_carga_horaria[(guia_carga_horaria_valor+17):guia_carga_horaria_horas].strip()
                                if valor_da_hora != val_horas:
                                    results+= [f'No Guia do Participante no item "3. Carga horária e período de disponibilidade", está com o valor da carga horária divergente do exibido na apresentação inicial da Página do Curso.']
                            else:
                                results+= [f'O termo "carga horária de XXX horas." não foi encontrado no item "3. Carga horária e período de disponibilidade" deste Guia do Participante.']

                        if lista.nth(x).get_attribute('title') == 'Certificado':
                            lista.nth(x).click()
                            time.sleep(1)
                            pagina_certificado = page.locator('xpath=//div[@role="main"]').inner_text()
                            guia_nota_valor = pagina_certificado.find('obter')
                            guia_nota_pontos = pagina_certificado.find('pontos')
                            if guia_nota_valor != -1 and guia_nota_pontos != -1:
                                valor_nota = pagina_certificado[(guia_nota_valor+6):guia_nota_pontos].strip()
                                if nota_minima_aprovacao != valor_nota:
                                    results+= [f'No Guia do Participante no item "7. Certificado", está com o valor da nota divergente do exibido na apresentação inicial da Página do Curso.']
                            else:
                                results+= [f'O termo "obter XXX pontos." não foi encontrado no item "7. Certificado" deste Guia do Participante.']
                        
                    #RETORNAR PARA A PÁGINA INICIAL
                    time.sleep(1)
                    
                    page.goto(context["course_url"], wait_until="load")

                    time.sleep(0.5)
            print('Guia do participante concluído')            
        except Exception as err:
            results+=  [f"Não foi possível validar Guia do Participante. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results