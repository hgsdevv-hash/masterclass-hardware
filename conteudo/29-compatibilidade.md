Saber se as peças são **compatíveis** é a habilidade que separa quem "compra peças" de quem **monta computadores**. A boa notícia: compatibilidade segue **regras**, e todas estão nas fichas técnicas. Este módulo ensina a checar uma por uma, na ordem certa, e depois a montar o PC passo a passo.

## A regra de ouro: comece pela placa-mãe

A placa-mãe é o "**centro da compatibilidade**": praticamente todas as outras peças precisam ser compatíveis **com ela**. A ordem de decisão recomendada é:

1. **Processador** (define o soquete e a plataforma)
2. **Placa-mãe** (soquete + chipset + formato + tipo de memória)
3. **Memória RAM** (geração DDR + velocidade + quantidade)
4. **Placa de vídeo** (desempenho + tamanho + consumo)
5. **Armazenamento** (tipo de slot: M.2 NVMe/SATA, SATA 2,5")
6. **Fonte** (potência + conectores)
7. **Cooler** (soquete + TDP + altura)
8. **Gabinete** (formato da placa + comprimento da GPU + altura do cooler + radiador)

## O checklist de compatibilidade, peça por peça

| # | Verificação | Onde conferir | Exemplo de incompatibilidade |
|---|---|---|---|
| 1 | **CPU × soquete da placa-mãe** | Ficha da CPU ("Socket") e da placa | Ryzen 7 7700 (AM5) numa placa AM4 ❌ |
| 2 | **CPU × chipset e BIOS** | "**CPU Support List**" no site do fabricante da placa | Ryzen 9000 numa B650 com BIOS antiga ❌ (resolve com atualização) |
| 3 | **RAM × geração DDR** | Ficha da placa ("Memory: DDR5") | DDR4 em placa DDR5 ❌ (nem encaixa) |
| 4 | **RAM × velocidade e capacidade máximas** | Ficha e **QVL** (lista de memórias testadas) da placa | Kit DDR5-8000 numa placa que só suporta até 6.400 ⚠️ (funciona mais lento) |
| 5 | **RAM × altura do cooler** | Altura dos pentes × "RAM clearance" do cooler | Pente com RGB alto encostando numa torre grande ⚠️ |
| 6 | **GPU × slot PCIe** | Toda placa moderna tem PCIe x16 | Placa x8 em PCIe 3.0 ⚠️ (perde um pouco de desempenho) |
| 7 | **GPU × gabinete** | "Max GPU length" do gabinete × comprimento da GPU | GPU de 340 mm em gabinete de 300 mm ❌ |
| 8 | **GPU × fonte** | "Fonte recomendada" e conectores da GPU | RTX 5080 com fonte de 550 W ❌ |
| 9 | **SSD × slot M.2** | Manual da placa (M.2 aceita NVMe? SATA? PCIe 4.0 ou 5.0?) | SSD M.2 SATA num slot só NVMe ❌ |
| 10 | **Slots compartilhados** | Manual da placa ("M2_2 desativa SATA 5 e 6") | Usar o 2º M.2 desliga duas portas SATA ⚠️ |
| 11 | **Fonte × potência total** | Soma do consumo + margem de 30–50% | — |
| 12 | **Fonte × conectores** | 24 pinos, EPS 8 pinos (1 ou 2), PCIe 6+2 ou 12V-2x6 | Placa-mãe pede 8 + 8 pinos de CPU e a fonte só tem um ⚠️ |
| 13 | **Fonte × gabinete** | Formato (ATX × SFX) e comprimento | Fonte ATX longa num gabinete compacto ❌ |
| 14 | **Cooler × soquete** | Lista de soquetes do cooler | Cooler antigo sem kit para AM5 ou LGA1851 ❌ |
| 15 | **Cooler × TDP da CPU** | TDP suportado × consumo da CPU | Cooler box num Core i9 ❌ |
| 16 | **Cooler × altura no gabinete** | "CPU cooler max height" × altura do cooler | Torre de 165 mm em gabinete de 155 mm ❌ |
| 17 | **Radiador × gabinete** | Suportes de 240/280/360 mm no topo e na frente | AIO 360 num gabinete que aceita só 240 ❌ |
| 18 | **Placa-mãe × gabinete** | Formatos suportados (ATX, mATX, ITX) | Placa ATX num gabinete mini tower ❌ |
| 19 | **Vídeo integrado** | Sufixo "F" (Intel), "G" e série (AMD) | Core i5-14400F **sem placa de vídeo** = sem imagem ❌ |
| 20 | **Sistema operacional** | Windows 11 exige **TPM 2.0**, **Secure Boot** e CPU da lista oficial | PC com CPU de 7ª geração Intel não instala o Windows 11 oficialmente ⚠️ |

:::dica Ferramentas para checar compatibilidade
- **PCPartPicker** (pcpartpicker.com): monta a lista e **alerta incompatibilidades automaticamente** (soquete, tamanho, potência). Tem versão para o Brasil com preços limitados.
- **Sites dos fabricantes**: CPU Support List e QVL de memória da placa-mãe.
- **Calculadoras de fonte**: OuterVision, Cooler Master e be quiet!.
- **CPU-Z / HWiNFO**: identificam o que já está instalado (para upgrades).
:::

## Como identificar as peças de um PC que já existe

| Peça | Como descobrir sem abrir |
|---|---|
| **Processador** | **Ctrl + Shift + Esc** → Desempenho → CPU; ou o **CPU-Z** (aba CPU) |
| **Placa-mãe (modelo e chipset)** | **CPU-Z** (aba Mainboard) ou `Win + R` → **msinfo32** |
| **Memória (geração, velocidade, slots ocupados)** | **CPU-Z** (abas Memory e SPD); Gerenciador de Tarefas → Memória ("Slots usados") |
| **Placa de vídeo** | **GPU-Z**; Gerenciador de Tarefas → GPU; `dxdiag` |
| **Armazenamento** | **CrystalDiskInfo**; Gerenciador de Tarefas → Disco |
| **Fonte** | Só abrindo: ler a **etiqueta** lateral (modelo, potência, certificação) |
| **Versão da BIOS** | **msinfo32** → "Versão/data do BIOS" |

:::exemplo Exemplo: planejando um upgrade de memória
O cliente tem 8 GB e quer 16 GB. No **CPU-Z → SPD**, você vê: **DDR4-3200, 1 pente de 8 GB no slot 2, 2 slots livres**. A solução mais barata: **comprar outro pente de 8 GB DDR4-3200** (de preferência igual) e instalar no slot correspondente, ativando o **dual channel**. Ganho duplo: mais memória **e** mais largura de banda.
:::

## Exemplo completo: montando uma configuração compatível (out/2026)

**Objetivo**: PC para jogos em 1080p/1440p e edição de vídeo leve.

| Peça | Escolha | Por que é compatível |
|---|---|---|
| CPU | **Ryzen 5 7600** (AM5, 65 W, com vídeo integrado básico) | — |
| Placa-mãe | **B650M** (AM5, DDR5, Micro-ATX, 1 slot M.2 PCIe 4.0) | Soquete AM5 ✅ · BIOS atual ✅ |
| RAM | **2 × 16 GB DDR5-6000 CL30** | DDR5 ✅ · Na QVL ✅ · Dual channel ✅ · Ativar EXPO |
| GPU | **RTX 5060 Ti 16 GB** (≈ 180 W, 2 slots, ≈ 230–300 mm) | PCIe x16 (a placa usa x8) ✅ |
| SSD | **NVMe PCIe 4.0 1 TB** | Slot M.2 NVMe ✅ |
| Fonte | **650 W 80 PLUS Gold, ATX 3.1** | ≈ 88 + 180 + 75 = 343 W de consumo → folga de ≈ 90% ✅ |
| Cooler | **Torre de 4–5 heatpipes** com suporte a AM5 (≈ 155 mm) | Soquete ✅ · TDP ✅ |
| Gabinete | **Mid tower** com suporte a mATX/ATX, GPU de até 360 mm e cooler de até 165 mm | Tudo cabe ✅ |

## Montagem passo a passo

:::atencao Antes de começar
Bancada limpa, boa luz, **pulseira antiestática** ligada ao gabinete, manual da placa-mãe aberto, fonte **fora da tomada**, chave Phillips nº 2 e um potinho para parafusos.
:::

### Fase 1: fora do gabinete (sobre a caixa da placa-mãe)
1. **Instale o processador**: levante a alavanca do soquete, alinhe o **triângulo dourado** da CPU com o triângulo do soquete, **apoie sem forçar** e abaixe a alavanca. Nas plataformas LGA, a tampa plástica salta sozinha. Guarde-a (a garantia exige).
2. **Instale o(s) SSD(s) M.2**: retire o dissipador do slot, **tire a película do pad térmico**, encaixe o SSD a ≈ 30°, abaixe e fixe.
3. **Instale a memória RAM**: abra as travas, alinhe o **chanfro** e pressione **as duas pontas** até ouvir o clique. Use os **slots indicados** para dual channel (geralmente **A2 e B2**).
4. **Instale o cooler** (se for torre e o gabinete permitir instalar depois, pode deixar para o fim): monte o *backplate* e os suportes conforme o manual, aplique **pasta térmica** (um grão de ervilha), retire a **película da base do cooler** e aperte os parafusos **em "X", aos poucos**.
5. **Teste fora do gabinete (recomendado)**: ligue a fonte na placa (24 e 8 pinos), a GPU (ou use o vídeo integrado), o monitor, e dê partida encostando uma chave de fenda nos pinos **PWR_SW**. Se entrar na **BIOS**, está tudo certo. Desligue e desconecte.

### Fase 2: no gabinete
6. **Prepare o gabinete**: retire as laterais, confira os **espaçadores** (eles devem coincidir com os furos da placa; nenhum espaçador sobrando).
7. **Instale o espelho de I/O** (se não for integrado à placa).
8. **Instale a fonte**: com a ventoinha **virada para baixo** (se houver filtro e o gabinete estiver fora do carpete). Passe os cabos principais pelos furos antes de instalar a placa.
9. **Instale a placa-mãe**: encaixe nas portas do espelho de I/O e parafuse **todos os pontos**, sem apertar demais.
10. **Conecte os cabos de energia**: **24 pinos** e **EPS de 8 pinos** (no canto superior, de preferência antes de instalar o cooler e o radiador do topo).
11. **Conecte o painel frontal**: **F_PANEL** (Power, Reset, LEDs), **USB 3.0**, **USB-C**, **HD Audio**.
12. **Instale a placa de vídeo**: retire as tampas traseiras dos slots, abra a trava do slot PCIe x16, encaixe com firmeza até o clique, parafuse e conecte os **cabos PCIe** (cabos **separados** para cada conector, ou o 12V-2x6 **até o fim**). Instale o **suporte anti-sag**, se houver.
13. **Instale o armazenamento SATA** (se houver): HD ou SSD de 2,5" nas baias, com cabo SATA de dados e de energia.
14. **Conecte as ventoinhas**: CPU_FAN, SYS_FAN e a bomba (PUMP) do AIO; o RGB e o ARGB nos headers certos.
15. **Organize os cabos** (*cable management*) atrás da bandeja, com abraçadeiras ou velcro.

### Fase 3: primeiro boot e configuração
16. **Ligue** e entre na BIOS (**Del** ou **F2**).
17. Confira se **CPU, memória (quantidade e velocidade), SSDs e temperaturas** aparecem corretamente.
18. **Ative o XMP ou EXPO** da memória.
19. **Atualize a BIOS**, se necessário (pelo utilitário interno, com o arquivo num pen drive).
20. Ajuste a **curva das ventoinhas** e a **ordem de boot**.
21. **Instale o sistema operacional** (pen drive criado com a **Media Creation Tool** da Microsoft, com pelo menos 8 GB).
22. **Instale os drivers**: chipset (do site da AMD ou da Intel), placa de vídeo (NVIDIA, AMD ou Intel), rede, áudio. Depois, rode o **Windows Update**.
23. **Teste de estabilidade**: Cinebench (CPU), 3DMark ou um jogo (GPU), MemTest86 ou TestMem5 (RAM), monitorando temperaturas no **HWiNFO64**.

:::dica Se não ligar ou não der imagem
Siga a ordem: **(1)** tomada e interruptor da fonte; **(2)** cabos de 24 e 8 pinos; **(3)** cabo do monitor ligado **na placa de vídeo**; **(4)** memória encaixada (teste com 1 pente no slot A2); **(5)** LEDs de diagnóstico da placa (CPU, DRAM, VGA, BOOT); **(6)** BIOS compatível com a CPU; **(7)** espaçador fazendo curto; **(8)** **Clear CMOS**.
:::
