A internet não foi inventada por uma pessoa, nem num dia. Ela é uma **rede de redes**, construída em camadas, ao longo de décadas, por militares, cientistas, universidades e, depois, empresas. E é importante separar logo dois conceitos que quase todo mundo confunde:

:::atencao Internet ≠ Web
- **Internet** é a **infraestrutura**: cabos, roteadores, satélites e o protocolo **TCP/IP** que liga bilhões de dispositivos. Nasceu entre **1969** (ARPANET) e **1983** (adoção do TCP/IP).
- **World Wide Web (WWW)** é **um serviço que roda sobre a internet**: páginas ligadas por links, acessadas por navegador. Nasceu entre **1989 e 1991**, no CERN.

E-mail, WhatsApp, jogos online e streaming também usam a internet, mas **não são a Web**.
:::

## 1. O contexto: Guerra Fria (1957–1962)

- Em **4 de outubro de 1957**, a União Soviética lançou o **Sputnik**, o primeiro satélite artificial. Os EUA ficaram em choque.
- Em resposta, em **1958** foi criada a **ARPA** (*Advanced Research Projects Agency*, hoje **DARPA**), para financiar pesquisa de ponta.
- Em **1962**, **J. C. R. Licklider** (MIT/ARPA) escreveu memorandos sobre uma **"Rede Galáctica"**: computadores interligados no mundo todo, acessíveis de qualquer lugar. Era a visão da internet, 30 anos antes.

## 2. A grande ideia técnica: comutação de pacotes (1960–1965)

Antes, as redes funcionavam como o **telefone antigo**: abria-se um **circuito dedicado** entre as duas pontas (a comutação de circuitos). Se um trecho caísse, a ligação caía.

Dois pesquisadores tiveram, de forma independente, a mesma ideia:
- **Paul Baran** (RAND Corporation, EUA, 1960–1964): uma rede **distribuída**, sem centro, capaz de sobreviver a um ataque nuclear.
- **Donald Davies** (National Physical Laboratory, Reino Unido, 1965–1966): concebeu a ideia em 1965 e criou o termo **"pacote"** num documento de 1966.
- **Leonard Kleinrock** (MIT/UCLA) desenvolveu a **teoria matemática** das filas em redes (tese de 1962, livro de 1964). Atribuir a ele a invenção da comutação de pacotes é controverso: esse crédito costuma ir para Baran e Davies.

**Como funciona a comutação de pacotes**: a mensagem é dividida em pedaços (**pacotes**), cada um com o endereço de destino. Cada pacote pode seguir **um caminho diferente** e, no destino, eles são **remontados na ordem certa**. Se um caminho cair, os pacotes desviam.

:::exemplo Exemplo: os Correios e o quebra-cabeça
Imagine mandar um quebra-cabeça de 1.000 peças para outra cidade, colocando **cada peça num envelope** com o endereço e o número da peça. Os envelopes vão por caminhões diferentes, chegam fora de ordem, e quem recebe monta o quebra-cabeça pelos números. Se um envelope se perder, o destinatário pede de novo só a peça 347. É exatamente assim que uma foto viaja pelo WhatsApp: em milhares de pacotes.
:::

## 3. ARPANET: a primeira rede (1969)

- Em **29 de outubro de 1969, por volta das 22h30**, o estudante **Charley Kline**, no laboratório de **Leonard Kleinrock** na **UCLA**, tentou enviar a palavra **"LOGIN"** para o computador do **SRI (Stanford Research Institute)**, a cerca de 560 km.
- O sistema **travou depois das letras "L" e "O"**. A primeira mensagem da história da internet foi, sem querer, **"LO"** ("lo and behold", algo como "eis que..."). Uma hora depois, o LOGIN completo funcionou.
- Os equipamentos de rede eram os **IMPs** (*Interface Message Processors*), minicomputadores Honeywell programados pela empresa **BBN**: os primeiros **roteadores** da história.
- Em **dezembro de 1969**, a ARPANET tinha **4 nós**: **UCLA, SRI, UC Santa Barbara e Universidade de Utah**.

| Ano | Tamanho da ARPANET |
|---|---|
| 1969 | 4 nós |
| 1971 | 15 nós |
| 1973 | ≈ 40 nós (primeiras conexões internacionais: Noruega e Inglaterra) |
| 1981 | 213 *hosts* (computadores conectados) |

## 4. E-mail e a arroba (1971)

Em **1971**, **Ray Tomlinson** (BBN) enviou o primeiro **e-mail entre computadores diferentes** pela ARPANET. Ele escolheu o símbolo **@** (*at*, "em") para separar o usuário do computador: `usuario@computador`. Ele não lembrava o conteúdo da mensagem; provavelmente era algo como "QWERTYUIOP". O e-mail virou rapidamente o principal uso da rede.

## 5. TCP/IP: a "língua comum" das redes (1974–1983)

Nos anos 1970 surgiram várias redes diferentes (rádio, satélite, ARPANET) que **não conversavam entre si**. **Vint Cerf e Bob Kahn** publicaram em **1974** o artigo *A Protocol for Packet Network Intercommunication*, descrevendo o **TCP**, mais tarde dividido em **TCP + IP**:

| Protocolo | Função | Analogia |
|---|---|---|
| **IP** (*Internet Protocol*) | Endereça e encaminha cada pacote | O **endereço** escrito no envelope |
| **TCP** (*Transmission Control Protocol*) | Garante que todos os pacotes cheguem, na ordem, sem erro | O **aviso de recebimento** e a numeração das peças |
| **UDP** | Envia rápido, sem garantia | Panfleto jogado por baixo da porta (usado em chamadas de vídeo e jogos) |

Em **1º de janeiro de 1983** (o *flag day*), a ARPANET trocou oficialmente seu protocolo antigo (NCP) pelo **TCP/IP**. Muitos historiadores consideram essa data o **nascimento da internet** como a conhecemos.

## 6. DNS: nomes em vez de números (1983–1985)

Cada computador tem um endereço **IP** numérico (por exemplo, `142.250.79.46`). Decorar isso é impossível. Em **1983**, **Paul Mockapetris** criou o **DNS** (*Domain Name System*), a "lista telefônica" da internet, que traduz `google.com` em números. Os primeiros domínios `.com` foram registrados em **1985** (o primeiro foi **symbolics.com**, em 15 de março de 1985).

:::exemplo Exemplo: o que acontece quando você digita um endereço
1. Você digita `hgsdev.com.br`.
2. O computador pergunta ao **servidor DNS**: "qual é o IP de hgsdev.com.br?"
3. O DNS responde com um número IP.
4. O navegador abre uma conexão **TCP** com esse IP e pede a página por **HTTPS**.
5. A página chega em pacotes, que são remontados e desenhados na tela.

Tudo isso leva, normalmente, **menos de meio segundo**.
:::

## 7. NSFNET: a internet sai do quartel e vai para a universidade (1986–1995)

- Em **1986**, a **NSF** (Fundação Nacional de Ciência dos EUA) criou a **NSFNET**, um *backbone* (espinha dorsal) de alta velocidade ligando supercomputadores e universidades. Ela substituiu a ARPANET, que foi **desligada em 1990**.
- Ao redor do mundo, redes acadêmicas se conectaram à NSFNET, entre elas as do Brasil (próximo módulo).
- Em **1995**, a NSFNET foi desativada e o tráfego passou para **provedores comerciais**. A internet virou um negócio.

## 8. A World Wide Web (1989–1993)

- Em **março de 1989**, o físico britânico **Tim Berners-Lee**, do **CERN** (laboratório europeu de física, na Suíça), escreveu a proposta *Information Management: A Proposal*. O chefe dele anotou na capa: *"Vague but exciting..."* ("Vago, mas empolgante...").
- Entre **1990 e 1991**, com **Robert Cailliau**, ele criou os três pilares da Web:
  - **HTML**: a linguagem das páginas.
  - **HTTP**: o protocolo que transfere as páginas.
  - **URL**: o endereço de cada recurso.
- Criou também o **primeiro navegador** (chamado *WorldWideWeb*, depois *Nexus*) e o **primeiro servidor web**, num computador **NeXT** com um adesivo que dizia: *"This machine is a server. DO NOT POWER IT DOWN!!"*
- O **primeiro servidor**, `info.cern.ch`, funcionava no CERN desde **dezembro de 1990**. Em **6 de agosto de 1991**, Berners-Lee anunciou a Web publicamente no grupo de discussão *alt.hypertext*. O site ainda está no ar, restaurado pelo CERN.
- Em **30 de abril de 1993**, o CERN colocou a Web em **domínio público, sem royalties**. Essa decisão fez a Web explodir.

:::especialista Tim Berners-Lee
Berners-Lee nunca patenteou a Web. Ele foi nomeado cavaleiro (Sir) em 2004, ganhou o **Prêmio Turing de 2016** (anunciado em 2017) e fundou o **W3C**, consórcio que mantém os padrões da Web até hoje. Na abertura das Olimpíadas de Londres (2012), apareceu digitando a mensagem *"This is for everyone"* ("Isto é para todos").
:::

## 9. Navegadores, empresas e a bolha (1993–2001)

| Ano | Marco |
|---|---|
| 1993 | **Mosaic** (NCSA, Marc Andreessen e Eric Bina): primeiro navegador popular com imagens na página |
| 1994 | **Netscape Navigator**; fundação da **Amazon** e do **Yahoo!** |
| 1995 | **Internet Explorer**, **eBay**, linguagem **JavaScript** (Brendan Eich, em 10 dias) |
| 1997 | **Wi-Fi** (padrão IEEE 802.11) |
| 1998 | **Google** |
| 2000–2001 | Estouro da **bolha da internet** (*dot-com*): empresas sem lucro quebram |

## 10. Web 2.0, mobile, nuvem e o mundo atual (2004–hoje)

| Período | O que mudou |
|---|---|
| 2004–2006 | **Web 2.0**: o usuário cria conteúdo (Facebook, YouTube, Wikipedia, Orkut, que foi febre no Brasil) |
| 2007–2010 | **Smartphones** e **3G/4G**: a internet vai para o bolso |
| 2010–2020 | **Nuvem**, **streaming** (Netflix, Spotify), **redes sociais** e apps de mensagem |
| 2012 | **IPv6** ativado em larga escala, porque os endereços IPv4 estavam acabando (só existem cerca de 4,3 bilhões) |
| 2019–hoje | **5G**, **Wi-Fi 6/7**, **fibra óptica** residencial, internet via satélite de baixa órbita (Starlink) |
| 2022–hoje | **IA generativa** acessada pela internet |

:::curiosidade Curiosidade: quem "manda" na internet?
Ninguém sozinho. Os padrões técnicos são definidos pela **IETF** (documentos chamados RFCs), os padrões da Web pelo **W3C**, e os números IP e nomes de domínio são coordenados pela **ICANN/IANA**. Cada país administra seu domínio; o `.br` é do **NIC.br**.
:::

## As camadas da internet (modelo TCP/IP)

| Camada | O que faz | Exemplos |
|---|---|---|
| **Aplicação** | O serviço que o usuário usa | HTTP/HTTPS (Web), SMTP (e-mail), DNS |
| **Transporte** | Entrega confiável ou rápida | TCP, UDP |
| **Internet (rede)** | Endereçamento e rota | IP (IPv4, IPv6) |
| **Acesso à rede (enlace + físico)** | O meio físico | Ethernet (cabo), Wi-Fi, fibra, 4G/5G |

A **placa de rede** do seu computador trabalha nas camadas mais baixas (física e enlace). Veremos isso em detalhe no módulo de Placa de Rede.
