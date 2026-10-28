(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var guarda = {
    ler: function (k, padrao) { try { var v = localStorage.getItem('mh-' + k); return v === null ? padrao : JSON.parse(v); } catch (e) { return padrao; } },
    gravar: function (k, v) { try { localStorage.setItem('mh-' + k, JSON.stringify(v)); } catch (e) {} }
  };
  var fmt = function (n, casas) { return Number(n).toLocaleString('pt-BR', { maximumFractionDigits: casas === undefined ? 2 : casas }); };

  // ---- tema ----
  var tema = guarda.ler('tema', null);
  if (tema) document.documentElement.setAttribute('data-theme', tema);
  $('#tema').addEventListener('click', function () {
    var escuro = document.documentElement.getAttribute('data-theme') === 'dark' ||
      (!document.documentElement.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
    var novo = escuro ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', novo);
    guarda.gravar('tema', novo);
  });

  // ---- menu móvel ----
  var lateral = $('#lateral'), menuBtn = $('#menu-btn');
  function fecharMenu() { lateral.classList.remove('aberta'); menuBtn.setAttribute('aria-expanded', 'false'); }
  menuBtn.addEventListener('click', function () {
    var aberto = lateral.classList.toggle('aberta');
    menuBtn.setAttribute('aria-expanded', aberto ? 'true' : 'false');
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { fecharMenu(); fecharBusca(); } });

  // ---- progresso ----
  var lidos = guarda.ler('lidos', {});
  function atualizarProgresso() {
    var total = $$('.lateral li a').length, feitos = 0;
    $$('.lateral li a').forEach(function (a) {
      var ok = !!lidos[a.dataset.m];
      a.classList.toggle('lido', ok);
      if (ok) feitos++;
    });
    var barra = $('#prog-barra');
    if (barra) barra.style.width = (100 * feitos / total) + '%';
    var txt = $('#prog-txt');
    if (txt) txt.textContent = feitos ? feitos + ' de ' + total + ' módulos lidos' : 'Seu progresso fica salvo neste navegador';
  }

  // ---- roteamento ----
  function mostrar() {
    var h = decodeURIComponent(location.hash.slice(1)) || 'inicio';
    var partes = h.split('/');
    var alvo = partes[0] === 'inicio' ? 'm-inicio' : partes[0] === 'ferramentas' ? 'm-ferramentas' : partes[0];
    var mod = document.getElementById(alvo);
    if (!mod || !mod.classList.contains('mod')) { mod = $('#m-inicio'); alvo = 'm-inicio'; }
    $$('.mod').forEach(function (m) { m.hidden = m !== mod; });
    $$('.lateral li a').forEach(function (a) { a.classList.toggle('atual', 'm-' + a.dataset.m === alvo); });
    var atual = $('.lateral a.atual');
    if (atual) atual.scrollIntoView({ block: 'nearest' });
    fecharMenu();
    var titulo = $('h1', mod);
    document.title = (titulo && alvo !== 'm-inicio' ? titulo.textContent + ' · ' : '') + 'Masterclass de Hardware';
    if (partes[1]) {
      var sec = document.getElementById(partes[1]);
      if (sec && mod.contains(sec)) { sec.scrollIntoView(); return; }
    }
    window.scrollTo(0, 0);
    if (alvo.indexOf('m-') === 0 && /^m-\d+$/.test(alvo)) {
      lidos[alvo.slice(2)] = true;
      guarda.gravar('lidos', lidos);
    }
    atualizarProgresso();
  }
  window.addEventListener('hashchange', mostrar);
  // links internos para seções: "#m-09/slug" já funcionam; âncoras simples dentro do módulo:
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute('href').slice(1);
    if (id && !/^m-|^inicio$|^ferramentas$|^conteudo$/.test(id)) {
      var mod = a.closest('.mod');
      if (mod) { e.preventDefault(); location.hash = mod.id + '/' + id; }
    }
  });

  // ---- busca ----
  var campo = $('#busca'), caixa = $('#busca-res'), sel = -1;
  var semAcento = function (s) { return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); };
  var indice = (window.BUSCA || []).map(function (i) { return { i: i, n: semAcento(i.s + ' ' + i.t) }; });
  function fecharBusca() { caixa.hidden = true; sel = -1; }
  function trecho(t, termos) {
    var n = semAcento(t), p = n.indexOf(termos[0]);
    var ini = Math.max(0, p - 50), fim = Math.min(t.length, ini + 160);
    var s = (ini ? '…' : '') + t.slice(ini, fim) + (fim < t.length ? '…' : '');
    var esc = s.replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; });
    termos.forEach(function (tt) {
      if (tt.length < 2) return;
      var re = new RegExp('(' + tt.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').split('').map(function (c) { return c + '[\\u0300-\\u036f]?'; }).join('') + ')', 'gi');
      esc = esc.normalize('NFD').replace(re, '<mark>$1</mark>').normalize('NFC');
    });
    return esc;
  }
  campo.addEventListener('input', function () {
    var q = semAcento(campo.value.trim());
    if (q.length < 2) { fecharBusca(); return; }
    var termos = q.split(/\s+/);
    var res = indice.filter(function (x) { return termos.every(function (t) { return x.n.indexOf(t) >= 0; }); }).slice(0, 30);
    caixa.innerHTML = res.length ? res.map(function (x) {
      return '<a href="#m-' + x.i.m + (x.i.a ? '/' + x.i.a : '') + '"><small>' + x.i.m + ' · ' + x.i.mt + '</small><b>' + x.i.s + '</b><span>' + trecho(x.i.t, termos) + '</span></a>';
    }).join('') : '<p class="busca-vazio">Nada encontrado. Tente outra palavra.</p>';
    caixa.hidden = false; sel = -1;
  });
  campo.addEventListener('keydown', function (e) {
    var links = $$('a', caixa);
    if (!links.length) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length;
      links.forEach(function (l, i) { l.classList.toggle('sel', i === sel); });
      links[sel].scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter') { (links[sel] || links[0]).click(); fecharBusca(); campo.blur(); }
  });
  caixa.addEventListener('click', function (e) { if (e.target.closest('a')) fecharBusca(); });
  document.addEventListener('click', function (e) { if (!e.target.closest('.busca')) fecharBusca(); });

  // ---- quizzes ----
  var placares = guarda.ler('quiz', {});
  $$('.quiz').forEach(function (qz) {
    var m = qz.dataset.m, qs = $$('.q', qz), placar = $('.q-placar', qz);
    function contar() {
      var resp = qs.filter(function (q) { return q.dataset.r !== undefined; });
      var certas = resp.filter(function (q) { return q.dataset.r === q.dataset.certa; }).length;
      if (resp.length === qs.length) {
        placar.textContent = 'Você acertou ' + certas + ' de ' + qs.length + '.';
        placares[m] = certas; guarda.gravar('quiz', placares);
      }
    }
    qs.forEach(function (q) {
      $$('.op', q).forEach(function (b) {
        b.addEventListener('click', function () {
          var certa = q.dataset.certa;
          q.dataset.r = b.dataset.i;
          $$('.op', q).forEach(function (o) {
            o.disabled = true;
            if (o.dataset.i === certa) o.classList.add('certa');
            else if (o === b) o.classList.add('errada');
          });
          $('.q-e', q).hidden = false;
          contar();
        });
      });
    });
  });

  // ---- linha do tempo ----
  $$('.tl').forEach(function (tl) {
    $$('.chip', tl).forEach(function (c) {
      c.addEventListener('click', function () {
        $$('.chip', tl).forEach(function (x) { x.classList.toggle('on', x === c); });
        $$('.tl-lista li', tl).forEach(function (li) { li.hidden = c.dataset.era !== '*' && li.dataset.era !== c.dataset.era; });
      });
    });
  });

  // ---- ASCII ----
  var bin8 = function (n) { return ('00000000' + n.toString(2)).slice(-8); };
  var asciiIn = $('#ascii-in');
  if (asciiIn) {
    var out = $('#ascii-out'), det = $('#ascii-det');
    var desenhar = function () {
      var chars = Array.from(asciiIn.value).slice(0, 40);
      var bytes = 0;
      out.innerHTML = chars.map(function (ch) {
        var cp = ch.codePointAt(0), n = new TextEncoder().encode(ch).length; bytes += n;
        var info = cp < 128 ? cp + ' · ' + bin8(cp) : 'U+' + cp.toString(16).toUpperCase() + ' · ' + n + ' bytes';
        return '<span><b>' + (ch === ' ' ? '␠' : ch.replace(/[&<>]/g, '')) + '</b>' + info + '</span>';
      }).join('');
      det.textContent = chars.length ? 'Total em UTF-8: ' + bytes + ' bytes (' + bytes * 8 + ' bits).' : 'Toque num caractere para ver o binário.';
    };
    asciiIn.addEventListener('input', desenhar);
    $$('.ac').forEach(function (b) {
      b.addEventListener('click', function () {
        $$('.ac').forEach(function (x) { x.classList.toggle('sel', x === b); });
        var n = +b.dataset.n;
        det.textContent = '"' + (n === 32 ? 'espaço' : String.fromCharCode(n)) + '" → decimal ' + n + ' · hexadecimal ' + n.toString(16).toUpperCase() + ' · binário ' + bin8(n);
      });
    });
    desenhar();
  }

  // ---- ferramentas ----
  var num = function (id) { var v = parseFloat(String($(id).value).replace(',', '.')); return isNaN(v) ? null : v; };
  var ligar = function (ids, fn) { ids.forEach(function (id) { $(id).addEventListener('input', fn); }); fn(); };

  if ($('#u-v')) ligar(['#u-v', '#u-u'], function () {
    var bytes = (num('#u-v') || 0) * parseFloat($('#u-u').value);
    var linhas = [['bits', bytes * 8], ['bytes', bytes], ['KB', bytes / 1e3], ['MB', bytes / 1e6], ['GB', bytes / 1e9], ['TB', bytes / 1e12],
      ['KiB', bytes / 1024], ['MiB', bytes / 1048576], ['GiB', bytes / 1073741824], ['TiB', bytes / 1099511627776]];
    $('#u-r').innerHTML = '<table>' + linhas.map(function (l) { return '<tr><td>' + l[0] + '</td><td><b style="font-size:15px;display:inline">' + fmt(l[1], 4) + '</b></td></tr>'; }).join('') + '</table>';
  });

  if ($('#d-g')) ligar(['#d-g', '#d-m', '#d-e'], function () {
    var gb = num('#d-g') || 0, mbps = num('#d-m') || 1, ef = (num('#d-e') || 100) / 100;
    var mbs = mbps / 8 * ef, seg = gb * 1000 / mbs;
    var h = Math.floor(seg / 3600), mi = Math.floor(seg % 3600 / 60), s = Math.round(seg % 60);
    $('#d-r').innerHTML = '<b>' + (h ? h + ' h ' : '') + (mi || h ? mi + ' min ' : '') + s + ' s</b>Velocidade real ≈ ' + fmt(mbs, 1) + ' MB/s (' + fmt(mbps) + ' Mbps ÷ 8 × ' + Math.round(ef * 100) + '%).';
  });

  if ($('#o-v')) ligar(['#o-v', '#o-i', '#o-r', '#o-p'], function () {
    var V = num('#o-v'), I = num('#o-i'), R = num('#o-r'), P = num('#o-p');
    var dados = [V, I, R, P].filter(function (x) { return x !== null; }).length;
    if (dados < 2) { $('#o-res').innerHTML = 'Preencha pelo menos dois valores.'; return; }
    if (V !== null && I !== null) { R = V / I; P = V * I; }
    else if (V !== null && R !== null) { I = V / R; P = V * I; }
    else if (V !== null && P !== null) { I = P / V; R = V / I; }
    else if (I !== null && R !== null) { V = I * R; P = V * I; }
    else if (I !== null && P !== null) { V = P / I; R = V / I; }
    else if (R !== null && P !== null) { I = Math.sqrt(P / R); V = I * R; }
    $('#o-res').innerHTML = '<table><tr><td>Tensão</td><td><b style="font-size:15px;display:inline">' + fmt(V, 3) + ' V</b></td></tr><tr><td>Corrente</td><td><b style="font-size:15px;display:inline">' + fmt(I, 3) + ' A</b></td></tr><tr><td>Resistência</td><td><b style="font-size:15px;display:inline">' + fmt(R, 3) + ' Ω</b></td></tr><tr><td>Potência</td><td><b style="font-size:15px;display:inline">' + fmt(P, 2) + ' W</b></td></tr></table>' +
      (I > 10 && V < 300 ? '<p style="margin:8px 0 0;color:var(--alerta)">Acima de 10 A: além do limite de uma tomada padrão de 10 A.</p>' : '');
  });

  if ($('#e-w')) ligar(['#e-w', '#e-h', '#e-d', '#e-t'], function () {
    var kwh = (num('#e-w') || 0) / 1000 * (num('#e-h') || 0) * (num('#e-d') || 0), r = kwh * (num('#e-t') || 0);
    $('#e-r').innerHTML = '<b>R$ ' + fmt(r, 2) + ' por mês</b>' + fmt(kwh, 1) + ' kWh/mês · R$ ' + fmt(r * 12, 2) + ' por ano';
  });

  if ($('#p-c')) ligar(['#p-c', '#p-g', '#p-o', '#p-m'], function () {
    var soma = (num('#p-c') || 0) + (num('#p-g') || 0) + (num('#p-o') || 0), alvo = soma * (1 + (num('#p-m') || 0) / 100);
    var padroes = [400, 450, 500, 550, 650, 750, 850, 1000, 1200, 1300, 1600], rec = padroes.find(function (p) { return p >= alvo; }) || 1600;
    $('#p-r').innerHTML = '<b>Fonte recomendada: ' + rec + ' W</b>Consumo estimado ' + fmt(soma, 0) + ' W · com margem ' + fmt(alvo, 0) + ' W. Prefira 80 PLUS Gold e ATX 3.1 para GPUs modernas, e confira a recomendação do fabricante da placa de vídeo.';
  });

  if ($('#b-d')) {
    var bd = $('#b-d'), bb = $('#b-b'), bh = $('#b-h');
    var sync = function (de) {
      var v;
      if (de === 'd') v = parseInt(bd.value, 10);
      if (de === 'b') v = parseInt(bb.value.replace(/\s/g, ''), 2);
      if (de === 'h') v = parseInt(bh.value.replace(/^0x/i, ''), 16);
      if (isNaN(v) || v < 0) { $('#b-r').textContent = 'Valor inválido.'; return; }
      if (de !== 'd') bd.value = v;
      if (de !== 'b') bb.value = v.toString(2);
      if (de !== 'h') bh.value = v.toString(16).toUpperCase();
      var bits = v.toString(2).length;
      $('#b-r').innerHTML = 'Precisa de <b style="display:inline;font-size:16px">' + bits + ' bit' + (bits > 1 ? 's' : '') + '</b>' +
        (v >= 32 && v <= 126 ? ' · em ASCII é o caractere "' + String.fromCharCode(v) + '"' : '');
    };
    bd.addEventListener('input', function () { sync('d'); });
    bb.addEventListener('input', function () { sync('b'); });
    bh.addEventListener('input', function () { sync('h'); });
    sync('d');
  }

  if ($('#h-v')) ligar(['#h-v', '#h-u'], function () {
    var bytes = (num('#h-v') || 0) * parseFloat($('#h-u').value), gib = bytes / 1073741824;
    $('#h-r').innerHTML = '<b>O Windows mostra ≈ ' + (gib >= 1024 ? fmt(gib / 1024, 2) + ' TB' : fmt(gib, 1) + ' GB') + '</b>São os mesmos ' + fmt(bytes, 0) + ' bytes, divididos por 1.024 em vez de 1.000. Não falta nada.';
  });

  // ---- treino de atalhos ----
  var ATALHOS = [
    ['Copiar', 'Ctrl + C'], ['Colar', 'Ctrl + V'], ['Recortar', 'Ctrl + X'], ['Desfazer', 'Ctrl + Z'], ['Refazer', 'Ctrl + Y'],
    ['Selecionar tudo', 'Ctrl + A'], ['Salvar', 'Ctrl + S'], ['Procurar na página', 'Ctrl + F'], ['Abrir o Gerenciador de Tarefas', 'Ctrl + Shift + Esc'],
    ['Alternar entre janelas', 'Alt + Tab'], ['Fechar a janela', 'Alt + F4'], ['Mostrar a área de trabalho', 'Win + D'], ['Abrir o Explorador de Arquivos', 'Win + E'],
    ['Bloquear o computador', 'Win + L'], ['Histórico da área de transferência', 'Win + V'], ['Recortar um pedaço da tela', 'Win + Shift + S'],
    ['Abrir o painel de emojis', 'Win + .'], ['Nova aba no navegador', 'Ctrl + T'], ['Fechar a aba', 'Ctrl + W'], ['Reabrir a aba fechada', 'Ctrl + Shift + T'],
    ['Ir para a barra de endereço', 'Ctrl + L'], ['Janela anônima (Chrome/Edge)', 'Ctrl + Shift + N'], ['Renomear arquivo selecionado', 'F2'],
    ['Apagar a palavra inteira', 'Ctrl + Backspace'], ['Ir para o fim do documento', 'Ctrl + End'], ['Abrir as Configurações', 'Win + I'], ['Executar (Win + R)', 'Win + R']
  ];
  if ($('#a-q')) {
    var rodada = [], idx = 0, acertos = 0;
    var embaralhar = function (a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; };
    var novaRodada = function () { rodada = embaralhar(ATALHOS).slice(0, 10); idx = 0; acertos = 0; pergunta(); };
    var pergunta = function () {
      if (idx >= rodada.length) {
        $('#a-q').textContent = 'Você acertou ' + acertos + ' de ' + rodada.length + '!';
        $('#a-ops').innerHTML = '<button class="op" id="a-novo">Jogar outra rodada</button>';
        $('#a-novo').addEventListener('click', novaRodada); $('#a-p').textContent = ''; return;
      }
      var certo = rodada[idx];
      var opcoes = embaralhar([certo].concat(embaralhar(ATALHOS.filter(function (x) { return x !== certo; })).slice(0, 3)));
      $('#a-q').textContent = (idx + 1) + '/10 · ' + certo[0];
      $('#a-ops').innerHTML = opcoes.map(function (o) { return '<button class="op">' + o[1] + '</button>'; }).join('');
      $('#a-p').textContent = 'Acertos: ' + acertos;
      $$('#a-ops .op').forEach(function (b) {
        b.addEventListener('click', function () {
          var ok = b.textContent === certo[1];
          if (ok) acertos++;
          $$('#a-ops .op').forEach(function (x) { x.disabled = true; if (x.textContent === certo[1]) x.classList.add('certa'); else if (x === b) x.classList.add('errada'); });
          setTimeout(function () { idx++; pergunta(); }, ok ? 650 : 1400);
        });
      });
    };
    novaRodada();
  }

  mostrar();
})();
