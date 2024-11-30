# Automação de Testes Mobile com Appium e Selenium

Este projeto é uma solução de automação de testes para aplicativos móveis, utilizando **Appium** e **Selenium** para suportar dispositivos Android e iOS. Ele possui uma estrutura modular e escalável, permitindo a fácil manutenção e integração de novos dispositivos ou funcionalidades.

## Índice

- [Introdução](#introdução)
- [Pré-requisitos](#pré-requisitos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração](#configuração)
- [Executando os Testes](#executando-os-testes)
- [Funcionalidades](#funcionalidades)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Introdução

Este projeto foi desenvolvido para simplificar a automação de testes em aplicativos móveis. Ele suporta a execução em dispositivos Android e iOS, permite a captura de screenshots e organiza evidências de teste de forma estruturada.

## Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [Appium Server](https://appium.io/)
- Drivers apropriados para dispositivos Android e iOS:
  - **Android**: [Android SDK](https://developer.android.com/studio)
  - **iOS**: [Xcode](https://developer.apple.com/xcode/)

Além disso, as seguintes bibliotecas Python devem ser instaladas:

```bash
pip install -r requirements.txt
```

### Arquivo `requirements.txt`

```plaintext
selenium==4.x.x
Appium-Python-Client==2.x.x
pytest==7.x.x
pytest-html==3.x.x
```

## Estrutura do Projeto

A organização do projeto segue uma estrutura modular:

```
/tests
    /data
        test_data.json           # Dados de teste em formato JSON
    /pages
        base_page.py             # Classe BasePage
        intro_page.py            # Classe IntroPage
        main_page.py             # Classe MainPage
        transactions_page.py     # Classe TransactionsPage
        budget_page.py           # Classe BudgetPage
        add_budget_page.py       # Classe AddBudgetPage
        add_expenses_page.py     # Classe AddExpensesPage
    /tests
        transactions_tests.py    # Arquivo de testes
    /utils
        screenshot_util.py       # Captura de screenshots
        appium_config.py         # Configuração do Appium
        data_loader.py           # Carregamento de dados de teste JSON
    /evidencias                  # Armazena screenshots de evidências
/config
    app_config.json              # Configurações gerais
```

### Descrição dos Diretórios e Arquivos

- **`/tests/pages`**: Contém as classes que representam as telas do aplicativo, encapsulando localizadores e ações.
- **`/tests/tests`**: Contém os arquivos de teste baseados no `pytest`.
- **`/tests/utils`**: Funções auxiliares como configuração do driver, captura de evidências e carregamento de dados.
- **`/config/app_config.json`**: Configuração para plataformas e dispositivos.

## Configuração

### 1. Configurar o `app_config.json`

Edite o arquivo `app_config.json` para definir os dispositivos e plataformas usados nos testes:

```json
{
  "platforms": [
    {
      "name": "Android",
      "version": "12.0",
      "deviceName": "Pixel_4_Emulator",
      "appPath": "app/budgetwatch.apk"
    },
    {
      "name": "iOS",
      "version": "15.0",
      "deviceName": "iPhone 14 Pro Max",
      "appPath": "app/budgetwatch.ipa"
    }
  ]
}
```

### 2. Inicializar o Appium Server

Inicie o servidor Appium antes de executar os testes:

```bash
appium --base-path /wd/hub 
```

### 3. Configurar o Ambiente

Certifique-se de que o ambiente para Android e iOS esteja configurado corretamente.

## Executando os Testes

### 1. Executar Todos os Testes

Para executar todos os testes, use:

```bash
pytest --html=report.html
```

### 2. Executar Testes Específicos

Para executar testes específicos, use o nome do arquivo de teste:

```bash
pytest tests/tests/transactions_tests.py
```

### 3. Armazenamento de Evidências

As screenshots são armazenadas no diretório `/tests/evidencias`.

## Funcionalidades

- **Suporte a Android e iOS**: Configure múltiplos dispositivos simultaneamente.
- **Modularidade**: Arquitetura baseada em Page Objects.
- **Evidências Automatizadas**: Captura automática de screenshots.
- **Dados Centralizados**: Utilização de JSON para dados de teste.
- **Relatórios HTML**: Geração de relatórios com pytest-html.

## Contribuindo

1. Faça um fork do projeto.
2. Crie um branch para sua feature: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m 'Adicionei minha feature'`.
4. Envie para o branch principal: `git push origin minha-feature`.
5. Crie uma Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE) MIT © [Raul Batalha ](https://github.com/raulbatalha)
