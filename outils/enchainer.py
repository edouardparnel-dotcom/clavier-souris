# À deux : les 4 exercices s'enchaînent avec un seul code, et la progression
# se voit (demande de Parnel, 05/10/2026). S'applique aux bureaux niveaux 1 et 2 ;
# le niveau 3 est fabriqué à partir du niveau 2 et en hérite.
#     python outils/enchainer.py
import io, os

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def patch(chemin, extra=None):
    raw = io.open(chemin, encoding='utf-8', newline='').read(); crlf = '\r\n' in raw
    s = raw.replace('\r\n', '\n')
    if 'function lancerExercice' in s:
        print('déjà fait :', chemin); return
    def rep(a, b):
        nonlocal s
        assert s.count(a) == 1, (chemin, s.count(a), a[:80])
        s = s.replace(a, b)
    rep('</style>\n</head>', """  .b-prog { display:flex; gap:6px; flex-wrap:wrap; margin:0 0 10px; }
  .b-prog button { font:inherit; font-size:13px; padding:4px 10px; border-radius:999px; border:1px solid var(--tranche); background:var(--carte); color:var(--encre-doux); cursor:pointer; }
  .b-prog button.ok { background:var(--vert-pale); color:var(--vert); border-color:var(--vert); }
  .b-prog button.ici { border:2px solid var(--bleu); color:var(--encre); font-weight:600; }
</style>
</head>""")
    rep('<div id="b-jeu" hidden>', '<div id="b-jeu" hidden>\n        <div class="b-prog" id="b-prog" aria-label="Les exercices"></div>')
    rep("const bi = { actif: false, code: '', place: null, scen: null, d: null, etapes: [], e: 0, fait: false };",
        "const bi = { actif: false, code: '', place: null, scen: null, d: null, etapes: [], e: 0, fait: false, ordre: [], ix: 0, finis: new Set() };")
    rep("""      $('#b-num').textContent = bi.scen.titre;
      $('#b-qui').className = 'niv niv-moi'; $('#b-qui').textContent = 'Terminé';
      $('#b-faire').textContent = '✓ Bravo à vous deux !';
      $('#b-voir').textContent = '→ Changez de code pour un autre scénario.';""", """      bi.finis.add(bi.ix);
      const dernier = bi.finis.size >= bi.ordre.length;
      $('#b-num').textContent = `Exercice ${bi.ix + 1} sur ${bi.ordre.length}`;
      $('#b-qui').className = 'niv niv-moi'; $('#b-qui').textContent = 'Réussi';
      $('#b-faire').textContent = dernier ? `✓ Les ${bi.ordre.length} exercices sont faits. Bravo à vous deux !` : '✓ Exercice réussi !';
      $('#b-voir').textContent = dernier ? '→ Pour en refaire un : cliquez son nom, en haut.' : '→ Passez ensemble à l’exercice suivant.';""")
    rep("      $('#b-etat').textContent = ''; $('#b-ok').hidden = true; $('#b-suiv').hidden = true;",
        "      $('#b-etat').textContent = ''; $('#b-ok').hidden = true; $('#b-suiv').hidden = dernier;\n      $('#b-suiv').textContent = 'Exercice suivant, tous les deux →'; $('#b-suiv').classList.add('fort'); majProg();")
    rep("    $('#b-num').textContent = `Étape ${bi.e + 1} sur ${total}`;",
        "    $('#b-num').textContent = `Exercice ${bi.ix + 1} sur ${bi.ordre.length} · Étape ${bi.e + 1} sur ${total}`;\n    majProg();")
    rep("""    const d = s.donnees(hasard(+c * 7919 + 13));
    Object.assign(bi, { code: c, scen: s, d, etapes: s.etapes(d), e: 0, fait: false });
    $('#b-err').textContent = '';
    binomePreparer();
    majBinome();""", """    const k0 = SCENARIOS.indexOf(s);
    Object.assign(bi, { code: c, ordre: SCENARIOS.map((_, k) => (k0 + k) % SCENARIOS.length), finis: new Set() });
    $('#b-err').textContent = '';
    lancerExercice(0);""")
    rep("  $('#b-suiv').onclick = () => { bi.e++; bi.fait = false; majBinome(); };", """  $('#b-suiv').onclick = () => {
    if (bi.e >= bi.etapes.length) {
      const n = bi.ordre.length;
      for (let k = 1; k <= n; k++) { const j = (bi.ix + k) % n; if (!bi.finis.has(j)) return lancerExercice(j); }
      return;
    }
    bi.e++; bi.fait = false; majBinome();
  };""")
    rep("  function lireCode(c) {", """  // Les exercices s'enchaînent avec le même code : le premier chiffre choisit
  // par où commencer, les autres suivent. Chaque exercice repart d'un bureau propre.
  function lancerExercice(ix) {
    const s = SCENARIOS[bi.ordre[ix]];
    const d = s.donnees(hasard(+bi.code * 7919 + 13 + bi.ordre[ix] * 1009));
    Object.assign(bi, { ix, scen: s, d, etapes: s.etapes(d), e: 0, fait: false });
    toutRemettre();
    majBinome();
  }
  function majProg() {
    const p = $('#b-prog'); p.innerHTML = '';
    bi.ordre.forEach((k, ix) => {
      const b = document.createElement('button');
      b.className = (bi.finis.has(ix) ? 'ok' : '') + (ix === bi.ix ? ' ici' : '');
      b.textContent = (bi.finis.has(ix) ? '✓ ' : (ix + 1) + '. ') + SCENARIOS[k].titre;
      b.title = 'Aller à cet exercice (votre voisin aussi)';
      b.onclick = () => lancerExercice(ix);
      p.appendChild(b);
    });
  }
  function lireCode(c) {""")
    if extra: s = extra(s)
    io.open(chemin, 'w', encoding='utf-8', newline='').write(s.replace('\n', '\r\n') if crlf else s)
    print('ok :', chemin)

# Le niveau 2 n'avait que 3 exercices à deux : le 4e, la clé USB du club.
QUATRIEME = r"""
    { titre: 'La clé USB du club', donnees(r) {
        const p = tirer(r, Object.keys(PHOTOS), 2);
        return { pg: p[0], pd: p[1] };
      },
      secret: (d, place, e) => {
        if (e === 0 && place === 'droite') return 'La photo à mettre sur sa clé : ' + d.pg.replace(/\.jpg$/, '');
        if (e === 2 && place === 'gauche') return 'La photo à mettre sur sa clé : ' + d.pd.replace(/\.jpg$/, '');
        return '';
      },
      etapes: d => {
        const surCle = p => v => (v[USB] || []).some(i => i.nom === p);
        const brancher = { faire: 'Sous l’écran : Brancher la clé USB. Cliquez le message.', voir: 'La clé s’ouvre dans l’Explorateur.', ...fait('usb_brancher') };
        const dicter = { faire: 'Dites-lui quelle photo mettre sur sa clé.', voir: 'Le nom est dans le cadre 🔒.', ...manuel('Je l’ai dit') };
        const copier = p => ({ faire: 'Images : clic droit sur la photo dite, Copier. Clé USB : clic droit, Coller.', voir: 'La photo est sur la clé.', ...fait('fichiers', surCle(p)) });
        const verifier = { faire: 'Regardez son écran : la bonne photo est sur la clé ?', voir: 'Dans Clé USB, pas dans Images.', ...manuel('C’est la bonne') };
        const retirer = { faire: 'Clic droit sur Clé USB : Éjecter. Puis Retirer, sous l’écran.', voir: 'La clé revient sur la table.', ...fait('usb_retirer') };
        return [
          { g: brancher, d: dicter, parle: 'Dites le nom de la photo, pas sa couleur.' },
          { g: copier(d.pg), d: verifier },
          { g: dicter, d: brancher },
          { g: verifier, d: copier(d.pd) },
          { g: retirer, d: retirer, parle: 'Éjecter d’abord, retirer ensuite : sinon la photo peut être abîmée.' },
        ];
      } },
  ];

  const bi ="""

def niveau2(s):
    a = "\n  ];\n\n  const bi ="
    assert s.count(a) == 1
    return s.replace(a, QUATRIEME, 1)

patch(os.path.join(ICI, 'windows', 'index.html'))
patch(os.path.join(ICI, 'windows', 'niveau2', 'index.html'), niveau2)
