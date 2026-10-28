Tudo o que o computador guarda ou processa (texto, foto, música, vídeo, jogo, IA) vira, no fim, uma **sequência de 0 e 1**. Para medir o tamanho dessas sequências, usamos bits, bytes e seus múltiplos. Este módulo ensina o que cada unidade é, de onde veio e, principalmente, **como calcular**.

## Bit

### O que é
**Bit** é a **menor unidade de informação**. Ele só pode ter **dois valores: 0 ou 1**. Pode representar sim/não, ligado/desligado, verdadeiro/falso.

### De onde veio o nome
**Bit** é a contração de ***bi**nary digi**t*** (dígito binário). O termo foi criado pelo estatístico **John W. Tukey** em **1947**, no Bell Labs, e popularizado por **Claude Shannon** no artigo de **1948** que fundou a Teoria da Informação.

### Como o hardware representa um bit
| Onde | 0 | 1 |
|---|---|---|
| Processador e RAM | Tensão baixa (≈ 0 V) | Tensão alta (≈ 1,1 V na DDR5) |
| HD | Domínio magnético num sentido | No sentido oposto |
| SSD | Célula com uma carga elétrica | Célula com outra carga |
| CD/DVD | Sem transição na trilha | Transição entre *pit* (cavidade) e *land* (plano) |
| Fibra óptica | Luz apagada ou fraca | Luz acesa ou forte |
| Wi-Fi | Uma fase ou amplitude da onda | Outra fase ou amplitude |

### Quanto valem vários bits juntos
Com **n** bits, dá para representar **2ⁿ** combinações diferentes:

| Bits | Combinações | Exemplo de uso |
|---|---|---|
| 1 | 2 | Interruptor: ligado ou desligado |
| 2 | 4 | As quatro estações |
| 4 | 16 | Um dígito hexadecimal (0–F) |
| 7 | 128 | A tabela ASCII original |
| 8 | 256 | Um byte; tons de cada cor num pixel |
| 16 | 65.536 | Cores do "High Color"; áudio de CD por amostra |
| 24 | 16.777.216 | "16 milhões de cores" (8 bits × 3 cores RGB) |
| 32 | ≈ 4,3 bilhões | Endereços IPv4; limite de 4 GB de RAM dos sistemas de 32 bits |
| 64 | ≈ 18,4 quintilhões | Processadores e sistemas de 64 bits |
| 128 | ≈ 3,4 × 10³⁸ | Endereços IPv6 |

:::exemplo Exemplo: por que o Windows de 32 bits só usava 4 GB de RAM
Um sistema de 32 bits endereça 2³² posições de memória = 4.294.967.296 bytes = **4 GiB**. Mesmo com 8 GB instalados, ele "enxergava" no máximo 4 GB (na prática, uns 3,2–3,5 GB, porque parte dos endereços ia para a placa de vídeo e outros dispositivos). Com 64 bits, o limite teórico passou para 16 exabytes.
:::

### Como contar em binário
O sistema binário é **posicional**, como o decimal, só que cada posição vale **o dobro** da anterior (potências de 2):

| Posição | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Valor | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

:::exemplo Exemplo: converter binário para decimal
`01000001` = 0×128 + **1×64** + 0×32 + 0×16 + 0×8 + 0×4 + 0×2 + **1×1** = 64 + 1 = **65**.
65 é a letra **"A"** na tabela ASCII. Ou seja, quando você digita "A", o computador guarda `01000001`.
:::

:::exemplo Exemplo: converter decimal para binário (divisões sucessivas)
Converter **13**:
- 13 ÷ 2 = 6, resto **1**
- 6 ÷ 2 = 3, resto **0**
- 3 ÷ 2 = 1, resto **1**
- 1 ÷ 2 = 0, resto **1**

Lendo os restos **de baixo para cima**: **1101**. Conferindo: 8 + 4 + 0 + 1 = 13. ✔
:::

### Hexadecimal: o atalho dos técnicos
Escrever binário é cansativo. Por isso se usa **hexadecimal (base 16)**: cada dígito hexa representa exatamente **4 bits**. Os dígitos vão de 0 a 9 e depois de **A (10) a F (15)**.

- `1111 1111` = **FF** = 255
- `0100 0001` = **41** = 65 = "A"
- Cores em HTML: `#FF0000` = vermelho puro (R=255, G=0, B=0)
- Endereço MAC de placa de rede: `3C:52:82:1A:9F:04`

## Byte

### O que é
**Byte** é um conjunto de **8 bits**. É a unidade básica de armazenamento: o tamanho de um caractere simples (como "A") e a menor porção de memória que o computador endereça.

- 1 byte = 8 bits
- 1 byte representa 2⁸ = **256 valores** (de 0 a 255)

### De onde veio
O termo **byte** foi criado por **Werner Buchholz**, da IBM, em **1956**, durante o projeto do supercomputador **IBM Stretch**. A grafia com "y" (em vez de *bite*, "mordida") foi proposital, para não confundir com *bit*. No começo, um byte podia ter de 1 a 6 bits. O **IBM System/360 (1964)** padronizou o **byte de 8 bits**, que virou norma mundial.

:::curiosidade Nibble e octeto
- Meio byte (4 bits) se chama **nibble** (de *nibble*, "mordiscar"). É um dígito hexadecimal.
- Em redes e documentos técnicos, usa-se **octeto** para deixar claro que são exatamente 8 bits. Os franceses dizem *octet* e escrevem "Mo" em vez de "MB".
:::

### Atenção à letra: b minúsculo × B maiúsculo
| Símbolo | Significa | Usado em |
|---|---|---|
| **b** (minúsculo) | **bit** | Velocidade de internet: **Mbps** = megabits por segundo |
| **B** (maiúsculo) | **Byte** | Tamanho de arquivo e armazenamento: **MB**, **GB** |

Essa diferença é a causa da maior confusão do cliente de internet. Veremos no próximo módulo.

## Os múltiplos: KB, MB, GB, TB e além

### Dois sistemas: decimal (SI) e binário (IEC)
Aqui está o ponto que separa o leigo do profissional. Existem **dois jeitos** de contar:

- **Decimal (SI)**: kilo = 1.000, como no quilômetro. É o padrão usado por **fabricantes de HD, SSD e pen drive** e pelo **macOS**.
- **Binário**: "kilo" = **1.024** (2¹⁰), porque o computador trabalha em potências de 2. É o que o **Windows** usa (mesmo mostrando "KB", "MB", "GB").

Para acabar com a confusão, em **1998** a **IEC** (Comissão Eletrotécnica Internacional) criou prefixos binários próprios: **kibi (KiB), mebi (MiB), gibi (GiB), tebi (TiB)**.

| Nome (SI) | Símbolo | Valor decimal | Nome (IEC) | Símbolo | Valor binário |
|---|---|---|---|---|---|
| Kilobyte | **KB** (kB) | 1.000 bytes | Kibibyte | **KiB** | 1.024 bytes |
| Megabyte | **MB** | 1.000.000 bytes | Mebibyte | **MiB** | 1.048.576 bytes |
| Gigabyte | **GB** | 10⁹ bytes | Gibibyte | **GiB** | 1.073.741.824 bytes |
| Terabyte | **TB** | 10¹² bytes | Tebibyte | **TiB** | 1.099.511.627.776 bytes |
| Petabyte | **PB** | 10¹⁵ bytes | Pebibyte | **PiB** | 2⁵⁰ bytes |
| Exabyte | **EB** | 10¹⁸ bytes | Exbibyte | **EiB** | 2⁶⁰ bytes |
| Zettabyte | **ZB** | 10²¹ bytes | Zebibyte | **ZiB** | 2⁷⁰ bytes |
| Yottabyte | **YB** | 10²⁴ bytes | Yobibyte | **YiB** | 2⁸⁰ bytes |

Em 2022, o SI adotou ainda o **ronnabyte (RB, 10²⁷)** e o **quettabyte (QB, 10³⁰)**.

### O mistério do "HD de 1 TB que só tem 931 GB"
Esta é a pergunta que todo técnico escuta. **O cliente não foi enganado.** O fabricante vende em decimal e o Windows mostra em binário:

:::exemplo Exemplo resolvido: 1 TB no Windows
- O fabricante diz: 1 TB = **1.000.000.000.000 bytes**.
- O Windows divide por 1.024 três vezes (para chegar em "GB" binário):
- 1.000.000.000.000 ÷ 1.024 ÷ 1.024 ÷ 1.024 = **931,32 GiB**.

O Windows mostra "931 GB", mas na verdade são **931 GiB**. Não sumiu nada: é a mesma quantidade de bytes, em outra unidade. E ainda há uma pequena parte usada pela formatação e pelas partições de recuperação.
:::

| Capacidade vendida | O Windows mostra (aprox.) | "Perda" aparente |
|---|---|---|
| 128 GB | 119 GB | 7% |
| 256 GB | 238 GB | 7% |
| 500 GB | 465 GB | 7% |
| 1 TB | 931 GB | 7% |
| 2 TB | 1,81 TB | 9% |
| 4 TB | 3,63 TB | 9% |

A diferença cresce com a unidade: ≈ 2,4% no KB, ≈ 4,9% no MB, ≈ 7,4% no GB e ≈ 9,9% no TB.

### Cada unidade em detalhe

#### KB: kilobyte
- **Valor**: 1.000 bytes (SI) ou 1.024 bytes (KiB).
- **Origem**: o prefixo grego *khilioi* (mil). Nos anos 1970–80, as memórias eram medidas em KB (o Apple II de 1977 vinha com 4 KB).
- **Exemplos**: um e-mail só de texto (≈ 5–20 KB), uma página de texto puro (≈ 2–3 KB), um ícone (≈ 1–10 KB).
- **Curiosidade**: o computador de bordo da **Apollo 11** (1969) tinha cerca de **4 KB de RAM** e **72 KB de memória fixa**.

#### MB: megabyte
- **Valor**: 1.000 KB = 1.000.000 bytes (SI) ou 1.048.576 bytes (MiB).
- **Origem**: grego *megas* (grande). Ficou popular com os disquetes (1,44 MB) e os primeiros HDs de PC (10 MB no IBM PC XT, 1983).
- **Exemplos**: foto de celular (2–6 MB), música MP3 de 4 minutos (≈ 4 MB a 128 kbps), livro digital (1–5 MB), um minuto de vídeo em Full HD (≈ 60–130 MB).

#### GB: gigabyte
- **Valor**: 1.000 MB = 10⁹ bytes (SI) ou 1.024 MiB (GiB).
- **Origem**: grego *gigas* (gigante). Os HDs de PC passaram de 1 GB por volta de 1991–1995.
- **Exemplos**: filme em Full HD (≈ 2–5 GB), Windows 11 instalado (≈ 25–30 GB), jogo moderno (50–150 GB), memória RAM (8, 16, 32 GB), plano de celular (20 GB por mês).

#### TB: terabyte
- **Valor**: 1.000 GB = 10¹² bytes (SI) ou 1.024 GiB (TiB).
- **Origem**: grego *teras* (monstro). O primeiro HD de 1 TB para consumidores foi o **Hitachi Deskstar 7K1000**, em **2007**.
- **Exemplos**: SSD de PC (1–2 TB), HD de backup (2–8 TB), cerca de **250 mil fotos** de 4 MB, cerca de **500 horas** de vídeo Full HD.

#### PB e além
- **1 PB** ≈ 1.000 TB: o armazenamento de um data center pequeno.
- A consultoria **IDC** projetou, em 2018, que a "datasfera" global chegaria a **≈ 175 ZB em 2025**, e a IA acelerou ainda mais esse crescimento.

## Como calcular: o método de bancada

### Regra geral
- Para **subir** de unidade (B → KB → MB → GB → TB): **divida** por 1.000 (ou 1.024).
- Para **descer** de unidade (TB → GB → MB...): **multiplique** por 1.000 (ou 1.024).
- **Bits → bytes**: divida por 8. **Bytes → bits**: multiplique por 8.

:::exemplo Exemplo 1: quantas fotos cabem num celular de 128 GB?
- Espaço livre real: ≈ 100 GB (o sistema e os apps ocupam o resto).
- Foto média: 4 MB.
- 100 GB = 100.000 MB → 100.000 ÷ 4 = **≈ 25.000 fotos**.
:::

:::exemplo Exemplo 2: quantas músicas cabem num pen drive de 32 GB?
- Windows mostra ≈ 29,8 GB livres.
- Música de 4 MB → 29.800 MB ÷ 4 = **≈ 7.450 músicas**, ou cerca de 500 horas de música.
:::

:::exemplo Exemplo 3: quanto espaço ocupa uma foto sem compressão?
Uma foto de **12 megapixels** com **24 bits por pixel** (3 bytes):
12.000.000 × 3 = 36.000.000 bytes = **36 MB** sem compressão. Em JPEG, ela cai para ≈ 3–5 MB. A compressão reduz o tamanho entre 7 e 12 vezes.
:::

:::exemplo Exemplo 4: quantos bits tem um arquivo de 2 MB?
2 MB = 2.000.000 bytes × 8 = **16.000.000 bits** (16 megabits).
:::

## Para que servem essas unidades na prática

| Situação | Unidade usada | Exemplo |
|---|---|---|
| Comprar SSD ou HD | GB / TB (decimal) | SSD de 1 TB |
| Comprar memória RAM | GB (na prática, binário: 16 GB = 16 GiB) | 2 × 8 GB DDR5 |
| Tamanho de arquivo no Windows | KB, MB, GB (binários com nome SI) | "Vídeo.mp4 – 1,2 GB" |
| Velocidade de internet | **Mbps**, **Gbps** (bits!) | Fibra de 500 Mbps |
| Velocidade de SSD | **MB/s**, **GB/s** (bytes) | NVMe de 7.000 MB/s |
| Cache de processador | MB | 32 MB de L3 |
| Memória de vídeo (VRAM) | GB | RTX com 8 GB |
| Plano de celular | GB por mês | 30 GB |
