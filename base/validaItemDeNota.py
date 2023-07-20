# Instalação da lib do Selenium
# pip3 install selenium

# Instalação Beautifulsoup4
# pip3 install beautifulsoup4

# Instalação lxml
# pip3 install lxml

# ABRINDO O QUADRO DE NOTAS
# Verificar o Quadro de Notas  aggregatesum
# linkQuadroNotas = "https://ead.ifrn.edu.br/ava/academico/grade/edit/tree/index.php?id=639" #+ codCurso #"639"
# navegador.get(url=linkQuadroNotas)

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select

from time import sleep

service = FirefoxService(
    executable_path="./geckodriver",
)

options = Options()
options.headless = False  # executar de forma visível ou oculta


def itemDeNota(navegador, link, contItemDeNota):
    navegador.find_element(by=By.LINK_TEXT, value="Notas").click()
    sleep(1)

    navegador.find_element(by=By.LINK_TEXT, value="Configurações").click()
    sleep(1)

    lista = navegador.find_elements(By.CLASS_NAME, "gradeitemheader")
    # print(len(lista))
    qntAtv = len(lista)
    # print("Total de atividades: %i" % qntAtv)
    i = 1
    x = 2

    vetor = list(range(qntAtv))
    k = 0
    for j in lista:
        #    i += 1
        # print("Validando.....")
        # print("Lista é: %s" % j.text)
        # print(k)
        vetor[k] = j.text
        # print(vetor[k])
        k += 1

    k = 0
    while x <= qntAtv:
        checagemTotal = 0
        contItemDeNota = 0
        # print("X é: %i" % x)
        # print(listaAtv[k])
        # k+=1
        # print("Valor de X: %i" % x)
        variavel = "action-menu-toggle-" + str(x)
        # print(variavel)
        # print("Validando o " + j.text)
        # print(vetor[k])
        # k+=1
        navegador.find_element(by=By.ID, value=variavel).click()
        sleep(1)
        navegador.find_element(
            by=By.LINK_TEXT, value="Editar configurações"
        ).click()  # Abrir
        sleep(1)

        # ENTRANDO NO ITEM DE NOTA
        navegador.find_element(
            by=By.LINK_TEXT, value="Mostrar mais ..."
        ).click()  # Abrir
        # sleep(1)

        print(
            "Analisando as configurações do Quadro de Notas - Item de nota: %s"
            % navegador.find_element(by=By.ID, value="id_itemname").get_attribute(
                "value"
            )
        )
        # NOTA PARA APROVAÇÃO - PADRÃO É: 0,00
        checagemTotal += 1
        input_ItemDeNotaNotaAprovacao = False
        inputItemDeNotaNotaAprovacao = navegador.find_element(
            by=By.ID, value="id_gradepass"
        )
        if (
            navegador.find_element(by=By.ID, value="id_gradepass").get_attribute(
                "value"
            )
            != "0,00"
        ):
            inputItemDeNotaNotaAprovacao.clear()
            inputItemDeNotaNotaAprovacao.send_keys("0,00")
            input_ItemDeNotaNotaAprovacao = True
            contItemDeNota += 1
            # sleep(1)

        # FATOR MULTIPLICADOR - PADRÃO É: 1,0000
        checagemTotal += 1
        input_ItemDeNotaFatorMultiplicador = False
        inputItemDeNotaFatorMultiplicador = navegador.find_element(
            by=By.ID, value="id_multfactor"
        )
        if (
            navegador.find_element(by=By.ID, value="id_multfactor").get_attribute(
                "value"
            )
            != "1,0000"
        ):
            inputItemDeNotaFatorMultiplicador.clear()
            inputItemDeNotaFatorMultiplicador.send_keys("1,0000")
            input_ItemDeNotaFatorMultiplicador = True
            contItemDeNota += 1
            # sleep(1)

        # COMPENSAÇÃO - PADRÃO É: 0,0000
        checagemTotal += 1
        input_ItemDeNotaCompensacao = False
        inputItemDeNotaCompensacao = navegador.find_element(
            by=By.ID, value="id_plusfactor"
        )
        if (
            navegador.find_element(by=By.ID, value="id_plusfactor").get_attribute(
                "value"
            )
            != "0,0000"
        ):
            inputItemDeNotaCompensacao.clear()
            inputItemDeNotaCompensacao.send_keys("0,0000")
            input_ItemDeNotaCompensacao = True
            contItemDeNota += 1
            # sleep(1)

        # TIPO DE APRESENTAÇÃO DA NOTA - PADRÃO É: PADRÃO(REAL)
        checagemTotal += 1
        input_ItemDeNotaTipoApresentacaoNota = False
        inputItemDeNotaTipoApresentacaoNota = Select(
            navegador.find_element(by=By.ID, value="id_display")
        )
        if (
            navegador.find_element(by=By.ID, value="id_display").get_attribute("value")
            != "0"
        ):  # 0 É PADRAL(REAL)
            inputItemDeNotaTipoApresentacaoNota.select_by_value("0")  # 0 É PADRAL(REAL)
            input_ItemDeNotaTipoApresentacaoNota = True
            contItemDeNota += 1
            # sleep(1)

        # PONTOS DECIMAIS GERAL - PADRÃO É: PADRÃO(2)
        checagemTotal += 1
        input_ItemDeNotaPontosDecimaisGeral = False
        inputItemDeNotaPontosDecimaisGeral = Select(
            navegador.find_element(by=By.ID, value="id_decimals")
        )
        if (
            navegador.find_element(by=By.ID, value="id_decimals").get_attribute("value")
            != "-1"
        ):  # -1 É PADRÃO(2)
            inputItemDeNotaPontosDecimaisGeral.select_by_value("-1")  # -1 É PADRÃO(2)
            input_ItemDeNotaPontosDecimaisGeral = True
            contItemDeNota += 1
            # sleep(1)

        # TRAVADO - PADRÃO É: DESTRAVADO
        checagemTotal += 1
        input_ItemDeNotaPontosDecimaisGeralTravado = False
        inputItemDeNotaPontosDecimaisGeralTravado = navegador.find_element(
            by=By.ID, value="id_locked"
        )
        if navegador.find_element(
            by=By.ID, value="id_locked"
        ).is_selected():  # PADRÃO É DESMARCADO
            inputItemDeNotaPontosDecimaisGeralTravado.click()
            input_ItemDeNotaPontosDecimaisGeralTravado = True
            contItemDeNota += 1
            # sleep(1)

        # TRAVAR DEPOIS DE - PADRÃO É: DESABILITADO
        checagemTotal += 1
        input_ItemDeNotaTravarDepoisDe = False
        inputItemDeNotaTravarDepoisDe = navegador.find_element(
            by=By.ID, value="id_locktime_enabled"
        )
        if navegador.find_element(
            by=By.ID, value="id_locktime_enabled"
        ).is_selected():  # PADRÃO É DESMARCADO
            inputItemDeNotaTravarDepoisDe.click()
            input_ItemDeNotaTravarDepoisDe = True
            contItemDeNota += 1
            # sleep(1)

        # PESO AJUSTADO - PADRÃO É: DESMARCADO
        checagemTotal += 1
        input_ItemDeNotaCatPaiPesoAjustado = False
        inputItemDeNotaCatPaiPesoAjustado = navegador.find_element(
            by=By.ID, value="id_weightoverride"
        )
        if navegador.find_element(
            by=By.ID, value="id_weightoverride"
        ).is_selected():  # PADRÃO É DESMARCADO
            inputItemDeNotaCatPaiPesoAjustado.click()
            input_ItemDeNotaCatPaiPesoAjustado = True
            contItemDeNota += 1
            # sleep(1)

        # CRÉDITO EXTRA - PADRÃO É: DESMARCADO
        checagemTotal += 1
        input_ItemDeNotaCatPaiCreditoExtra = False
        inputItemDeNotaCatPaiCreditoExtra = navegador.find_element(
            by=By.ID, value="id_aggregationcoef"
        )
        if navegador.find_element(
            by=By.ID, value="id_aggregationcoef"
        ).is_selected():  # PADRÃO É DESMARCADO
            inputItemDeNotaCatPaiCreditoExtra.click()
            input_ItemDeNotaCatPaiCreditoExtra = True
            contItemDeNota += 1
            # sleep(1)

        # CLICAR NO BOTÃO DE SALVAR
        navegador.find_element(by=By.ID, value="id_submitbutton").click()

        sleep(1)
        x += 1

        print("Total de verificações: %i " % checagemTotal)
        if contItemDeNota > 0:
            if contItemDeNota < 2:
                print("Total de modificação: %i" % contItemDeNota)
            else:
                print("Total de modificações: %i" % contItemDeNota)

            if (
                input_ItemDeNotaNotaAprovacao != False
                or input_ItemDeNotaFatorMultiplicador != False
                or input_ItemDeNotaCompensacao != False
                or input_ItemDeNotaTipoApresentacaoNota != False
                or input_ItemDeNotaPontosDecimaisGeral != False
                or input_ItemDeNotaPontosDecimaisGeral != False
                or input_ItemDeNotaPontosDecimaisGeralTravado != False
                or input_ItemDeNotaTravarDepoisDe != False
                or input_ItemDeNotaCatPaiPesoAjustado != False
                or input_ItemDeNotaCatPaiCreditoExtra != False
            ):
                print(vetor[k])

            if input_ItemDeNotaNotaAprovacao != False:
                print("'Nota de aprovação' foi alterado para o padrão. Padrão (0,00).")
            if input_ItemDeNotaFatorMultiplicador != False:
                print(
                    "'Fator Multiplicador' foi alterado para o padrão. Padrão (1,0000)."
                )
            if input_ItemDeNotaCompensacao != False:
                print("'Compensação' foi alterado para o padrão. Padrão (0,0000).")
            if input_ItemDeNotaTipoApresentacaoNota != False:
                print(
                    "'Tipo de apresentação' foi alterado para o padrão. Padrão (PADRÃO - REAL)."
                )
            if input_ItemDeNotaPontosDecimaisGeral != False:
                print(
                    "'Pontos decimais geral' foi alterado para o padrão. Padrão (PADRÃO - 2)."
                )
            if input_ItemDeNotaPontosDecimaisGeralTravado != False:
                print("'Travado' foi alterado para o padrão. Padrão (DESMARCADO).")
            if input_ItemDeNotaTravarDepoisDe != False:
                print(
                    "'Travar depois de' foi alterado para o padrão. Padrão (DESMARCADO)."
                )
            if input_ItemDeNotaCatPaiPesoAjustado != False:
                print(
                    "'Peso ajustado' foi alterado para o padrão. Padrão (DESMARCADO)."
                )
            if input_ItemDeNotaCatPaiCreditoExtra != False:
                print(
                    "'Crédito extra' foi alterado para o padrão. Padrão (DESMARCADO)."
                )
        else:
            print(
                "Análise do Quadro de Notas - Itens de Nota foi concluída sem observações!"
            )

        print("############ FIM ############")
        k += 1
        # sleep(1)
    # print("Verificação concluída")

    # SALVAR E SAIR DE CONFIGURAÇÕES DE NOTAS
    # navegador.find_element(By.XPATH, "//input[@class='advanced btn btn-primary' and @type='submit' and @value='Salvar mudanças']").click()
    # sleep(1)
    # IR PARA A PÁGINA INICIAL
    navegador.find_element(By.CLASS_NAME, "media-body ").click()
    sleep(1)
    return contItemDeNota
