# -*- coding: utf-8 -*-
"""
XXII player 사이트의 모든 문구. 언어를 추가하려면 LANGS 에 항목 하나를 더하고
tools/build_pages.py 를 실행하면 됩니다. HTML 을 직접 고치지 마십시오 — 생성물입니다.
"""

PLAY_URL = "https://play.google.com/store/apps/details?id=com.media.xxiiplayer"
SITE = "https://baseonsell.co.kr"
EMAIL = "scbaek65@gmail.com"

# 언어 코드 → URL 경로. 한국어가 기본이라 루트에 놓입니다.
LANG_ORDER = ["ko", "en", "fr", "es", "ar"]
LANG_PATHS = {"ko": "", "en": "en/", "fr": "fr/", "es": "es/", "ar": "ar/"}
LANG_SHORT = {"ko": "한국어", "en": "EN", "fr": "FR", "es": "ES", "ar": "AR"}
LANG_HREFLANG = {"ko": "ko", "en": "en", "fr": "fr", "es": "es", "ar": "ar"}
LANG_OG_LOCALE = {"ko": "ko_KR", "en": "en_US", "fr": "fr_FR", "es": "es_ES", "ar": "ar_AR"}
RTL = {"ar"}

# 스크린샷 — images/shots/ 에 넣으면 자동으로 표시됩니다.
SHOTS = {
    # 키 → images/shots/ 안의 파일명. tools/sync_shots.py 가 앱 마케팅 폴더에서 가져옵니다.
    "songs":          "01_songs.png",
    "now_playing":    "02_now_playing.png",
    "equalizer":      "03_equalizer.png",
    "playlists":      "04a_playlists.png",
    "playlist_detail":"04b_playlist_detail.png",
    "edit_aac":       "05_edit_aac.png",
    "multi_select":   "06_multi_select.png",
    "videos":         "08_videos.png",
    "video_player":   "09_video_player.png",
    "studio":         "10_studio.png",
    "community":      "11_community.png",
    "community_post": "12_community_post.png",
    "auto_playlist":  "13_android_auto_playlist.png",
    "auto_now":       "14_android_auto_now_playing.png",
}

# 히어로에 기울여 겹쳐 놓는 두 장
HERO_SHOTS = ["now_playing", "playlist_detail"]

LANGS = {

# ══════════════════════════════════════════════════════════════════ 한국어
"ko": {
    "title": "XXII player — 내 음악을, 더 좋은 소리로",
    "description": "휴대폰에 이미 있는 음악과 영상을 위한 플레이어. 이퀄라이저, 공간 음향 AAC 변환, 안드로이드 오토, 그리고 직접 노래를 녹음하는 레코딩 스튜디오까지. 광고 없음, 업로드 없음.",
    "keywords": "XXII player, 안드로이드 음악 플레이어, 안드로이드 오토 음악 플레이어, 로컬 음악 플레이어, 오프라인 음악 플레이어, FLAC 플레이어, MP3 플레이어, 이퀄라이저 앱, 공간 음향, AAC 변환, 레코딩 앱, 녹음 앱, 자막 플레이어, 동영상 플레이어, Android Automotive",
    "skip": "본문으로 건너뛰기",
    "nav": {"features": "기능", "plans": "무료와 Pro", "faq": "자주 묻는 질문"},
    "play_short": "Google Play",

    "hero_kicker": "Android Auto · 로컬 플레이어 · 레코딩 스튜디오",
    "hero_h1": "내 음악을,<br>더 좋은 소리로",
    "hero_lead": "휴대폰에 이미 들어 있는 음악과 영상을 위한 플레이어입니다. 진짜 이퀄라이저, 공간 음향 AAC 변환, 안드로이드 오토, 그리고 직접 노래를 녹음하는 스튜디오까지 갖췄습니다.",
    "hero_cta": "Google Play에서 받기",
    "hero_trust": ["광고 없음", "업로드 없음", "Pro는 1회 구매, 구독 아님"],

    "values_kicker": "핵심",
    "values": [
        ("headphones", "내 파일을 재생합니다",
         "내 음악과 영상 파일을 폴더 그대로 정리하고, 검색할 수 있으며, 어디에도 업로드하지 않습니다."),
        ("faders", "소리가 좋아집니다",
         "이퀄라이저, 베이스 부스트와 볼륨 부스트, 그리고 공간 음향 AAC 변환."),
        ("car", "차를 위해 만들었습니다",
         "안드로이드 오토와 Android Automotive OS를 지원해, 재생목록을 차량 화면에서 그대로 봅니다."),
    ],

    "feats_kicker": "기능 · 07",
    "feats_title": "필요한 것만, 촘촘하게",
    "feats_intro": "화면을 채우는 대신 비웁니다. 목록은 빽빽하고 여백은 짧으며, 강조는 얇은 선 하나로 끝냅니다.",
    "feats": [
        {"icon": "folder", "title": "내 방식대로 정리한 라이브러리", "shots": ["songs", "playlists"], "items": [
            "곡이 담긴 폴더 그대로 묶어 보여주고, 커버 아트와 빠른 검색을 제공합니다",
            "제목·아티스트·커버를 고치면 파일 자체에 기록되고, 파일 이름도 맞춰 바뀝니다",
            "Google Drive나 Downloads에서 음악을 한 번에 추가합니다",
            "목록에서 바로 파일을 공유하거나 삭제합니다",
        ]},
        {"icon": "faders", "title": "직접 빚는 소리", "pro": True, "shots": ["equalizer"], "items": [
            "프리셋을 갖춘 기기 이퀄라이저, 베이스 부스트와 볼륨 부스트",
            "재생 속도, A-B 구간 반복, 그리고 무료 취침 타이머",
            "오디오북·강의 같은 긴 파일은 듣던 자리에서 이어집니다",
        ]},
        {"icon": "sparkle", "title": "공간 음향 AAC 변환", "shots": ["edit_aac", "multi_select"], "items": [
            "어떤 곡이든 넓어진 공간 음향의 AAC(.m4a)로 다시 인코딩합니다",
            "제목·아티스트·커버 아트가 그대로 따라갑니다",
            "선택한 곡 전체를 한 번에 변환합니다 (Pro)",
        ]},
        {"icon": "car", "title": "차 안에서", "shots": ["auto_playlist", "auto_now"], "wide": True, "items": [
            "안드로이드 오토 완전 지원 — 차량 화면에서 안전하게 곡과 재생목록을 탐색합니다",
            "Android Automotive OS가 내장된 차량을 위한 네이티브 앱",
            "실행할 때마다 재생목록을 섞도록 설정할 수 있습니다",
        ]},
        {"icon": "video", "title": "내 영상", "shots": ["videos", "video_player"], "items": [
            "휴대폰에 담긴 영상을 재생합니다. PIP와 백그라운드 재생까지 (Pro)",
            "자막을 자동으로 불러옵니다 — .srt · .smi · .vtt · .ass, 한국어와 아랍어 인코딩도 바로잡습니다",
            "영상의 소리를 곡으로 저장합니다 (Pro)",
        ]},
        {"icon": "mic", "title": "레코딩 스튜디오", "pro": True, "lead": True,
         "note": "로그인 필요", "shots": ["studio"], "items": [
            "파트를 나눠 녹음하고, 이미 녹음한 소리 위에 노래하며 한 곡으로 겹쳐 쌓습니다",
            "테이크가 자동으로 정렬되고, 타이밍을 세밀하게 조절할 수 있습니다",
            "반주를 불러와 파트별 균형을 맞추고, 제목·아티스트·커버와 함께 AAC로 저장합니다",
            "모든 곡에 창작자 이름이 담깁니다. 이메일 주소는 파일에 절대 기록되지 않습니다",
        ]},
        {"icon": "chat", "title": "커뮤니티", "shots": ["community", "community_post"], "items": [
            "글과 사진을 올리고, 댓글을 달고, 다른 사람들과 음악 이야기를 나눕니다",
            "신고와 차단 기능으로 편안한 분위기를 지킵니다",
        ]},
    ],

    "plans_kicker": "무료와 Pro",
    "plans_title": "어디까지가 무료인가",
    "plans_free": "Free",
    "plans_pro": "Pro",
    "plans_feature_col": "기능",
    "plans_rows": [
        ("음악·영상 재생, 폴더, 검색", True, True),
        ("제목·아티스트·커버 편집", True, True),
        ("재생목록 + 클라우드 백업", True, True),
        ("안드로이드 오토 / Automotive OS", True, True),
        ("공간 음향 AAC 변환 (한 곡)", True, True),
        ("취침 타이머, 자막, 커뮤니티", True, True),
        ("이퀄라이저, 베이스·볼륨 부스트", False, True),
        ("재생 속도, A-B 구간 반복", False, True),
        ("PIP, 백그라운드 영상 재생", False, True),
        ("영상의 소리를 곡으로 저장", False, True),
        ("일괄 변환", False, True),
        ("레코딩 스튜디오", False, True),
    ],
    "plans_note": "Pro는 1회 구매이며 구독이 아닙니다. 가격은 국가마다 다르게 표시되므로 Google Play에서 확인해 주세요.",
    "plans_included": "포함",
    "plans_not_included": "미포함",

    "trust_kicker": "개인정보",
    "trust_title": "올리지 않습니다",
    "trust_items": [
        ("광고는 없습니다.", "앞으로도 넣지 않습니다."),
        ("파일은 휴대폰에 그대로 있습니다.", "커뮤니티에 직접 올리거나 재생목록을 백업하지 않는 한, 아무것도 업로드되지 않습니다."),
        ("계정은 선택입니다.", "재생목록 백업, 스튜디오, 커뮤니티에만 필요하며, 앱에서 언제든 삭제할 수 있습니다."),
    ],
    "trust_langs": "지원 언어 — English · 한국어 · Français · Español · العربية",

    "faq_kicker": "자주 묻는 질문",
    "faq_title": "먼저 확인해 보세요",
    "faq": [
        ("음악을 스트리밍하나요?", "아닙니다. 기기에 들어 있는 음악·영상 파일을 재생합니다."),
        ("Pro는 구독인가요?", "아닙니다. 1회 구매입니다."),
        (".ass 자막이 안 불러와집니다.", "안드로이드가 .ass 파일을 앱에서 숨기기 때문입니다. 자막 메뉴에서 해당 폴더를 한 번만 연결해 주세요."),
        ("계정은 어떻게 삭제하나요?", '앱에서 계정 → 계정 삭제를 누르시거나, <a href="{deletion}">계정 및 데이터 삭제</a> 페이지의 안내를 따르시면 됩니다.'),
    ],

    "cta_kicker": "지금 시작",
    "cta_title": "무료로 지금 바로 시작하세요",
    "cta_lead": "로컬 재생은 모두 무료입니다. 계정 없이도 바로 쓸 수 있습니다.",
    "cta_btn": "Google Play에서 다운로드",

    "footer_privacy": "개인정보 처리방침",
    "footer_deletion": "계정 및 데이터 삭제",
    "footer_contact": "문의",
    "footer_rights": "© 2026 XXII player. All rights reserved.",
    "footer_langlabel": "언어",

    "shot_missing": "스크린샷을 넣어 주세요",
    "pro_tag": "Pro",
},

# ══════════════════════════════════════════════════════════════════ English
"en": {
    "title": "XXII player — Your music, sounding better",
    "description": "A player for the music and videos already on your phone, with a real equalizer, spatial AAC conversion, Android Auto, and a studio to record your own songs. No ads, nothing uploaded.",
    "keywords": "XXII player, android music player, android auto music player, local music player, offline music player, FLAC player, MP3 player, equalizer app, spatial audio, AAC conversion, multitrack recording app, subtitle video player, Android Automotive",
    "skip": "Skip to content",
    "nav": {"features": "Features", "plans": "Free & Pro", "faq": "FAQ"},
    "play_short": "Google Play",

    "hero_kicker": "Android Auto · Local player · Recording studio",
    "hero_h1": "Your music,<br>sounding better",
    "hero_lead": "A player for the music and videos already on your phone, with a real equalizer, spatial AAC conversion, Android Auto, and a studio to record your own songs.",
    "hero_cta": "Get it on Google Play",
    "hero_trust": ["No ads", "Nothing uploaded", "One-time Pro, no subscription"],

    "values_kicker": "In short",
    "values": [
        ("headphones", "Plays what you own",
         "Your own music and video files, organised by folder, searchable, and never uploaded."),
        ("faders", "Sounds better",
         "Equalizer, bass and volume boost, and conversion to spatial AAC."),
        ("car", "Made for the car",
         "Android Auto and Android Automotive OS, with your playlists on the car screen."),
    ],

    "feats_kicker": "Features · 07",
    "feats_title": "Only what you need, closely packed",
    "feats_intro": "Space rather than fill. Lists are dense, margins are short, and emphasis ends at a single thin line.",
    "feats": [
        {"icon": "folder", "title": "Your library, your way", "shots": ["songs", "playlists"], "items": [
            "Songs grouped by the folder they sit in, with cover art and fast search",
            "Edit titles, artists and covers; edits are written into the file itself and the file is renamed to match",
            "Add music from Google Drive or Downloads in a tap",
            "Share or delete files right from the list",
        ]},
        {"icon": "faders", "title": "Sound you can shape", "pro": True, "shots": ["equalizer"], "items": [
            "Device equalizer with presets, plus bass boost and volume boost",
            "Playback speed, A-B repeat, and a free sleep timer",
            "Long files (audiobooks, lectures) pick up where you left off",
        ]},
        {"icon": "sparkle", "title": "Spatial AAC conversion", "shots": ["edit_aac", "multi_select"], "items": [
            "Re-encode any track to AAC (.m4a) with a widened, spatial sound",
            "Title, artist and cover art carry over",
            "Convert a whole selection in one run (Pro)",
        ]},
        {"icon": "car", "title": "In the car", "shots": ["auto_playlist", "auto_now"], "wide": True, "items": [
            "Full Android Auto support: browse songs and playlists safely on the car screen",
            "A native app for cars with Android Automotive OS built in",
            "Playlists can shuffle on every launch",
        ]},
        {"icon": "video", "title": "Your own videos", "shots": ["videos", "video_player"], "items": [
            "Play the videos on your phone, with picture-in-picture and background playback (Pro)",
            "Subtitles load automatically: .srt, .smi, .vtt and .ass, with Korean and Arabic encodings fixed",
            "Save a video’s sound as a song (Pro)",
        ]},
        {"icon": "mic", "title": "Recording studio", "pro": True, "lead": True,
         "note": "sign-in required", "shots": ["studio"], "items": [
            "Record in parts and layer takes into one song, singing over what you already recorded",
            "Takes line up automatically, with fine timing control",
            "Bring in a backing track, balance each part, and save the mix as AAC with title, artist and cover",
            "Every song carries your creator name; your email address is never written into the file",
        ]},
        {"icon": "chat", "title": "Community", "shots": ["community", "community_post"], "items": [
            "Share posts with text and photos, comment, and talk music with other listeners",
            "Report and block tools keep it friendly",
        ]},
    ],

    "plans_kicker": "Free & Pro",
    "plans_title": "What the free version covers",
    "plans_free": "Free",
    "plans_pro": "Pro",
    "plans_feature_col": "Feature",
    "plans_rows": [
        ("Music &amp; video playback, folders, search", True, True),
        ("Edit titles, artists, covers", True, True),
        ("Playlists + cloud backup", True, True),
        ("Android Auto / Automotive OS", True, True),
        ("Spatial AAC conversion (one track)", True, True),
        ("Sleep timer, subtitles, community", True, True),
        ("Equalizer, bass &amp; volume boost", False, True),
        ("Speed, A-B repeat", False, True),
        ("Picture-in-picture, background video", False, True),
        ("Save video sound as a song", False, True),
        ("Batch conversion", False, True),
        ("Recording studio", False, True),
    ],
    "plans_note": "Pro is a one-time purchase, not a subscription. Prices differ by country, so check the current price on Google Play.",
    "plans_included": "Included",
    "plans_not_included": "Not included",

    "trust_kicker": "Privacy",
    "trust_title": "Nothing leaves your phone",
    "trust_items": [
        ("No ads. Ever.", "There is no advertising in the app, and none is planned."),
        ("Your files stay on your phone.", "Nothing is uploaded unless you post it to the community or back up playlists."),
        ("An account is optional.", "It’s only needed for playlist backup, the studio and the community, and you can delete it in the app at any time."),
    ],
    "trust_langs": "Available in English · 한국어 · Français · Español · العربية",

    "faq_kicker": "FAQ",
    "faq_title": "Before you ask",
    "faq": [
        ("Does it stream music?", "No. It plays the music and video files on your device."),
        ("Is Pro a subscription?", "No, a one-time purchase."),
        ("Why won’t my .ass subtitles load?", "Android hides them from apps. Link the folder once in the subtitle menu."),
        ("How do I delete my account?", 'In the app, Account → Delete account, or follow the instructions on the <a href="{deletion}">account &amp; data deletion</a> page.'),
    ],

    "cta_kicker": "Get the app",
    "cta_title": "Start now, for free",
    "cta_lead": "Local playback is entirely free. No account needed to begin.",
    "cta_btn": "Download on Google Play",

    "footer_privacy": "Privacy policy",
    "footer_deletion": "Account deletion",
    "footer_contact": "Contact",
    "footer_rights": "© 2026 XXII player. All rights reserved.",
    "footer_langlabel": "Language",

    "shot_missing": "Screenshot pending",
    "pro_tag": "Pro",
},

# ══════════════════════════════════════════════════════════════════ Français
"fr": {
    "title": "XXII player — Votre musique, en mieux",
    "description": "Un lecteur pour la musique et les vidéos déjà sur votre téléphone, avec un vrai égaliseur, la conversion AAC spatiale, Android Auto et un studio pour enregistrer vos propres morceaux. Sans publicité, rien n’est téléversé.",
    "keywords": "XXII player, lecteur de musique android, lecteur musique android auto, lecteur musique local, lecteur hors ligne, lecteur FLAC, lecteur MP3, égaliseur, son spatial, conversion AAC, application d’enregistrement, lecteur vidéo sous-titres, Android Automotive",
    "skip": "Aller au contenu",
    "nav": {"features": "Fonctions", "plans": "Gratuit et Pro", "faq": "Questions"},
    "play_short": "Google Play",

    "hero_kicker": "Android Auto · Lecteur local · Studio d’enregistrement",
    "hero_h1": "Votre musique,<br>en mieux",
    "hero_lead": "Un lecteur pour la musique et les vidéos déjà présentes sur votre téléphone, avec un vrai égaliseur, la conversion AAC spatiale, Android Auto et un studio pour enregistrer vos propres morceaux.",
    "hero_cta": "Disponible sur Google Play",
    "hero_trust": ["Sans publicité", "Rien n’est téléversé", "Pro en achat unique, sans abonnement"],

    "values_kicker": "L’essentiel",
    "values": [
        ("headphones", "Lit ce qui vous appartient",
         "Vos propres fichiers musique et vidéo, classés par dossier, consultables, et jamais téléversés."),
        ("faders", "Sonne mieux",
         "Égaliseur, amplification des basses et du volume, et conversion en AAC spatial."),
        ("car", "Pensé pour la voiture",
         "Android Auto et Android Automotive OS, avec vos playlists sur l’écran du véhicule."),
    ],

    "feats_kicker": "Fonctions · 07",
    "feats_title": "Rien que le nécessaire, en dense",
    "feats_intro": "On évide plutôt que l’on remplit. Les listes sont serrées, les marges courtes, et l’accent se résume à un trait fin.",
    "feats": [
        {"icon": "folder", "title": "Votre bibliothèque, à votre façon", "shots": ["songs", "playlists"], "items": [
            "Les morceaux sont regroupés par dossier, avec pochette et recherche rapide",
            "Modifiez titres, artistes et pochettes : la modification est écrite dans le fichier, qui est renommé en conséquence",
            "Ajoutez de la musique depuis Google Drive ou Téléchargements d’un seul geste",
            "Partagez ou supprimez un fichier directement depuis la liste",
        ]},
        {"icon": "faders", "title": "Un son que vous façonnez", "pro": True, "shots": ["equalizer"], "items": [
            "Égaliseur de l’appareil avec préréglages, amplification des basses et du volume",
            "Vitesse de lecture, répétition A-B et minuterie de veille gratuite",
            "Les fichiers longs (livres audio, cours) reprennent là où vous vous étiez arrêté",
        ]},
        {"icon": "sparkle", "title": "Conversion AAC spatiale", "shots": ["edit_aac", "multi_select"], "items": [
            "Réencodez n’importe quel morceau en AAC (.m4a) avec un son élargi et spatialisé",
            "Titre, artiste et pochette sont conservés",
            "Convertissez toute une sélection en une seule fois (Pro)",
        ]},
        {"icon": "car", "title": "En voiture", "shots": ["auto_playlist", "auto_now"], "wide": True, "items": [
            "Prise en charge complète d’Android Auto : parcourez morceaux et playlists en toute sécurité sur l’écran du véhicule",
            "Une application native pour les voitures équipées d’Android Automotive OS",
            "Les playlists peuvent se mélanger à chaque démarrage",
        ]},
        {"icon": "video", "title": "Vos propres vidéos", "shots": ["videos", "video_player"], "items": [
            "Lisez les vidéos de votre téléphone, avec image dans l’image et lecture en arrière-plan (Pro)",
            "Les sous-titres se chargent tout seuls : .srt, .smi, .vtt et .ass, encodages coréen et arabe corrigés",
            "Enregistrez le son d’une vidéo comme morceau (Pro)",
        ]},
        {"icon": "mic", "title": "Studio d’enregistrement", "pro": True, "lead": True,
         "note": "connexion requise", "shots": ["studio"], "items": [
            "Enregistrez par parties et superposez les prises en un seul morceau, en chantant par-dessus ce que vous avez déjà enregistré",
            "Les prises s’alignent automatiquement, avec un réglage fin du timing",
            "Importez un accompagnement, équilibrez chaque partie et enregistrez le mixage en AAC avec titre, artiste et pochette",
            "Chaque morceau porte votre nom de créateur ; votre adresse e-mail n’est jamais inscrite dans le fichier",
        ]},
        {"icon": "chat", "title": "Communauté", "shots": ["community", "community_post"], "items": [
            "Publiez textes et photos, commentez et parlez musique avec d’autres auditeurs",
            "Les outils de signalement et de blocage maintiennent une bonne ambiance",
        ]},
    ],

    "plans_kicker": "Gratuit et Pro",
    "plans_title": "Ce que couvre la version gratuite",
    "plans_free": "Gratuit",
    "plans_pro": "Pro",
    "plans_feature_col": "Fonction",
    "plans_rows": [
        ("Lecture musique et vidéo, dossiers, recherche", True, True),
        ("Modifier titres, artistes, pochettes", True, True),
        ("Playlists + sauvegarde cloud", True, True),
        ("Android Auto / Automotive OS", True, True),
        ("Conversion AAC spatiale (un morceau)", True, True),
        ("Minuterie de veille, sous-titres, communauté", True, True),
        ("Égaliseur, basses et volume", False, True),
        ("Vitesse, répétition A-B", False, True),
        ("Image dans l’image, vidéo en arrière-plan", False, True),
        ("Enregistrer le son d’une vidéo", False, True),
        ("Conversion par lot", False, True),
        ("Studio d’enregistrement", False, True),
    ],
    "plans_note": "Pro est un achat unique, pas un abonnement. Les prix varient selon le pays : consultez le prix actuel sur Google Play.",
    "plans_included": "Inclus",
    "plans_not_included": "Non inclus",

    "trust_kicker": "Confidentialité",
    "trust_title": "Rien ne quitte votre téléphone",
    "trust_items": [
        ("Aucune publicité. Jamais.", "Il n’y a aucune publicité dans l’application, et il n’en est pas prévu."),
        ("Vos fichiers restent sur votre téléphone.", "Rien n’est téléversé, sauf si vous publiez dans la communauté ou sauvegardez vos playlists."),
        ("Le compte est facultatif.", "Il n’est nécessaire que pour la sauvegarde des playlists, le studio et la communauté, et vous pouvez le supprimer à tout moment dans l’application."),
    ],
    "trust_langs": "Disponible en English · 한국어 · Français · Español · العربية",

    "faq_kicker": "Questions fréquentes",
    "faq_title": "Avant de demander",
    "faq": [
        ("Est-ce que l’application diffuse de la musique en streaming ?", "Non. Elle lit les fichiers musique et vidéo présents sur votre appareil."),
        ("Pro est-il un abonnement ?", "Non, c’est un achat unique."),
        ("Pourquoi mes sous-titres .ass ne se chargent-ils pas ?", "Android les masque aux applications. Liez le dossier une fois depuis le menu des sous-titres."),
        ("Comment supprimer mon compte ?", 'Dans l’application, Compte → Supprimer le compte, ou suivez les instructions de la page <a href="{deletion}">suppression du compte et des données</a>.'),
    ],

    "cta_kicker": "Télécharger",
    "cta_title": "Commencez maintenant, gratuitement",
    "cta_lead": "La lecture locale est entièrement gratuite. Aucun compte n’est nécessaire pour commencer.",
    "cta_btn": "Télécharger sur Google Play",

    "footer_privacy": "Politique de confidentialité",
    "footer_deletion": "Suppression du compte",
    "footer_contact": "Contact",
    "footer_rights": "© 2026 XXII player. Tous droits réservés.",
    "footer_langlabel": "Langue",

    "shot_missing": "Capture à venir",
    "pro_tag": "Pro",
},

# ══════════════════════════════════════════════════════════════════ Español
"es": {
    "title": "XXII player — Tu música, con mejor sonido",
    "description": "Un reproductor para la música y los vídeos que ya tienes en el teléfono, con un ecualizador de verdad, conversión a AAC espacial, Android Auto y un estudio para grabar tus propias canciones. Sin anuncios, no se sube nada.",
    "keywords": "XXII player, reproductor de música android, reproductor android auto, reproductor de música local, reproductor sin conexión, reproductor FLAC, reproductor MP3, ecualizador, sonido espacial, conversión AAC, app de grabación, reproductor de vídeo con subtítulos, Android Automotive",
    "skip": "Saltar al contenido",
    "nav": {"features": "Funciones", "plans": "Gratis y Pro", "faq": "Preguntas"},
    "play_short": "Google Play",

    "hero_kicker": "Android Auto · Reproductor local · Estudio de grabación",
    "hero_h1": "Tu música,<br>con mejor sonido",
    "hero_lead": "Un reproductor para la música y los vídeos que ya tienes en el teléfono, con un ecualizador de verdad, conversión a AAC espacial, Android Auto y un estudio para grabar tus propias canciones.",
    "hero_cta": "Consíguelo en Google Play",
    "hero_trust": ["Sin anuncios", "No se sube nada", "Pro de pago único, sin suscripción"],

    "values_kicker": "En resumen",
    "values": [
        ("headphones", "Reproduce lo que es tuyo",
         "Tus propios archivos de música y vídeo, organizados por carpeta, con búsqueda, y nunca se suben."),
        ("faders", "Suena mejor",
         "Ecualizador, refuerzo de graves y de volumen, y conversión a AAC espacial."),
        ("car", "Hecho para el coche",
         "Android Auto y Android Automotive OS, con tus listas en la pantalla del coche."),
    ],

    "feats_kicker": "Funciones · 07",
    "feats_title": "Solo lo necesario, bien compacto",
    "feats_intro": "Vaciar en lugar de llenar. Las listas son densas, los márgenes cortos y el énfasis se resuelve con una línea fina.",
    "feats": [
        {"icon": "folder", "title": "Tu biblioteca, a tu manera", "shots": ["songs", "playlists"], "items": [
            "Las canciones se agrupan por la carpeta en la que están, con carátula y búsqueda rápida",
            "Edita títulos, artistas y carátulas: el cambio se escribe en el propio archivo y este se renombra para coincidir",
            "Añade música desde Google Drive o Descargas con un toque",
            "Comparte o elimina archivos directamente desde la lista",
        ]},
        {"icon": "faders", "title": "Un sonido que puedes moldear", "pro": True, "shots": ["equalizer"], "items": [
            "Ecualizador del dispositivo con preajustes, además de refuerzo de graves y de volumen",
            "Velocidad de reproducción, repetición A-B y temporizador de apagado gratuito",
            "Los archivos largos (audiolibros, clases) continúan donde los dejaste",
        ]},
        {"icon": "sparkle", "title": "Conversión a AAC espacial", "shots": ["edit_aac", "multi_select"], "items": [
            "Recodifica cualquier pista a AAC (.m4a) con un sonido más amplio y espacial",
            "El título, el artista y la carátula se conservan",
            "Convierte una selección entera de una vez (Pro)",
        ]},
        {"icon": "car", "title": "En el coche", "shots": ["auto_playlist", "auto_now"], "wide": True, "items": [
            "Compatibilidad completa con Android Auto: explora canciones y listas con seguridad en la pantalla del coche",
            "Una app nativa para coches con Android Automotive OS integrado",
            "Las listas pueden reproducirse en aleatorio en cada arranque",
        ]},
        {"icon": "video", "title": "Tus propios vídeos", "shots": ["videos", "video_player"], "items": [
            "Reproduce los vídeos de tu teléfono, con imagen en imagen y reproducción en segundo plano (Pro)",
            "Los subtítulos se cargan solos: .srt, .smi, .vtt y .ass, con las codificaciones coreana y árabe corregidas",
            "Guarda el sonido de un vídeo como canción (Pro)",
        ]},
        {"icon": "mic", "title": "Estudio de grabación", "pro": True, "lead": True,
         "note": "requiere iniciar sesión", "shots": ["studio"], "items": [
            "Graba por partes y superpón tomas en una sola canción, cantando sobre lo que ya has grabado",
            "Las tomas se alinean automáticamente, con control fino del tiempo",
            "Carga una pista de acompañamiento, equilibra cada parte y guarda la mezcla en AAC con título, artista y carátula",
            "Cada canción lleva tu nombre de creador; tu dirección de correo nunca se escribe en el archivo",
        ]},
        {"icon": "chat", "title": "Comunidad", "shots": ["community", "community_post"], "items": [
            "Publica textos y fotos, comenta y habla de música con otros oyentes",
            "Las herramientas de denuncia y bloqueo mantienen el buen ambiente",
        ]},
    ],

    "plans_kicker": "Gratis y Pro",
    "plans_title": "Hasta dónde llega la versión gratuita",
    "plans_free": "Gratis",
    "plans_pro": "Pro",
    "plans_feature_col": "Función",
    "plans_rows": [
        ("Reproducción de música y vídeo, carpetas, búsqueda", True, True),
        ("Editar títulos, artistas, carátulas", True, True),
        ("Listas + copia en la nube", True, True),
        ("Android Auto / Automotive OS", True, True),
        ("Conversión a AAC espacial (una pista)", True, True),
        ("Temporizador, subtítulos, comunidad", True, True),
        ("Ecualizador, graves y volumen", False, True),
        ("Velocidad, repetición A-B", False, True),
        ("Imagen en imagen, vídeo en segundo plano", False, True),
        ("Guardar el sonido de un vídeo", False, True),
        ("Conversión por lotes", False, True),
        ("Estudio de grabación", False, True),
    ],
    "plans_note": "Pro es un pago único, no una suscripción. Los precios varían según el país: consulta el precio actual en Google Play.",
    "plans_included": "Incluido",
    "plans_not_included": "No incluido",

    "trust_kicker": "Privacidad",
    "trust_title": "Nada sale de tu teléfono",
    "trust_items": [
        ("Sin anuncios. Nunca.", "No hay publicidad en la aplicación ni está previsto añadirla."),
        ("Tus archivos se quedan en tu teléfono.", "No se sube nada salvo que publiques en la comunidad o hagas copia de tus listas."),
        ("La cuenta es opcional.", "Solo hace falta para la copia de listas, el estudio y la comunidad, y puedes eliminarla en la app cuando quieras."),
    ],
    "trust_langs": "Disponible en English · 한국어 · Français · Español · العربية",

    "faq_kicker": "Preguntas frecuentes",
    "faq_title": "Antes de preguntar",
    "faq": [
        ("¿Reproduce música en streaming?", "No. Reproduce los archivos de música y vídeo que hay en tu dispositivo."),
        ("¿Pro es una suscripción?", "No, es un pago único."),
        ("¿Por qué no se cargan mis subtítulos .ass?", "Android los oculta a las aplicaciones. Vincula la carpeta una vez desde el menú de subtítulos."),
        ("¿Cómo elimino mi cuenta?", 'En la app, Cuenta → Eliminar cuenta, o sigue las instrucciones de la página de <a href="{deletion}">eliminación de cuenta y datos</a>.'),
    ],

    "cta_kicker": "Descargar",
    "cta_title": "Empieza ahora, gratis",
    "cta_lead": "La reproducción local es totalmente gratuita. No necesitas cuenta para empezar.",
    "cta_btn": "Descargar en Google Play",

    "footer_privacy": "Política de privacidad",
    "footer_deletion": "Eliminación de cuenta",
    "footer_contact": "Contacto",
    "footer_rights": "© 2026 XXII player. Todos los derechos reservados.",
    "footer_langlabel": "Idioma",

    "shot_missing": "Captura pendiente",
    "pro_tag": "Pro",
},

# ══════════════════════════════════════════════════════════════════ العربية
"ar": {
    "title": "XXII player — موسيقاك، بصوت أفضل",
    "description": "مشغّل للموسيقى والفيديو الموجودة على هاتفك بالفعل، مع معادل صوت حقيقي، وتحويل إلى AAC مكاني، ودعم Android Auto، واستوديو لتسجيل أغانيك. بلا إعلانات، ولا يُرفَع أي شيء.",
    "keywords": "XXII player, مشغل موسيقى أندرويد, مشغل موسيقى Android Auto, مشغل موسيقى محلي, مشغل بدون إنترنت, مشغل FLAC, مشغل MP3, معادل صوت, صوت مكاني, تحويل AAC, تطبيق تسجيل, مشغل فيديو بترجمة, Android Automotive",
    "skip": "تخطّي إلى المحتوى",
    "nav": {"features": "المزايا", "plans": "المجاني و Pro", "faq": "الأسئلة"},
    "play_short": "Google Play",

    "hero_kicker": "Android Auto · مشغّل محلي · استوديو تسجيل",
    "hero_h1": "موسيقاك،<br>بصوت أفضل",
    "hero_lead": "مشغّل للموسيقى والفيديو الموجودة على هاتفك بالفعل، مع معادل صوت حقيقي، وتحويل إلى AAC مكاني، ودعم Android Auto، واستوديو لتسجيل أغانيك الخاصة.",
    "hero_cta": "احصل عليه من Google Play",
    "hero_trust": ["بلا إعلانات", "لا يُرفَع أي شيء", "Pro بشراء لمرة واحدة، بلا اشتراك"],

    "values_kicker": "باختصار",
    "values": [
        ("headphones", "يشغّل ما تملكه",
         "ملفاتك الموسيقية والمرئية، مرتَّبة حسب المجلد، وقابلة للبحث، ولا تُرفَع أبدًا."),
        ("faders", "صوت أفضل",
         "معادل صوت، وتعزيز للجهير ولمستوى الصوت، وتحويل إلى AAC مكاني."),
        ("car", "مصمَّم للسيارة",
         "يدعم Android Auto و Android Automotive OS، مع قوائم التشغيل على شاشة السيارة."),
    ],

    "feats_kicker": "المزايا · ٠٧",
    "feats_title": "ما تحتاجه فقط، بكثافة",
    "feats_intro": "إفراغٌ بدل الملء. القوائم متقاربة، والهوامش قصيرة، والتأكيد ينتهي عند خط رفيع واحد.",
    "feats": [
        {"icon": "folder", "title": "مكتبتك على طريقتك", "shots": ["songs", "playlists"], "items": [
            "تُجمَع الأغاني حسب المجلد الذي توجد فيه، مع صورة الغلاف وبحث سريع",
            "عدِّل العناوين والفنانين والأغلفة؛ يُكتب التعديل داخل الملف نفسه ويُعاد تسمية الملف ليطابقه",
            "أضف الموسيقى من Google Drive أو مجلد التنزيلات بلمسة واحدة",
            "شارك الملفات أو احذفها مباشرةً من القائمة",
        ]},
        {"icon": "faders", "title": "صوتٌ تصوغه بنفسك", "pro": True, "shots": ["equalizer"], "items": [
            "معادل صوت الجهاز مع إعدادات جاهزة، إضافةً إلى تعزيز الجهير ومستوى الصوت",
            "سرعة التشغيل، وتكرار المقطع A-B، ومؤقّت نوم مجاني",
            "الملفات الطويلة (الكتب الصوتية والمحاضرات) تُستأنف من حيث توقّفت",
        ]},
        {"icon": "sparkle", "title": "التحويل إلى AAC مكاني", "shots": ["edit_aac", "multi_select"], "items": [
            "أعد ترميز أي مقطع إلى AAC‏ (.m4a) بصوت أوسع ومكاني",
            "يُنقَل العنوان والفنان وصورة الغلاف كما هي",
            "حوِّل تحديدًا كاملًا دفعةً واحدة (Pro)",
        ]},
        {"icon": "car", "title": "في السيارة", "shots": ["auto_playlist", "auto_now"], "wide": True, "items": [
            "دعم كامل لـ Android Auto: تصفَّح الأغاني وقوائم التشغيل بأمان على شاشة السيارة",
            "تطبيق أصلي للسيارات المزوَّدة بنظام Android Automotive OS",
            "يمكن خلط قوائم التشغيل عند كل تشغيل",
        ]},
        {"icon": "video", "title": "مقاطعك المرئية", "shots": ["videos", "video_player"], "items": [
            "شغّل مقاطع الفيديو الموجودة على هاتفك، مع وضع صورة داخل صورة والتشغيل في الخلفية (Pro)",
            "تُحمَّل الترجمات تلقائيًا: ‎.srt‎ و‎.smi‎ و‎.vtt‎ و‎.ass‎، مع تصحيح الترميزين الكوري والعربي",
            "احفظ صوت المقطع المرئي كأغنية (Pro)",
        ]},
        {"icon": "mic", "title": "استوديو التسجيل", "pro": True, "lead": True,
         "note": "يتطلّب تسجيل الدخول", "shots": ["studio"], "items": [
            "سجِّل على أجزاء وطبِّق التسجيلات فوق بعضها في أغنية واحدة، وغنِّ فوق ما سجّلته من قبل",
            "تصطفّ التسجيلات تلقائيًا، مع تحكّم دقيق في التوقيت",
            "أدخِل مقطعًا موسيقيًا مصاحبًا، وازِن بين الأجزاء، واحفظ المزيج بصيغة AAC مع العنوان والفنان والغلاف",
            "تحمل كل أغنية اسمك كمنشئ؛ ولا يُكتب بريدك الإلكتروني في الملف أبدًا",
        ]},
        {"icon": "chat", "title": "المجتمع", "shots": ["community", "community_post"], "items": [
            "انشر نصوصًا وصورًا، وعلِّق، وتحدَّث عن الموسيقى مع مستمعين آخرين",
            "أدوات الإبلاغ والحظر تحافظ على أجواء ودّية",
        ]},
    ],

    "plans_kicker": "المجاني و Pro",
    "plans_title": "ما تغطّيه النسخة المجانية",
    "plans_free": "مجاني",
    "plans_pro": "Pro",
    "plans_feature_col": "الميزة",
    "plans_rows": [
        ("تشغيل الموسيقى والفيديو، المجلدات، البحث", True, True),
        ("تعديل العناوين والفنانين والأغلفة", True, True),
        ("قوائم التشغيل + النسخ الاحتياطي السحابي", True, True),
        ("Android Auto / Automotive OS", True, True),
        ("التحويل إلى AAC مكاني (مقطع واحد)", True, True),
        ("مؤقّت النوم، الترجمات، المجتمع", True, True),
        ("معادل الصوت، تعزيز الجهير ومستوى الصوت", False, True),
        ("السرعة، تكرار المقطع A-B", False, True),
        ("صورة داخل صورة، الفيديو في الخلفية", False, True),
        ("حفظ صوت المقطع المرئي كأغنية", False, True),
        ("التحويل الدفعي", False, True),
        ("استوديو التسجيل", False, True),
    ],
    "plans_note": "‏Pro شراء لمرة واحدة وليس اشتراكًا. تختلف الأسعار حسب البلد، لذا تحقَّق من السعر الحالي على Google Play.",
    "plans_included": "مُضمَّن",
    "plans_not_included": "غير مُضمَّن",

    "trust_kicker": "الخصوصية",
    "trust_title": "لا شيء يغادر هاتفك",
    "trust_items": [
        ("بلا إعلانات. أبدًا.", "لا توجد أي إعلانات في التطبيق، ولا يوجد ما يخطَّط له."),
        ("ملفاتك تبقى على هاتفك.", "لا يُرفَع أي شيء إلا إذا نشرتَه في المجتمع أو أنشأتَ نسخة احتياطية لقوائم التشغيل."),
        ("الحساب اختياري.", "لا يلزم إلا للنسخ الاحتياطي لقوائم التشغيل وللاستوديو وللمجتمع، ويمكنك حذفه من داخل التطبيق في أي وقت."),
    ],
    "trust_langs": "متوفّر بلغات English · 한국어 · Français · Español · العربية",

    "faq_kicker": "الأسئلة الشائعة",
    "faq_title": "قبل أن تسأل",
    "faq": [
        ("هل يبثّ الموسيقى عبر الإنترنت؟", "لا. يشغّل ملفات الموسيقى والفيديو الموجودة على جهازك."),
        ("هل Pro اشتراك؟", "لا، هو شراء لمرة واحدة."),
        ("لماذا لا تُحمَّل ترجمات ‎.ass‎ لديّ؟", "يُخفيها نظام أندرويد عن التطبيقات. اربط المجلد مرةً واحدة من قائمة الترجمات."),
        ("كيف أحذف حسابي؟", 'من داخل التطبيق: الحساب ← حذف الحساب، أو اتبع التعليمات في صفحة <a href="{deletion}">حذف الحساب والبيانات</a>.'),
    ],

    "cta_kicker": "احصل على التطبيق",
    "cta_title": "ابدأ الآن، مجانًا",
    "cta_lead": "التشغيل المحلي مجاني بالكامل. ولا تحتاج إلى حساب لتبدأ.",
    "cta_btn": "نزِّله من Google Play",

    "footer_privacy": "سياسة الخصوصية",
    "footer_deletion": "حذف الحساب",
    "footer_contact": "اتصل بنا",
    "footer_rights": "© 2026 XXII player. جميع الحقوق محفوظة.",
    "footer_langlabel": "اللغة",

    "shot_missing": "لقطة الشاشة قيد الإعداد",
    "pro_tag": "Pro",
},

}
