Agora que o vocabulário e a segurança estão dominados, vamos ao centro da masterclass: o **hardware**.

## O que é hardware

**Hardware** é todo o **conjunto físico** de um sistema computacional: componentes eletrônicos, circuitos, placas, cabos, periféricos e a estrutura mecânica. Em resumo, **tudo o que tem massa e ocupa espaço**.

A palavra vem do inglês ***hard*** (duro, rígido) + ***ware*** (mercadoria, artigo). Originalmente, *hardware* significava **"ferragens"**: parafusos, pregos e ferramentas. As lojas de material de construção nos EUA ainda se chamam *hardware stores*. Na década de **1950**, o termo passou a designar as **máquinas de computação**, e em **1958** o estatístico **John Tukey** (o mesmo do "bit") usou pela primeira vez por escrito **software** como contraponto: a parte "macia", mutável.

## Origem do hardware de computador

| Fase | Hardware típico |
|---|---|
| Mecânica (1600–1930) | Engrenagens, alavancas, cilindros, cartões perfurados |
| Eletromecânica (1930–1945) | Relés (interruptores acionados por eletroímã) |
| Eletrônica a válvulas (1946–1958) | Válvulas termiônicas, memória de núcleo magnético |
| Transistorizada (1958–1964) | Transistores discretos soldados em placas |
| Circuito integrado (1964–1971) | Chips com dezenas ou centenas de transistores |
| Microprocessada (1971–hoje) | CPU em um chip, placas-mãe, barramentos padronizados (ISA, PCI, PCIe) |
| SoC e chiplets (2010–hoje) | Sistema inteiro num chip ou em vários chips num mesmo pacote |

## Para que serve

O hardware tem quatro funções, as mesmas do ciclo IPO visto no módulo 1:

1. **Receber dados** (entrada): teclado, mouse, microfone, câmera, sensores.
2. **Processar** (transformar dados): CPU, GPU, NPU.
3. **Armazenar**: RAM (temporário), SSD e HD (permanente).
4. **Entregar resultados** (saída): monitor, caixas de som, impressora, rede.

E três funções de **suporte**:
5. **Alimentar** com energia: fonte e bateria.
6. **Conectar** tudo: placa-mãe, barramentos, cabos.
7. **Proteger e resfriar**: gabinete, dissipadores, coolers.

## Como funciona: do clique ao pixel

Vamos seguir o que acontece **dentro do hardware** quando você dá **dois cliques num vídeo** para assistir:

1. **Mouse (entrada)**: o sensor óptico detecta o movimento e o clique e envia pacotes de dados pelo **USB** (ou por rádio 2,4 GHz / Bluetooth) até o **chipset** da placa-mãe.
2. **Placa-mãe**: o chipset encaminha a informação à **CPU** por um barramento interno.
3. **CPU**: o sistema operacional (software rodando na CPU) entende "abrir este arquivo com o player". A CPU pede o arquivo ao **SSD**.
4. **SSD**: o controlador lê as células de memória flash e envia os dados pelo barramento **PCIe** (NVMe) para a **memória RAM**.
5. **RAM**: guarda o player e os primeiros segundos do vídeo, para acesso rápido.
6. **GPU**: o bloco **decodificador de vídeo** da placa de vídeo (ou da GPU integrada) descomprime o vídeo (H.264, H.265, AV1) quadro a quadro. Isso é muito mais eficiente que fazer na CPU.
7. **Monitor (saída)**: a GPU envia os quadros prontos pelo **HDMI ou DisplayPort**.
8. **Áudio (saída)**: o som segue pelo chip de áudio da placa-mãe (ou pelo HDMI) até as caixas ou o fone.
9. **Fonte**: durante tudo isso, fornece energia estável em 12 V, 5 V e 3,3 V.
10. **Coolers**: retiram o calor gerado, que é toda a energia consumida virando calor no fim.

Tudo isso leva **menos de um segundo**.

## Classificações do hardware

### Por função
| Categoria | Exemplos |
|---|---|
| **Processamento** | CPU, GPU, NPU, chipset |
| **Memória primária** (volátil, rápida) | RAM, cache, registradores |
| **Memória secundária** (permanente) | SSD, HD, pen drive, cartão SD |
| **Entrada** | Teclado, mouse, microfone, webcam, scanner |
| **Saída** | Monitor, impressora, caixas de som |
| **Entrada e saída (mistos)** | Tela touch, placa de rede, headset, multifuncional, pen drive |
| **Energia** | Fonte, bateria, nobreak |
| **Interconexão** | Placa-mãe, cabos, barramentos |
| **Refrigeração** | Dissipadores, coolers, water cooler, pasta térmica |
| **Estrutura** | Gabinete, suportes, baias |

### Por localização
- **Hardware interno**: dentro do gabinete (CPU, RAM, placa-mãe, SSD, fonte, GPU).
- **Periféricos (hardware externo)**: fora do gabinete, ligados por cabo ou sem fio (teclado, mouse, monitor, impressora).

### Por tipo de computador
| Tipo | Característica | Exemplos |
|---|---|---|
| **Desktop** | Gabinete separado, peças trocáveis | PC de escritório, PC gamer |
| **All-in-one** | Tudo atrás da tela | iMac, Dell Inspiron AIO |
| **Notebook** | Portátil com bateria | Ultrabook, notebook gamer |
| **Mini PC** | Gabinete minúsculo | Intel NUC, Mac mini, Beelink |
| **Servidor** | Feito para funcionar 24 h por dia, com redundância | Dell PowerEdge, HPE ProLiant (formato rack) |
| **Workstation** | Desktop profissional, com memória ECC e GPUs profissionais | Engenharia, 3D, IA |
| **Embarcado** | Computador dentro de outro aparelho | Carro, micro-ondas, smart TV, Arduino, Raspberry Pi |
| **Supercomputador** | Milhares de nós em paralelo | El Capitan, Frontier (EUA) |

## Mapa do gabinete: onde fica cada peça

```
┌─────────────────────────────────────────────┐
│ [ventoinha]          GABINETE   [ventoinha] │ ← saída de ar (topo/traseira)
│  ┌───────────────────────────────┐          │
│  │  PLACA-MÃE                    │ [I/O]    │ ← painel traseiro: USB, rede, áudio
│  │  ┌──────┐ ┌──┐┌──┐            │          │
│  │  │ CPU  │ │RAM││RAM│           │          │
│  │  │+cooler│ └──┘└──┘           │          │
│  │  └──────┘    [SSD M.2]        │          │
│  │  ═════════ PLACA DE VÍDEO ═══ │ [HDMI/DP]│
│  │  [chipset]  [slots PCIe]      │          │
│  └───────────────────────────────┘          │
│ [baias: HD/SSD 2,5"/3,5"]                   │
│  ┌─────────────┐                            │
│  │   FONTE     │ ← cabo de força            │ ← normalmente embaixo, com "túnel"
│  └─────────────┘                            │
│ [ventoinha]                                 │ ← entrada de ar (frente/baixo)
└─────────────────────────────────────────────┘
```

Nos próximos módulos, cada uma dessas peças ganha sua ficha completa.

:::dica O princípio do técnico
"**Do simples para o complexo, do barato para o caro, do externo para o interno.**" Antes de condenar uma placa-mãe, confira o cabo de força, a tomada, o cabo de vídeo, a memória mal encaixada e a bateria da BIOS. Na prática, **a maioria dos defeitos de bancada é mau contato, sujeira ou configuração**, e não peça queimada.
:::
