# Fabrique windows/niveau3/index.html à partir du bureau Windows niveau 2.
# Le niveau 3 ne reprend pas ce que fait le niveau 2 (clé USB, Wi-Fi,
# verrouillage, téléchargements) : il porte sur la SÉCURITÉ et le CONFORT.
#     python outils/win_n3.py      (depuis C:\Dev\clavier-souris)
import io, os

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ICI, 'windows', 'niveau2', 'index.html')
DST = os.path.join(ICI, 'windows', 'niveau3', 'index.html')
s = io.open(SRC, encoding='utf-8').read().replace('\r\n', '\n')

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)

def entre(debut, fin, neuf):
    global s
    i = s.index(debut); j = s.index(fin, i)
    s = s[:i] + neuf + s[j:]

# ── En-tête ──────────────────────────────────────────────────────────
rep("<title>", "<title>")  # contrôle d'existence
i = s.index('<title>'); j = s.index('</title>')
s = s[:i] + '<title>Bureau Windows · niveau 3' + s[j:]
rep("""    <h1>Le bureau Windows, niveau 2</h1>
    <p class="chapo">Plusieurs fenêtres, copier-coller, la clé USB, le Wi-Fi. Tout est faux ici : rien ne peut casser.</p>
    <nav class="liens-niveaux">
      <a href="../">← Bureau Windows, niveau 1</a>""", """    <h1>Le bureau Windows, niveau 3</h1>
    <p class="chapo">Se protéger des arnaques, régler l’ordinateur à sa vue, laisser un poste partagé propre. Tout est faux ici : rien ne peut casser.</p>
    <nav class="liens-niveaux">
      <a href="../">← Bureau Windows, niveau 1</a>
      <a href="../niveau2/">← Bureau Windows, niveau 2</a>""")

# Le lien du niveau 2 vers le niveau 3 ne sert à rien sur le niveau 3 lui-même.
rep('      <a href="../niveau3/">Bureau Windows, niveau 3 →</a>\n', '')

# ── Styles ───────────────────────────────────────────────────────────
rep("  .b-secret {", r"""  .b-choix { display:flex; gap:10px; flex-wrap:wrap; margin:6px 0; }
  .b-choix:empty { display:none; }
  .ico .fleche { position:absolute; left:24px; top:30px; width:18px; height:18px; }
  .fen.fige .fen-corps { filter:grayscale(1) brightness(1.06); cursor:progress; }
  .gele { padding:40px 20px; text-align:center; color:#444; font-size:16px; }
  .fen-corps { zoom:var(--zt, 1); }
  #ecran .ico .nom { font-size:calc(12px * var(--zt, 1)); }
  #ecran.pointeur-grand, #ecran.pointeur-grand * { cursor:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 24 24'%3E%3Cpath d='M3 2l15 11-6.5 1.2L15 21l-3 1.4-3.4-6.8L3 20z' fill='%23fff' stroke='%23000' stroke-width='1.4'/%3E%3C/svg%3E") 4 2, auto !important; }
  #ecran.nuit::after { content:''; position:absolute; inset:0; background:rgba(255,140,0,.16); pointer-events:none; z-index:3000; }
  .nav-fav { display:flex; gap:4px; padding:4px 8px; background:#f3f5f8; border-bottom:1px solid #dde2e8; flex-wrap:wrap; align-items:center; }
  .nav-fav button { border:0; background:transparent; font:inherit; font-size:13px; color:#1b4c9c; cursor:pointer; padding:3px 8px; border-radius:4px; }
  .nav-fav button:hover { background:#e2e8f2; }
  .nav-fav .zoom { margin-left:auto; display:flex; align-items:center; gap:2px; color:#333; font-size:13px; }
  .nav-fav .zoom button { color:#333; font-weight:700; font-size:15px; }
  .nav-page { position:relative; }
  .nav-page .zoomable { zoom:var(--zp, 1); }
  .nav-page .pub { font:inherit; font-size:20px; font-weight:700; color:#fff; background:#E8452C; border:0; border-radius:6px; padding:14px 22px; margin:8px 6px 0 0; cursor:pointer; }
  .nav-page .pub.vert { background:#21A35B; }
  .nav-page .petit-lien a { font-size:13px; color:#1b4c9c; }
  .nav-page .rep { font:inherit; padding:6px 18px; border:1px solid #9aa5b4; background:#fff; border-radius:4px; cursor:pointer; margin-right:6px; }
  .arnaque { position:absolute; inset:10px; background:#C8102E; color:#fff; border:4px solid #fff; box-shadow:0 0 0 3px #C8102E; padding:18px; text-align:center; font-size:15px; z-index:5; }
  .arnaque b { font-size:22px; display:block; margin-bottom:6px; }
  .arnaque button { font:inherit; font-weight:700; margin:6px; padding:8px 16px; border:0; border-radius:4px; cursor:pointer; }
  .mail-l { display:flex; gap:10px; padding:8px 6px; border-bottom:1px solid #e6e9ee; cursor:pointer; font-size:13px; }
  .mail-l:hover { background:#f2f6fc; }
  .mail-l b { min-width:150px; }
  .mail-o p { font-size:13px; margin:6px 0; }
  .mail-o .pj { display:inline-flex; gap:6px; align-items:center; border:1px solid #c9d0d8; border-radius:4px; padding:4px 10px; cursor:pointer; background:#fff; font:inherit; font-size:13px; }
  .mail-o .pj svg { width:18px; height:18px; }
  .par-cote div { cursor:pointer; }
  .par-ptr button { font:inherit; font-size:14px; padding:6px 14px; margin:4px 6px 0 0; border:1px solid #b9c2ce; background:#fff; border-radius:4px; cursor:pointer; }
  .par-ptr button.ici { border-color:#0A7BE0; background:#e5f0fc; }
  .regles { list-style:none; padding:0; margin:8px 0; font-size:13px; }
  .regles li::before { content:'✗ '; color:#B3261E; }
  .regles li.ok::before { content:'✓ '; color:#2E7D54; }
  .b-secret {""")
rep("  .b-secret { margin:10px 0 4px;", "  .b-secret { white-space:pre-line; margin:10px 0 4px;")

# ── Balisage ─────────────────────────────────────────────────────────
rep('          <button data-alim="redemarrer">Redémarrer</button>', '          <button data-alim="redemarrer">Redémarrer</button>\n          <button data-alim="majarret">Mettre à jour et arrêter</button>')
rep('        <p class="b-parle" id="b-parle"></p>', '        <p class="b-parle" id="b-parle"></p>\n        <div class="b-choix" id="b-choix"></div>')

# ── Missions ─────────────────────────────────────────────────────────
entre("  const MISSIONS = [", "  const NIVEAUX", r"""  const MISSIONS = [
    { k: 'telecharge', n: 1, faire: 'Internet, favori Mairie : téléchargez le formulaire.', voir: '→ Un message : téléchargement terminé.', dep: '⚠ Le vrai lien est petit, sous le titre. Les gros boutons sont des pubs.' },
    { k: 'ouvrir_pdf', t: v => v.startsWith('Formulaire'), n: 1, faire: 'Cliquez le message, ou Téléchargements : ouvrez le formulaire.', voir: '→ Le formulaire s’ouvre pour être lu.' },
    { k: 'arnaque_fermee', n: 1, faire: 'Internet, favori Actualités. Une alerte surgit : fermez Internet par sa croix.', voir: '→ La fenêtre se ferme. On n’appelle jamais.', dep: '⚠ Les boutons de l’alerte font partie du piège.' },
    { k: 'faux_site', n: 1, faire: 'Favori Banque : vrai site ou faux ?', voir: '→ Lisez l’adresse, juste avant le premier /.' },
    { k: 'vrai_site', n: 1, faire: 'Favori Impôts : vrai site ou faux ?', voir: '→ Un site de l’État finit par .gouv.fr' },
    { k: 'courriel_signale', n: 1, faire: 'Favori Messagerie : signalez le faux courriel d’Ameli.', voir: '→ Ouvrez-le. Bouton : Signaler une arnaque.', dep: '⚠ Ne cliquez pas sur son lien bleu.' },
    { k: 'notif_ignoree', n: 1, faire: 'Un message « PC lent » arrive en bas à droite : Ignorer.', voir: '→ Windows ne vend rien par des messages.', dep: '⚠ Pas de message ? Attendez quelques secondes.' },
    { k: 'texte_taille', t: v => v >= 125, n: 2, faire: 'Paramètres, Accessibilité : texte à 125 %, puis Appliquer.', voir: '→ Le texte des fenêtres grossit.', dep: '⚠ Paramètres : Démarrer, la roue dentée.' },
    { k: 'pointeur', t: v => v === 'grand', n: 2, faire: 'Même page : pointeur de la souris Grand.', voir: '→ La flèche devient plus grosse.' },
    { k: 'nuit', n: 2, faire: 'Même page : Éclairage nocturne, Activer.', voir: '→ L’écran devient plus chaud, plus doux le soir.' },
    { k: 'force', n: 2, faire: 'Deux clics sur « Vieux jeu ». Il ne répond pas : fermez-le.', voir: '→ Sa croix, puis : Fermer le programme.' },
    { k: 'imprimer_pdf', n: 2, faire: 'Bloc-notes : votre nom. Fichier, Imprimer, Microsoft Print to PDF.', voir: '→ Un PDF arrive dans Documents, rien sur papier.' },
    { k: 'raccourci', n: 2, faire: 'Explorateur : clic droit sur le formulaire, Envoyer vers le Bureau.', voir: '→ Une icône à petite flèche, sur le bureau.' },
    { k: 'piece_jointe', n: 3, faire: 'Messagerie : ouvrez le courriel de la mairie, puis sa pièce jointe.', voir: '→ Un vrai expéditeur, une pièce attendue : on peut ouvrir.' },
    { k: 'deconnecte', n: 3, faire: 'Messagerie : Se déconnecter, en haut à droite.', voir: '→ Sur un poste partagé, on se déconnecte toujours.' },
    { k: 'historique', n: 3, faire: 'Internet : le bouton ⋯, Effacer l’historique.', voir: '→ Le suivant ne verra pas vos pages.' },
    { k: 'zoom', t: v => v >= 150, n: 3, faire: 'Internet : agrandissez la page à 150 % avec le +.', voir: '→ Tout grossit dans la page, rien ailleurs.' },
    { k: 'mdp_fort', n: 3, faire: 'Paramètres, Comptes : inventez un mot de passe solide.', voir: '→ Les quatre règles passent au vert.' },
    { k: 'colle_usb', n: 3, faire: 'Sauvegardez « Rendez-vous » sur la clé : Copier, puis Coller.', voir: '→ Le fichier est en double : sur l’ordinateur et sur la clé.', dep: '⚠ La clé : le bouton sous l’écran, Brancher.' },
    { k: 'suppr_cle', n: 3, faire: 'Sur la clé, supprimez « Ancien CV ».', voir: '→ Attention : une clé n’a pas de Corbeille.' },
    { k: 'maj_arret', n: 3, faire: 'Démarrer, bouton rond : Mettre à jour et arrêter.', voir: '→ « Ne pas éteindre » : on attend, sans toucher.' },
    { k: 'rallumer', n: 3, faire: 'Rallumez : un seul appui sur le bouton.', voir: '→ Le bureau revient.' },
  ];
""")
rep("      if (m.k === 'maj_plus_tard') proposerMaj();", "      if (m.k === 'notif_ignoree') proposerNotif();")

# ── Scénarios à deux ─────────────────────────────────────────────────
entre("  const SCENARIOS = [", "\n  const bi =", r"""  const MESSAGES = [
    { t: 'SMS : « Votre colis est bloqué. Payez 1,99 € ici : colis-relivraison.info »', v: 'Arnaque', p: 'Un vrai transporteur ne réclame pas de frais par SMS.' },
    { t: 'Courriel : « Ameli : un remboursement de 247 € vous attend. Cliquez pour le recevoir. »', v: 'Arnaque', p: 'Ameli ne demande jamais vos coordonnées bancaires par courriel.' },
    { t: 'SMS : « Dr Moreau : rappel de votre rendez-vous demain à 10 h. Ne pas répondre. »', v: 'Sérieux', p: 'Un simple rappel, sans lien ni paiement.' },
    { t: 'Courriel : « Votre compte sera bloqué dans 24 h. Confirmez votre mot de passe. »', v: 'Arnaque', p: 'L’urgence et le mot de passe demandé : les deux signes de l’arnaque.' },
    { t: 'SMS : « Maman, j’ai changé de numéro. Envoie-moi 300 € vite, je t’explique. »', v: 'Arnaque', p: 'On appelle l’ancien numéro avant tout : c’est l’arnaque « coucou maman ».' },
    { t: 'Courriel de la mairie : « Inscriptions au repas des anciens jusqu’au 15, à l’accueil. »', v: 'Sérieux', p: 'Aucun lien, aucun paiement : il suffit de se déplacer.' },
  ];
  const ADRESSES = [
    { t: 'www.impots.gouv.fr/accueil', v: 'Vrai', p: 'Avant le premier / : impots.gouv.fr, le site de l’État.' },
    { t: 'www.ameli.fr/assure', v: 'Vrai', p: 'Avant le premier / : ameli.fr, le vrai site de l’Assurance maladie.' },
    { t: 'www.ameli-remboursement.com/dossier', v: 'Faux', p: 'ameli-remboursement.com n’est pas ameli.fr : un faux.' },
    { t: 'www.caf.fr.dossier-maj.net/connexion', v: 'Faux', p: 'Avant le premier /, on lit dossier-maj.net : la CAF n’est qu’un leurre.' },
    { t: 'www.service-public.fr/particuliers', v: 'Vrai', p: 'service-public.fr : le site officiel des démarches.' },
    { t: 'www.laposte-suivi-colis.info/payer', v: 'Faux', p: 'laposte-suivi-colis.info : ce n’est pas laposte.fr.' },
  ];
  const alterne = (liste, quoi) => liste.map((m, k) => {
    const lit = { faire: quoi.lire, voir: 'Sans donner votre avis.', ...manuel('J’ai lu') };
    const juge = { faire: quoi.juger, voir: quoi.indice, choix: quoi.choix, bon: m.v, pourquoi: '✓ ' + m.p, indice: quoi.indice };
    return k % 2 === 0 ? { g: lit, d: juge, parle: quoi.parle } : { g: juge, d: lit };
  });
  const REGLAGES = [
    { taille: 150, pointeur: 'grand', nuit: true },
    { taille: 125, pointeur: 'grand', nuit: true },
    { taille: 140, pointeur: 'normal', nuit: true },
    { taille: 130, pointeur: 'grand', nuit: true },
  ];
  const dire = r => `Texte : ${r.taille} %\nPointeur : ${r.pointeur === 'grand' ? 'Grand' : 'Normal'}\nÉclairage nocturne : ${r.nuit ? 'activé' : 'non'}`;

  const SCENARIOS = [
    { titre: 'Vrai ou faux ?', donnees(r) { return { m: tirer(r, MESSAGES, 4) }; },
      secret: (d, place, e) => place === (e % 2 === 0 ? 'gauche' : 'droite') ? d.m[e].t : '',
      etapes: d => alterne(d.m, { lire: 'Lisez ce message à voix haute, deux fois.', juger: 'Arnaque ou sérieux ? Décidez, puis cliquez.', choix: ['Arnaque', 'Sérieux'], indice: 'Cherchez : urgence, lien, argent, mot de passe.', parle: 'Celui qui juge dit pourquoi, à voix haute.' }) },

    { titre: 'Le bon site', donnees(r) { return { m: tirer(r, ADRESSES, 4) }; },
      secret: (d, place, e) => place === (e % 2 === 0 ? 'gauche' : 'droite') ? 'L’adresse affichée : ' + d.m[e].t : '',
      etapes: d => alterne(d.m, { lire: 'Épelez cette adresse, point par point.', juger: 'Écrivez-la sur papier. Vrai site ou faux ?', choix: ['Vrai', 'Faux'], indice: 'Ce qui compte : juste avant le premier /.', parle: 'Dites « point » pour chaque point, « tiret » pour chaque tiret.' }) },

    { titre: 'Le poste partagé', donnees() { return {}; },
      etapes: () => [
        { g: { faire: 'Internet, favori Messagerie : Se déconnecter.', voir: 'Le message : vous êtes déconnecté.', ...fait('deconnecte') },
          d: { faire: 'Quelqu’un propose de vous aider s’il a votre mot de passe. Vous le donnez ?', voir: 'Un mot de passe ne se prête pas.', choix: ['Oui', 'Non'], bon: 'Non', pourquoi: '✓ Même pour aider : il montre, vous tapez vous-même.', indice: 'Un mot de passe ne se prête jamais.' },
          parle: 'Au club, d’autres s’assoient à votre place après vous.' },
        { g: { faire: 'L’ordinateur propose d’enregistrer votre mot de passe. Au club, vous acceptez ?', voir: 'Le suivant pourrait entrer chez vous.', choix: ['Oui', 'Non'], bon: 'Non', pourquoi: '✓ Sur un poste partagé : jamais « Enregistrer le mot de passe ».', indice: 'Pensez à la personne qui s’assoit après vous.' },
          d: { faire: 'Internet : le bouton ⋯, Effacer l’historique.', voir: 'Le suivant ne verra pas vos pages.', ...fait('historique') } },
        { g: { faire: 'Démarrer, votre nom en bas : Verrouiller.', voir: 'L’écran de verrouillage s’affiche.', ...fait('verrouiller') },
          d: { faire: 'Démarrer, votre nom en bas : Verrouiller.', voir: 'L’écran de verrouillage s’affiche.', ...fait('verrouiller') },
          parle: 'On verrouille dès qu’on quitte sa place. Code PIN pour revenir : 2580.' },
      ] },

    { titre: 'Les réglages à sa vue', donnees(r) { const t = tirer(r, REGLAGES, 2); return { rg: t[0], rd: t[1] }; },
      secret: (d, place, e) => {
        if (e < 3 && place === 'gauche') return 'Les réglages de votre voisin :\n' + dire(d.rg);
        if (e >= 3 && place === 'droite') return 'Les réglages de votre voisin :\n' + dire(d.rd);
        return '';
      },
      etapes: d => {
        const dicte = { faire: 'Dictez le premier réglage. Vérifiez sur son écran.', voir: 'Paramètres, Accessibilité.', ...manuel('C’est réglé') };
        const regle = (r, k) => k === 0
          ? { faire: 'Paramètres, Accessibilité : la taille dictée, puis Appliquer.', voir: 'Le texte des fenêtres change.', ...fait('texte_taille', v => v === r.taille) }
          : k === 1
            ? { faire: 'Même page : le pointeur dicté.', voir: 'La flèche change, ou reste.', ...fait('pointeur', v => v === r.pointeur) }
            : { faire: 'Même page : l’éclairage nocturne, comme dicté.', voir: 'Activé, ou désactivé.', ...fait('nuit_etat', v => v === r.nuit) };
        const dicteK = k => ({ ...dicte, faire: ['Dictez la taille du texte.', 'Dictez le pointeur.', 'Dictez l’éclairage nocturne.'][k] });
        return [
          { g: dicteK(0), d: regle(d.rg, 0), parle: 'On règle l’ordinateur à sa vue, pas l’inverse.' },
          { g: dicteK(1), d: regle(d.rg, 1) },
          { g: dicteK(2), d: regle(d.rg, 2) },
          { g: regle(d.rd, 0), d: dicteK(0) },
          { g: regle(d.rd, 1), d: dicteK(1) },
          { g: regle(d.rd, 2), d: dicteK(2), parle: 'Lequel de ces réglages garderiez-vous chez vous ?' },
        ];
      } },
  ];
""")

# Réponses à choix dans le mode à deux.
rep("    const sec = $('#b-secret');\n    if (bi.e >= total) {", "    const sec = $('#b-secret');\n    const ch = $('#b-choix'); ch.innerHTML = '';\n    if (bi.e >= total) {")
rep("    $('#b-ok').hidden = !moi.manuel || bi.fait; $('#b-ok').textContent = moi.manuel || '';", """    $('#b-ok').hidden = !moi.manuel || bi.fait; $('#b-ok').textContent = moi.manuel || '';
    if (moi.choix && !bi.fait) moi.choix.forEach(c => {
      const b = document.createElement('button'); b.className = 'b-place'; b.textContent = c;
      b.onclick = () => {
        if (c === moi.bon) { bi.fait = true; majBinome(); $('#b-etat').textContent = moi.pourquoi || ''; }
        else $('#b-etat').textContent = '✗ ' + (moi.indice || 'Regardez encore.');
      };
      ch.appendChild(b);
    });""")

# ── Dessins, applications, état ──────────────────────────────────────
rep("    img: `", r"""    jeu: `<svg viewBox="0 0 48 48"><rect x="5" y="14" width="38" height="22" rx="11" fill="#6B4FA3"/><path d="M14 21v8M10 25h8" stroke="#fff" stroke-width="3"/><circle cx="31" cy="23" r="2.6" fill="#FFD259"/><circle cx="36" cy="28" r="2.6" fill="#7EE2A8"/></svg>`,
    fleche: `<svg class="fleche" viewBox="0 0 16 16"><rect x=".5" y=".5" width="15" height="15" rx="2" fill="#fff" stroke="#7D8794"/><path d="M4 12L11 5M6 5h5v5" stroke="#1565C0" stroke-width="2" fill="none"/></svg>`,
    img: `""")
rep("    pdf:         { titre: 'Lecteur PDF', l: 520, h: 420, g: 'pdf' },\n  };", "    pdf:         { titre: 'Lecteur PDF', l: 520, h: 420, g: 'pdf' },\n    jeu:         { titre: 'Vieux jeu', l: 430, h: 300, g: 'jeu' },\n  };")
rep("      { id: 'internet', nom: 'Internet', genre: 'app', app: 'internet', col: 0, row: 4 },\n    ];",
    "      { id: 'internet', nom: 'Internet', genre: 'app', app: 'internet', col: 0, row: 4 },\n      { id: 'jeu', nom: 'Vieux jeu', genre: 'app', app: 'jeu', col: 1, row: 0 },\n    ];")
rep("    usb = { etat: 'table', contenu: [{ nom: 'Lisez-moi.txt', genre: 'txt', contenu: 'Cette clé appartient à l’atelier informatique.\\nMerci de la rendre après usage.' }] };",
    "    usb = { etat: 'table', contenu: [{ nom: 'Lisez-moi.txt', genre: 'txt', contenu: 'Cette clé appartient à l’atelier informatique.\\nMerci de la rendre après usage.' }, { nom: 'Ancien CV.txt', genre: 'txt', contenu: 'Curriculum vitae\\n(ancienne version, à jeter)' }] };\n    tailleTexte = 100; pointeur = 'normal'; nuit = false; historique = []; connecteMail = true; notifVisible = null;")
rep("  const USB = 'Clé USB (E:)';", r"""  const USB = 'Clé USB (E:)';
  let tailleTexte = 100, pointeur = 'normal', nuit = false, historique = [], connecteMail = true, notifVisible = null;
  function appliquerReglages() {
    ecran.style.setProperty('--zt', tailleTexte / 100);
    ecran.classList.toggle('pointeur-grand', pointeur === 'grand');
    ecran.classList.toggle('nuit', nuit);
  }
  function ouCherche(item) { return Object.keys(fs).find(k => (fs[k] || []).includes(item)); }
  function ouvrirCible(item) {
    const ch = ouCherche(item);
    if (!ch) { demander({ titre: 'Élément introuvable', texte: 'L’élément visé a été déplacé, supprimé, ou la clé est retirée.', boutons: ['OK'] }); return; }
    if (item.genre === 'txt') ouvrir('blocnotes', { chemin: ch, nom: item.nom, item });
    else if (item.genre === 'pdf') ouvrir('pdf', item);
    else if (item.genre === 'img') ouvrir('photos', item.nom);
    else if (item.genre === 'dossier') ouvrir('explorateur', ch + '/' + item.nom);
  }
  function raccourci(item) {
    const [col, row] = celluleLibre();
    icones.push({ id: 'i' + (++compteId), nom: item.nom.replace(/\.[a-z]+$/i, '') + ' – Raccourci', genre: 'raccourci', cible: item, col, row });
    dessinerIcones();
    signal('raccourci', item.nom);
  }
  function telecharger(nom, doc) {
    const l = fs['Téléchargements'];
    const item = { nom: nomUnique(nom, l.map(x => x.nom)), genre: 'pdf', doc };
    l.push(item); fsChange();
    notifier({ qui: 'Internet', titre: 'Téléchargement terminé', texte: item.nom + ' · Cliquez pour l’ouvrir.', clic: () => ouvrir('pdf', item), duree: 9000 });
    signal('telecharge', item.nom);
    return item;
  }
  function proposerNotif() {
    if (notifVisible || eteint || faites.has('notif_ignoree')) return;
    setTimeout(() => {
      if (notifVisible || eteint || faites.has('notif_ignoree')) return;
      notifVisible = notifier({ qui: 'Nettoyeur Express', titre: '⚠ Votre PC est lent !', texte: '1 284 erreurs trouvées. Nettoyez maintenant pour 29,99 €.', alerte: true,
        boutons: [['Ignorer', () => { notifVisible = null; signal('notif_ignoree'); }],
                  ['Nettoyer maintenant', () => { notifVisible = null; notifier({ titre: 'C’était une publicité', texte: 'Windows ne vend rien par des messages. On choisit Ignorer.', alerte: true, duree: 9000 }); }]] });
    }, 1500);
  }
  function arreterMaj() {
    fermerPopups(true); eteint = true;
    const n = noir('<div><div class="rond"></div><div class="texte">Mise à jour en cours <span class="pct">0</span> %</div><div class="petit">Ne pas éteindre l’ordinateur.</div></div>');
    let p = 0;
    const t = setInterval(() => {
      p = Math.min(100, p + 25); n.querySelector('.pct').textContent = p;
      if (p >= 100) { clearInterval(t); n.remove(); signal('maj_arret'); arreter(false); }
    }, 500);
  }""")
rep("    etatDepart(); binomePreparer(); appliquerFond();", "    etatDepart(); binomePreparer(); appliquerFond(); appliquerReglages();")

# Icônes : raccourcis.
rep("    if (i.genre === 'txt') return G.txt;\n    return G[i.app] || G.txt;\n  }",
    "    if (i.genre === 'txt') return G.txt;\n    if (i.genre === 'raccourci') return (G[i.cible.genre] || G.txt) + G.fleche;\n    return G[i.app] || G.txt;\n  }")
rep("    else if (i.genre === 'dossier') ouvrir('explorateur', i.chemin);\n  }", "    else if (i.genre === 'dossier') ouvrir('explorateur', i.chemin);\n    else if (i.genre === 'raccourci') ouvrirCible(i.cible);\n  }")

# Explorateur : Envoyer vers le Bureau.
rep("              { t: 'Renommer', f: () => renommerItem(item), off: !!w.q },",
    "              ...(item.genre !== 'dossier' ? [{ t: 'Envoyer vers le Bureau', f: () => raccourci(item) }] : []),\n              { t: 'Renommer', f: () => renommerItem(item), off: !!w.q },")
# Clé USB : pas de Corbeille. Coller sur la clé.
rep("""  function jeterFichier(chemin, item) {
    const liste = fs[chemin]; if (!liste) return;""", """  function jeterFichier(chemin, item) {
    const liste = fs[chemin]; if (!liste) return;
    if (chemin === USB || chemin.startsWith(USB + '/')) {
      demander({ titre: 'Supprimer le fichier', texte: `Supprimer définitivement « ${item.nom} » ? Une clé USB n’a pas de Corbeille : il ne reviendra pas.`, boutons: ['Oui', 'Non'] })
        .then(r => { if (r.bouton !== 'Oui') return; fs[chemin] = fs[chemin].filter(x => x !== item); fsChange(); signal('suppr_cle', item.nom); });
      return;
    }""")
rep("    if (dest === USB && double.genre === 'img') signal('usb_copier');", "    if (dest === USB && double.genre === 'img') signal('usb_copier');\n    if (dest === USB) signal('colle_usb', double.nom);")
# Imprimer vers PDF.
rep("        notifier({ titre: 'Rien n’est sorti sur papier',", "        signal('imprimer_pdf', nomPdf);\n        notifier({ titre: 'Rien n’est sorti sur papier',")
# Alimentation.
rep("    ({ veille, arreter: () => arreter(false), redemarrer: () => arreter(true) })[b.dataset.alim]();",
    "    ({ veille, arreter: () => arreter(false), redemarrer: () => arreter(true), majarret: arreterMaj })[b.dataset.alim]();")

# ── Internet, Paramètres, Vieux jeu ──────────────────────────────────
entre("    internet(w) {", "    corbeille(w) {", r"""    internet(w) {
      w.corps.innerHTML = `<div class="nav"><div class="nav-barre"><span title="Connexion">🔒</span><input readonly><button class="btn-w nav-plus" title="Plus d’options">⋯</button></div><div class="nav-fav"></div><div class="nav-page"><div class="zoomable"></div></div></div>`;
      const barre = w.corps.querySelector('.nav-barre input'), cadre = w.corps.querySelector('.nav-page'), page = w.corps.querySelector('.zoomable'), fav = w.corps.querySelector('.nav-fav');
      let zoom = 100;
      const PAGES = {
        accueil() {
          barre.value = 'www.recherche-exemple.fr';
          page.innerHTML = `<h3>Recherche</h3><form><input placeholder="Tapez votre recherche" spellcheck="false"><button>Chercher</button></form><div class="nav-res"></div>`;
          const f = page.querySelector('form'), res = page.querySelector('.nav-res');
          f.onsubmit = e => {
            e.preventDefault(); const q = f.querySelector('input').value.trim(); if (!q) return;
            signal('cherche', q);
            res.innerHTML = `<p style="color:#666">Résultats pour « ${esc(q)} » (exemple, rien n’est vrai)</p>` + ['Tout savoir sur', 'Les meilleures idées :', 'Guide pratique :'].map(t => `<p><b>${t} ${esc(q)}</b>Une page d’exemple.</p>`).join('');
          };
        },
        mairie() {
          barre.value = 'www.mairie-saint-martin.fr/formulaires';
          page.innerHTML = `<h3>Mairie de Saint-Martin · Formulaires</h3><p class="petit-lien"><a href="#" data-vrai>Formulaire de recensement (PDF, 120 Ko)</a></p>
            <button class="pub">⬇ TÉLÉCHARGER</button><button class="pub vert">▶ DÉMARRER LE TÉLÉCHARGEMENT</button><p style="color:#999;font-size:12px;margin-top:4px">Annonce</p>`;
          page.querySelector('[data-vrai]').onclick = e => { e.preventDefault(); telecharger('Formulaire recensement.pdf', { titre: 'Formulaire de recensement', lignes: ['Nom :', 'Prénom :', 'Adresse :', 'À rapporter à l’accueil de la mairie.'] }); };
          page.querySelectorAll('.pub').forEach(b => b.onclick = () => { page.innerHTML = '<h3>Publicité</h3><p>Ce gros bouton était une publicité, pas le formulaire. Revenez sur le favori Mairie : le vrai lien est petit, sous le titre.</p>'; });
        },
        actus() {
          barre.value = 'www.infos-du-jour-exemple.fr';
          page.innerHTML = '<h3>Les infos du jour</h3><p>Le marché de Noël ouvre samedi. La piscine ferme pour travaux.</p>';
          setTimeout(() => {
            if (fen.internet !== w || !page.isConnected || barre.value !== 'www.infos-du-jour-exemple.fr') return;
            w.alerte = true;
            const a = document.createElement('div'); a.className = 'arnaque';
            a.innerHTML = '<b>⚠ VIRUS DÉTECTÉ</b><p>Votre ordinateur est bloqué. Appelez immédiatement le support Windows : 01 23 45 67 89</p><button>Appeler le support</button><button>OK</button>';
            a.querySelectorAll('button').forEach(b => b.onclick = () => { a.innerHTML = '<b>C’était le piège</b><p>Ces boutons font partie de l’arnaque. On ferme la fenêtre par SA croix, tout en haut à droite. Et on n’appelle jamais.</p>'; });
            cadre.appendChild(a);
          }, 600);
        },
        banque() { quiz('www.banque-exemple.fr.securite-clients.com/connexion', 'Votre banque · Connexion', 'non', 'faux_site',
          '✓ Juste. Avant le premier /, on lit securite-clients.com : un faux site.', '✗ Avant le premier /, on lit securite-clients.com : ce n’est pas votre banque.'); },
        impots() { quiz('www.impots.gouv.fr/accueil', 'Impôts · Votre espace particulier', 'oui', 'vrai_site',
          '✓ Juste. Avant le premier / : impots.gouv.fr, le site de l’État.', '✗ Avant le premier / : impots.gouv.fr. C’est bien le site officiel.'); },
        messagerie() {
          barre.value = 'mail.exemple.fr/boite-de-reception';
          if (!connecteMail) { page.innerHTML = '<h3>Messagerie</h3><p>Vous êtes déconnecté. Personne ne peut lire vos courriels depuis ce poste.</p>'; return; }
          const MAILS = [
            { de: 'Ameli <remboursement@ameli-sante.info>', objet: 'Remboursement de 247 € en attente', corps: ['Bonjour,', 'Un remboursement de 247 € vous attend. Pour le recevoir, confirmez vos coordonnées bancaires sous 24 h.'], lien: 'Recevoir mon remboursement', faux: true },
            { de: 'Mairie de Saint-Martin <accueil@mairie-saint-martin.fr>', objet: 'Repas des anciens : le menu', corps: ['Bonjour,', 'Vous trouverez ci-joint le menu du repas des anciens. Inscriptions à l’accueil jusqu’au 15.'], pj: 'Menu du repas.pdf' },
            { de: 'Club informatique', objet: 'Prochaine séance', corps: ['Bonjour à toutes et à tous,', 'La prochaine séance porte sur la sécurité. À jeudi !'] },
          ];
          const liste = () => {
            page.innerHTML = `<div style="display:flex;justify-content:space-between;align-items:center"><h3>Boîte de réception</h3><button class="btn-w m-deco">Se déconnecter</button></div>` + MAILS.map((m, k) => `<div class="mail-l" data-k="${k}"><b>${esc(m.de.split(' <')[0])}</b><span>${esc(m.objet)}</span></div>`).join('');
            page.querySelector('.m-deco').onclick = () => { connecteMail = false; PAGES.messagerie(); signal('deconnecte'); };
            page.querySelectorAll('.mail-l').forEach(l => l.onclick = () => lire(MAILS[+l.dataset.k]));
          };
          const lire = m => {
            page.innerHTML = `<div class="mail-o"><button class="btn-w m-ret">← Boîte de réception</button><p><b>De :</b> ${esc(m.de)}</p><p><b>Objet :</b> ${esc(m.objet)}</p><hr>${m.corps.map(p => `<p>${esc(p)}</p>`).join('')}
              ${m.lien ? `<p><a href="#" class="m-lien">${esc(m.lien)}</a></p>` : ''}${m.pj ? `<p><button class="pj">${G.pdf}${esc(m.pj)}</button></p>` : ''}
              <p style="margin-top:14px"><button class="btn-w m-sig">Signaler une arnaque</button></p><p class="m-rep"></p></div>`;
            page.querySelector('.m-ret').onclick = liste;
            const rep = page.querySelector('.m-rep');
            const l = page.querySelector('.m-lien'); if (l) l.onclick = e => { e.preventDefault(); rep.textContent = '✗ Ce lien menait vers un faux site. Regardez l’adresse de l’expéditeur : ameli-sante.info n’est pas ameli.fr.'; };
            const p = page.querySelector('.pj'); if (p) p.onclick = () => { const it = telecharger(m.pj, { titre: 'Repas des anciens', lignes: ['Entrée : velouté de potiron', 'Plat : blanquette, riz', 'Dessert : tarte aux pommes'] }); ouvrir('pdf', it); signal('piece_jointe'); };
            page.querySelector('.m-sig').onclick = () => {
              if (m.faux) { rep.textContent = '✓ Signalé, et rangé dans les indésirables. L’expéditeur ameli-sante.info n’est pas ameli.fr.'; signal('courriel_signale'); }
              else rep.textContent = '✗ Ce courriel est sérieux : un expéditeur connu, aucun paiement demandé.';
            };
          };
          liste();
        },
        historique() {
          barre.value = 'Historique';
          page.innerHTML = '<h3>Historique</h3>' + (historique.length ? historique.map(h => `<p>${esc(h)}</p>`).join('') : '<p>L’historique est vide.</p>');
        },
      };
      const quiz = (adr, titre, bon, sig, ok, ko) => {
        barre.value = adr;
        page.innerHTML = `<h3>${esc(titre)}</h3><p>Regardez l’adresse, tout en haut. Ce qui compte, c’est juste avant le premier /.</p><p><b>Est-ce le vrai site ?</b></p><button class="rep" data-r="oui">Oui</button><button class="rep" data-r="non">Non</button><p class="rep-txt" style="margin-top:10px"></p>`;
        page.querySelectorAll('.rep').forEach(b => b.onclick = () => {
          const juste = b.dataset.r === bon;
          page.querySelector('.rep-txt').textContent = juste ? ok : ko;
          if (juste) signal(sig);
        });
      };
      const aller = k => {
        w.alerte = false; cadre.querySelectorAll('.arnaque').forEach(a => a.remove());
        PAGES[k]();
        if (k !== 'historique') historique.unshift(barre.value);
      };
      [['Accueil', 'accueil'], ['Mairie', 'mairie'], ['Actualités', 'actus'], ['Banque', 'banque'], ['Impôts', 'impots'], ['Messagerie', 'messagerie']].forEach(([t, k]) => {
        const b = document.createElement('button'); b.textContent = '★ ' + t; b.onclick = () => aller(k); fav.appendChild(b);
      });
      const z = document.createElement('span'); z.className = 'zoom';
      z.innerHTML = '<button title="Réduire la page">−</button><span class="z-val">100 %</span><button title="Agrandir la page">+</button>';
      const majZoom = d => { zoom = Math.max(50, Math.min(200, zoom + d)); page.style.setProperty('--zp', zoom / 100); z.querySelector('.z-val').textContent = zoom + ' %'; signal('zoom', zoom); };
      z.querySelectorAll('button')[0].onclick = () => majZoom(-10);
      z.querySelectorAll('button')[1].onclick = () => majZoom(10);
      fav.appendChild(z);
      w.corps.querySelector('.nav-plus').onclick = e => {
        const r = e.currentTarget.getBoundingClientRect();
        menuContexte({ clientX: r.left - 120, clientY: r.bottom + 2 }, [
          { t: 'Historique', f: () => aller('historique') },
          { t: 'Effacer l’historique', f: () => { historique = []; if (barre.value === 'Historique') PAGES.historique(); notifier({ qui: 'Internet', titre: 'Historique effacé', texte: 'Les pages visitées ne s’affichent plus.' }); signal('historique'); } },
        ]);
        e.stopPropagation();
      };
      w.fin = () => { if (w.alerte) signal('arnaque_fermee'); };
      aller('accueil');
    },

    parametres(w) {
      w.corps.innerHTML = '<div class="par"><div class="par-cote"></div><div class="par-main"></div></div>';
      const cote = w.corps.querySelector('.par-cote'), main = w.corps.querySelector('.par-main');
      const SECTIONS = [['perso', 'Personnalisation'], ['acces', 'Accessibilité'], ['comptes', 'Comptes']];
      w.section = w.section || 'perso';
      const VUES = {
        perso() {
          main.innerHTML = '<h3>Arrière-plan</h3><p>L’image derrière les icônes du bureau.</p><div class="apercu"></div><div class="fonds"></div>';
          main.querySelector('.apercu').style.background = FONDS[fond].css;
          const box = main.querySelector('.fonds');
          FONDS.forEach((f, k) => {
            const b = document.createElement('button'); b.className = k === fond ? 'ici' : '';
            b.innerHTML = `<div style="background:${f.css}"></div>${esc(f.nom)}`;
            b.onclick = () => { if (k !== fond) { fond = k; appliquerFond(); signal('fond', k); } w.rafraichir(); };
            box.appendChild(b);
          });
        },
        acces() {
          main.innerHTML = `<h3>Accessibilité</h3><p><b>Taille du texte</b></p><input type="range" min="100" max="150" step="5" value="${tailleTexte}" class="par-taille"> <span class="par-val">${tailleTexte} %</span>
            <p class="par-ex" style="font-size:${Math.round(14 * tailleTexte / 100)}px;margin:8px 0">Exemple de texte</p><button class="btn-w plein par-appl">Appliquer</button>
            <p style="margin-top:16px"><b>Pointeur de la souris</b></p><div class="par-ptr"><button data-p="normal">Normal</button><button data-p="grand">Grand</button></div>
            <p style="margin-top:16px"><b>Éclairage nocturne</b> : des couleurs plus chaudes, plus douces le soir.</p><div class="par-ptr"><button class="par-nuit">${nuit ? 'Désactiver' : 'Activer'}</button></div>`;
          const r = main.querySelector('.par-taille');
          r.oninput = () => { main.querySelector('.par-val').textContent = r.value + ' %'; main.querySelector('.par-ex').style.fontSize = Math.round(14 * r.value / 100) + 'px'; };
          main.querySelector('.par-appl').onclick = () => { tailleTexte = +r.value; appliquerReglages(); signal('texte_taille', tailleTexte); };
          main.querySelectorAll('.par-ptr button[data-p]').forEach(b => {
            b.classList.toggle('ici', b.dataset.p === pointeur);
            b.onclick = () => { pointeur = b.dataset.p; appliquerReglages(); w.rafraichir(); signal('pointeur', pointeur); };
          });
          main.querySelector('.par-nuit').onclick = () => { nuit = !nuit; appliquerReglages(); w.rafraichir(); if (nuit) signal('nuit'); signal('nuit_etat', nuit); };
        },
        comptes() {
          main.innerHTML = `<h3>Comptes · Mot de passe</h3><p>Inventez un mot de passe solide. Personne ne le verra : rien n’est gardé.</p>
            <input type="password" class="mdp" spellcheck="false" autocomplete="off" style="font-size:15px;padding:6px 10px;width:260px"> <button class="btn-w m-oeil" title="Afficher">👁</button>
            <ul class="regles"><li data-r="long">Au moins 12 caractères</li><li data-r="maj">Une majuscule</li><li data-r="chiffre">Un chiffre</li><li data-r="signe">Un signe : ! ? - _ . @</li></ul><p class="m-ok"></p>`;
          const i = main.querySelector('.mdp');
          main.querySelector('.m-oeil').onclick = () => { i.type = i.type === 'password' ? 'text' : 'password'; i.focus(); };
          i.addEventListener('keydown', e => e.stopPropagation());
          i.oninput = () => {
            const v = i.value, r = { long: v.length >= 12, maj: /[A-ZÀ-Ý]/.test(v), chiffre: /\d/.test(v), signe: /[^A-Za-zÀ-ÿ0-9\s]/.test(v) };
            main.querySelectorAll('.regles li').forEach(li => li.classList.toggle('ok', r[li.dataset.r]));
            const tout = Object.values(r).every(Boolean);
            main.querySelector('.m-ok').textContent = tout ? '✓ Solide. Astuce : trois mots et un chiffre, faciles à retenir pour vous seul.' : '';
            if (tout) signal('mdp_fort');
          };
        },
      };
      w.rafraichir = () => {
        cote.innerHTML = '';
        SECTIONS.forEach(([k, t]) => { const d = document.createElement('div'); d.textContent = t; d.className = k === w.section ? 'ici' : ''; d.onclick = () => { w.section = k; w.rafraichir(); }; cote.appendChild(d); });
        VUES[w.section]();
      };
      w.rafraichir();
    },

    jeu(w) {
      titreFenetre(w, 'Vieux jeu (Ne répond pas)');
      w.el.classList.add('fige');
      w.corps.innerHTML = '<div class="gele">Le programme ne répond pas.<br><small>Rien ne bouge, même en cliquant.</small></div>';
      w.avantFermer = async () => {
        const r = await demander({ titre: 'Vieux jeu ne répond pas', texte: 'Vous pouvez attendre qu’il se réveille, ou fermer le programme.', boutons: ['Fermer le programme', 'Attendre'] });
        if (r.bouton !== 'Fermer le programme') return false;
        signal('force'); return true;
      };
    },

""")

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(s))
