"""Baixa as imagens do Wikimedia Commons usadas na masterclass e registra autor e licença."""
import io, json, os, re, sys, urllib.parse, urllib.request
from html import unescape

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, 'saida', 'img')
UA = 'MasterclassHardware/1.0 (hgsdevv@gmail.com) python-urllib'

# módulo -> [(arquivo no Commons, legenda)]
IMAGENS = {
    '02': [
        ('Chinese_Suanpan_Abacus.jpg', 'Ábaco chinês (suanpan)'),
        ('Antikythera_Fragment_A_(Front).webp', 'Mecanismo de Anticítera, fragmento A'),
        ('Machine_a_Calculer_Blaise_Pascale_1642_-_Musée_des_arts_et_métiers.jpg', 'Pascalina, de Blaise Pascal'),
        ('Charles_Babbage_Difference_Engine_No1.jpg', 'Máquina Diferencial de Charles Babbage'),
        ('Ada_Lovelace_portrait.jpg', 'Ada Lovelace, a primeira programadora'),
        ('Harvard_Mark_I_Computer_-_Left_Segment.jpg', 'Harvard Mark I (1944)'),
        ('Replica-of-first-transistor.jpg', 'Réplica do primeiro transistor (Bell Labs, 1947)'),
        ('C4004_(Intel).jpg', 'Intel 4004, o primeiro microprocessador comercial (1971)'),
        ('IBM_PC-5150.JPG', 'IBM PC 5150 (1981)'),
    ],
    '03': [
        ('Glen_Beck_and_Betty_Snyder_program_the_ENIAC_in_building_328_at_the_Ballistic_Research_Laboratory.jpg', 'Glen Beck e Betty Snyder programando o ENIAC'),
        ('Eniac_(cropped).jpg', 'O ENIAC'),
    ],
    '07': [('Arpanet_logical_map,_march_1977.png', 'Mapa lógico da ARPANET, março de 1977')],
    '16': [
        ('Remington_No._1_typewriter,_made_by_Remington_&_Songs,_Ilion,_NY,_1873-1878,_the_first_Sholes_&_Glidden_model_typewriter_made_by_Remington_-_Wisconsin_Historical_Museum_-_DSC02806.JPG', 'Sholes & Glidden / Remington nº 1, a primeira máquina QWERTY'),
        ('KB_Portuguese_Brazil_ABNT2.svg', 'Layout de teclado ABNT2'),
    ],
    '18': [('Asus-ROG-Strix-Z390-F-Gaming-Motherboard_20201120_DSC6025.jpg', 'Placa-mãe ATX')],
    '19': [('AMD_Ryzen_9_9950X.jpg', 'Processador AMD Ryzen 9 9950X')],
    '22': [('Desktop_DDR_Memory_Comparison.svg', 'Comparação dos módulos DDR de desktop: repare no chanfro em posições diferentes')],
    '23': [('Asus_C501PS_Nvidia_Geforce_7600_graphics_card_1.JPG', 'Placa de vídeo dedicada')],
    '25': [('ATX_Computer_power_supply_unit.jpg', 'Fonte de alimentação ATX')],
    '27': [('Laptop-hard-drive-exposed.jpg', 'Interior de um HD: prato e braço com a cabeça de leitura')],
    '28': [('Samsung_NVMe_M.2_970_EVO_Plus_18540.jpg', 'SSD M.2 NVMe')],
}


def api(titulos):
    q = urllib.parse.urlencode({
        'action': 'query', 'format': 'json', 'prop': 'imageinfo',
        'iiprop': 'url|extmetadata', 'iiurlwidth': '1400',
        'titles': '|'.join('File:' + t for t in titulos)})
    req = urllib.request.Request('https://commons.wikimedia.org/w/api.php?' + q, headers={'User-Agent': UA})
    return json.load(urllib.request.urlopen(req, timeout=60))


def limpa(html):
    return unescape(re.sub(r'<[^>]+>', '', html or '')).strip()


def main():
    os.makedirs(DESTINO, exist_ok=True)
    creditos = {}
    todos = [t for lista in IMAGENS.values() for t, _ in lista]
    for i in range(0, len(todos), 20):
        dados = api(todos[i:i + 20])
        normal = {n['to']: n['from'] for n in dados['query'].get('normalized', [])}
        for pagina in dados['query']['pages'].values():
            titulo = normal.get(pagina['title'], pagina['title'])[5:].replace(' ', '_')
            if 'imageinfo' not in pagina:
                print('FALTOU', titulo); continue
            info = pagina['imageinfo'][0]
            meta = info.get('extmetadata', {})
            url = info.get('thumburl') or info['url']
            ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower() or '.jpg'
            nome = re.sub(r'[^A-Za-z0-9]+', '-', os.path.splitext(titulo)[0])[:60].strip('-').lower() + ext
            caminho = os.path.join(DESTINO, nome)
            if not os.path.exists(caminho):
                req = urllib.request.Request(url, headers={'User-Agent': UA})
                io.open(caminho, 'wb').write(urllib.request.urlopen(req, timeout=120).read())
            creditos[titulo] = {
                'arquivo': 'img/' + nome,
                'autor': limpa(meta.get('Artist', {}).get('value')) or 'Autor desconhecido',
                'licenca': limpa(meta.get('LicenseShortName', {}).get('value')),
                'pagina': info.get('descriptionurl'),
            }
            print('ok', nome)
    saida = {m: [dict(creditos.get(t.replace(' ', '_'), {}), legenda=leg) for t, leg in lista]
             for m, lista in IMAGENS.items()}
    io.open(os.path.join(RAIZ, 'conteudo', 'imagens.json'), 'w', encoding='utf-8').write(
        json.dumps(saida, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
