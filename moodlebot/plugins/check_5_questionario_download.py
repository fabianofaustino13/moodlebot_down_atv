import time
import requests
import os

from moodlebot.plugin import CheckPlugin

class CheckQuestionarioDownload(CheckPlugin):
    """Validando as configurações do Questionário Avaliativo."""
    def handle(self, page, context):
        results = []
        print("Download da Estatística do Questionário")
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

                navegacao_secundaria = page.locator('xpath=//div[@class="secondary-navigation d-print-none"]')
                time.sleep(0.5)
                navegacao_secundaria.locator('a:has-text("Resultados")').click()
                time.sleep(1) 
                selecao = page.locator('select[name="jump"] > option[selected]').inner_text()
                print(selecao)
                if selecao != 'Estatísticas':
                    page.locator('select[name="jump"]').click()
                    time.sleep(1)
                    page.locator('select[name="jump"]').select_option('Estatísticas')
                    time.sleep(1)
                
                selecao_tipo = page.locator("select[id='downloadtype_download']").input_value()
                print(selecao_tipo)
                if (page.locator("select[id='downloadtype_download']").input_value()) != 'pdf':
                    page.locator("select[id='downloadtype_download']").select_option('pdf')
                    time.sleep(2)
                    page.locator('xpath=//button[@type="submit" and @class="btn btn-secondary"]').click()
                    
                    resposta = requests.get(page)
                    if resposta.status_code == requests.codes.OK:
                        with open(endereco, 'wb') as novo_arquivo:
                            novo_arquivo.writable(resposta.content)
                        print('Download finalizado. Savo em: {}'.format(endereco))
                    else:
                        resposta.raise_for_status
                time.sleep(3)

                
            print('Questionário concluído')
        except Exception as err:
            results+=  [f"Não foi possível validar Questionário. Uma possível falha de conexão. Se possível, tente rodar novamente."]
            results+=  [f"Erro {err}, {type(err)=}."]
            print(f"Erro {err}, {type(err)=}.")
        return results
