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


def validarBotao(navegador, link, contBotao, notaMinima):
    checagemTotal = 0
    contarBotao = 0
    # print("Nota mínima: %s" % notaMinima)
    # print("botão")
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    print("Analisando as configurações do Botão - Obter certificado")
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)
    # GERAL - DESCRIÇÃO
    checagemTotal += 1
    input_GeralDescricao = False
    inputGeralDescricao = navegador.find_element(
        by=By.ID, value="id_introeditoreditable"
    )
    # print(inputGeralDescricao.text)
    if inputGeralDescricao.text == '{GENERICO:type="certificate"}':
        input_GeralDescricao = True
    else:
        print("ATENÇÃO: EXISTEM 2 BOTÕES, OBSERVAR QUAL O QUE IRÁ GERAR O CERTIFICADO")
        contarBotao += 1

    # CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE
    checagemTotal += 1
    input_ConfComumModuloDisponibilidade = False
    inputConfComumModuloDisponibilidade = Select(
        navegador.find_element(by=By.ID, value="id_visible")
    )
    if (
        navegador.find_element(by=By.ID, value="id_visible").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(MOSTRAR NA PÁGINA DO CURSO)
        inputConfComumModuloDisponibilidade.select_by_value(
            "1"
        )  # 1 É PADRÃO(MOSTRAR NA PÁGINA DO CURSO)
        input_ConfComumModuloDisponibilidade = True
        contarBotao += 1
        # sleep(1)

    # RESTRIÇÃO ACESSO - ESTUDANTE
    botaoCertificadoEscolhaEstudante = navegador.find_element(
        By.XPATH,
        "//select[@class='availability-neg custom-select mx-1' and @title='Tipo de restrição']",
    )
    todasOpcoes = botaoCertificadoEscolhaEstudante.find_elements(By.TAG_NAME, "option")
    for opcao in todasOpcoes:
        # print("Valores são: %s" % opcao.get_attribute("value"))
        # print(opcao.text)
        if opcao.text == "deve":
            # print("O valor é: %s" % opcao.get_attribute("value"))
            opcao.click()
    # contarBotao+=1
    # sleep(1)

    # RESTRIÇÃO ACESSO - NOTA
    botaoCertificadoEscolhaNota = navegador.find_element(
        By.XPATH, "//select[@class='custom-select' and @name='id']"
    )
    todasOpcoes = botaoCertificadoEscolhaNota.find_elements(By.TAG_NAME, "option")
    for opcao in todasOpcoes:
        # print("Valores são: %s" % opcao.get_attribute("value"))
        # print(opcao.text)
        if opcao.text == "Total do curso":
            # print("O valor é: %s" % opcao.get_attribute("value"))
            opcao.click()
    # contarBotao+=1
    # sleep(1)

    # RESTRIÇÃO ACESSO - NOTA MÍNIMA SELECIONAR A OPÇÃO
    input_botaoCertificadoNotaMinima = False
    inputbotaoCertificadoNotaMinima = navegador.find_element(
        By.XPATH, "//input[@class='form-check-input mx-1' and @name='min']"
    )
    # todasOpcoes = botaoCertificadoNotaMinima.find_elements(By.TAG_NAME,"option")
    if (
        inputbotaoCertificadoNotaMinima.is_selected() == False
    ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
        # print("clicando em nota mínima")
        inputbotaoCertificadoNotaMinima.click()
        navegador.find_element(
            By.XPATH, "//input[@class='form-control mx-1' and @name='minval']"
        ).clear()
        navegador.find_element(
            By.XPATH, "//input[@class='form-control mx-1' and @name='minval']"
        ).send_keys(notaMinima)
        input_botaoCertificadoNotaMinima = True
        # input_botaoCertificadoInserirNotaMinima = True
        contarBotao += 1
        # sleep(1)
    # TESTAR PARA PEGAR SEMPRE A NOTA DA SEÇÃO
    # else:
    #    navegador.find_element(By.XPATH, "//input[@class='form-control mx-1' and @name='minval']").clear()
    #    navegador.find_element(By.XPATH, "//input[@class='form-control mx-1' and @name='minval']").send_keys(notaMinima)

    # RESTRINGIR ACESSO - NÃO SERÁ TRATADO

    # CONCLUSÃO DE ATIVIDADE
    # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
    checagemTotal += 1
    input_ConclusaoAtividadeAcompanhamento = False
    inputConclusaoAtividadeAcompanhamento = Select(
        navegador.find_element(by=By.ID, value="id_completion")
    )
    if (
        navegador.find_element(by=By.ID, value="id_completion").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NÃO INDICAR A CONCLUSÃO DE ATIVIDADE)
        inputConclusaoAtividadeAcompanhamento.select_by_value(
            "0"
        )  # 0 É PADRÃO(NÃO INDICAR A CONCLUSÃO DE ATIVIDADE)
        input_ConclusaoAtividadeAcompanhamento = True
        contarBotao += 1
        # sleep(1)

    # CONCLUSÇÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM
    # checagemTotal+=1
    # input_ConclusaoAtividadeConclusaoEsperadaEm = False
    # inputConclusaoAtividadeConclusaoEsperadaEm = navegador.find_element(by=By.ID,value="id_completionexpected_enabled")
    # if navegador.find_element(by=By.ID,value="id_completionexpected_enabled").is_selected(): #PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
    #    inputConclusaoAtividadeConclusaoEsperadaEm.click()
    #    input_ConclusaoAtividadeConclusaoEsperadaEm = True
    #    contarBotao+=1
    #    sleep(1)

    # sleep(2)
    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contarBotao > 0:
        if contarBotao < 2:
            print("Total de modificação: %i" % contarBotao)
        else:
            print("Totais de modificações: %i" % contarBotao)

        if input_GeralDescricao == False:
            print(
                '"Texto do rótulo" foi alterado para o Padrão - PADRÃO ({GENERICO:type="certificate"}).'
            )

        if input_ConfComumModuloDisponibilidade != False:
            print(
                "'Disponibilidade' foi alterado para o Padrão - PADRÃO (MOSTRAR NA PÁGINA DO CURSO)."
            )
        # if input_ConfComumModuloNumIdentificacao != False:
        #    print("'Número de identificação do módulo' foi alterado para o Padrão - PADRÃO ('VAZIO').")

        if input_botaoCertificadoNotaMinima != False:
            print(
                "' Restrições de acesso ' foi alterado para o Padrão - PADRÃO (DEVE - TOTAL DO CURSO - NOTA MÍNIMA)."
            )

        if input_ConclusaoAtividadeAcompanhamento != False:
            print(
                "'Acompanhamento de conclusão' foi alterado para o Padrão - PADRÃO (NÃO INDICAR A CONCLUSÃO DE ATIVIDADE)."
            )

        # if input_ConclusaoAtividadeConclusaoEsperadaEm != False:
        #    print("'Conclusão esperada em' foi alterado para o Padrão - PADRÃO ('DESMARCADO').")
    else:
        print("Análise do Botão foi concluída sem observações!")
    return contBotao
