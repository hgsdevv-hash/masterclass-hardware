Antes de falar de peças, precisamos alinhar o vocabulário. Muita gente usa "computador", "informática", "TI" e "ciência da computação" como sinônimos, mas são coisas diferentes, e entender a diferença organiza todo o resto do estudo.

## As áreas: TI, Ciência da Computação, Engenharia da Computação

| Área | Pergunta central | Foco | Exemplo de profissional |
|---|---|---|---|
| **Ciência da Computação** | "O que pode ser computado, e como fazer isso do melhor jeito?" | Algoritmos, teoria, linguagens, IA | Pesquisador de algoritmos, cientista de dados |
| **Engenharia da Computação** | "Como construir a máquina que computa?" | Circuitos, processadores, sistemas embarcados, hardware + software | Projetista de chips, engenheiro de firmware |
| **Sistemas de Informação / TI** | "Como usar a computação para resolver problemas de pessoas e empresas?" | Infraestrutura, redes, suporte, segurança, gestão | Técnico de suporte, analista de infraestrutura |
| **Técnico em Informática / Manutenção** | "Como manter as máquinas funcionando?" | Montagem, manutenção, redes locais, instalação | Técnico de bancada |

:::exemplo Exemplo
Quando o processador do seu celular foi projetado, um **engenheiro de computação** desenhou os circuitos. O **cientista da computação** criou o algoritmo que deixa a câmera mais nítida. O **profissional de TI** da operadora mantém a rede que leva o seu vídeo para a internet. E o **técnico** troca a bateria quando ela estufa.
:::

## O que é computar

**Computar** é transformar dados de entrada em dados de saída seguindo regras bem definidas. Somar dois números é computar. Ordenar uma lista de nomes, converter um áudio em MP3 ou calcular a rota do GPS também é.

Todo computador, do ábaco ao supercomputador, segue o mesmo ciclo, chamado **ciclo IPO** (Input, Processing, Output), ou em português **Entrada → Processamento → Saída**, com o **Armazenamento** guardando dados e resultados:

```
 ENTRADA  ──►  PROCESSAMENTO  ──►  SAÍDA
 (teclado,     (CPU, GPU)          (monitor,
  mouse,           ▲ │              caixa de som,
  câmera)          │ ▼              impressora)
              ARMAZENAMENTO
              (RAM, SSD, HD)
```

:::exemplo Exemplo: abrir uma aba no navegador
1. **Entrada**: você aperta `Ctrl + T` e digita um endereço no teclado.
2. **Processamento**: a CPU interpreta o comando, a placa de rede busca a página na internet e a CPU e a GPU montam a página.
3. **Armazenamento**: a página fica na RAM enquanto a aba está aberta, e partes dela (o cache) vão para o SSD.
4. **Saída**: a GPU manda a imagem para o monitor.
:::

## Hardware e software: a diferença em uma frase

- **Hardware** é a parte **física**, aquilo que você pode tocar: processador, memória, placa-mãe, teclado, cabos.
- **Software** é a parte **lógica**: as instruções que dizem ao hardware o que fazer (programas, sistema operacional, aplicativos).

Uma frase clássica dos laboratórios de informática resume isso: *"Hardware é o que você chuta; software é o que você xinga."*

### Software, bem resumido (nosso foco é hardware)

| Tipo de software | O que faz | Exemplos |
|---|---|---|
| **Firmware** | Software gravado no próprio hardware, que o "acorda" e controla em baixo nível | BIOS/UEFI da placa-mãe, firmware do SSD |
| **Sistema operacional** | Gerencia o hardware e serve de ponte para os programas | Windows 11, Linux (Ubuntu), macOS, Android |
| **Drivers** | "Tradutores" que ensinam o sistema a conversar com cada peça | Driver NVIDIA, driver de áudio Realtek |
| **Aplicativos** | Programas que o usuário usa | Chrome, Word, Photoshop, jogos |
| **Utilitários** | Ferramentas de manutenção e diagnóstico | CPU-Z, CrystalDiskInfo, antivírus |

:::curiosidade Curiosidade
O **firmware** fica no meio do caminho: é software, mas mora gravado num chip de hardware. Por isso, ao atualizar a BIOS, você está trocando o software de dentro de uma peça física, e uma queda de energia nessa hora pode deixar a placa-mãe sem conseguir ligar.
:::

## Analógico x digital

- **Analógico**: representa informação com grandezas **contínuas** (um ponteiro de relógio, a agulha do toca-discos, a tensão variando suavemente).
- **Digital**: representa informação com **valores discretos**, contados, normalmente só dois: 0 e 1.

O computador moderno é **digital e binário** porque é muito mais fácil e confiável construir circuitos que diferenciam só dois estados ("tem tensão" ou "não tem tensão") do que circuitos que distinguem dez níveis diferentes. Ruído elétrico pequeno não transforma um 1 em 0, mas facilmente transformaria um 7 em 8.

:::exemplo Exemplo
Um disco de vinil guarda o som como um sulco ondulado contínuo, ou seja, de forma analógica. Um arquivo MP3 guarda o mesmo som como milhões de números medidos 44.100 vezes por segundo, ou seja, de forma digital. Copiar um vinil perde qualidade; copiar um MP3 gera uma cópia idêntica, bit a bit.
:::

## Os quatro pilares de qualquer computador

1. **Processar**: CPU (e GPU).
2. **Memorizar a curto prazo**: memória RAM.
3. **Guardar a longo prazo**: SSD ou HD.
4. **Comunicar**: dispositivos de entrada e saída, rede e barramentos.

Todo o resto (placa-mãe, fonte, cooler, gabinete, cabos) existe para **alimentar, conectar, resfriar e proteger** esses quatro pilares. Guarde essa ideia, porque ela vai organizar toda a parte de componentes.
