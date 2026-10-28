"""Imprime a apostila em PDF com o Chrome headless, em duas passadas para numerar o sumário.

Precisa do servidor local rodando em http://localhost:5750 (pasta saida/).
"""
import io, os, re, subprocess
import pymupdf

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, 'saida')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PDF = os.path.join(SAIDA, 'Masterclass-de-Hardware.pdf')
HTML = os.path.join(SAIDA, 'apostila.html')


def imprimir():
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=20000', '--print-to-pdf=' + PDF,
                    'http://localhost:5750/apostila.html'], check=True, capture_output=True)


def paginas_dos_modulos():
    doc = pymupdf.open(PDF)
    achadas = {}
    for i, pagina in enumerate(doc):
        texto = pagina.get_text()
        for m in re.findall(r'M[óÓ]DULO (\d{2})', texto, flags=re.I):
            achadas.setdefault(m, i + 1)
    return achadas, doc.page_count


def main():
    imprimir()
    achadas, total = paginas_dos_modulos()
    pagina = io.open(HTML, encoding='utf-8').read()
    pagina = re.sub(r'<b class="pg" data-m="(\d+)">[^<]*</b>',
                    lambda m: f'<b class="pg" data-m="{m.group(1)}">{achadas.get(m.group(1), "")}</b>', pagina)
    io.open(HTML, 'w', encoding='utf-8').write(pagina)
    imprimir()
    conferidas, total2 = paginas_dos_modulos()
    diferentes = {k: (achadas[k], conferidas.get(k)) for k in achadas if achadas[k] != conferidas.get(k)}
    print('páginas:', total2, '| módulos encontrados:', len(conferidas), '| divergências:', diferentes or 'nenhuma')


if __name__ == '__main__':
    main()
