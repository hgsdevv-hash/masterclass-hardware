"Qual foi o primeiro computador?" parece uma pergunta simples, mas é uma das mais debatidas da história da tecnologia. A resposta depende de **qual definição de computador** você usa. Vamos resolver isso com critério de professor e depois mergulhar no ENIAC, o gigante que virou símbolo da era eletrônica.

## O debate: depende da definição

Para chamar uma máquina de "computador moderno", os historiadores costumam exigir quatro características:

1. **Eletrônico**: funciona com válvulas ou transistores, não com engrenagens ou relés.
2. **Digital**: trabalha com valores discretos, não contínuos.
3. **Programável**: dá para mudar a tarefa sem reconstruir a máquina.
4. **De propósito geral (Turing-completo)**: em teoria, resolve qualquer problema computável.

E existe um quinto critério, o mais rigoroso: **programa armazenado**, em que as instruções ficam na mesma memória que os dados.

| Máquina | Ano | Eletrônico | Digital | Programável | Propósito geral | Programa armazenado | Veredito |
|---|---|---|---|---|---|---|---|
| Máquina Analítica (Babbage) | 1837 (projeto) | ❌ | ✅ | ✅ | ✅ | ❌ | Primeiro **projeto** de computador, nunca construído |
| Z3 (Zuse) | 1941 | ❌ (relés) | ✅ | ✅ | ✅ (provado em 1998) | ❌ | Primeiro **programável e automático funcional** |
| ABC (Atanasoff-Berry) | 1942 | ✅ | ✅ | ❌ | ❌ | ❌ | Primeiro **eletrônico digital** |
| Colossus | 1944 | ✅ | ✅ | Parcial | ❌ | ❌ | Primeiro eletrônico programável, mas especializado |
| **ENIAC** | **1945/46** | ✅ | ✅ | ✅ | ✅ | ❌ (depois de 1948, parcialmente) | Primeiro **eletrônico, digital, programável e de propósito geral** |
| Manchester Baby | 1948 | ✅ | ✅ | ✅ | ✅ | ✅ | Primeiro com **programa armazenado** |

:::dica Resposta de prova
Se perguntarem numa prova ou entrevista: **"O ENIAC é considerado o primeiro computador eletrônico digital de propósito geral."** E vale complementar: *"O Z3 de Konrad Zuse (1941) foi o primeiro computador programável funcional, mas era eletromecânico, e o ABC (1942) foi o primeiro eletrônico digital, mas não era programável."* Essa resposta mostra domínio do debate.
:::

### O caso na Justiça: Honeywell x Sperry Rand (1973)
Eckert e Mauchly patentearam o ENIAC. Em **19 de outubro de 1973**, na disputa judicial **Honeywell v. Sperry Rand**, um juiz federal dos EUA **invalidou a patente**. Ele considerou que Mauchly tinha visitado **John Atanasoff** em 1941 e se inspirado no ABC. Com isso, a ideia de "computador eletrônico digital" passou a ser de **domínio público**, o que ajudou a indústria a crescer sem pagar royalties.

## ENIAC em detalhes

**ENIAC** significa *Electronic Numerical Integrator and Computer* (Integrador e Computador Numérico Eletrônico).

### Origem
- **Por quê**: o Exército dos EUA precisava calcular **tabelas de tiro de artilharia**, que dizem como apontar um canhão de acordo com distância, vento e tipo de munição. Uma única trajetória levava cerca de **20 horas** à mão com calculadora de mesa.
- **Quem**: **John Mauchly** (físico) e **J. Presper Eckert** (engenheiro eletrônico), na **Moore School of Electrical Engineering, Universidade da Pensilvânia**.
- **Quando**: contrato secreto assinado em **junho de 1943** (Projeto PX). A máquina ficou pronta no fim de **1945** e foi apresentada à imprensa em **14 de fevereiro de 1946** (a dedicação formal foi no dia 15).
- **Custo**: cerca de **US$ 487 mil** da época, algo como US$ 8 milhões em valores atuais.

### Ficha técnica

| Característica | Valor |
|---|---|
| Válvulas termiônicas | **17.468** (algumas fontes arredondam para 18.000) |
| Diodos de cristal | ≈ 7.200 |
| Relés | ≈ 1.500 |
| Resistores | ≈ 70.000 |
| Capacitores | ≈ 10.000 |
| Juntas soldadas à mão | ≈ **5 milhões** |
| Peso | ≈ **27 toneladas** |
| Área ocupada | ≈ **167 m²** (uma sala de 9 × 15 m) |
| Consumo elétrico | ≈ **150–160 kW** (o equivalente a uns 27 chuveiros elétricos de 5.500 W ligados ao mesmo tempo) |
| Velocidade | ≈ **5.000 somas por segundo** |
| Sistema numérico | **Decimal** (não binário), com 20 acumuladores de 10 dígitos |
| Programação | Cabos e chaves, reconectados à mão |

:::exemplo Exemplo: ENIAC x celular
O ENIAC fazia **5.000 somas por segundo**. Um celular intermediário de 2026 faz **trilhões de operações por segundo**, ou seja, centenas de milhões de vezes mais. E pesa 200 gramas contra 27 toneladas, gastando cerca de 5 watts contra 150.000 watts. Seu celular de bolso é mais potente que todos os computadores do mundo juntos em 1960.
:::

### Como o ENIAC funcionava
- **Válvulas como interruptores**: cada válvula era um tubo de vidro a vácuo com um filamento aquecido. Conforme a tensão aplicada, ela deixava ou não a corrente passar, funcionando como um "liga/desliga" eletrônico, sem partes móveis, milhares de vezes mais rápido que um relé.
- **Contadores em anel**: para guardar um algarismo de 0 a 9, o ENIAC usava **10 válvulas em anel** (na verdade, flip-flops), das quais só uma ficava "acesa". Isso explica por que ele precisava de tantas válvulas.
- **Programação física**: não havia teclado nem tela. Programar era **reconectar cabos em painéis** e ajustar milhares de chaves. Trocar de programa levava **dias**.
- **Problema das válvulas queimadas**: com 17 mil válvulas, uma queimava a cada um ou dois dias. A equipe descobriu que a maioria queimava ao **ligar** a máquina (pelo choque térmico) e passou a **deixá-la sempre ligada**. Também usava válvulas de qualidade selecionada e com tensão reduzida. A disponibilidade passou a ser boa para a época.

### As programadoras do ENIAC
O ENIAC foi programado por seis matemáticas, que **não foram citadas** na apresentação de 1946 e só receberam reconhecimento décadas depois:

- **Kathleen "Kay" McNulty**
- **Betty Jean Jennings (Bartik)**
- **Frances "Betty" Snyder (Holberton)**
- **Marlyn Wescoff (Meltzer)**
- **Frances Bilas (Spence)**
- **Ruth Lichterman (Teitelbaum)**

Elas aprenderam a programar **pelos diagramas elétricos**, sem manual e sem linguagem de programação. Betty Holberton depois ajudou a criar o **COBOL** e o primeiro programa de ordenação (*sort-merge*) do UNIVAC. Elas foram incluídas no **Women in Technology International Hall of Fame** em 1997.

### Fim e legado
- O ENIAC foi transferido para o Campo de Provas de Aberdeen em 1947, recebeu modificações em 1948 para executar programas guardados em tabelas de funções (uma forma primitiva de programa armazenado) e foi **desligado em 2 de outubro de 1955**.
- Ele calculou tabelas balísticas, estudos para a **bomba de hidrogênio**, previsões do tempo (1950) e números de π e *e*.
- Partes dele estão expostas na Universidade da Pensilvânia, no Smithsonian (Washington) e em Fort Sill (Oklahoma).
- O mais importante: o projeto do ENIAC reuniu Mauchly, Eckert e **John von Neumann**, e daí saiu a arquitetura que todos os computadores usam até hoje (próximo módulo).

:::curiosidade O mito do "bug"
É comum dizer que o termo "bug" nasceu de um inseto no ENIAC, mas não foi lá. Em **9 de setembro de 1947**, a equipe de **Grace Hopper**, no **Harvard Mark II**, encontrou uma **mariposa presa num relé** e a colou no diário de bordo com a anotação *"First actual case of bug being found"*. A palavra "bug" já era usada por engenheiros desde o tempo de Thomas Edison; a graça estava em ser um bug **de verdade**. O diário está no Smithsonian.
:::
