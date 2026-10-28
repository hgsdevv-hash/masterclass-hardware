## O que é

O **cooler**, no sentido técnico, é o **sistema ativo de refrigeração**: a **ventoinha** (*fan*) que movimenta o ar e, num sentido mais amplo, todo o sistema de resfriamento (ventoinha + dissipador, ou o **water cooler** com bomba, radiador e ventoinhas).

A palavra vem do inglês *to cool* (esfriar). No Brasil, "cooler" virou sinônimo do **conjunto** que fica em cima do processador.

## Para que serve: sua função

- **Forçar a troca de calor** entre o dissipador e o ar, que é muito mais rápida que a convecção natural.
- **Renovar o ar do gabinete**: trazer ar frio de fora e expulsar o ar quente de dentro.
- **Manter as peças abaixo do limite térmico**, garantindo **desempenho máximo** (sem *throttling*) e **vida útil** maior. Como regra prática da eletrônica, a cada ≈ 10 °C a mais, a vida útil de capacitores e semicondutores **cai pela metade** (Lei de Arrhenius).

:::exemplo Exemplo: o cooler no dia a dia
- **Abrindo abas e navegando**: as ventoinhas ficam lentas e silenciosas (500–900 rpm).
- **Exportando vídeo**: a CPU vai a 100% e a ventoinha acelera para 1.500–2.000 rpm; um cooler bom segura o clock no máximo.
- **Jogando ou gerando imagens com IA**: as ventoinhas da **placa de vídeo** sobem para 1.500–2.500 rpm, e as do **gabinete** precisam tirar o ar quente que a GPU joga dentro dele.
:::

## Onde fica

| Local | Função |
|---|---|
| **Sobre a CPU** (cooler do processador) | Resfriar o processador |
| **Na placa de vídeo** (1–3 ventoinhas integradas) | Resfriar a GPU, a VRAM e o VRM da placa |
| **Frente e base do gabinete** | **Entrada** de ar frio |
| **Topo e traseira do gabinete** | **Saída** de ar quente |
| **Dentro da fonte** | Resfriar os componentes da fonte |
| **Radiador do water cooler** | Retirar o calor do líquido |
| **Notebooks** | Ventoinhas tipo **"blower"** (centrífugas) que sopram pelas aletas até a saída lateral ou traseira |

## Como funciona uma ventoinha

1. Um **motor elétrico sem escovas (*brushless* DC)** gira as **pás**.
2. O controle da velocidade é feito pela placa-mãe:
   - **3 pinos (DC)**: a velocidade muda variando a **tensão** (de ≈ 5 a 12 V).
   - **4 pinos (PWM)**: tensão fixa de 12 V, e um **sinal PWM** (*Pulse Width Modulation*, em ≈ 25 kHz) liga e desliga o motor muito rápido, controlando a velocidade com mais precisão e alcançando **rotações mais baixas**.
   - O terceiro fio (*tach*) informa a **rotação** à placa-mãe.
3. A **curva de ventoinha** (*fan curve*), configurada na BIOS ou em software, define a rotação conforme a temperatura.

### Ficha técnica de ventoinhas
| Especificação | O que significa | Valor típico |
|---|---|---|
| **Tamanho** | Diâmetro | 80, 92, **120**, **140**, 200 mm |
| **Rotação** | rpm | 500–2.000 rpm (até 3.000+ em modelos de alto desempenho) |
| **Vazão (*airflow*)** | **CFM** (pés cúbicos por minuto) | 40–80 CFM |
| **Pressão estática** | **mm H₂O** | 1,0–3,5 mm H₂O; alta é melhor para **radiadores** e **dissipadores densos** |
| **Ruído** | **dBA** | 15–35 dBA (abaixo de 25 dBA é muito silencioso) |
| **Rolamento** | Tipo de mancal | Bucha (*sleeve*), rolamento de esferas (*ball*), fluido dinâmico (**FDB**), levitação magnética |
| **Conector** | 3 pinos (DC) ou 4 pinos (PWM) | **4 pinos PWM** é o recomendado |
| **Vida útil (MTBF)** | Horas médias até a falha | 30.000–150.000 horas |

### Tipos de mancal (rolamento)
| Tipo | Ruído | Durabilidade | Preço | Observação |
|---|---|---|---|---|
| **Bucha (*sleeve bearing*)** | Baixo no início | **Menor** (resseca e começa a "roncar") | Barato | Não gosta de ficar **deitada** (horizontal) |
| **Esferas (*ball bearing*)** | Um pouco mais alto | Alta | Médio | Funciona em qualquer posição |
| **FDB / hidrodinâmico** | **Muito baixo** | **Alta** | Médio-alto | O melhor custo-benefício |
| **Levitação magnética** | Muito baixo | Muito alta | Alto | Premium |

## Material

| Parte | Material |
|---|---|
| **Pás e moldura** | Plástico **PBT** ou **PP**, às vezes com fibra de vidro; nas premium, **LCP** (polímero de cristal líquido, mais rígido) |
| **Motor** | Bobinas de **cobre**, ímãs de **ferrite ou neodímio** |
| **Eixo** | Aço |
| **Mancal** | Bronze sinterizado (bucha), esferas de aço ou cerâmica, fluido lubrificante |
| **Cantos** | Borracha antivibração (nos bons modelos) |
| **Cabo** | Cobre com isolamento de PVC, às vezes trançado em nylon |

## Tipos de cooler (sistemas de refrigeração)

### 1. Refrigeração a ar (*air cooler*)
Dissipador + ventoinha (vimos os tipos no módulo anterior: **box**, **torre**, **dual tower**, **low profile**). É **simples, barato, durável** e sem risco de vazamento. A peça que se desgasta é só a ventoinha, que é **trocável**.

### 2. Water cooler AIO (*All-in-One*)
Sistema **fechado e selado de fábrica**:
1. Um **bloco (*waterblock*) com bomba** fica sobre a CPU.
2. O **líquido** (água destilada com aditivos e anticorrosivo, geralmente à base de propilenoglicol) absorve o calor.
3. **Mangueiras** levam o líquido até o **radiador**.
4. O **radiador** com ventoinhas (120, 240, 280, **360**, 420 mm) troca o calor com o ar.
5. O líquido frio volta ao bloco.

| Tamanho do radiador | Ventoinhas | Indicado para |
|---|---|---|
| 120 mm | 1 × 120 | CPUs de entrada (não supera uma boa torre) |
| 240 mm | 2 × 120 | CPUs intermediárias |
| 280 mm | 2 × 140 | Intermediárias e altas |
| **360 mm** | 3 × 120 | CPUs topo de linha (o mais vendido) |
| 420 mm | 3 × 140 | Entusiastas |

### 3. Water cooling customizado (*custom loop*)
Montado peça por peça: **reservatório**, **bomba**, **blocos** para CPU e GPU, **radiadores**, conexões (*fittings*) e tubos rígidos ou flexíveis. Tem o **melhor desempenho** e uma estética única, mas é **caro** (R$ 3.000 a mais de 10.000), exige **manutenção** (troca do líquido a cada 6–12 meses) e tem **risco de vazamento**.

### 4. Outros tipos
| Tipo | Como funciona | Uso |
|---|---|---|
| **Blower (centrífugo)** | Suga o ar pelo centro e sopra num único sentido | Notebooks, GPUs de servidor |
| **Peltier (TEC)** | Uma pastilha termoelétrica "bombeia" calor de um lado para o outro com eletricidade | Nichos; gasta muita energia e pode condensar água |
| **Nitrogênio líquido (LN₂)** | −196 °C num copo metálico sobre a CPU | Recordes de overclock (só por alguns minutos) |
| **Refrigeração por imersão** | Placas mergulhadas em **fluido dielétrico** (não condutor) | Data centers e mineração |
| **Refrigeração direta a líquido (*direct-to-chip*)** | Placas frias nos chips, com líquido refrigerado pelo prédio | **Data centers de IA** (ex.: racks NVIDIA GB200 NVL72) |

### Ar × Water cooler: qual escolher
| Critério | **Air cooler (torre)** | **Water cooler AIO** |
|---|---|---|
| Desempenho | Excelente até ≈ 200–250 W | Melhor nas CPUs mais quentes (> 250 W) |
| Preço | Menor | Maior |
| Durabilidade | Muito alta (só a ventoinha desgasta) | A **bomba** tem vida útil (5–7 anos); o líquido evapora lentamente pelas mangueiras |
| Risco | Nenhum | **Vazamento** (raro em marcas boas, mas possível) |
| Ruído | Baixo | A bomba pode fazer zumbido |
| Estética | Grande sobre a placa | Visual limpo, com bloco RGB e tela |
| Manutenção | Limpar a poeira | Limpar o radiador; observar ruídos da bomba |

:::especialista O que mostram os testes
Canais de testes independentes, como o **Gamers Nexus** (EUA) e, no Brasil, o **Adrenaline** e o **Hardware Unboxed** (Austrália), mostram repetidamente que **torres de ar de R$ 200–400** (como a Thermalright Peerless Assassin) **empatam com water coolers de 240 mm** em CPUs intermediárias. O AIO de 360 mm faz diferença real nas CPUs mais quentes, como o Core i9 ou o Ryzen 9 em carga total.
:::

## Preço médio (Brasil, out/2026)

| Item | Faixa de preço |
|---|---|
| Ventoinha avulsa 120 mm simples | R$ 15–40 |
| Ventoinha 120 mm de qualidade (FDB, PWM) | R$ 50–150 (Arctic P12 ≈ R$ 50–70; Noctua NF-A12x25 ≈ R$ 250+) |
| Kit 3 ventoinhas ARGB com controladora | R$ 80–300 |
| Cooler torre (CPU) | R$ 100–400 (premium até R$ 1.200) |
| Water cooler AIO 240 mm | R$ 350–800 |
| Water cooler AIO 360 mm | R$ 600–1.400 |
| Water cooling customizado | R$ 3.000–10.000+ |

## Instalação e orientação correta

1. **A seta na lateral** da ventoinha mostra o **sentido do ar** e o de rotação. O ar **sai** pelo lado das hastes de suporte do motor (a "aranha").
2. **Cooler da CPU**: ar soprando **para trás**, em direção à ventoinha de saída traseira do gabinete.
3. **Radiador do AIO**:
   - **No topo**, puxando o ar para fora: posição ideal para a vida útil da bomba (o ar acumulado no sistema fica no radiador, longe da bomba).
   - **Na frente**, puxando ar frio: a CPU fica mais fria, mas o ar quente entra no gabinete. Nesse caso, as **mangueiras devem ficar embaixo** e o topo do radiador acima da bomba.
   - **Nunca** deixe a bomba no ponto mais alto do circuito: o ar acumula nela, ela faz barulho (o "gorgolejo") e se desgasta.
4. **Conecte** a ventoinha da CPU no header **CPU_FAN** e a bomba do AIO no header **AIO_PUMP** ou **PUMP** (que fornece 100% de tensão). Se a placa não detectar nada no CPU_FAN, ela pode **não ligar** ou mostrar um alerta.

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **Ventoinha barulhenta ("ronco")** | Ruído que aumenta com o tempo | Preferir mancal FDB ou de esferas | Limpar; nas de bucha, uma gota de óleo de máquina (paliativo); **trocar a ventoinha** |
| **Ventoinha parada** | Temperaturas altas, alerta "CPU Fan Error" | Organizar os cabos para não encostarem nas pás | Verificar a conexão no header; testar em outro header; trocar |
| **Ventoinha sempre no máximo** | Barulho constante | Ligar no header correto | Ajustar a curva na BIOS (modo PWM × DC) |
| **Ventoinhas em sentidos errados** | Calor preso no gabinete | Conferir as setas | Reorientar (entrada na frente e na base, saída no topo e na traseira) |
| **Bomba do AIO com defeito** | CPU a 100 °C em segundos, mangueiras não esquentam, bomba sem rpm | Montar na posição correta | Verificar se a bomba está ligada e com rpm; trocar o AIO (geralmente está na garantia: 3–6 anos) |
| **Ruído de bolha na bomba** | "Gorgolejo" | Radiador acima da bomba | Inclinar o gabinete para mover as bolhas para o radiador; reposicionar |
| **Vazamento** | Líquido na placa | Marcas confiáveis; não dobrar as mangueiras | **Desligar na hora**, desconectar da tomada e secar; limpar com isopropílico; **acionar a garantia** (algumas marcas cobrem as peças danificadas) |
| **Poeira** | Perda de desempenho | Filtros, pressão positiva | Limpeza periódica (a cada 3–6 meses) |
| **RGB não funciona ou queimou** | LEDs apagados | Diferenciar ARGB (3 pinos, 5 V) de RGB (4 pinos, 12 V) | Conectar no header certo; se queimou por ligação errada, só trocando |
