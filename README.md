# Moodlebot

Robô para validação de cursos Moodle para plataforma EV.G.

## Setup

### Ubuntu

Recomenda-se o uso de um ambiente virtual Python:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.in
playwright install
```

Você também precisará ter o [Nodejs](https://nodejs.org) instalado.

```bash
cd web/public/vendor
npm install
```

## Executando

Para executar a aplicação, realize a instalação conforme o passo anterior.

Acesse a pasta **moodlebot** e execute:

```bash
flask --app moodlebot run --debug
```

Em seguida, acesse a interface no navegador **http://127.0.0.1:5000**.

---

 O arquivo principal é o validação.py

 Baixar todos os arquivos para uma pasta

 Executar o validação.py

 Inserir a url do curso
 
 Inserir o usuário e senha com permissão de edição no curso



Tipo de Questões que estão funcionando para validação:

Arrastar e soltar sobre o texto
	Feedback Geral - Se está vazio. Se estiver, informar.
	Opção de Embaralhar - Se estiver marcado, será desmarcado. Padrão é desmarcado.
	Mostrar o número de respostas corretas uma vez terminada a questão. Se estiver marcado, será desmarcado. Padrão é desmarcado.
	Múltiplas tentativas - Penalidade - Se estiver diferente de zero será alterado. Padrão é Zero.
	
Associação
	Feedback Geral - Se está vazio. Se estiver, informar.
	Opção de Embaralhar - Se estiver marcado, será desmarcado. Padrão é desmarcado.
	Mostrar o número de respostas corretas uma vez terminada a questão. Se estiver marcado, será desmarcado. Padrão é desmarcado.
	Múltiplas tentativas - Penalidade - Se estiver diferente de zero será alterado. Padrão é Zero.

Dissertação
	Feedback Geral - Se está vazio. Se estiver, informar.

Múltipla Escolha
	Feedback Geral - Se está vazio. Se estiver, informar.
	Opção de Uma ou Múltiplas respostas - Se estiver diferente de 1 resposta, será alterado para o padrão. Padrão é 1.
	Opção de Mistrutrar Alternativas - Se estiver marcado, será desmarcado. Padrão é desmarcado
	Opção de numerar as Alternativas - Se estiver diferente de "abc", será alterado para o padrão. Padrão é "abc"
	É feito um teste de quantas Alternativas estão com a resposta correta (100%). Se tiver mais de 1 Alternativa, será informado.
	Múltiplas tentativas - Penalidade - Se estiver diferente de zero será alterado. Padrão é Zero.

Selecionar palavras que faltam
	Feedback Geral - Se está vazio. Se estiver, informar.
	Opção de Embaralhar - Se estiver desmarcado, será marcado. Padrão é marcado.
	Mostrar o número de respostas corretas uma vez terminada a questão. Se estiver marcado, será desmarcado. Padrão é desmarcado.
	Múltiplas tentativas - Penalidade - Se estiver diferente de zero será alterado. Padrão é Zero.

Verdadeiro ou Falso
	Feedback Geral - Se está vazio. Se estiver, informar.
	Feedback Verdadeiro - Se está vazio. Se estiver, informar.
	Feedback Falso - Se está vazio. Se estiver, informar.
