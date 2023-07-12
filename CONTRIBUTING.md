<!-- omit in toc -->
# Contribuindo para Python Basics

Antes de tudo, obrigado por dedicar seu tempo para contribuir! ❤️

Todos os tipos de contribuições são incentivados e valorizados. Veja a [Tabela de Conteúdos](#tabela-de-conteúdos) para diferentes maneiras de ajudar e detalhes sobre como este projeto lida com elas. Por favor, certifique-se de ler a seção relevante antes de fazer sua contribuição. Isso facilitará para nós, mantenedores, e tornará a experiência mais suave para todos os envolvidos. A comunidade aguarda suas contribuições. 🎉

> E se você gosta do projeto, mas simplesmente não tem tempo para contribuir, tudo bem. Existem outras maneiras fáceis de apoiar o projeto e mostrar seu apreço, com as quais também ficaríamos muito felizes:
> - Favoritar o projeto
> - Twittar sobre ele
> - Mencionar o projeto no readme do seu projeto
> - Mencionar o projeto em encontros locais e contar para seus amigos/colegas

<!-- omit in toc -->
## Tabela de Conteúdos

- [Código de Conduta](#código-de-conduta)
- [Tenho uma Pergunta](#tenho-uma-pergunta)
- [Quero Contribuir](#quero-contribuir)
  - [Relatando Bugs](#relatando-bugs)
  - [Sugerindo Melhorias](#sugerindo-melhorias)
  - [Sua Primeira Contribuição de Código](#sua-primeira-contribuição-de-código)
  - [Melhorando a Documentação](#melhorando-a-documentação)
- [Estilo de Guia](#estilo-de-guia)
  - [Mensagens de Commit](#mensagens-de-commit)
- [Junte-se à Equipe do Projeto](#junte-se-à-equipe-do-projeto)


## Código de Conduta

Este projeto e todos os participantes nele são regidos pelo
[Código de Conduta do Python Basics](https://github.com/g3rley/python-basicsblob/master/CODE_OF_CONDUCT.md).
Ao participar, espera-se que você cumpra este código.


## Tenho uma Pergunta

> Se você quiser fazer uma pergunta, pressupomos que você tenha lido a [Documentação](./README.md) e não encontrou uma resposta para sua pergunta. Se você encontrou uma resposta, mas ainda precisa de esclarecimentos, você pode escrever sua pergunta na seção de comentários da documentação. Se você não encontrou uma resposta, continue lendo.

Antes de fazer uma pergunta, é melhor procurar por [Issues](https://github.com/g3rley/python-basics/issues) existentes que possam ajudar você. Caso você tenha encontrado uma issue adequada e ainda precise de esclarecimentos, você pode escrever sua pergunta nessa issue. Também é aconselhável procurar respostas na internet primeiro.

Se ainda assim você sentir a necessidade de fazer uma pergunta e precisar de esclarecimentos, recomendamos o seguinte:

- Abra uma [Issue](https://github.com/g3rley/python-basics/issues/new).
- Forneça o máximo de contexto possível sobre o que você está enfrentando.
- Forneça as versões do projeto e da plataforma (nodejs, npm, etc), dependendo do que pareça relevante.

Nós cuidaremos da issue o mais rápido possível.

<!--
Você pode criar uma tag de issue separada para perguntas e incluí-la nesta descrição. As pessoas devem marcar suas issues de acordo.

Dependendo do tamanho do projeto, você pode querer terceirizar a questão, por exemplo, para o Stack Overflow ou Gitter. Você pode adicionar contatos adicionais e possibilidades de informações:
- IRC
- Slack
- Gitter
- Tag do Stack Overflow
- Blog
- FAQ
- Roadmap
- Lista de E-mails
- Fórum
-->

## Quero Contribuir

> ### Aviso Legal <!-- omit in toc -->
> Ao contribuir para este projeto, você concorda que criou 100% do conteúdo, que possui os direitos necessários sobre o conteúdo e que o conteúdo que você contribui possa ser fornecido sob a licença do projeto.

### Relatando Bugs

<!-- omit in toc -->
#### Antes de enviar um Relatório de Bug

Um bom relatório de bug não deve deixar os outros precisando procurar mais informações. Portanto, pedimos que você investigue cuidadosamente, colete informações e descreva o problema em detalhes no seu relatório. Por favor, siga os seguintes passos com antecedência para nos ajudar a corrigir qualquer bug potencial o mais rápido possível.

- Certifique-se de que você está usando a versão mais recente.
- Determine se o seu bug é realmente um bug e não um erro seu, como usar componentes/versões de ambiente incompatíveis (Certifique-se de ler a [documentação]() correspondente. Se você estiver procurando por suporte, você pode querer verificar [esta seção](#tenho-uma-pergunta)).
- Para ver se outros usuários já encontraram (e possivelmente já resolveram) o mesmo problema que você está enfrentando, verifique se já existe um relatório de bug para o seu bug ou erro no [rastreador de bugs](https://github.com/g3rley/python-basicsissues?q=label%3Abug).
- Certifique-se também de pesquisar na internet (incluindo o Stack Overflow) para ver se usuários fora da comunidade do GitHub discutiram o problema.
- Colete informações sobre o bug:
  - Stack trace (Traceback)
  - SO, Plataforma e Versão (Windows, Linux, macOS, x86, ARM)
  - Versão do interpretador, compilador, SDK, ambiente de execução, gerenciador de pacotes, dependendo do que pareça relevante.
  - Possivelmente sua entrada e saída
  - Você pode reproduzir o problema de forma confiável? E você também pode reproduzi-lo com versões mais antigas?

<!-- omit in toc -->
#### Como Eu Envio um Bom Relatório de Bug?

> Você nunca deve relatar problemas relacionados à segurança, vulnerabilidades ou bugs contendo informações sensíveis no rastreador de problemas ou em qualquer outro lugar público. Em vez disso, bugs sensíveis devem ser enviados por e-mail para g3rley@gmail.com.
<!-- Você pode adicionar uma chave PGP para permitir que as mensagens sejam enviadas criptografadas também. -->

Usamos as issues do GitHub para rastrear bugs e erros. Se você encontrar um problema com o projeto:

- Abra uma [Issue](https://github.com/g3rley/python-basics/issues/new). (Como não podemos ter certeza neste momento se é um bug ou não, pedimos que você não fale sobre um bug ainda e não rotule a issue.)
- Explique o comportamento que você espera e o comportamento atual.
- Forneça o máximo de contexto possível e descreva as etapas de reprodução que alguém pode seguir para recriar o problema por conta própria. Isso geralmente inclui seu código. Para bons relatórios de bugs, você deve isolar o problema e criar um caso de teste reduzido.
- Forneça as informações que você coletou na seção anterior.

Depois de enviar:

- A equipe do projeto rotulará a issue adequadamente.
- Um membro da equipe tentará reproduzir o problema com as etapas fornecidas. Se não houver etapas de reprodução ou nenhuma maneira óbvia de reproduzir o problema, a equipe pedirá que você forneça essas etapas e marcará a issue como `needs-repro`. Bugs com a tag `needs-repro` não serão tratados até serem reproduzidos.
- Se a equipe conseguir reproduzir o problema, ele será marcado como `needs-fix`, além de possivelmente outras tags (como `critical`), e a issue será deixada para ser [implementada por alguém](#sua-primeira-contribuição-de-código).

<!-- Você pode criar um template de issue para bugs e erros que pode ser usado como guia e que define a estrutura das informações a serem incluídas. Se fizer isso, faça referência a ele aqui na descrição. -->


### Sugerindo Melhorias

Esta seção orienta você a enviar uma sugestão de melhoria para o Python Basics, **incluindo novos recursos completos e melhorias menores na funcionalidade existente**. Seguir estas diretrizes ajudará os mantenedores e a comunidade a entender sua sugestão e encontrar sugestões relacionadas.

<!-- omit in toc -->
#### Antes de Enviar uma Melhoria

- Certifique-se de que você está usando a versão mais recente.
- Leia a [documentação]() cuidadosamente e descubra se a funcionalidade já está coberta, talvez por uma configuração individual.
- Realize uma [pesquisa](https://github.com/g3rley/python-basics/issues) para ver se a melhoria já foi sugerida. Se já foi, adicione um comentário à issue existente em vez de abrir uma nova.
- Descubra se sua ideia se encaixa no escopo e nos objetivos do projeto. Depende de você apresentar um caso forte para convencer os desenvolvedores do projeto dos méritos desse recurso. Tenha em mente que queremos recursos que sejam úteis para a maioria dos usuários e não apenas para um pequeno subconjunto. Se você está direcionando apenas uma minoria de usuários, considere escrever uma biblioteca de complemento/plugin.

<!-- omit in toc -->
#### Como Eu Envio uma Boa Sugestão de Melhoria?

As sugestões de melhoria são rastreadas como [issues do GitHub](https://github.com/g3rley/python-basics/issues).

- Use um **título claro e descritivo** para a issue, para identificar a sugestão.
- Forneça uma **descrição passo a passo da melhoria sugerida** com o máximo de detalhes possível.
- **Descreva o comportamento atual** e **explique qual comportamento você esperava ver em vez disso** e por quê. Neste ponto, você também pode mencionar quais alternativas não funcionam para você.
- Você pode querer **incluir capturas de tela e GIFs animados** que ajudam a demonstrar as etapas ou destacar a parte à qual a sugestão está relacionada. Você pode usar [esta ferramenta](https://www.cockos.com/licecap/) para gravar GIFs no macOS e Windows, e [esta ferramenta](https://github.com/colinkeenan/silentcast) ou [esta ferramenta](https://github.com/GNOME/byzanz) no Linux. <!-- this should only be included if the project has a GUI -->
- **Explique por que essa melhoria seria útil** para a maioria dos usuários do Python Basics. Você também pode mencionar outros projetos que resolveram melhor esse problema e que poderiam servir de inspiração.

<!-- Você pode criar um template de issue para sugestões de melhoria que pode ser usado como guia e que define a estrutura das informações a serem incluídas. Se fizer isso, faça referência a ele aqui na descrição. -->

### Sua Primeira Contribuição de Código
<!-- TODO
include Setup of env, IDE and typical getting started instructions?

-->

```bash
# Clone o repositório
git clone

# Entre no diretório
cd python-basics

# Instale as dependências
pip install -r requirements.txt

# Execute os testes
pytest
```

<!-- omit in toc -->
## Atribuição
Este guia é baseado no **contributing-gen**. [Faça o seu](https://github.com/bttger/contributing-gen)!
