O computador só entende números. Então, como ele guarda a letra "A", o "ç" ou um emoji? A resposta é uma **tabela de codificação**: um acordo que diz "o número 65 significa A". A primeira tabela universal foi a **ASCII**, e ela ainda está no coração de tudo o que você digita.

## O que é ASCII

**ASCII** significa ***American Standard Code for Information Interchange*** (Código Padrão Americano para o Intercâmbio de Informação). É uma tabela que associa **128 caracteres** a números de **0 a 127**, usando **7 bits** (2⁷ = 128).

## Como surgiu

- **Antes do ASCII**, cada fabricante tinha o seu código. A IBM usava o **EBCDIC**, e os teletipos usavam o **código Baudot** (5 bits, de 1870). Computadores de marcas diferentes não conseguiam trocar texto.
- Em **1960**, a **ASA** (*American Standards Association*, hoje **ANSI**) criou o comitê **X3.2** para fazer um código comum. Um dos principais criadores foi **Bob Bemer** (IBM), muitas vezes chamado de "pai do ASCII" (embora o padrão seja obra de um comitê), que também popularizou a tecla **ESC** e a barra invertida **\\**.
- A primeira versão foi publicada em **1963**; as **letras minúsculas** foram aprovadas em 1965 e publicadas na revisão de **1967**; a forma definitiva, em **1986**.
- Em **1968**, o presidente dos EUA, **Lyndon Johnson**, determinou que todos os computadores do governo federal fossem compatíveis com ASCII, o que o tornou padrão de fato.

## Por que 7 bits?
Na época, cada bit custava caro em transmissão e armazenamento. **7 bits** davam espaço para letras maiúsculas e minúsculas, números, pontuação e comandos de controle. O **8º bit** do byte era usado como **bit de paridade**, para detectar erros na transmissão.

## Como a tabela é organizada

| Faixa (decimal) | Faixa (hexa) | Conteúdo |
|---|---|---|
| **0–31** | 00–1F | **Caracteres de controle** (não imprimíveis): comandos para teletipos e impressoras |
| **32** | 20 | **Espaço** |
| **33–47** | 21–2F | Pontuação e símbolos: `! " # $ % & ' ( ) * + , - . /` |
| **48–57** | 30–39 | **Dígitos 0–9** |
| **58–64** | 3A–40 | `: ; < = > ? @` |
| **65–90** | 41–5A | **Letras maiúsculas A–Z** |
| **91–96** | 5B–60 | ``[ \ ] ^ _ ` `` |
| **97–122** | 61–7A | **Letras minúsculas a–z** |
| **123–126** | 7B–7E | `{ | } ~` |
| **127** | 7F | **DEL** (apagar) |

### Os caracteres de controle mais importantes
| Dec | Sigla | Nome | Uso até hoje |
|---|---|---|---|
| 0 | NUL | Nulo | Marca o fim de texto na linguagem C |
| 7 | BEL | Campainha | Fazia o teletipo tocar um sino; ainda gera o "bip" do terminal |
| 8 | BS | Backspace | Tecla Backspace |
| 9 | HT | Tabulação horizontal | Tecla **Tab** |
| 10 | LF | *Line Feed* (nova linha) | Quebra de linha no Linux e no macOS |
| 13 | CR | *Carriage Return* (retorno do carro) | Junto com LF, quebra de linha no Windows (**CR+LF**) |
| 27 | ESC | *Escape* | Tecla **Esc** |

:::curiosidade A máquina de escrever ainda está no seu Windows
"**Carriage Return**" vem da máquina de escrever: era a alavanca que fazia o **carro** (o rolo com o papel) voltar para o começo da linha. "**Line Feed**" girava o rolo uma linha para cima. O Windows ainda usa os **dois comandos juntos (CR+LF)** para cada "Enter", herança direta das máquinas de escrever e dos teletipos.
:::

## Tabela ASCII imprimível (32–126)

{{tabela-ascii}}

## Truques de quem domina a tabela

1. **Maiúscula × minúscula: diferença de 32.** "A" = 65 e "a" = 97. Em binário, só muda **um bit** (o de valor 32): `01000001` × `01100001`. Os programadores usam isso para converter letras rapidamente.
2. **Dígito para número: subtraia 48.** O caractere "7" é o código 55; 55 − 48 = 7.
3. **Ordem alfabética = ordem numérica.** Por isso o computador ordena "A, B, C..." facilmente. Mas maiúsculas (65–90) vêm **antes** das minúsculas (97–122), por isso "Zebra" pode aparecer antes de "abacaxi" numa ordenação simples.

:::exemplo Exemplo: "Oi!" em ASCII
| Caractere | Decimal | Hexa | Binário |
|---|---|---|---|
| O | 79 | 4F | 01001111 |
| i | 105 | 69 | 01101001 |
| ! | 33 | 21 | 00100001 |

A palavra "Oi!" ocupa **3 bytes** = 24 bits: `01001111 01101001 00100001`.
:::

## Como calcular e consultar

- **Letra → número**: A = 65, então B = 66, C = 67... Para qualquer maiúscula: **65 + posição no alfabeto − 1**. Exemplo: H é a 8ª letra → 65 + 7 = **72**.
- **Minúscula**: some 32 à maiúscula. h = 72 + 32 = **104**.
- **No Windows**: segure **Alt** e digite o código no **teclado numérico**:
  - `Alt + 64` → **@**
  - `Alt + 0199` → **Ç** (com o zero na frente, usa a tabela Windows-1252)
  - `Alt + 0231` → **ç**
  - `Alt + 0176` → **°** (grau)
  - `Alt + 0169` → **©**
- **No Excel**: `=CÓDIGO("A")` retorna 65 e `=CARACT(65)` retorna "A".

## Depois do ASCII: o "ASCII estendido" e o problema dos acentos

O ASCII foi feito para o inglês e **não tem acentos**: nada de á, ç, ã. Como o byte tem 8 bits, sobravam **128 posições (128–255)**, e cada fabricante ou país as preencheu de um jeito:

| Codificação | Uso |
|---|---|
| **Code page 437** | O IBM PC original (símbolos gráficos de caixas, letras gregas) |
| **Code page 850** | MS-DOS na Europa Ocidental e no Brasil |
| **ISO-8859-1 (Latin-1)** | Padrão para línguas da Europa Ocidental, incluindo o português |
| **Windows-1252** | Versão da Microsoft do Latin-1 |

Resultado: um texto escrito num padrão e lido em outro vira **"mojibake"** (lixo de caracteres). É o famoso `ação` aparecendo como **`aÃ§Ã£o`**, problema que todo brasileiro já viu em e-mail ou site.

## Unicode e UTF-8: a solução definitiva

- **Unicode (1991)**: um catálogo **único** para todos os caracteres de todas as línguas, mais símbolos e emojis. Cada caractere recebe um "número de identidade" (*code point*), como `U+00E7` para o **ç** e `U+1F600` para o 😀. A versão **17.0** (setembro de 2025) tem **159.801 caracteres**.
- **UTF-8 (1992)**: o jeito mais usado de **gravar** Unicode em bytes, criado por **Ken Thompson e Rob Pike** (os mesmos do Unix e da linguagem Go). Dizem que o esboço foi rabiscado num **guardanapo**, num restaurante em Nova Jersey.
  - Os caracteres ASCII (0–127) continuam ocupando **1 byte**, idênticos ao ASCII. Por isso o UTF-8 é **100% compatível com ASCII**.
  - Acentos como **ç, ã, é** ocupam **2 bytes**.
  - Caracteres chineses e japoneses ocupam **3 bytes**.
  - **Emojis** ocupam **4 bytes**.
- Hoje, **≈ 99% dos sites** usam UTF-8 (W3Techs, 2026).

:::exemplo Exemplo: quantos bytes tem "Ação 😀"?
| Caractere | Bytes em UTF-8 |
|---|---|
| A | 1 |
| ç | 2 |
| ã | 2 |
| o | 1 |
| (espaço) | 1 |
| 😀 | 4 |
| **Total** | **11 bytes** |

Por isso uma mensagem de SMS com acentos ou emoji "cabe menos letras": a codificação muda.
:::

## Para que serve saber isso

- **Suporte técnico**: resolver texto com caracteres estranhos (problema de codificação, não de vírus).
- **Programação e web**: sempre salvar arquivos em **UTF-8** e declarar `<meta charset="utf-8">` no HTML.
- **Redes e segurança**: ler pacotes e arquivos em hexadecimal (os dumps mostram o ASCII ao lado).
- **Teclado**: entender os códigos Alt e por que o layout ABNT2 precisa ser configurado corretamente (módulo de Teclado).
