# Instalação da lib do Selenium
# pip3 install selenium

# Instalação Beautifulsoup4
# pip3 install beautifulsoup4

# Instalação lxml
# pip3 install lxml

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


def validarURL(navegador, link, contURL):
    checagemTotal = 0
    contURL = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)
    # GERAL - DESMARCANDO A OPÇÃO DE EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO
    checagemTotal += 1
    input_GeralURLExterna = False
    inputGeralURLExterna = navegador.find_element(
        by=By.ID, value="id_externalurl"
    ).get_attribute(
        "value"
    )  # PEGANDO O VALOR DA URL
    # print(inputGeralURLExterna[0:39])
    print("URL utilizada: %s " % inputGeralURLExterna)  # IMPRIMINDO A URL
    # testeString = inputGeralURLExterna.find("fabiano")
    if inputGeralURLExterna.find("https://cdn.evg.gov.br/") != 0:
        print("Esta URL não está no padrão CDN")
        # inputGeralURLExterna.click()
        input_GeralURLExterna = True
        contURL += 1
    # GERAL - DESMARCANDO A OPÇÃO DE EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO
    checagemTotal += 1
    input_GeralExibirDescricaoNaPaginaCurso = False
    inputGeralExibirDescricaoNaPaginaCurso = navegador.find_element(
        by=By.ID, value="id_showdescription"
    )
    if navegador.find_element(
        by=By.ID, value="id_showdescription"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputGeralExibirDescricaoNaPaginaCurso.click()
        input_GeralExibirDescricaoNaPaginaCurso = True
        contURL += 1
    # GERAL - TIPO DE GLOSSÁRIO, PODE SER QUALQUER UM - PRINCIPAL OU SECUNDÁRIO

    # APARENCIA - EXIBIR
    checagemTotal += 1
    input_AparenciaExibir = False
    inputAparenciaExibir = Select(navegador.find_element(by=By.ID, value="id_display"))
    if (
        navegador.find_element(by=By.ID, value="id_display").get_attribute("value")
        != "3"
    ):  # 3 É PADRÃO(NOVA JANELA)
        inputAparenciaExibir.select_by_value("3")  # 3 É PADRÃO(NOVA JANELA)
        input_AparenciaExibir = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 0
    checagemTotal += 1
    input_VariavelURLParametro_0 = False
    inputVariavelURLParametro_0 = navegador.find_element(
        by=By.ID, value="id_parameter_0"
    )
    if (
        navegador.find_element(by=By.ID, value="id_parameter_0").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLParametro_0.clear()
        # inputVariavelURLParametro_0.send_keys("")
        input_VariavelURLParametro_0 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 0
    checagemTotal += 1
    input_VariavelURLVariavel_0 = False
    inputVariavelURLVariavel_0 = Select(
        navegador.find_element(by=By.ID, value="id_variable_0")
    )
    if (
        navegador.find_element(by=By.ID, value="id_variable_0").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLVariavel_0.select_by_value("")  # VAZIO
        input_VariavelURLVariavel_0 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 1
    checagemTotal += 1
    input_VariavelURLParametro_1 = False
    inputVariavelURLParametro_1 = navegador.find_element(
        by=By.ID, value="id_parameter_1"
    )
    if (
        navegador.find_element(by=By.ID, value="id_parameter_1").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLParametro_1.clear()
        # inputVariavelURLParametro_0.send_keys("")
        input_VariavelURLParametro_1 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 1
    checagemTotal += 1
    input_VariavelURLVariavel_1 = False
    inputVariavelURLVariavel_1 = Select(
        navegador.find_element(by=By.ID, value="id_variable_1")
    )
    if (
        navegador.find_element(by=By.ID, value="id_variable_1").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLVariavel_1.select_by_value("")  # VAZIO
        input_VariavelURLVariavel_1 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 2
    checagemTotal += 1
    input_VariavelURLParametro_2 = False
    inputVariavelURLParametro_2 = navegador.find_element(
        by=By.ID, value="id_parameter_2"
    )
    if (
        navegador.find_element(by=By.ID, value="id_parameter_2").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLParametro_2.clear()
        # inputVariavelURLParametro_0.send_keys("")
        input_VariavelURLParametro_2 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 2
    checagemTotal += 1
    input_VariavelURLVariavel_2 = False
    inputVariavelURLVariavel_2 = Select(
        navegador.find_element(by=By.ID, value="id_variable_2")
    )
    if (
        navegador.find_element(by=By.ID, value="id_variable_2").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLVariavel_2.select_by_value("")  # VAZIO
        input_VariavelURLVariavel_2 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 3
    checagemTotal += 1
    input_VariavelURLParametro_3 = False
    inputVariavelURLParametro_3 = navegador.find_element(
        by=By.ID, value="id_parameter_3"
    )
    if (
        navegador.find_element(by=By.ID, value="id_parameter_3").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLParametro_3.clear()
        # inputVariavelURLParametro_0.send_keys("")
        input_VariavelURLParametro_3 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 3
    checagemTotal += 1
    input_VariavelURLVariavel_3 = False
    inputVariavelURLVariavel_3 = Select(
        navegador.find_element(by=By.ID, value="id_variable_3")
    )
    if (
        navegador.find_element(by=By.ID, value="id_variable_3").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLVariavel_3.select_by_value("")  # VAZIO
        input_VariavelURLVariavel_3 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 4
    checagemTotal += 1
    input_VariavelURLParametro_4 = False
    inputVariavelURLParametro_4 = navegador.find_element(
        by=By.ID, value="id_parameter_4"
    )
    if (
        navegador.find_element(by=By.ID, value="id_parameter_4").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLParametro_4.clear()
        # inputVariavelURLParametro_0.send_keys("")
        input_VariavelURLParametro_4 = True
        contURL += 1
    # VARIÁVEL DE URL - &parâmetro=variável 4
    checagemTotal += 1
    input_VariavelURLVariavel_4 = False
    inputVariavelURLVariavel_4 = Select(
        navegador.find_element(by=By.ID, value="id_variable_4")
    )
    if (
        navegador.find_element(by=By.ID, value="id_variable_4").get_attribute("value")
        != ""
    ):  # VAZIO
        inputVariavelURLVariavel_4.select_by_value("")  # VAZIO
        input_VariavelURLVariavel_4 = True
        contURL += 1

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
        # print("Item de Nota em Pontos Decimais Geral foi alterado para o Padrão - PADRÃO(2).")
        contURL += 1
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - NÚMERO DE IDENTIFICAÇÃO DO MÚDULO
    checagemTotal += 1
    input_ConfComumModuloNumIdentificacao = False
    inputConfComumModuloNumIdentificacao = navegador.find_element(
        by=By.ID, value="id_cmidnumber"
    )
    if (
        navegador.find_element(by=By.ID, value="id_cmidnumber").get_attribute("value")
        != ""
    ):  # PADRÃO É VAZIO
        inputConfComumModuloNumIdentificacao.clear()
        input_ConfComumModuloNumIdentificacao = True
        contURL += 1
    # RESTRINGIR ACESSO - NÃO SERÁ TRATADO

    # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
    try:
        checagemTotal += 1
        input_ConclusaoAtividadeBloqueada = False
        input_ConclusaoAtividadeAcompanhamento = False
        inputConclusaoAtividadeAcompanhamento = Select(
            navegador.find_element(by=By.ID, value="id_completion")
        )
        if (
            navegador.find_element(by=By.ID, value="id_completion").get_attribute(
                "value"
            )
            != "2"
        ):  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            inputConclusaoAtividadeAcompanhamento.select_by_value(
                "2"
            )  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            input_ConclusaoAtividadeAcompanhamento = True
            contURL += 1
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionview"
        )
        if (
            navegador.find_element(by=By.ID, value="id_completionview").is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contURL += 1
    except:
        # CONCLUSÃO DE ATIVIDADE - BLOQUEADO
        checagemTotal += 1
        input_ConclusaoAtividadeBloqueada = False
        input_ConclusaoAtividadeAcompanhamento = False
        input_ConclusaoAtividadeRequerVisualizacao = False
        if (
            navegador.find_element(by=By.ID, value="id_unlockcompletion").get_attribute(
                "value"
            )
            == "Desbloquear opções de conclusão"
        ):
            # print("entrou para desbloquear")
            atvBloqueada = navegador.find_element(by=By.ID, value="id_unlockcompletion")
            atvBloqueada.click()
            input_ConclusaoAtividadeBloqueada = True
            contURL += 1
            sleep(1)
        # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
        checagemTotal += 1
        input_ConclusaoAtividadeAcompanhamento = False
        inputConclusaoAtividadeAcompanhamento = Select(
            navegador.find_element(by=By.ID, value="id_completion")
        )
        if (
            navegador.find_element(by=By.ID, value="id_completion").get_attribute(
                "value"
            )
            != "2"
        ):  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            inputConclusaoAtividadeAcompanhamento.select_by_value(
                "2"
            )  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            input_ConclusaoAtividadeAcompanhamento = True
            contURL += 1
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionview"
        )
        if (
            navegador.find_element(by=By.ID, value="id_completionview").is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contURL += 1

    # CONCLUSÇÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM
    checagemTotal += 1
    input_ConclusaoAtividadeConclusaoEsperadaEm = False
    inputConclusaoAtividadeConclusaoEsperadaEm = navegador.find_element(
        by=By.ID, value="id_completionexpected_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_completionexpected_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
        inputConclusaoAtividadeConclusaoEsperadaEm.click()
        input_ConclusaoAtividadeConclusaoEsperadaEm = True
        contURL += 1

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contURL > 0:
        if contURL == 1 and input_GeralURLExterna:
            print("Apenas uma observação na URL")
        elif contURL < 2:
            print("Total de modificação: %i" % contURL)
        else:
            print("Totais de modificações: %i" % contURL)

        if input_GeralURLExterna != False:
            print(
                "'URL externa' não está usando o Padrão CDN -->> %s "
                % inputGeralURLExterna
            )
        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_AparenciaExibir != False:
            print("'Exibir' foi alterado para o Padrão - PADRÃO (NOVA JANELA).")

        if input_VariavelURLParametro_0 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (CAMPO EM BRANCO)."
            )
        if input_VariavelURLVariavel_0 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (ESCOLHA UMA VARIÁVEL)."
            )
        if input_VariavelURLParametro_1 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (CAMPO EM BRANCO)."
            )
        if input_VariavelURLVariavel_1 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (ESCOLHA UMA VARIÁVEL)."
            )
        if input_VariavelURLParametro_2 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (CAMPO EM BRANCO)."
            )
        if input_VariavelURLVariavel_2 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (ESCOLHA UMA VARIÁVEL)."
            )
        if input_VariavelURLParametro_3 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (CAMPO EM BRANCO)."
            )
        if input_VariavelURLVariavel_3 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (ESCOLHA UMA VARIÁVEL)."
            )
        if input_VariavelURLParametro_4 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (CAMPO EM BRANCO)."
            )
        if input_VariavelURLVariavel_4 != False:
            print(
                "'&parâmetro=variável' foi alterado para o Padrão - PADRÃO (ESCOLHA UMA VARIÁVEL)."
            )

        if input_ConfComumModuloDisponibilidade != False:
            print(
                "'Disponibilidade' foi alterado para o Padrão - PADRÃO (MOSTRAR NA PÁGINA DO CURSO)."
            )
        if input_ConfComumModuloNumIdentificacao != False:
            print(
                "'Número de identificação do módulo' foi alterado para o Padrão - PADRÃO ('VAZIO')."
            )
        if input_ConclusaoAtividadeBloqueada != False:
            print(
                "'Acompanhamento de conclusão bloqueada.' Foi desbloqueada para habilitar o padrão"
            )
        if input_ConclusaoAtividadeAcompanhamento != False:
            print(
                "'Acompanhamento de conclusão' foi alterado para o Padrão - PADRÃO (MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)."
            )
        if input_ConclusaoAtividadeRequerVisualizacao != False:
            print(
                "'Requer visualização' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_ConclusaoAtividadeConclusaoEsperadaEm != False:
            print(
                "'Conclusão esperada em' foi alterado para o Padrão - PADRÃO ('DESMARCADO')."
            )
    else:
        print("Análise da URL foi concluída sem observações!")
    return contURL
