# -*- coding: utf-8 -*-
"""
언어별 랜딩 페이지 생성기.

    python tools/build_pages.py

한국어는 /index.html, 나머지는 /en/, /fr/, /es/, /ar/ 아래에 씁니다.
문구는 tools/content.py 에 있습니다. 생성된 HTML 을 직접 고치면 다음 실행 때 덮어쓰입니다.
"""
import io
import json
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (  # noqa: E402
    LANGS, LANG_ORDER, LANG_PATHS, LANG_SHORT, LANG_HREFLANG, LANG_OG_LOCALE,
    RTL, SHOTS, HERO_SHOTS, PLAY_URL, SITE, EMAIL,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Phosphor 아이콘 (Regular, 256 뷰박스, MIT) ──────────────────────────
ICONS = {
    "note": "M210.3,56.34l-80-24A8,8,0,0,0,120,40V148.26A48,48,0,1,0,136,184V98.75l69.7,20.91A8,8,0,0,0,216,112V64A8,8,0,0,0,210.3,56.34ZM88,216a32,32,0,1,1,32-32A32,32,0,0,1,88,216Zm112-114.75L136,82.05V50.75l64,19.2Z",
    "play": "M232.4,114.49,88.32,26.35a16,16,0,0,0-16.2-.3A15.86,15.86,0,0,0,64,39.87V216.13A15.94,15.94,0,0,0,80,232a16.07,16.07,0,0,0,8.36-2.35L232.4,141.51a15.81,15.81,0,0,0,0-27ZM80,215.94V40l143.83,88Z",
    "caret": "M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z",
    "faders": "M40,88H73a32,32,0,0,0,62,0h81a8,8,0,0,0,0-16H135a32,32,0,0,0-62,0H40a8,8,0,0,0,0,16Zm64-24a16,16,0,1,1-16,16A16,16,0,0,1,104,64ZM216,168H199a32,32,0,0,0-62,0H40a8,8,0,0,0,0,16h97a32,32,0,0,0,62,0h17a8,8,0,0,0,0-16Zm-48,24a16,16,0,1,1,16-16A16,16,0,0,1,168,192Z",
    "folder": "M216,72H131.31L104,44.69A15.86,15.86,0,0,0,92.69,40H40A16,16,0,0,0,24,56V200.62A15.4,15.4,0,0,0,39.38,216H216.89A15.13,15.13,0,0,0,232,200.89V88A16,16,0,0,0,216,72ZM40,56H92.69l16,16H40ZM216,200H40V88H216Z",
    "video": "M251.77,73a8,8,0,0,0-8.21.39L208,97.05V72a16,16,0,0,0-16-16H32A16,16,0,0,0,16,72V184a16,16,0,0,0,16,16H192a16,16,0,0,0,16-16V159l35.56,23.71A8,8,0,0,0,248,184a8,8,0,0,0,8-8V80A8,8,0,0,0,251.77,73ZM192,184H32V72H192V184Zm48-22.95-32-21.33V116.28L240,95Z",
    "sparkle": "M197.58,129.06,146,110l-19-51.62a15.92,15.92,0,0,0-29.88,0L78,110l-51.62,19a15.92,15.92,0,0,0,0,29.88L78,178l19,51.62a15.92,15.92,0,0,0,29.88,0L146,178l51.62-19a15.92,15.92,0,0,0,0-29.88ZM137,164.22a8,8,0,0,0-4.74,4.74L112,223.85,91.78,169A8,8,0,0,0,87,164.22L32.15,144,87,123.78A8,8,0,0,0,91.78,119L112,64.15,132.22,119a8,8,0,0,0,4.74,4.74L191.85,144ZM144,40a8,8,0,0,1,8-8h16V16a8,8,0,0,1,16,0V32h16a8,8,0,0,1,0,16H184V64a8,8,0,0,1-16,0V48H152A8,8,0,0,1,144,40ZM248,88a8,8,0,0,1-8,8h-8v8a8,8,0,0,1-16,0V96h-8a8,8,0,0,1,0-16h8V72a8,8,0,0,1,16,0v8h8A8,8,0,0,1,248,88Z",
    "image": "M216,40H40A16,16,0,0,0,24,56V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V56A16,16,0,0,0,216,40Zm0,16V158.75l-26.07-26.06a16,16,0,0,0-22.63,0l-20,20-44-44a16,16,0,0,0-22.62,0L40,149.37V56ZM40,172l52-52,80,80H40Zm176,28H194.63l-36-36,20-20L216,181.31V200Zm-72-92a12,12,0,1,1,12,12A12,12,0,0,1,144,108Z",
    # 자동차 — Phosphor car-simple
    "car": "M240,112H229.2L201.42,49.5A16,16,0,0,0,186.8,40H69.2a16,16,0,0,0-14.62,9.5L26.8,112H16a8,8,0,0,0,0,16h8v80a16,16,0,0,0,16,16H64a16,16,0,0,0,16-16V192h96v16a16,16,0,0,0,16,16h24a16,16,0,0,0,16-16V128h8a8,8,0,0,0,0-16ZM69.2,56H186.8l24.89,56H44.31ZM64,208H40V192H64Zm128,0V192h24v16Zm24-32H40V128H216ZM56,152a8,8,0,0,1,8-8H80a8,8,0,0,1,0,16H64A8,8,0,0,1,56,152Zm112,0a8,8,0,0,1,8-8h16a8,8,0,0,1,0,16H176A8,8,0,0,1,168,152Z",
    # 헤드폰 — Phosphor headphones
    "headphones": "M201.89,62.11A104,104,0,0,0,24,136v56a24,24,0,0,0,24,24H64a24,24,0,0,0,24-24V160a24,24,0,0,0-24-24H40.36A88,88,0,0,1,128,48h.67a88,88,0,0,1,87,88H192a24,24,0,0,0-24,24v32a24,24,0,0,0,24,24h16a24,24,0,0,0,24-24V136A103.32,103.32,0,0,0,201.89,62.11ZM64,152a8,8,0,0,1,8,8v32a8,8,0,0,1-8,8H48a8,8,0,0,1-8-8V152Zm152,40a8,8,0,0,1-8,8H192a8,8,0,0,1-8-8V160a8,8,0,0,1,8-8h24Z",
    # 마이크 — Phosphor microphone
    "mic": "M128,176a48.05,48.05,0,0,0,48-48V64a48,48,0,0,0-96,0v64A48.05,48.05,0,0,0,128,176ZM96,64a32,32,0,0,1,64,0v64a32,32,0,0,1-64,0Zm40,143.6V232a8,8,0,0,1-16,0V207.6A80.11,80.11,0,0,1,48,128a8,8,0,0,1,16,0,64,64,0,0,0,128,0,8,8,0,0,1,16,0A80.11,80.11,0,0,1,136,207.6Z",
    # 대화 — Phosphor chat-circle
    "chat": "M128,24A104,104,0,0,0,36.18,176.88L24.83,210.93a16,16,0,0,0,20.24,20.24l34.05-11.35A104,104,0,1,0,128,24Zm0,192a87.87,87.87,0,0,1-44.06-11.81,8,8,0,0,0-6.54-.67L40,216,52.47,178.6a8,8,0,0,0-.66-6.54A88,88,0,1,1,128,216Z",
    "check": "M229.66,77.66l-128,128a8,8,0,0,1-11.32,0l-56-56a8,8,0,0,1,11.32-11.32L96,188.69,218.34,66.34a8,8,0,0,1,11.32,11.32Z",
}


def svg(name, size=None):
    """인라인 Phosphor SVG. 색은 currentColor 로 주변 텍스트를 물려받습니다."""
    attrs = 'viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"'
    if size:
        attrs = 'width="%d" height="%d" ' % (size, size) + attrs
    return '<svg %s><path d="%s"/></svg>' % (attrs, ICONS[name])


def png_size(fname):
    """PNG 헤더에서 실제 픽셀 크기를 읽습니다 — width/height 로 레이아웃 흔들림을 없앱니다."""
    path = os.path.join(ROOT, "images", "shots", fname)
    try:
        with open(path, "rb") as fh:
            head = fh.read(24)
        if head[1:4] == b"PNG" and len(head) == 24:
            return struct.unpack(">II", head[16:24])
    except (IOError, OSError, struct.error):
        pass
    return (1080, 2400)          # 파일이 아직 없을 때의 기본 비율


def shot(base, key, alt, missing_label, eager=False):
    """스크린샷 한 장. 파일이 없으면 같은 비율의 조용한 자리 표시로 바뀝니다."""
    fname = SHOTS[key]
    w, h = png_size(fname)
    loading = "" if eager else ' loading="lazy"'
    return (
        '<figure class="shot">\n'
        '          <img src="%simages/shots/%s" alt="%s" width="%d" height="%d"%s decoding="async"\n'
        '               onload="this.closest(\'.shot\').classList.add(\'is-loaded\')">\n'
        '          <figcaption class="shot-note" style="aspect-ratio:%d/%d">%s'
        '<span>%s</span><code>images/shots/%s</code></figcaption>\n'
        '        </figure>' % (base, fname, alt, w, h, loading,
                               w, h, svg("image"), missing_label, fname)
    )


def alternates(current):
    """hreflang — 5개 언어 + x-default(한국어)."""
    out = []
    for code in LANG_ORDER:
        out.append('<link rel="alternate" hreflang="%s" href="%s/%s" />'
                   % (LANG_HREFLANG[code], SITE, LANG_PATHS[code]))
    out.append('<link rel="alternate" hreflang="x-default" href="%s/" />' % SITE)
    return "\n".join(out)


def lang_switch(current, base):
    links = []
    for code in LANG_ORDER:
        href = (base + LANG_PATHS[code]) or "./"
        cur = ' aria-current="true"' if code == current else ""
        links.append('<a href="%s" hreflang="%s" lang="%s"%s>%s</a>'
                     % (href, LANG_HREFLANG[code], code, cur, LANG_SHORT[code]))
    return "\n        ".join(links)


def jsonld(code, t, deletion_url):
    app = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "XXII player",
        "applicationCategory": "MusicApplication",
        "operatingSystem": "Android",
        "inLanguage": code,
        "description": t["description"],
        "url": "%s/%s" % (SITE, LANG_PATHS[code]),
        "image": "%s/images/Frame512.png" % SITE,
        "downloadUrl": PLAY_URL,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.0", "ratingCount": "2000"},
        "author": {"@type": "Organization", "name": "XXII player"},
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": code,
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer",
                                "text": a.replace('<a href="{deletion}">', "").replace("</a>", "")
                                         .format(deletion=deletion_url)}}
            for q, a in t["faq"]
        ],
    }
    dump = lambda o: json.dumps(o, ensure_ascii=False, indent=2)
    return ('<script type="application/ld+json">\n%s\n</script>\n\n'
            '<script type="application/ld+json">\n%s\n</script>' % (dump(app), dump(faq)))


def build(code):
    t = LANGS[code]
    path = LANG_PATHS[code]
    base = "" if code == "ko" else "../"          # 자원 경로 접두사
    is_rtl = code in RTL
    dir_attr = ' dir="rtl"' if is_rtl else ""
    canonical = "%s/%s" % (SITE, path)
    privacy = base + "privacy-policy.html"
    deletion = base + "account-deletion.html"

    # ── 세 가지 핵심 가치 ──
    values = "\n".join(
        '      <article class="value">\n'
        '        <div class="value-icon">%s</div>\n'
        '        <h3>%s</h3>\n'
        '        <p>%s</p>\n'
        '      </article>' % (svg(icon), title, body)
        for icon, title, body in t["values"]
    )

    # ── 기능 상세 ──
    feats = []
    for i, f in enumerate(t["feats"], 1):
        pro = ('<span class="tag">%s%s</span>' % (svg("sparkle"), t["pro_tag"])) if f.get("pro") else ""
        note = ('<span class="feat-note text-muted">%s</span>' % f["note"]) if f.get("note") else ""
        items = "\n".join("          <li>%s</li>" % it for it in f["items"])
        shots = f.get("shots", [])

        if not shots:
            cls = "feat feat-textonly"
            media = ""
        else:
            cls = "feat"
            if f.get("lead"):
                cls += " feat-lead"
            if f.get("wide"):
                cls += " feat-wide"
                mcls = " is-stack"      # 가로 캡처는 위아래로 쌓습니다
            elif len(shots) > 1:
                mcls = " is-pair"
                cls += " feat-pair"
            else:
                mcls = ""
            figs = "\n        ".join(
                shot(base, k, "%s — XXII player" % f["title"], t["shot_missing"]) for k in shots
            )
            media = '\n      <div class="feat-media%s">\n        %s\n      </div>' % (mcls, figs)

        feats.append(
            '    <article class="%s">\n'
            '      <div class="feat-copy">\n'
            '        <div class="feat-head">\n'
            '          <span class="feat-num">%02d</span>\n'
            '          <span class="feat-icon">%s</span>\n'
            '          %s%s\n'
            '        </div>\n'
            '        <h3>%s</h3>\n'
            '        <ul class="feat-list">\n%s\n        </ul>\n'
            '      </div>%s\n'
            '    </article>' % (cls, i, svg(f["icon"]), pro, note, f["title"], items, media)
        )
    feats = "\n".join(feats)

    # ── 요금 비교표 ──
    yes = '<span class="yes">%s<span class="sr-only">%s</span></span>' % (
        svg("check"), t["plans_included"])
    no = '<span class="no"></span><span class="sr-only">%s</span>' % t["plans_not_included"]
    rows = "\n".join(
        '          <tr><th scope="row">%s</th>'
        '<td class="col-plan">%s</td><td class="col-plan">%s</td></tr>'
        % (label, yes if free else no, yes if pro else no)
        for label, free, pro in t["plans_rows"]
    )

    # ── 신뢰 ──
    trust = "\n".join(
        '      <li><strong>%s</strong>%s</li>' % (head, body)
        for head, body in t["trust_items"]
    )

    # ── FAQ ──
    faq = "\n".join(
        '      <details%s>\n'
        '        <summary>%s</summary>\n'
        '        <p>%s</p>\n'
        '      </details>' % (" open" if n == 0 else "", q, a.format(deletion=deletion))
        for n, (q, a) in enumerate(t["faq"])
    )

    hero_trust = ('\n        <span class="dot"></span>\n        '
                  .join('<span>%s</span>' % x for x in t["hero_trust"]))

    html = """<!DOCTYPE html>
<html lang="{code}"{dir_attr}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>

<meta name="description" content="{description}" />
<meta name="keywords" content="{keywords}" />
<meta name="author" content="XXII player" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
<meta name="theme-color" content="#161826" />

<link rel="canonical" href="{canonical}" />
{alternates}

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:site_name" content="XXII player" />
<meta property="og:locale" content="{og_locale}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{site}/images/Frame512.png" />
<meta property="og:image:width" content="512" />
<meta property="og:image:height" content="512" />
<meta property="og:image:alt" content="XXII player" />

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{site}/images/Frame512.png" />

<!-- 파비콘 -->
<link rel="icon" type="image/png" sizes="32x32" href="{base}images/Frame32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="{base}images/Frame16.png" />
<link rel="apple-touch-icon" sizes="180x180" href="{base}images/Frame180.png" />
<link rel="manifest" href="/site.webmanifest" />

<!-- 디자인 시스템 — Nocturne (브랜드 레드 액센트) -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Noto+Sans+KR:wght@400;500&family=Noto+Sans+Arabic:wght@400;500&display=swap" />
<link rel="stylesheet" href="{base}css/nocturne.css" />
<link rel="stylesheet" href="{base}css/landing.css" />

{jsonld}
</head>
<body>

<a class="skip-link" href="#main">{skip}</a>

<!-- ============================ 상단 바 ============================ -->
<nav class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="{base_home}">
      <span class="brand-mark">{note_icon}</span>
      <span class="brand-name">XXII player</span>
    </a>

    <ul class="topbar-nav">
      <li><a href="#features">{nav_features}</a></li>
      <li><a href="#plans">{nav_plans}</a></li>
      <li><a href="#faq">{nav_faq}</a></li>
    </ul>

    <div class="lang-switch" role="group" aria-label="{footer_langlabel}">
        {lang_switch}
    </div>

    <a class="btn btn-accent" href="{play}">{play_icon}{play_short}</a>
  </div>
</nav>

<main id="main">

<!-- ============================ 히어로 ============================ -->
<section class="hero">
  <div class="hero-copy">
    <p class="kicker">{hero_kicker}</p>
    <h1>{hero_h1}</h1>
    <hr class="mark mark-lg">
    <p class="hero-lead">{hero_lead}</p>

    <div class="hero-actions">
      <a class="btn btn-accent btn-lg" href="{play}">{play_icon}{hero_cta}</a>
    </div>

    <p class="hero-trust">
        {hero_trust}
    </p>
  </div>

  <div class="hero-shots">
    {hero_shot_a}
    {hero_shot_b}
  </div>
</section>

<!-- ============================ 핵심 가치 ============================ -->
<section class="section">
  <p class="kicker">{values_kicker}</p>
  <hr class="mark">
  <div class="values" style="margin-top:44px">
{values}
  </div>
</section>

<!-- ============================ 기능 상세 ============================ -->
<section class="section" id="features">
  <div class="section-head">
    <p class="kicker">{feats_kicker}</p>
    <h2>{feats_title}</h2>
    <hr class="mark mark-lg">
    <p>{feats_intro}</p>
  </div>

  <div class="feats">
{feats}
  </div>
</section>

<!-- ============================ 무료와 Pro ============================ -->
<section class="section" id="plans">
  <div class="section-head">
    <p class="kicker">{plans_kicker}</p>
    <h2>{plans_title}</h2>
    <hr class="mark mark-lg">
  </div>

  <div class="plans">
    <table>
      <thead>
        <tr>
          <th scope="col">{plans_feature_col}</th>
          <th scope="col" class="col-plan">{plans_free}</th>
          <th scope="col" class="col-plan col-pro">{plans_pro}</th>
        </tr>
      </thead>
      <tbody>
{rows}
      </tbody>
    </table>
    <p class="plans-note">{plans_note}</p>
  </div>
</section>

<!-- ============================ 개인정보 · 신뢰 ============================ -->
<section class="section">
  <div class="section-head">
    <p class="kicker">{trust_kicker}</p>
    <h2>{trust_title}</h2>
    <hr class="mark mark-lg">
  </div>

  <ul class="trust-list">
{trust}
  </ul>
  <p class="trust-langs">{trust_langs}</p>
</section>

<!-- ============================ FAQ ============================ -->
<section class="section" id="faq">
  <div class="section-head">
    <p class="kicker">{faq_kicker}</p>
    <h2>{faq_title}</h2>
    <hr class="mark mark-lg">
  </div>

  <div class="faq">
{faq}
  </div>
</section>

<!-- ============================ CTA ============================ -->
<section class="cta-section">
  <p class="kicker">{cta_kicker}</p>
  <h2>{cta_title}</h2>
  <hr class="mark mark-lg">
  <p>{cta_lead}</p>
  <div class="hero-actions">
    <a class="btn btn-accent btn-lg" href="{play}">{play_icon}{cta_btn}</a>
  </div>
</section>

</main>

<!-- ============================ 푸터 ============================ -->
<footer>
  <div class="footer-links">
    <a href="{privacy}">{footer_privacy}</a>
    <a href="{deletion}">{footer_deletion}</a>
    <a href="mailto:{email}">{footer_contact}</a>
  </div>
  <p>{footer_rights}</p>
  <p>{email}</p>
</footer>

</body>
</html>
""".format(
        code=code, dir_attr=dir_attr, title=t["title"], description=t["description"],
        keywords=t["keywords"], canonical=canonical, alternates=alternates(code),
        og_locale=LANG_OG_LOCALE[code], site=SITE, base=base,
        base_home=(base or "./"), jsonld=jsonld(code, t, deletion),
        skip=t["skip"], note_icon=svg("note"), play_icon=svg("play"),
        nav_features=t["nav"]["features"], nav_plans=t["nav"]["plans"], nav_faq=t["nav"]["faq"],
        lang_switch=lang_switch(code, base), footer_langlabel=t["footer_langlabel"],
        play=PLAY_URL, play_short=t["play_short"],
        hero_kicker=t["hero_kicker"], hero_h1=t["hero_h1"], hero_lead=t["hero_lead"],
        hero_cta=t["hero_cta"], hero_trust=hero_trust,
        hero_shot_a=shot(base, HERO_SHOTS[0], "XXII player", t["shot_missing"], eager=True),
        hero_shot_b=shot(base, HERO_SHOTS[1], "XXII player", t["shot_missing"], eager=True),
        values_kicker=t["values_kicker"], values=values,
        feats_kicker=t["feats_kicker"], feats_title=t["feats_title"],
        feats_intro=t["feats_intro"], feats=feats,
        plans_kicker=t["plans_kicker"], plans_title=t["plans_title"],
        plans_feature_col=t["plans_feature_col"], plans_free=t["plans_free"],
        plans_pro=t["plans_pro"], rows=rows, plans_note=t["plans_note"],
        trust_kicker=t["trust_kicker"], trust_title=t["trust_title"],
        trust=trust, trust_langs=t["trust_langs"],
        faq_kicker=t["faq_kicker"], faq_title=t["faq_title"], faq=faq,
        cta_kicker=t["cta_kicker"], cta_title=t["cta_title"],
        cta_lead=t["cta_lead"], cta_btn=t["cta_btn"],
        privacy=privacy, deletion=deletion, email=EMAIL,
        footer_privacy=t["footer_privacy"], footer_deletion=t["footer_deletion"],
        footer_contact=t["footer_contact"], footer_rights=t["footer_rights"],
    )

    out = os.path.join(ROOT, path, "index.html")
    d = os.path.dirname(out)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    io.open(out, "w", encoding="utf-8", newline="\n").write(html)
    return os.path.relpath(out, ROOT), len(html)


def sitemap():
    urls = "\n".join(
        "  <url>\n    <loc>%s/%s</loc>\n%s    <changefreq>monthly</changefreq>\n  </url>"
        % (SITE, LANG_PATHS[c],
           "".join('    <xhtml:link rel="alternate" hreflang="%s" href="%s/%s"/>\n'
                   % (LANG_HREFLANG[o], SITE, LANG_PATHS[o]) for o in LANG_ORDER))
        for c in LANG_ORDER
    )
    extra = "\n".join(
        "  <url>\n    <loc>%s/%s</loc>\n    <changefreq>yearly</changefreq>\n  </url>" % (SITE, p)
        for p in ("privacy-policy.html", "account-deletion.html")
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           '%s\n%s\n</urlset>\n' % (urls, extra))
    io.open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(xml)
    return "sitemap.xml"


if __name__ == "__main__":
    for c in LANG_ORDER:
        rel, n = build(c)
        print("  %-20s %6d bytes" % (rel, n))
    print("  %-20s" % sitemap())
    print("\n%d개 언어 페이지를 생성했습니다." % len(LANG_ORDER))
