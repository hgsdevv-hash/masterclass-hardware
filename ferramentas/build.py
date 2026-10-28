"""Gera a masterclass em HTML interativo, apostila para PDF e documento Word.

Uso: python ferramentas/build.py
Saídas em saida/: index.html, apostila.html, img/, (PDF e DOCX são gerados por pdf.py e docx_build.py).
"""
import html, io, json, os, re, shutil
import markdown
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTEUDO = os.path.join(RAIZ, 'conteudo')
SAIDA = os.path.join(RAIZ, 'saida')
TITULO = 'Masterclass de Hardware'
SUBTITULO = 'Do ábaco à computação quântica: história, fundamentos e cada componente do computador'
DATA = 'Outubro de 2026'

ROTULOS = {
    'exemplo': 'Exemplo', 'dica': 'Dica', 'atencao': 'Atenção',
    'curiosidade': 'Curiosidade', 'especialista': 'Especialista',
}


def ler(nome):
    return io.open(os.path.join(CONTEUDO, nome), encoding='utf-8').read()


def carregar_json(nome):
    return json.loads(ler(nome))


def slug(texto):
    texto = re.sub(r'<[^>]+>', '', texto).lower()
    tabela = str.maketrans('áàâãäéèêëíìîïóòôõöúùûüç', 'aaaaaeeeeiiiiooooouuuuc')
    texto = texto.translate(tabela)
    return re.sub(r'[^a-z0-9]+', '-', texto).strip('-')[:60]


# ---------- Markdown ----------

def preprocessar(md):
    def callout(m):
        tipo, titulo, corpo = m.group(1), m.group(2).strip(), m.group(3)
        rotulo = ROTULOS.get(tipo, tipo.title())
        cabeca = html.escape(titulo) if titulo and titulo.lower() != rotulo.lower() else ''
        return (f'<div class="callout c-{tipo}" markdown="1">\n'
                f'<p class="callout-t"><span>{rotulo}</span>{(" " + cabeca) if cabeca else ""}</p>\n\n'
                f'{corpo}\n\n</div>')
    md = re.sub(r'^:::(\w+)[ \t]*(.*?)\n(.*?)\n:::[ \t]*$', callout, md, flags=re.S | re.M)
    md = re.sub(r'\{\{img:[^}]*\}\}\n?', '', md)
    md = re.sub(r'^# (.+)$', r'## \1 {: .divisor }', md, flags=re.M)
    return md


def md_para_html(md):
    corpo = markdown.markdown(preprocessar(md), extensions=['tables', 'fenced_code', 'md_in_html', 'sane_lists', 'attr_list'])
    usados = set()

    def ancora(m):
        nivel, attrs, texto = m.group(1), m.group(2) or '', m.group(3)
        base = slug(texto) or 'secao'
        s, n = base, 2
        while s in usados:
            s, n = f'{base}-{n}', n + 1
        usados.add(s)
        return f'<h{nivel} id="{s}"{attrs}>{texto}</h{nivel}>'
    corpo = re.sub(r'<h([23])((?: [^>]*)?)>(.*?)</h\1>', ancora, corpo)
    corpo = re.sub(r'<table>', '<div class="tabela"><table>', corpo)
    corpo = corpo.replace('</table>', '</table></div>')
    return corpo


# ---------- Imagens ----------

def preparar_imagens(imagens):
    """Converte as imagens para web (≤ 1400 px, JPEG/PNG) em saida/img."""
    origem = os.path.join(SAIDA, 'img')
    destino = os.path.join(SAIDA, 'assets')
    os.makedirs(destino, exist_ok=True)
    for lista in imagens.values():
        for im in lista:
            if not im.get('arquivo'):
                continue
            src = os.path.join(SAIDA, im['arquivo'])
            base = os.path.splitext(os.path.basename(src))[0]
            img = Image.open(src)
            transparente = img.mode in ('RGBA', 'LA', 'P') and src.lower().endswith('.png')
            img.thumbnail((1400, 1400))
            if transparente:
                nome = base + '.png'
                fundo = Image.new('RGB', img.size, (255, 255, 255))
                fundo.paste(img.convert('RGBA'), mask=img.convert('RGBA').split()[-1])
                fundo.save(os.path.join(destino, nome), optimize=True)
            else:
                nome = base + '.jpg'
                img.convert('RGB').save(os.path.join(destino, nome), quality=82, optimize=True, progressive=True)
            im['web'] = 'assets/' + nome
    return imagens


def figuras_html(lista):
    if not lista:
        return ''
    itens = []
    for im in lista:
        if not im.get('web'):
            continue
        credito = f'{html.escape(im["autor"][:80])} · {html.escape(im["licenca"])} · Wikimedia Commons'
        itens.append(
            f'<figure><img src="{im["web"]}" alt="{html.escape(im["legenda"])}" loading="lazy">'
            f'<figcaption>{html.escape(im["legenda"])}<small><a href="{im["pagina"]}" target="_blank" rel="noopener">{credito}</a></small></figcaption></figure>')
    classe = 'galeria' if len(itens) > 1 else 'galeria unica'
    return f'<div class="{classe}">{"".join(itens)}</div>'


def videos_html(lista):
    if not lista:
        return ''
    linhas = ''.join(
        f'<li><a href="{u}" target="_blank" rel="noopener"><span class="v-t">{html.escape(t)}</span>'
        f'<span class="v-m">{html.escape(c)} · {lang} · {dur}</span></a></li>'
        for t, c, u, lang, dur in lista)
    return f'<section class="videos"><h2 id="para-assistir">Para assistir</h2><ul>{linhas}</ul></section>'


# ---------- Blocos especiais ----------

def tabela_ascii_print():
    linhas = []
    cods = list(range(32, 127))
    colunas = 5
    por_col = -(-len(cods) // colunas)
    cab = ''.join('<th>Dec</th><th>Hex</th><th>Car.</th>' for _ in range(colunas))
    for i in range(por_col):
        cel = ''
        for c in range(colunas):
            k = i + c * por_col
            if k < len(cods):
                n = cods[k]
                ch = 'espaço' if n == 32 else html.escape(chr(n))
                cel += f'<td>{n}</td><td>{n:02X}</td><td class="ch">{ch}</td>'
            else:
                cel += '<td></td><td></td><td></td>'
        linhas.append(f'<tr>{cel}</tr>')
    return f'<div class="tabela ascii-print"><table><thead><tr>{cab}</tr></thead><tbody>{"".join(linhas)}</tbody></table></div>'


def tabela_ascii_interativa():
    cards = ''.join(
        f'<button class="ac" data-n="{n}"><b>{"␠" if n == 32 else html.escape(chr(n))}</b><span>{n}</span><i>{n:02X}</i></button>'
        for n in range(32, 127))
    return ('<div class="ascii-tool"><label class="campo"><span>Digite um texto para ver os códigos</span>'
            '<input id="ascii-in" type="text" value="Oi!" autocomplete="off"></label>'
            '<div id="ascii-out" class="ascii-out"></div>'
            f'<div class="ascii-grid">{cards}</div>'
            '<p class="ascii-det" id="ascii-det">Toque num caractere para ver o binário.</p></div>')


def linha_do_tempo_print(eventos):
    linhas = ''.join(
        f'<tr><td class="ano">{html.escape(e["ano"])}</td><td><b>{html.escape(e["titulo"])}</b><br>{html.escape(e["texto"])}</td>'
        f'<td>{html.escape(e["quem"])}</td></tr>' for e in eventos)
    return (f'<div class="tabela"><table class="tl-print"><thead><tr><th>Ano</th><th>Marco</th><th>Quem</th></tr></thead>'
            f'<tbody>{linhas}</tbody></table></div>')


def linha_do_tempo_interativa(eventos):
    eras = []
    for e in eventos:
        if e['era'] not in eras:
            eras.append(e['era'])
    chips = '<button class="chip on" data-era="*">Todas</button>' + ''.join(
        f'<button class="chip" data-era="{html.escape(x)}">{html.escape(x)}</button>' for x in eras)
    itens = ''.join(
        f'<li data-era="{html.escape(e["era"])}"><span class="tl-ano">{html.escape(e["ano"])}</span>'
        f'<div class="tl-c"><b>{html.escape(e["titulo"])}</b><span class="tl-q">{html.escape(e["quem"])}</span>'
        f'<p>{html.escape(e["texto"])}</p></div></li>' for e in eventos)
    return f'<div class="tl"><div class="chips">{chips}</div><ol class="tl-lista">{itens}</ol></div>'


# ---------- Montagem ----------

def montar_modulos():
    modulos = carregar_json('modulos.json')
    eventos = carregar_json('linha-do-tempo.json')
    videos = carregar_json('videos.json')
    imagens = preparar_imagens(carregar_json('imagens.json'))
    quiz = carregar_json('quiz.json')
    for m in modulos:
        corpo = md_para_html(ler(m['arquivo']))
        m['html_i'] = (corpo.replace('<p>{{linha-do-tempo}}</p>', linha_do_tempo_interativa(eventos))
                            .replace('<p>{{tabela-ascii}}</p>', tabela_ascii_interativa()))
        m['html_p'] = (corpo.replace('<p>{{linha-do-tempo}}</p>', linha_do_tempo_print(eventos))
                            .replace('<p>{{tabela-ascii}}</p>', tabela_ascii_print()))
        m['figuras'] = figuras_html(imagens.get(m['id']))
        m['videos'] = videos_html(videos.get(m['id']))
        m['quiz'] = quiz.get(m['id'], [])
        m['secoes'] = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', corpo)
    return modulos, eventos


def texto_puro(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()


def indice_busca(modulos):
    itens = []
    for m in modulos:
        partes = re.split(r'(<h[23] id="[^"]+"[^>]*>.*?</h[23]>)', m['html_p'])
        atual, ancora = m['titulo'], ''
        for p in partes:
            cab = re.match(r'<h[23] id="([^"]+)"[^>]*>(.*?)</h[23]>', p)
            if cab:
                ancora, atual = cab.group(1), texto_puro(cab.group(2))
                continue
            t = texto_puro(p)
            if t:
                itens.append({'m': m['id'], 'a': ancora, 's': atual, 'mt': m['titulo'], 't': t[:1200]})
    return itens


def gerar_interativo(modulos, eventos):
    css = io.open(os.path.join(RAIZ, 'ferramentas', 'estilo.css'), encoding='utf-8').read()
    js = io.open(os.path.join(RAIZ, 'ferramentas', 'app.js'), encoding='utf-8').read()
    ferramentas = io.open(os.path.join(RAIZ, 'ferramentas', 'ferramentas.html'), encoding='utf-8').read()
    partes, nav = [], []
    parte_atual = None
    for m in modulos:
        if m['parte'] != parte_atual:
            if parte_atual is not None:
                nav.append('</ul>')
            parte_atual = m['parte']
            nav.append(f'<p class="nav-parte">{html.escape(parte_atual)}</p><ul>')
        nav.append(f'<li><a href="#m-{m["id"]}" data-m="{m["id"]}"><span class="n">{m["id"]}</span>{html.escape(m["titulo"])}<i class="ok" aria-hidden="true"></i></a></li>')
        quiz = ''
        if m['quiz']:
            perguntas = ''
            for qi, (perg, ops, certa, expl) in enumerate(m['quiz']):
                botoes = ''.join(f'<button class="op" data-i="{i}">{html.escape(o)}</button>' for i, o in enumerate(ops))
                perguntas += (f'<div class="q" data-certa="{certa}"><p class="q-p"><b>{qi + 1}.</b> {html.escape(perg)}</p>'
                              f'<div class="ops">{botoes}</div><p class="q-e" hidden>{html.escape(expl)}</p></div>')
            quiz = (f'<section class="quiz" data-m="{m["id"]}"><h2 id="quiz">Teste seus conhecimentos</h2>{perguntas}'
                    f'<p class="q-placar" aria-live="polite"></p></section>')
        anterior = modulos[modulos.index(m) - 1] if modulos.index(m) > 0 else None
        proximo = modulos[modulos.index(m) + 1] if modulos.index(m) < len(modulos) - 1 else None
        pagina = '<nav class="pag">'
        pagina += f'<a href="#m-{anterior["id"]}" class="ant"><small>Anterior</small>{html.escape(anterior["titulo"])}</a>' if anterior else '<span></span>'
        pagina += f'<a href="#m-{proximo["id"]}" class="prox"><small>Próximo</small>{html.escape(proximo["titulo"])}</a>' if proximo else '<span></span>'
        pagina += '</nav>'
        toc = ''.join(f'<li><a href="#m-{m["id"]}/{a}">{t}</a></li>' for a, t in m['secoes'] if a not in ('para-assistir', 'quiz'))
        partes.append(
            f'<article class="mod" id="m-{m["id"]}" hidden>'
            f'<header class="mod-h"><p class="mod-parte">{html.escape(m["parte"])} · Módulo {m["id"]}</p>'
            f'<h1>{html.escape(m["titulo"])}</h1></header>'
            f'{("<details class=toc open><summary>Neste módulo</summary><ol>" + toc + "</ol></details>") if len(m["secoes"]) > 2 else ""}'
            f'{m["figuras"]}<div class="prosa">{m["html_i"]}</div>{m["videos"]}{quiz}{pagina}</article>')
    nav.append('</ul>')
    cards = ''
    vistos = []
    for m in modulos:
        if m['parte'] not in vistos:
            vistos.append(m['parte'])
    for p in vistos:
        mods = [m for m in modulos if m['parte'] == p]
        lis = ''.join(f'<li><a href="#m-{m["id"]}">{html.escape(m["titulo"])}</a></li>' for m in mods)
        cards += f'<div class="parte-card"><h3>{html.escape(p)}</h3><ul>{lis}</ul></div>'
    total_q = sum(len(m['quiz']) for m in modulos)
    inicio = (
        '<article class="mod inicio" id="m-inicio" hidden>'
        '<div class="capa"><p class="capa-k">Masterclass completa · TI · Hardware</p>'
        f'<h1>{TITULO}</h1><p class="capa-s">{SUBTITULO}</p>'
        f'<div class="capa-n"><span><b>{len(modulos)}</b> módulos</span><span><b>{len(eventos)}</b> marcos na linha do tempo</span>'
        f'<span><b>{total_q}</b> perguntas de quiz</span><span><b>8</b> ferramentas interativas</span></div>'
        '<div class="capa-a"><a class="btn" href="#m-00">Começar pela abertura</a><a class="btn sec" href="#ferramentas">Abrir as ferramentas</a></div>'
        '<div class="capa-prog"><div class="barra"><i id="prog-barra"></i></div><span id="prog-txt"></span></div></div>'
        f'<div class="partes">{cards}</div></article>')
    tools = f'<article class="mod" id="m-ferramentas" hidden>{ferramentas}</article>'
    busca = json.dumps(indice_busca(modulos), ensure_ascii=False)
    pagina = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITULO}</title>
<meta name="description" content="{SUBTITULO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800;900&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo">
  <button class="menu-btn" id="menu-btn" aria-label="Abrir o menu de módulos" aria-expanded="false"><span></span><span></span><span></span></button>
  <a class="marca" href="#inicio"><b>Masterclass</b> de Hardware</a>
  <div class="busca"><input id="busca" type="search" placeholder="Buscar em todo o material" aria-label="Buscar em todo o material" autocomplete="off"><div id="busca-res" class="busca-res" hidden></div></div>
  <a class="topo-link" href="#ferramentas">Ferramentas</a>
  <button class="tema" id="tema" aria-label="Alternar tema claro/escuro" title="Alternar tema"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg></button>
</header>
<div class="layout">
<nav class="lateral" id="lateral" aria-label="Módulos">
<a class="nav-home" href="#inicio">Início</a><a class="nav-home" href="#ferramentas">Ferramentas interativas</a>
{"".join(nav)}
</nav>
<main id="conteudo" tabindex="-1">
{inicio}{tools}{"".join(partes)}
<footer class="rodape"><p>{TITULO} · {DATA}. Fatos conferidos em fontes primárias e preços de referência de 28/10/2026.</p><p><a href="https://hgsdev.com.br" target="_blank" rel="noopener">Produzido por HGS Dev</a></p></footer>
</main>
</div>
<script>window.BUSCA={busca};window.EVENTOS={json.dumps(eventos, ensure_ascii=False)};</script>
<script>{js}</script>
</body>
</html>'''
    io.open(os.path.join(SAIDA, 'index.html'), 'w', encoding='utf-8').write(pagina)


def gerar_apostila(modulos):
    css = io.open(os.path.join(RAIZ, 'ferramentas', 'apostila.css'), encoding='utf-8').read()
    sumario, corpo = [], []
    parte_atual = None
    for m in modulos:
        if m['parte'] != parte_atual:
            parte_atual = m['parte']
            sumario.append(f'<li class="s-parte">{html.escape(parte_atual)}</li>')
        sumario.append(f'<li><a href="#m-{m["id"]}"><span>{m["id"]}</span>{html.escape(m["titulo"])}<b class="pg" data-m="{m["id"]}"></b></a></li>')
        videos = m['videos'].replace('<section class="videos">', '<section class="videos-p">')
        corpo.append(
            f'<section class="cap" id="m-{m["id"]}"><p class="cap-k">{html.escape(m["parte"])} · Módulo {m["id"]}</p>'
            f'<h1>{html.escape(m["titulo"])}</h1>{m["figuras"]}{m["html_p"]}{videos}</section>')
    pagina = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>{TITULO} — Apostila</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800;900&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<section class="capa"><div><p class="capa-k">Masterclass completa · Tecnologia da Informação</p>
<h1>{TITULO}</h1><p class="capa-s">{SUBTITULO}</p></div>
<div class="capa-r"><p>Apostila completa · {len(modulos)} módulos</p><p>{DATA}</p></div></section>
<section class="sumario"><h1>Sumário</h1><ol>{"".join(sumario)}</ol></section>
{"".join(corpo)}
<section class="colofao"><p>{TITULO} · {DATA}</p><p>Fatos conferidos em fontes primárias e de referência. Preços de referência de 28/10/2026. Imagens: Wikimedia Commons, com autor e licença indicados em cada legenda.</p><p>Produzido por HGS Dev · hgsdev.com.br</p></section>
</body></html>'''
    io.open(os.path.join(SAIDA, 'apostila.html'), 'w', encoding='utf-8').write(pagina)


def main():
    os.makedirs(SAIDA, exist_ok=True)
    modulos, eventos = montar_modulos()
    gerar_interativo(modulos, eventos)
    gerar_apostila(modulos)
    io.open(os.path.join(SAIDA, 'modulos_render.json'), 'w', encoding='utf-8').write(
        json.dumps([{k: m[k] for k in ('id', 'parte', 'titulo', 'html_p', 'figuras', 'videos')} for m in modulos], ensure_ascii=False))
    print('ok', len(modulos), 'módulos')


if __name__ == '__main__':
    main()
