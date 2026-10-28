Na linguagem do dia a dia, "cooler" e "dissipador" são usados como sinônimos, mas **tecnicamente são coisas diferentes**. Por isso eles ganharam módulos separados:

- **Dissipador** (*heatsink*): a peça de **metal** que **retira o calor** do componente e o espalha numa grande área. É **passivo**: não tem motor.
- **Cooler / ventoinha** (*fan*): o **ventilador** que **empurra o ar** através do dissipador. É **ativo**.

O conjunto dissipador + ventoinha também é chamado de cooler. Ex.: "cooler box", "cooler tower".

## O que é

O **dissipador** é um bloco de metal **bom condutor de calor**, com muitas **aletas** (lâminas finas) para aumentar a **área de contato com o ar**. Ele fica **encostado** no componente quente, com uma camada de **pasta térmica** (ou *thermal pad*) entre os dois.

## Para que serve: sua função

Todo componente eletrônico transforma praticamente **100% da energia que consome em calor**. Uma CPU de 150 W é, termicamente, um **aquecedor de 150 W** numa área do tamanho de uma unha. Sem dissipador, ela passaria de 100 °C em **segundos** e desligaria (ou queimaria, nas CPUs antigas sem proteção).

O dissipador serve para:
1. **Puxar o calor** do componente por **condução**.
2. **Espalhar** esse calor por uma grande superfície.
3. **Entregar o calor ao ar** por **convecção** (com ou sem ajuda de ventoinha).

:::exemplo Exemplo: por que o dissipador importa para abrir abas, editar vídeo e gerar imagens
- **Abas e navegação**: a CPU trabalha em "rajadas". Um dissipador bom absorve os picos e mantém o clock alto, deixando o sistema mais responsivo.
- **Exportar um vídeo de 20 minutos**: a CPU fica em 100% por vários minutos. Com dissipador fraco, ela atinge o limite de temperatura e **reduz o clock**, e a exportação pode levar **20–40% mais tempo**.
- **Gerar imagens com IA na GPU**: a GPU fica em carga máxima; o **dissipador da placa de vídeo** decide se ela mantém o boost ou cai de frequência.
:::

## Como funciona: a física em três etapas

1. **Condução**: o calor passa do chip para o **IHS**, do IHS para a **pasta térmica** e da pasta para a **base do dissipador**. Por isso a base precisa ser **plana e de cobre**, ou ter **heatpipes em contato direto**.
2. **Transporte**: nos dissipadores modernos, **heatpipes** (tubos de cobre) levam o calor rapidamente da base até as aletas.
3. **Convecção**: o calor passa das aletas para o **ar**. Na **convecção natural**, o ar quente sobe sozinho; na **convecção forçada**, a ventoinha empurra o ar, o que é muito mais eficiente.

### Heatpipe: o "segredo" dos dissipadores modernos
Um **heatpipe** é um **tubo de cobre selado, com vácuo parcial e um pouco de líquido** (normalmente **água**). Por dentro, a parede tem uma estrutura porosa (de cobre sinterizado ou ranhuras):
1. Na ponta quente (base), o líquido **evapora** e absorve muito calor (calor latente).
2. O vapor corre até a ponta fria (as aletas) e **condensa**, liberando o calor.
3. O líquido volta pela estrutura porosa, por **capilaridade**, e o ciclo recomeça.

Um heatpipe conduz calor **dezenas ou centenas de vezes melhor** que uma barra de cobre maciça do mesmo tamanho.

### Câmara de vapor (*vapor chamber*)
É um "heatpipe achatado": uma placa oca que espalha o calor em **duas dimensões**. É usada em **placas de vídeo topo de linha**, **notebooks** e **celulares**.

## Material

| Material | Condutividade térmica (W/m·K) | Onde se usa |
|---|---|---|
| **Prata** | ≈ 430 | Raramente (muito cara) |
| **Cobre** | ≈ **400** | Bases, heatpipes, dissipadores premium |
| **Alumínio** | ≈ **205–237** | **Aletas** (leve e barato) |
| **Cobre niquelado** | ≈ 400 (cobre com camada fina de níquel contra oxidação) | Bases e heatpipes |
| Aço | ≈ 50 | Nunca em dissipador (só em suportes) |

O padrão da indústria é **base e heatpipes de cobre + aletas de alumínio**: o melhor equilíbrio entre desempenho, peso e preço.

## Pasta térmica e materiais de interface (TIM)

Superfícies metálicas que parecem lisas têm **imperfeições microscópicas**, com **ar** preso entre elas, e o ar é **péssimo condutor** (≈ 0,026 W/m·K). A **pasta térmica** preenche esses espaços.

| Tipo de TIM | Condutividade típica | Prós | Contras | Preço |
|---|---|---|---|---|
| **Pasta de silicone (branca, genérica)** | ≈ 0,5–1 W/m·K | Barata | Fraca, seca rápido | R$ 5–15 |
| **Pasta cerâmica/metálica de qualidade** (Arctic MX-4/MX-6, Noctua NT-H1/H2, Thermal Grizzly Kryonaut) | ≈ 5–13 W/m·K | Boa, **não condutiva** | Precisa trocar a cada 2–4 anos | R$ 30–100 |
| **Metal líquido** (gálio) | ≈ 70 W/m·K | Excelente | **Conduz eletricidade** (risco de curto); **corrói alumínio** | R$ 80–150 |
| **Thermal pad** | ≈ 1–15 W/m·K | Limpo, fácil | Espessura precisa estar certa | R$ 20–80 |
| **PTM (material de mudança de fase, ex.: Honeywell PTM7950)** | Alto; derrete com o calor | Durável, não seca | Exige ciclo de aquecimento | R$ 40–100 |

:::dica Quanto de pasta usar
Para CPUs de desktop, **um "grão de ervilha" no centro** (ou um "X" fino nos processadores maiores, como os Intel LGA1700/1851 e os Threadripper) é suficiente. A pressão do cooler espalha a pasta. **Pasta demais não ajuda** e suja o soquete; **de menos** deixa áreas sem contato. **Nunca espalhe com o dedo**, porque a gordura da pele atrapalha.
:::

## Tipos de dissipador

| Tipo | Como é | Uso | Capacidade típica |
|---|---|---|---|
| **Passivo (sem ventoinha)** | Bloco de alumínio com aletas grandes | Chipsets, VRM, SSDs M.2, PCs *fanless* | Até ≈ 10–35 W (depende muito do tamanho) |
| **Top-flow (box, de fábrica)** | Bloco de alumínio, às vezes com núcleo de cobre, ventoinha soprando para baixo | CPUs de entrada (Intel Laminar, AMD Wraith) | ≈ 65–95 W |
| **Tower (torre) com heatpipes** | Torre de aletas atravessada por 4–7 heatpipes, ventoinha lateral | O mais usado em PCs montados | 150–250 W |
| **Dual tower** | Duas torres e 1–2 ventoinhas | CPUs topo de linha | 220–300 W |
| **Low profile** | Baixo (< 70 mm) | PCs compactos e slim | 65–120 W |
| **Dissipador de GPU** | Grande, com heatpipes ou câmara de vapor + 2 ou 3 ventoinhas | Placas de vídeo | 100–600 W |
| **Dissipador de VRM / chipset / M.2** | Placas de alumínio sobre os chips | Placas-mãe | 5–30 W |
| **Bloco de water cooler (*waterblock*)** | Base de cobre com microcanais por onde passa o líquido | Water cooling (próximo módulo) | Depende do radiador |

### Contato direto × base plana
- **Heatpipe Direct Touch (HDT)**: os heatpipes encostam **diretamente** na CPU. É barato e eficiente, mas o contato perde eficiência se houver espaço entre os tubos.
- **Base de cobre plana**: os heatpipes ficam soldados numa base usinada. Tem contato mais uniforme e costuma aparecer nos modelos melhores.

## Preço médio (Brasil, out/2026)

| Categoria | Exemplos | Preço |
|---|---|---|
| Dissipador passivo de M.2 | Genéricos | R$ 20–60 |
| Cooler box (de fábrica) | Vem com a CPU | Incluso |
| Torre de entrada (4 heatpipes) | DeepCool AK400 (≈ R$ 150 no Pix), Thermalright Assassin X 120, Rise Mode | R$ 100–220 |
| Torre intermediária (5–6 heatpipes) | Thermalright Peerless Assassin 120 SE (≈ R$ 350), DeepCool AK620 | R$ 250–450 |
| Topo de linha | Noctua NH-D15 G2, Thermalright Frost Spirit 140 | R$ 450–1.200 |

## Como escolher

1. **TDP ou consumo real** da CPU: o dissipador deve dar conta, com folga, da potência máxima (PPT).
2. **Compatibilidade com o soquete**: AM4, AM5, LGA1700, LGA1851. Atenção: os coolers de **LGA1700 servem no LGA1851** (mesma furação); os de AM4 servem no AM5 na maioria dos casos.
3. **Altura máxima** que o gabinete aceita (ex.: "CPU cooler height: 160 mm").
4. **Espaço da memória RAM**: torres grandes podem encostar em pentes altos, com dissipador ou RGB.
5. **Ruído**: modelos maiores dissipam mais com a ventoinha mais lenta, ou seja, com menos barulho.

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **Pasta seca ou ressecada** | Temperatura subindo ao longo dos meses | Pasta de qualidade; trocar a cada 2–4 anos | Remover com álcool isopropílico e reaplicar |
| **Esquecer a película plástica** da base | Temperatura altíssima já no primeiro uso | Sempre conferir a base antes de instalar | Remover a película, limpar e reaplicar a pasta |
| **Aletas entupidas de poeira** | Temperatura e ruído altos | Filtros no gabinete | Ar comprimido ou soprador, com a ventoinha **travada** (não deixe girar livre: o giro gera corrente que pode danificar o motor e a placa) |
| **Contato ruim / pressão desigual** | Um núcleo muito mais quente que os outros | Apertar os parafusos em "X", aos poucos | Reinstalar |
| **Dissipador pesado entortando a placa** | Placa empenada | Usar o *backplate*; não transportar o PC com torre grande montada | Retirar o dissipador para transporte |
| **Metal líquido sobre alumínio** | Corrosão e "liga" destruída | **Nunca** usar metal líquido com alumínio | Trocar o dissipador |
| **Dissipador incompatível com o gabinete** | Lateral não fecha | Conferir a altura antes de comprar | Trocar por um *low profile* ou trocar o gabinete |

:::exemplo Exemplo de bancada: a CPU a 100 °C "do nada"
Um notebook de 3 anos esquentava a ponto de desligar jogando. Ao abrir, o técnico encontrou a pasta térmica **completamente seca** (virou pó) e as **aletas do dissipador** (na saída de ar, atrás das ventoinhas) **cobertas por um "carpete" de poeira**. Depois da limpeza e da troca da pasta por uma de qualidade, a temperatura em jogo caiu de **98 °C para 78 °C**, e o FPS subiu, porque a CPU parou de reduzir o clock.
:::
