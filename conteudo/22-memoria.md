"Memória" é uma das palavras mais mal usadas da informática. O cliente diz "meu celular está sem memória" quando quer dizer **armazenamento**. Vamos organizar tudo: a **hierarquia de memória**, a **RAM** em detalhe (inclusive a evolução dos DDRs) e a **ROM**.

## A hierarquia de memória

| Nível | Tipo | Tamanho típico | Velocidade (latência) | Volátil? |
|---|---|---|---|---|
| 1 | **Registradores** (dentro do núcleo) | Bytes | < 0,3 ns (1 ciclo) | Sim |
| 2 | **Cache L1** | 32–80 KB por núcleo | ≈ 1 ns | Sim |
| 3 | **Cache L2** | 512 KB–3 MB por núcleo | ≈ 3–5 ns | Sim |
| 4 | **Cache L3** | 8–128 MB | ≈ 10–20 ns | Sim |
| 5 | **Memória RAM** | 8–128 GB | ≈ **60–100 ns** | **Sim** |
| 6 | **SSD NVMe** | 500 GB–4 TB | ≈ 20–100 **µs** (≈ 1.000 vezes mais lento que a RAM) | Não |
| 7 | **HD** | 1–30 TB | ≈ 5–15 **ms** (≈ 100 mil vezes mais lento que a RAM) | Não |
| 8 | **Nuvem e rede** | Ilimitado | Dezenas de ms | Não |

**Regra de ouro**: quanto **mais perto da CPU**, mais **rápida, cara e pequena** é a memória.

:::exemplo Exemplo: a escala humana da hierarquia
Se o acesso ao **cache L1** levasse **1 segundo**:
- a **RAM** levaria ≈ **1,5 minuto**;
- o **SSD NVMe** levaria ≈ **1 dia**;
- o **HD** levaria ≈ **4 meses**;
- um pacote da internet entre o Brasil e os EUA levaria ≈ **5 anos**.

Por isso o computador fica lento quando a RAM acaba e ele precisa usar o disco como memória (o **arquivo de paginação**).
:::

# Memória RAM

## O que é

**RAM** (*Random Access Memory*, ou memória de acesso aleatório) é a **memória principal de trabalho** do computador. Ela guarda **temporariamente** os programas abertos e os dados em uso, para a CPU acessar rapidamente.

- **"Acesso aleatório"** quer dizer que qualquer posição pode ser lida no mesmo tempo, sem percorrer as anteriores, diferente de uma fita.
- É **volátil**: **perde tudo** quando o computador desliga.

## Para que serve: sua função

Pense na RAM como a **mesa de trabalho** e no SSD como o **armário**. Os documentos ficam guardados no armário, mas para trabalhar você os coloca sobre a mesa. **Quanto maior a mesa, mais coisas abertas ao mesmo tempo**, sem precisar ir ao armário toda hora.

| Atividade | Como usa a RAM | Quantidade recomendada (2026) |
|---|---|---|
| **Abrir abas no navegador** | Cada aba do Chrome ou do Edge consome de **100 MB a mais de 1 GB** (sites pesados, vídeos, redes sociais) | 30 abas ≈ 4–8 GB só do navegador |
| **Office, estudos, internet** | Moderado | **8 GB** (mínimo) / **16 GB** (confortável) |
| **Jogos** | O jogo carrega texturas, mapas e áudio | **16 GB** (mínimo) / **32 GB** (ideal em 2026) |
| **Editar vídeo e fotos** | Arquivos grandes e cache de prévia | **32 GB** (Full HD/4K) / **64 GB** (4K pesado, efeitos) |
| **Gerar imagens e rodar IA localmente** | O modelo é carregado na **VRAM** da GPU, e o excedente vai para a RAM | **32–64 GB** (+ GPU com VRAM generosa) |
| **Máquinas virtuais, servidores** | Cada VM reserva sua parte | 64–256 GB |

:::exemplo Exemplo: o "PC lento" com 8 GB
Um usuário com 8 GB de RAM abre o Windows 11 (≈ 3–4 GB), o Chrome com 20 abas (≈ 4 GB), o Spotify e o WhatsApp Desktop (≈ 1 GB). Total: ≈ **9 GB**. Faltando memória, o Windows passa a usar o **arquivo de paginação** no disco: **com HD, o PC "trava"**; com SSD, fica mais lento, mas usável. A solução é **mais RAM**, e não "limpar o PC".
:::

## Onde fica e como é

- **Onde**: nos **slots DIMM** da placa-mãe, ao lado do soquete da CPU. Nos notebooks, fica em slots **SO-DIMM**, embaixo do teclado ou atrás da tampa inferior, ou **soldada** na placa.
- **Como é**: uma **placa retangular (o "pente" ou módulo)**, com **chips de memória** de um ou dos dois lados, **contatos dourados** na borda e um **entalhe (chanfro)** em posição diferente para cada geração. Muitos têm **dissipador** metálico e **RGB**.

## Do que é feita (material)

| Parte | Material |
|---|---|
| **Chips DRAM** | **Silício**: cada bit é um **capacitor** minúsculo + um **transistor** (célula 1T1C) |
| **PCB do módulo** | Fibra de vidro (FR-4) com 6–10 camadas de cobre |
| **Contatos** | Cobre com banho de **ouro** |
| **Dissipador** | Alumínio |
| **Chips auxiliares** | **SPD** (EEPROM com a "identidade" do pente), **PMIC** (na DDR5, regulador de tensão no próprio pente) |

## Como funciona

1. Cada bit é um **capacitor**: **carregado = 1**, **descarregado = 0**.
2. O capacitor **vaza carga** naturalmente, por isso a memória precisa ser **"refrescada" (*refresh*) a cada ≈ 64 ms** na DDR3/DDR4 (≈ 32 ms na DDR5 e em temperaturas altas). Daí o nome **DRAM: Dynamic RAM**.
3. As células ficam organizadas em **bancos, linhas e colunas**. Para ler, o controlador **abre uma linha** (comando RAS) e lê uma **coluna** (comando CAS).
4. **SDRAM** (*Synchronous DRAM*): trabalha **sincronizada** com o clock do sistema.
5. **DDR** (*Double Data Rate*): transfere dados **duas vezes por ciclo de clock** (na subida e na descida do sinal).

### DRAM × SRAM
| | **DRAM** | **SRAM** |
|---|---|---|
| Célula | 1 transistor + 1 capacitor | 6 transistores (*flip-flop*) |
| Precisa de refresh? | **Sim** | Não |
| Velocidade | Rápida | **Muito mais rápida** |
| Densidade | Alta (muitos GB) | Baixa |
| Custo por bit | Baixo | Muito alto |
| Onde é usada | **Memória RAM** | **Cache** da CPU (L1, L2, L3) |

## A evolução dos DDRs

| Geração | Lançamento | Tensão | Pinos (desktop / notebook) | Velocidade (MT/s) | Capacidade típica por pente | Novidades |
|---|---|---|---|---|---|---|
| **SDR SDRAM** | ≈ 1993–1997 | 3,3 V | 168 / 144 | 66–133 MHz (PC66, PC100, PC133) | 32–512 MB | Sincronia com o clock |
| **DDR (DDR1)** | **2000** | 2,5 V | 184 / 200 | 200–400 | 128 MB–1 GB | Duas transferências por ciclo |
| **DDR2** | **2003** | 1,8 V | 240 / 200 | 400–1.066 | 512 MB–4 GB | *Prefetch* de 4 bits |
| **DDR3** | **2007** | 1,5 V (DDR3L: 1,35 V) | 240 / 204 | 800–2.133 | 2–8 GB | *Prefetch* de 8 bits, menor consumo |
| **DDR4** | **2014** (padrão JEDEC publicado em 2012) | **1,2 V** | **288 / 260** | **1.600–3.200** (overclock: 5.000+) | 4–32 GB | Grupos de bancos, maior capacidade |
| **DDR5** | **2020** (PCs desde 2021) | **1,1 V** | **288 / 262** | **4.800–8.000+** (2026: até 9.000+ em overclock) | 8–64 GB | **Dois subcanais de 32 bits por pente**, **PMIC no pente**, **ECC interno no chip (*on-die*)** |
| **DDR6** | Em desenvolvimento (previsão ≈ 2027+) | — | — | > 10.000 (previsto) | — | — |

:::atencao As gerações NÃO são compatíveis entre si
Cada geração tem o **chanfro (entalhe) em uma posição diferente**, justamente para impedir o encaixe no slot errado. **DDR4 não entra em placa DDR5**, e vice-versa. A placa-mãe (e o processador) definem qual geração usar.
:::

### Outros tipos de RAM
| Tipo | Onde é usada |
|---|---|
| **SO-DIMM** | Notebooks e mini PCs (pente menor, de ≈ 67 mm) |
| **LPDDR4X / LPDDR5 / LPDDR5X / LPDDR6** | **Soldada** em celulares, ultrabooks e Macs; baixo consumo; **não dá para fazer upgrade**. A JEDEC publicou a LPDDR6 em julho de 2025 |
| **CAMM2 / LPCAMM2** | Novo padrão (2023–2024) de módulo fino e **substituível** para notebooks, com desempenho de LPDDR |
| **CUDIMM / CSODIMM (DDR5)** | Pentes com **gerador de clock** próprio (CKD), para velocidades acima de 6.400 MT/s (Intel Core Ultra 200S) |
| **ECC (*Error-Correcting Code*)** | Servidores e workstations; detecta e corrige erros de bit |
| **RDIMM / LRDIMM (*Registered*)** | Servidores com muita memória |
| **GDDR6 / GDDR6X / GDDR7** | **Memória da placa de vídeo (VRAM)** |
| **HBM2e / HBM3 / HBM3E / HBM4** | Memória empilhada **ao lado de GPUs de IA** (NVIDIA H100/H200/B200, AMD MI300) |

### Velocidade e latência: lendo a etiqueta
Exemplo: **DDR5-6000 CL30 32 GB (2 × 16 GB)**
- **DDR5**: a geração.
- **6000**: a velocidade em **MT/s** (o comércio chama de "MHz").
- **CL30**: **CAS Latency**, o número de ciclos que a memória espera para entregar o dado. **Menor é melhor**.
- **2 × 16 GB**: um **kit** com dois pentes de 16 GB.

:::dica Latência real em nanossegundos
**Latência (ns) = CL × 2.000 ÷ velocidade (MT/s)**
- DDR4-3200 CL16: 16 × 2.000 ÷ 3.200 = **10 ns**
- DDR5-6000 CL30: 30 × 2.000 ÷ 6.000 = **10 ns**
- DDR5-4800 CL40: 40 × 2.000 ÷ 4.800 = **16,7 ns**

A DDR5-6000 CL30 tem a **mesma latência** de uma boa DDR4, mas **quase o dobro da largura de banda**.
:::

### Dual channel: por que dois pentes são melhores que um
A CPU tem **dois canais de memória** (nos desktops comuns). Com **dois pentes**, nos slots certos (geralmente **A2 e B2**, o 2º e o 4º slots a partir da CPU; confira no manual), ela acessa os dois **ao mesmo tempo**, **dobrando a largura de banda**.

:::exemplo Exemplo: 1 × 16 GB contra 2 × 8 GB
Num PC com vídeo **integrado**, trocar **1 × 16 GB** por **2 × 8 GB** (dual channel) pode aumentar o FPS em jogos entre **30% e 50%** (o vídeo integrado usa a RAM como VRAM). Com placa de vídeo dedicada, o ganho costuma ficar entre **5% e 20%**, conforme o jogo.
:::

### XMP e EXPO: ative-os
A memória sai de fábrica funcionando numa **velocidade padrão JEDEC** conservadora (ex.: DDR5-4800). A velocidade anunciada na caixa (ex.: 6.000) só é alcançada ao **ativar o perfil de overclock** na BIOS:
- **XMP** (*Extreme Memory Profile*): padrão da Intel.
- **EXPO** (*Extended Profiles for Overclocking*): padrão da AMD.

Muita gente compra memória de 6.000 MT/s e **usa a 4.800 por anos** sem saber.

## Preço médio da RAM (Brasil, out/2026)

:::atencao Crise de preços da DRAM (2025–2026)
Desde o fim de **2025**, a **demanda dos data centers de IA** por HBM e DRAM de servidor fez os fabricantes (**Samsung, SK Hynix, Micron**) desviarem a produção, e os preços da memória para consumidores **dispararam**, chegando a **2 a 4 vezes** os valores de 2024 em alguns casos. Os preços abaixo refletem esse momento e podem mudar bastante.
:::

| Produto | Menor preço à vista | Faixa comum nas lojas (out/2026) |
|---|---|---|
| DDR4 8 GB 3200 | ≈ R$ 350 | R$ 350–700 |
| DDR4 16 GB 3200 | ≈ R$ 600 | R$ 600–1.400 |
| DDR5 16 GB 5600 | ≈ R$ 1.400 | R$ 1.400–2.500 |
| DDR5 16 GB 6000 | ≈ R$ 2.100 | R$ 2.100–2.900 |
| Kit DDR5 32 GB (2 × 16) 6000 | ≈ R$ 3.950 | R$ 3.950–6.500 |
| SO-DIMM DDR5 16 GB (notebook) | — | R$ 2.000–2.400 |

*Fontes: menores preços à vista em agregadores (hardwarebarato.com) e listagens da KaBuM! em out/2026; por exemplo, a Kingston Fury Beast 16 GB DDR5-5600 aparecia entre R$ 2.400 e R$ 2.950 numa grande loja. A imprensa relata alta de **≈ 500% na DDR5** e de **120–180% na DDR4** em 12 meses. A TrendForce previu aumento de **58–63%** na DRAM convencional só no 2º trimestre de 2026.*

## Problemas mais comuns da RAM, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **Pente mal encaixado ou oxidado** | PC liga **sem imagem**, LED "DRAM" aceso, bipes | Encaixar até as **duas travas** fecharem | Retirar, **limpar os contatos com borracha** e isopropílico, reencaixar |
| **Memória com defeito** | **Telas azuis** (MEMORY_MANAGEMENT, IRQL_NOT_LESS_OR_EQUAL), travamentos, arquivos corrompidos | Comprar de marca confiável; evitar estática | Testar com **MemTest86** (pen drive de boot) ou com o **Diagnóstico de Memória do Windows** (`mdsched`); testar **um pente por vez** para achar o defeituoso; acionar a garantia (muitos pentes têm **garantia vitalícia**) |
| **XMP/EXPO instável** | Crashes depois de ativar o perfil | Comprar memórias da **QVL** (lista de compatibilidade) da placa-mãe | Atualizar a BIOS; usar um perfil mais leve; subir um pouco a tensão do SoC ou da memória (avançado) |
| **Pentes diferentes misturados** | Não liga, ou funciona na velocidade do mais lento | Comprar em **kit** | Usar pentes idênticos; configurar a velocidade manualmente |
| **Primeiro boot demorado com DDR5** | Tela preta por **1–3 minutos** no primeiro boot | Saber que é normal | **Aguardar**: é o *memory training* (a placa "aprende" os tempos ideais); depois, ativar o **Memory Context Restore** |
| **Só metade da memória reconhecida** | Instalou 32 GB e aparecem 16 | Slots corretos | Conferir os slots no manual; reencaixar; verificar pinos tortos no soquete (LGA) |
| **"Memória insuficiente"** | Lentidão, abas recarregando | Dimensionar para o uso | Instalar mais RAM; fechar programas em segundo plano |

# Memória ROM

## O que é

**ROM** (*Read-Only Memory*, ou memória somente de leitura) é uma memória **não volátil** (não perde os dados sem energia), usada para guardar o **firmware**: o software básico que **dá vida** ao hardware.

Hoje, na prática, a "ROM" dos computadores é **memória flash** que **pode ser regravada** (por exemplo, numa atualização de BIOS). O nome ficou por tradição.

## Para que serve

- **Guardar a BIOS/UEFI** da placa-mãe, que faz o **POST**, configura o hardware e inicia o sistema operacional.
- **Firmware** de placas de vídeo (VBIOS), SSDs, roteadores, impressoras, controles e TVs.
- **Microcódigo** dentro da CPU.
- Em videogames antigos, o **cartucho** era uma ROM com o jogo gravado.

:::atencao ROM do celular ≠ ROM de verdade
No mundo dos celulares, chama-se de "ROM" o **sistema operacional instalado** ("instalar uma ROM customizada"), e alguns anúncios chamam o armazenamento de "128 GB de ROM". São usos **populares** do termo. Tecnicamente, o armazenamento do celular é **flash NAND (UFS)**.
:::

## Onde fica e como é

- **Na placa-mãe**: um **pequeno chip de 8 pinos** (flash SPI, de 16 a 64 MB), às vezes num soquete, às vezes com um segundo chip de backup (*Dual BIOS*).
- **Dentro de outros dispositivos**: integrada ao controlador do SSD, ao chip da GPU, etc.

## Material
**Silício**, com células de memória baseadas em **transistores de porta flutuante** (*floating gate*) ou armadilha de carga (*charge trap*), encapsulados em plástico ou epóxi.

## Tipos e evolução da ROM

| Tipo | Ano | Como é gravada | Pode apagar? | Exemplo |
|---|---|---|---|---|
| **ROM (mask ROM)** | Anos 1960 | Na **fábrica**, durante a produção do chip | ❌ Nunca | Cartuchos de Atari e Nintendo |
| **PROM** (*Programmable ROM*) | **1956** (Wen Tsing Chow) | Uma única vez, **"queimando" fusíveis** internos com um gravador | ❌ | Equipamentos militares e industriais antigos |
| **EPROM** (*Erasable PROM*) | **1971** (Dov Frohman, Intel) | Eletricamente | ✅ Com **luz ultravioleta**, por uma **janelinha de quartzo** no chip (≈ 20 minutos) | BIOS dos anos 1980 |
| **EEPROM** (*Electrically Erasable PROM*) | ≈ **1978–1980** | Eletricamente | ✅ **Eletricamente**, byte a byte | Chip **SPD** dos pentes de memória, configurações |
| **Flash** (NOR e NAND) | **1980–1987** (Fujio Masuoka, Toshiba) | Eletricamente | ✅ Eletricamente, em **blocos** (muito mais rápida) | **BIOS/UEFI atual** (NOR/SPI), **SSDs, pen drives, cartões** (NAND) |

:::curiosidade Por que se chama "flash"
O nome foi sugerido por **Shoji Ariizumi**, colega de Fujio Masuoka na Toshiba, porque o processo de apagar a memória de uma vez o lembrava do **flash de uma câmera fotográfica**.
:::

## RAM × ROM: comparativo final

| Característica | **RAM** | **ROM (firmware)** |
|---|---|---|
| Volátil? | ✅ Sim (perde tudo ao desligar) | ❌ Não |
| Leitura e escrita | Leitura e escrita constantes | Principalmente leitura (escrita só em atualizações) |
| Velocidade | Muito alta | Mais lenta |
| Capacidade | GB (8–128 GB) | MB (16–64 MB na BIOS) |
| Função | Trabalho temporário (programas abertos) | Instruções permanentes de inicialização |
| Exemplo | Pente DDR5 de 16 GB | Chip da BIOS da placa-mãe |
| Quando você interage | O tempo todo | Ao ligar o PC e ao atualizar a BIOS |

## Problemas mais comuns da ROM (BIOS) e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **BIOS corrompida** | Placa liga mas não faz o POST, sem imagem | Não atualizar durante tempestades nem sem nobreak; usar o arquivo **exato** do modelo da placa | **BIOS Flashback**, **Dual BIOS**, recuperação por pen drive ou regravação do chip com um **gravador CH341A** (assistência técnica) |
| **Configurações perdidas** | Data errada, ordem de boot resetada | Bateria CR2032 boa | Trocar a bateria |
| **BIOS desatualizada** | Não reconhece a CPU nova, instabilidade | Verificar a lista de suporte de CPU | Atualizar pelo utilitário da própria BIOS (EZ Flash, M-Flash, Q-Flash) |
| **Senha de BIOS esquecida** | Bloqueio de acesso | Anotar as senhas | Clear CMOS (no desktop); em notebooks corporativos, pode exigir o fabricante |
