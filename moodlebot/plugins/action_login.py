from moodlebot.plugin import ActionPlugin


class Login(ActionPlugin):
    """Efetua login no Moodle."""

    def handle(self, page, context):
        username = context["username"]
        password = context["password"]
        login_url = context["login_url"]

        page.goto(login_url, wait_until="load")
        page.locator("#username").fill(username)

        password_field = page.locator("#password")
        password_field.fill(password)
        password_field.press("Enter")

        return {"page": page, "result": "Autenticação realizada com sucesso."}
