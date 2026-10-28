Antes de abrir qualquer gabinete, três temas precisam estar dominados: **eletricidade estática**, **oxidação** e **manuseio correto dos componentes**. São responsáveis por uma parte enorme das "peças que pararam do nada" nas bancadas.

## O que é a estática no hardware

### Definição
**Eletricidade estática** é o **acúmulo de carga elétrica** na superfície de um corpo, seja você, uma blusa de lã ou um saco plástico. Ela surge pelo **efeito triboelétrico**: quando dois materiais se atritam e se separam, elétrons passam de um para o outro.

Quando o corpo carregado encosta num objeto com potencial diferente (um componente, uma maçaneta), a carga **descarrega de uma vez**. Isso se chama **ESD** (*Electrostatic Discharge*, ou descarga eletrostática).

### Por que é perigosa para o hardware
| Tensão da descarga | O que acontece |
|---|---|
| ≈ 3.000 V | Você **sente** um choquinho |
| ≈ 5.000 V | Você **ouve** o estalo |
| ≈ 10.000 V | Você **vê** a faísca |
| **A partir de ≈ 10–100 V** | Já pode **danificar** transistores sensíveis (CMOS, MOSFET) |

Ou seja, **o componente pode ser danificado por uma descarga que você nem sente**. Caminhar num carpete com sapato de borracha num dia seco pode gerar **mais de 10.000 V** no corpo.

:::exemplo Exemplo: o tipo de dano
- **Dano catastrófico**: a peça morre na hora. A memória para de ser reconhecida, a placa não liga.
- **Dano latente (o pior)**: a descarga enfraquece o óxido isolante de alguns transistores. A peça **funciona**, mas passa a dar **telas azuis aleatórias, travamentos e corrupção de dados** semanas depois, e o técnico raramente associa à estática.
:::

### Quando o risco é maior
- **Clima seco** (inverno no Centro-Oeste e no Sudeste, umidade abaixo de 30–40%).
- **Roupas de lã, poliéster ou fleece**.
- **Carpetes e tapetes** sintéticos.
- **Cadeiras com rodinhas** de plástico.
- **Sacos plásticos comuns** e **isopor** perto das peças.

### Como evitar: o protocolo antiestático
1. **Pulseira antiestática** (≈ R$ 15–40): use no pulso, com a garra ligada a uma **parte metálica sem pintura do gabinete** ou a um ponto de terra. Ela tem um resistor de **1 MΩ** interno, que escoa a carga devagar e também protege você caso encoste em algo energizado.
2. **Manta antiestática** de bancada (≈ R$ 50–200): superfície dissipativa aterrada.
3. **Toque no gabinete metálico** antes de pegar uma peça, se não tiver pulseira. É um paliativo, não substituto.
4. **Desligue o PC da tomada** e aperte o botão de ligar por alguns segundos para descarregar os capacitores.
5. **Guarde as peças em embalagens antiestáticas** (os sacos prateados e metalizados ou os rosados dissipativos). **Nunca coloque uma peça em cima do saco antiestático** pensando que está protegida: o lado de fora pode ser condutivo. A peça vai **dentro**.
6. **Evite roupas sintéticas** e trabalhe descalço ou com calçado de couro num piso não acarpetado, se possível.
7. **Não ande** pela sala segurando uma peça desprotegida.

:::atencao Nunca use pulseira antiestática com o PC ligado na tomada sem saber o que está fazendo
A pulseira serve para trabalhar com o equipamento **desenergizado**. Trabalhar com a fonte ligada e o corpo aterrado aumenta o risco de choque se você encostar no primário da fonte.
:::

## Oxidação: por que "soprar" não resolve

### O que é oxidação
**Oxidação** é a reação química do **metal com o oxigênio** (e a umidade) do ar, formando uma camada de **óxido** na superfície. Nos contatos elétricos, essa camada **aumenta a resistência** e causa **mau contato**. É o que aparece como:
- Pontos **escurecidos ou esverdeados** nos contatos (o "azinhavre" do cobre).
- Memória RAM que "às vezes funciona".
- Placa de vídeo que dá **tela preta** até ser reencaixada.

Os contatos de memória e placas de vídeo são **banhados a ouro** justamente porque o ouro **praticamente não oxida**. Mas a camada é finíssima (micrômetros) e, com o tempo, poeira, gordura dos dedos, umidade, maresia (no litoral, onde o sal acelera tudo) e o próprio metal por baixo podem gerar sujeira e corrosão.

### O mito do "assoprar" (cartucho de videogame e pente de memória)
Gerações cresceram **assoprando cartuchos** de Nintendo e Mega Drive, e muita gente ainda **sopra pentes de memória** e o slot. **Isso não ajuda, e piora a situação**:

1. O sopro leva **saliva e umidade** aos contatos, o que **acelera a oxidação**.
2. A saliva tem **sais e enzimas** que deixam resíduos condutivos e corrosivos.
3. O que "conserta" na hora é o simples fato de **retirar e reencaixar**: o atrito raspa um pouco da sujeira e da oxidação, e o contato melhora. O sopro leva o crédito sem merecer.

:::especialista O que diz a Nintendo
Materiais de suporte da **Nintendo**, amplamente citados pela imprensa de games, orientam a **não assoprar** os cartuchos, porque a umidade do sopro pode corroer os contatos. A recomendação dela era limpar com cotonete e álcool isopropílico.
:::

### Como limpar contatos corretamente
| Situação | Como fazer |
|---|---|
| **Contatos dourados de memória e placa de vídeo** | Use **borracha escolar branca** (macia, sem pó colorido), esfregando no sentido **do contato para a borda**, com o pente apoiado e sem dobrar. Depois, passe um pincel ou pano sem fiapos com **álcool isopropílico 99%** e espere secar |
| **Slots e soquetes** | **Ar comprimido em lata** (em jatos curtos, com a lata **de pé**, para não sair líquido congelado) ou soprador elétrico; **pincel antiestático** |
| **Oxidação forte e esverdeada** | Álcool isopropílico + escova macia; em casos persistentes, **limpa-contatos** específico para eletrônica. **Nunca** use palha de aço, lixa ou lâmina, porque elas arrancam a camada de ouro |
| **Placa com resíduo de líquido derramado** | Desligue, retire a bateria (notebook), limpe com **isopropílico 99%** e escova macia o quanto antes; casos graves vão para banho em **lavadora ultrassônica** de bancada |

:::atencao Álcool certo
Use **álcool isopropílico (99%)**. O **álcool comum (etílico 70% ou 46°)** tem muita **água** e aditivos que podem deixar resíduos e causar curto ou oxidação. O isopropílico evapora rápido, quase sem deixar resíduo, e é encontrado em lojas de eletrônica e farmácias por ≈ R$ 25–50 o litro.
:::

## Como manusear os componentes

### Regras gerais
1. **Segure pelas bordas.** Nunca encoste os dedos nos **contatos dourados**, nos **pinos do processador**, nos **chips** ou nas **trilhas**. A gordura da pele causa oxidação e mau contato.
2. **Trabalhe numa superfície firme, limpa, seca e não condutora** (madeira ou manta antiestática), com boa iluminação.
3. **Organize os parafusos** num pote ou numa bandeja magnética, separando os de cada parte.
4. **Nunca force.** Se um conector não entra, ele está **na posição errada**. Quase todos os conectores de PC têm **chanfro ou trava** (*keying*) que só permite uma posição.
5. **Desconecte os cabos pelo conector**, nunca puxando pelos fios.
6. **Fotografe antes de desmontar**: ligações dos cabos do painel frontal, posição das memórias, roteamento dos cabos.

### Manuseio de cada componente
| Componente | Cuidado específico |
|---|---|
| **Processador** | Segure pelas laterais. Nos **Intel (LGA)** os pinos ficam **no soquete da placa** e entortam com qualquer toque; **mantenha a tampa plástica** até instalar. Nos **AMD AM4 (PGA)** os pinos ficam **no processador**; não o deixe cair nem o apoie de face para baixo. Os **AMD AM5** são LGA, como os Intel |
| **Memória RAM** | Segure pelas bordas curtas. Alinhe o **entalhe (chanfro)** com o slot e pressione **as duas pontas por igual**, até as travas fecharem com um "clique" |
| **Placa de vídeo** | Segure pela proteção ou pela placa traseira; nunca pelas ventoinhas. Use o **suporte (*anti-sag*)** se ela for pesada; GPUs modernas pesam mais de 1,5 kg e podem trincar o slot com o tempo |
| **SSD M.2** | Insira inclinado a ≈ 30°, abaixe e fixe com o parafuso ou a trava. **Não aperte demais** o parafuso pequeno |
| **HD** | Nunca o derrube nem bata, principalmente **ligado** (a cabeça de leitura pode riscar os pratos). Instale com parafusos que absorvem vibração |
| **Placa-mãe** | Instale sobre os **espaçadores (*standoffs*)** nos furos certos; um espaçador fora de lugar encosta na placa e causa **curto** |
| **Fonte** | **Nunca abra.** Mesmo fora da tomada, os capacitores podem guardar tensão perigosa |
| **Pasta térmica** | Não encoste os dedos na base do processador nem do dissipador; limpe a pasta antiga com isopropílico e papel sem fiapo |

### Ferramentas da bancada básica
| Ferramenta | Uso | Preço médio (2026) |
|---|---|---|
| Kit de chaves de precisão (Phillips PH0/PH1/PH2, Torx, Pentalobe) | Gabinete, notebook, celular | R$ 40–200 |
| Pulseira antiestática | ESD | R$ 15–40 |
| Pincel antiestático ou trincha macia | Limpeza | R$ 10–30 |
| Ar comprimido (lata) ou soprador elétrico | Poeira | R$ 30–50 a lata; R$ 150–400 o soprador |
| Álcool isopropílico 99% | Limpeza de contatos e pasta | R$ 25–50 / litro |
| Pasta térmica de qualidade | Processador | R$ 30–80 |
| Multímetro digital | Elétrica | R$ 50–250 |
| Testador de fonte ATX | Diagnóstico rápido | R$ 40–100 |
| Abraçadeiras e velcro | Organização de cabos | R$ 10–30 |
| Lanterna ou luminária com lupa | Inspeção | R$ 30–150 |
| Pen drive de boot com ferramentas | Diagnóstico de software | R$ 30–60 |
