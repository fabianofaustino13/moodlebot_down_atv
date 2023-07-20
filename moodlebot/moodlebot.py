import time
import pluginlib
from flask import Flask, render_template, request
from playwright.sync_api import sync_playwright
import pyautogui

#
# Carregando os plugins de verificação
#
loader = pluginlib.PluginLoader(modules=["moodlebot.plugins"])

#
# Interface web
#
app = Flask(
    __name__,
    static_url_path="/public",
    static_folder="web/public",
    template_folder="web/templates",
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analisar", methods=["POST"])

def analisar():
    context = request.form.to_dict()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,channel="chrome")
        page = browser.new_page()
        #AUMENTANDO A RESOLUÇÃO PARA 1920X1080 PARA ANTENDER AOS CURSOS NO FORMATO BOARD COM 25%
        page.set_viewport_size({"width": 1920, "height": 1080})
        
        timeInicio = time.perf_counter()  # INÍCIO DA CONTAGEM DO TEMPO
        # login
        login_action = loader.plugins.actions.Login()
        login_action.handle(page, context)

        # start checks
        results = []
        #DIMINUIR O ZOOM DO NAVEGADOR PARA 67% E PODER CLICAR EM TODOS O ELEMENTOS
        #QUANDO OS MÓDULOS ESTÃO COM TAMANHO DE 25% OS ITENS FICAM SOBREPOSTOS
        
        #for i in range(4):
        #    pyautogui.hotkey('Ctrl','Shift','-')

        for CheckPlugin in loader.plugins.checks.values():
            check_plugin = CheckPlugin()
            page.goto(context["course_url"], wait_until="load", timeout=50000 )
            try:
                check_plugin_results = check_plugin.handle(page, context)

                # EXPANDIR MENU LATERAL SE ESTIVER OCULTO
                #menuLateral = page.locator("xpath=//button[@class='btn nav-link float-sm-left mr-1 btn-light bg-gray' and @aria-controls='nav-drawer']")
                #if menuLateral.get_attribute("aria-expanded") == "false":
                #    menuLateral.click()
            
                # Nothing ? Success.
                if check_plugin.name == 'CheckNomeDoCurso':
                        nome = check_plugin_results
                        #print(f"O nome do curso é: {nome}")
                elif not check_plugin_results:
                    results.append({
                        "check": str(check_plugin),
                        "message": "Ok",
                        "status": True
                    })
                else:
                    for check_plugin_result in check_plugin_results:
                        results.append({
                            "check": str(check_plugin),
                            "message": check_plugin_result,
                            "status": False
                        })
            except Exception as ex:
                results.append({
                    "check": str(check_plugin),
                    "message": ex,
                    "status": False
                })

            finally:
                page.goto(context["course_url"], wait_until="load")

        browser.close()
        
    timeFim = time.perf_counter()
    formatacaoTempo = timeFim - timeInicio
    timeHora, timeResto = divmod(formatacaoTempo, 3600)
    timeMinutos, timeSegundos = divmod(timeResto, 60)

    print(
        "Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(
            horas=timeHora, minutos=timeMinutos, segundos=timeSegundos
        )
    )
    #print(nome)
    return render_template("result.html", context=context, nome_curso=nome, results=results)
