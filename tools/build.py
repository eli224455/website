#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for Elizabeth Tesfaye Law Office.

Usage:   python3 tools/build.py
Output:  plain .html files in the repository root, ready to serve.

No dependencies beyond the Python standard library.
"""

import os
import re
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config as C
import template as T
from content_practice import PRACTICE_CONTENT
from content_pages import FAQ_GROUPS, INSIGHTS, all_faq_pairs
import content_home as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()

WRITTEN = []

# Escape stray "&" in text and attributes (e.g. "Succession & Inheritance") so
# every page validates, while leaving real entities (&amp; &copy; &middot;) and
# the contents of <script> blocks — JSON-LD, where "&" is legal — untouched.
_SCRIPT_RE = re.compile(r"(<script\b.*?</script>)", re.S | re.I)
_BARE_AMP = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|[a-zA-Z][a-zA-Z0-9]{1,31};)")


def escape_bare_ampersands(html):
    parts = _SCRIPT_RE.split(html)
    for i in range(0, len(parts), 2):        # even indices are outside <script>
        parts[i] = _BARE_AMP.sub("&amp;", parts[i])
    return "".join(parts)


def write(path, html):
    """path is a site path like '/about/' or '/'."""
    html = escape_bare_ampersands(html)
    if path == "/":
        out = os.path.join(ROOT, "index.html")
    elif path.endswith("/"):
        out = os.path.join(ROOT, path.strip("/"), "index.html")
    else:
        out = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    WRITTEN.append((path, os.path.relpath(out, ROOT)))


def todo(text):
    """A placeholder the firm must replace before publishing.
    Deliberately conspicuous so it cannot ship unnoticed."""
    return ('<mark style="background:#FFF3CD;color:#7A5C00;padding:.1em .35em;'
            'border-bottom:2px solid #E0A800;font-weight:600">' + text + '</mark>')


# ===========================================================================
# Shared fragments
# ===========================================================================

def practice_cards(exclude=None, limit=None):
    cards = []
    for p in C.PRACTICE_AREAS:
        if exclude and p["slug"] == exclude:
            continue
        cards.append(f"""      <article class="card card--stretch reveal">
        <div class="card-icon">{T.ICONS[p['icon']]}</div>
        <h3><a href="/{p['slug']}/" style="text-decoration:none">{T.tx(p['title'], p.get('title_am', p['title']))}</a></h3>
        <p>{p['summary']}</p>
        <span class="card-link">{T.tx("Learn more", "ተጨማሪ ይመልከቱ")}</span>
      </article>""")
        if limit and len(cards) >= limit:
            break
    return "\n".join(cards)


def sidebar(current_slug):
    links = []
    for p in C.PRACTICE_AREAS:
        aria = ' aria-current="page"' if p["slug"] == current_slug else ""
        links.append(f'<li><a href="/{p["slug"]}/"{aria}>{T.tx(p["nav_title"], p.get("nav_title_am", p["nav_title"]))}</a></li>')
    return f"""<aside class="sidebar">
  <h4 style="font-family:var(--font-body);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem">Practice Areas</h4>
  <ul class="sidebar-nav">
    {"".join(links)}
  </ul>
  <div class="sidebar-card">
    <h3>{T.tx("Speak with us", "ያግኙን")}</h3>
    <p>{T.tx("Call, WhatsApp or email. Every conversation is confidential.", "ይደውሉ፣ WhatsApp ይላኩ ወይም ኢሜይል። እያንዳንዱ ውይይት በሚስጥር ይያዛል።")}</p>
    <p style="margin-bottom:1.25rem"><a href="tel:{C.PHONE}" style="color:#fff;text-decoration:none;font-weight:600">{C.PHONE_DISPLAY}</a></p>
    <a class="btn btn--gold" href="tel:{C.PHONE}">{T.tx("Call now", "አሁን ይደውሉ")}</a>
    <a class="btn btn--whatsapp" style="width:100%;justify-content:center;margin-top:.7rem" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</aside>"""


# ===========================================================================
# Pages
# ===========================================================================

def _paras(texts):
    return "\n".join(f"      <p>{t}</p>" for t in texts)


def build_home():
    path = "/"
    title = H.TITLE
    desc = H.DESCRIPTION

    trust = []
    for item in H.TRUST:
        featured = " trust-item--featured" if item.get("featured") else ""
        heading = item["title"]
        trust.append(f"""      <div class="trust-item{featured}">
        <div class="trust-icon">{T.ICONS[item['icon']]}</div>
        <p class="trust-title">{heading}</p>
        <p>{item['body']}</p>
      </div>""")

    audiences = "\n".join(f"""      <article class="audience-card reveal">
        <h3>{g['h3']}</h3>
        <p>{g['body']}</p>
      </article>""" for g in H.CLIENTS["groups"])

    why_points = "\n".join(f"""        <li>
          <h3>{ptitle}</h3>
          <p>{body}</p>
        </li>""" for ptitle, body in H.WHY["points"])

    steps = []
    for i, (step_title, body) in enumerate(H.PROCESS["steps"], 1):
        steps.append(f"""      <li class="process-step reveal">
        <span class="feature-num">{i}</span>
        <div>
          <h3>{step_title}</h3>
          <p>{body}</p>
        </div>
      </li>""")

    faqs = "\n".join(f"""      <article class="home-faq-item reveal">
        <h3>{q}</h3>
        <p>{a}</p>
      </article>""" for q, a in H.HOME_FAQ["items"])

    posts = "\n".join(f"""      <article class="post-card reveal">
        <p class="post-meta">{p['category']} &middot; {p['date_display']}</p>
        <p class="post-card-title"><a href="/insights/{p['slug']}/">{p['title']}</a></p>
        <p>{p['description']}</p>
      </article>""" for p in INSIGHTS)

    html = T.head(title, desc, path,
                  extra_schema=[T.attorney_schema(),
                                {"@context": "https://schema.org",
                                 "@type": "WebSite",
                                 "@id": C.SITE_URL + "/#website",
                                 "url": C.SITE_URL + "/",
                                 "name": C.FIRM_NAME,
                                 "inLanguage": "en",
                                 "publisher": {"@id": C.SITE_URL + "/#organization"}}])
    html += T.header(path)

    html += f"""<section class="hero hero--light">
  <div class="hero-split">
    <div class="hero-copy">
      <span class="eyebrow">{H.HERO['eyebrow']}</span>
      <h1>{H.HERO['h1']}</h1>
      <hr class="rule">
      <p class="hero-lead">{H.HERO['lead']}</p>
      <div class="btn-row">
        <a class="btn btn--gold" href="/contact/">Book a Consultation</a>
        <a class="btn btn--ghost" href="/practice-areas/">Explore Practice Areas</a>
      </div>
    </div>
    <figure class="hero-visual">
      <img src="/assets/img/hero-portrait.png" alt="Elizabeth Tesfaye, attorney at Elizabeth Tesfaye Law Office in Addis Ababa, Ethiopia" width="1024" height="576" fetchpriority="high" decoding="async">
    </figure>
  </div>
  <div class="hero-nap">
    <div class="wrap">
      <dl class="hero-meta">
        <div><dt>Office</dt><dd>{C.STREET}, {C.CITY}</dd></div>
        <div><dt>Telephone</dt><dd><a href="tel:{C.PHONE}">{C.PHONE_DISPLAY}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></dd></div>
        <div><dt>Languages</dt><dd>English &amp; አማርኛ</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="trust-bar" aria-label="Why this law office">
  <div class="wrap trust-grid">
{"".join(trust)}
  </div>
</section>

<section class="section section--paper">
  <div class="wrap grid grid--split split--photo">
    <figure class="photo-frame photo-frame--lg reveal">
      <img src="/assets/img/team-office.png" alt="Elizabeth Tesfaye Law Office — legal consultation in Addis Ababa" width="1024" height="768" loading="lazy">
    </figure>
    <div>
      <span class="eyebrow">{H.FIRM['eyebrow']}</span>
      <h2>{H.FIRM['h2']}</h2>
      <hr class="rule">
{_paras(H.FIRM['paras'])}
      <div class="btn-row">
        <a class="btn btn--gold" href="/contact/">Describe your matter</a>
        <a class="btn btn--ghost" href="/about/">About the firm</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="practice-intro grid grid--split split--photo">
      <div class="section-head" style="margin-bottom:0">
        <span class="eyebrow">{H.PRACTICE_INTRO['eyebrow']}</span>
        <h2>{H.PRACTICE_INTRO['h2']}</h2>
        <hr class="rule">
        <p class="lead">{H.PRACTICE_INTRO['lead']}</p>
      </div>
      <figure class="photo-frame reveal">
        <img src="/assets/img/courtroom.png" alt="Advocacy before the Ethiopian courts — Elizabeth Tesfaye Law Office" width="1024" height="576" loading="lazy">
      </figure>
    </div>
    <div class="grid grid--3" style="margin-top:clamp(2rem, 1.5rem + 2vw, 3.5rem)">
{practice_cards()}
    </div>
  </div>
</section>

<section class="section section--warm">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{H.CLIENTS['eyebrow']}</span>
      <h2>{H.CLIENTS['h2']}</h2>
      <hr class="rule">
    </div>
    <div class="grid grid--3">
{audiences}
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">{H.WHY['eyebrow']}</span>
      <h2>{H.WHY['h2']}</h2>
      <hr class="rule rule--center">
{_paras(H.WHY['paras'])}
    </div>
    <div class="stats stats--light">
      <div><div class="stat-value">6</div><div class="stat-label">Practice areas</div></div>
      <div><div class="stat-value">2</div><div class="stat-label">Languages, English &amp; Amharic</div></div>
      <div><div class="stat-value">1</div><div class="stat-label">Business day reply</div></div>
    </div>
    <ul class="why-grid">
{why_points}
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{H.PROCESS['eyebrow']}</span>
      <h2>{H.PROCESS['h2']}</h2>
      <hr class="rule">
      <p class="lead">{H.PROCESS['lead']}</p>
    </div>
    <ol class="process-list">
{"".join(steps)}
    </ol>
  </div>
</section>

<section class="section section--warm">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{H.HOME_FAQ['eyebrow']}</span>
      <h2>{H.HOME_FAQ['h2']}</h2>
      <hr class="rule">
    </div>
    <div class="home-faq">
{faqs}
    </div>
    <div class="btn-row">
      <a class="btn btn--ghost" href="/faq/">All 20 questions</a>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap grid grid--split split--photo">
    <div>
      <span class="eyebrow">{H.ATTORNEY['eyebrow']}</span>
      <h2>{H.ATTORNEY['h2']}</h2>
      <hr class="rule">
{_paras(H.ATTORNEY['paras'])}
      <figure class="quote">
        <blockquote>{H.ATTORNEY['quote']}</blockquote>
        <figcaption><strong>{H.ATTORNEY['quote_attr']}</strong></figcaption>
      </figure>
      <div class="btn-row">
        <a class="btn btn--ghost" href="/about/">Read more</a>
      </div>
    </div>
    <figure class="photo-frame photo-frame--portrait reveal">
      <img src="/assets/img/elizabeth-portrait.png" alt="Elizabeth Tesfaye, attorney-at-law and legal consultant in Addis Ababa" width="1024" height="576" loading="lazy">
    </figure>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid--split split--photo">
    <figure class="photo-frame photo-frame--lg reveal">
      <img src="/assets/img/library.png" alt="Law library at Elizabeth Tesfaye Law Office, Summit, Addis Ababa" width="1024" height="576" loading="lazy">
    </figure>
    <div>
      <span class="eyebrow">{H.VISIT['eyebrow']}</span>
      <h2>{H.VISIT['h2']}</h2>
      <hr class="rule">
{_paras(H.VISIT['paras'])}
      <div class="btn-row">
        <a class="btn btn--gold" href="/contact/">Contact &amp; directions</a>
        <a class="btn btn--ghost" href="tel:{C.PHONE}">Call {C.PHONE_DISPLAY}</a>
      </div>
      <address class="visit-nap">
        <strong>{C.FIRM_NAME}</strong><br>
        {C.STREET}<br>
        {C.CITY}, {C.COUNTRY}<br>
        <a href="tel:{C.PHONE}">{C.PHONE_DISPLAY}</a> · <a href="mailto:{C.EMAIL}">{C.EMAIL}</a>
        <p class="visit-hours">Monday – Friday, 8:30 AM – 5:30 PM · Saturday by appointment · Sunday closed</p>
      </address>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{H.INSIGHTS['eyebrow']}</span>
      <h2>{H.INSIGHTS['h2']}</h2>
      <hr class="rule">
      <p class="lead">{H.INSIGHTS['lead']}</p>
    </div>
    <div class="grid grid--3">
{posts}
    </div>
    <div class="btn-row">
      <a class="btn btn--ghost" href="/insights/">All insights</a>
    </div>
  </div>
</section>

<section class="cta-band cta-band--light">
  <div class="wrap">
    <span class="eyebrow">{H.CTA['eyebrow']}</span>
    <h2>{H.CTA['h2']}</h2>
    <p>{H.CTA['body']}</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--gold" href="/contact/">Book a Consultation</a>
      <a class="btn btn--navy" href="tel:{C.PHONE}">Call {C.PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""
    html += T.footer()
    write(path, html)


def build_about():
    path = "/about/"
    trail = [("Home", "/"), ("About", None)]
    title = "About Elizabeth Tesfaye | Lawyer in Addis Ababa"
    desc = ("Elizabeth Tesfaye is an Addis Ababa lawyer and former public prosecutor "
            "in criminal and civil matters, with 13 years in Ethiopian law.")

    html = T.head(title, desc, path, extra_schema=T.attorney_schema(),
                  breadcrumbs=trail)
    html += T.header(path)
    html += T.page_header(
        T.tx("About the firm", "ስለ ቢሮው"),
        T.tx("Former public prosecutor in criminal and civil matters. 13 years in Ethiopian law. Counsel in English and Amharic.",
             "በወንጀል እና በፍትሐ ብሔር የቀድሞ ዐቃቤ ሕግ። 13 ዓመት በኢትዮጵያ ህግ። ምክር በእንግሊዝኛ እና በአማርኛ።"), trail)

    html += f"""<section class="section section--paper">
  <div class="wrap about-hero-grid">
    <figure class="photo-frame photo-frame--portrait reveal">
      <img src="/assets/img/elizabeth-portrait.png" alt="Elizabeth Tesfaye, attorney-at-law, Addis Ababa" width="1024" height="576">
    </figure>
    <div class="article-body prose">
      <p class="i18n-en">Elizabeth Tesfaye Law Office is a private practice in Addis Ababa, advising individuals, families and businesses on matters of Ethiopian law.</p>
      <p class="i18n-am" lang="am">የኤልሳቤት ተስፋዬ የህግ ቢሮ በአዲስ አበባ የሚገኝ የግል ልምምድ ሲሆን ለግለሰቦች፣ ለቤተሰቦች እና ለንግድ ድርጅቶች በኢትዮጵያ ህግ ላይ ያማክራል።</p>

      <h2>{T.tx("The attorney", "ጠበቃዋ")}</h2>
      <p class="i18n-en"><strong>{C.ATTORNEY_NAME}</strong> served as a public prosecutor in criminal and civil matters before entering private practice. She has 13 years of experience in Ethiopian law and now represents clients from this office in Summit, Addis Ababa.</p>
      <p class="i18n-am" lang="am"><strong>{C.ATTORNEY_NAME}</strong> ወደ ግል ልምምድ ከመግባቷ በፊት በወንጀል እና በፍትሐ ብሔር ጉዳዮች ዐቃቤ ሕግ ሆና አገልግላለች። 13 ዓመት የኢትዮጵያ ህግ ልምድ አላት፣ አሁን ደግሞ ከሰሚት፣ አዲስ አበባ ከዚህ ቢሮ ደንበኞችን ትወክላለች።</p>

      <p class="i18n-en">Those years as a prosecutor shape how she works now: files are read closely, documents are prepared with care, and clients are told plainly where they stand — including when the news is not good. Private practice lets her stay with a matter from the first conversation through to judgment, settlement or enforcement.</p>
      <p class="i18n-am" lang="am">እንደ ዐቃቤ ሕግ ያሳለፈችው ጊዜ አሁን እንዴት እንደምትሠራ ይቀርጻል፦ ፋይሎች በጥንቃቄ ይነበባሉ፣ ሰነዶች በጥንቃቄ ይዘጋጃሉ፣ ደንበኞችም የት እንደሚቆሙ በግልጽ ይነገራቸዋል — ዜናው መልካም ባይሆንም። የግል ልምምድ ከመጀመሪያው ውይይት እስከ ፍርድ፣ ስምምነት ወይም አፈጻጸም ጉዳዩን አብራ እንድትከታተል ያስችላታል።</p>

      <div class="callout">
        <p class="i18n-en"><strong>Languages.</strong> Advice and representation are offered in English and Amharic. Ethiopians living abroad are routinely represented under power of attorney.</p>
        <p class="i18n-am" lang="am"><strong>ቋንቋዎች።</strong> ምክር እና ውክልና በእንግሊዝኛ እና በአማርኛ ይሰጣሉ። በውጭ የሚኖሩ ኢትዮጵያውያን በውክልና በመደበኛነት ይወከላሉ።</p>
      </div>

      <h2>{T.tx("Our approach", "አቀራረባችን")}</h2>
      <p class="i18n-en">Most people who need a lawyer are dealing with a problem they did not choose. A marriage has broken down. A relative has died and the family cannot agree. A supplier has not delivered. Someone has been arrested. The legal question sits inside a practical and often personal one.</p>
      <p class="i18n-am" lang="am">አብዛኛው ጠበቃ የሚያስፈልገው ሰው ያልመረጠውን ችግር እየተጋፈጠ ነው። ጋብቻ ተፈርሷል። ዘመድ ሞቶ ቤተሰቡ ሊስማማ አልቻለም። አቅራቢ አላደረሰም። አንድ ሰው ተያዘ። የህግ ጥያቄው በተግባራዊ እና ብዙ ጊዜ በግላዊ ጥያቄ ውስጥ ይቀመጣል።</p>

      <p class="i18n-en">The first job is to make the situation legible — what the law provides, what is likely to happen, roughly how long it will take and what it will cost — so the client can make an informed decision rather than an anxious one.</p>
      <p class="i18n-am" lang="am">የመጀመሪያው ስራ ሁኔታውን ግልጽ ማድረግ ነው — ህጉ ምን እንደሚሰጥ፣ ምን ሊሆን እንደሚችል፣ ምን ያህል ጊዜ እና ወጪ እንደሚወስድ — ደንበኛው በፍርሃት ሳይሆን በመረጃ ላይ ተመስርቶ እንዲወስን።</p>

      <h2>{T.tx("Who we act for", "ለማን እንሠራለን")}</h2>
      <ul>
        <li>{T.tx("Individuals and families in Addis Ababa and across Ethiopia", "በአዲስ አበባ እና በመላው ኢትዮጵያ የሚገኙ ግለሰቦች እና ቤተሰቦች")}</li>
        <li>{T.tx("Members of the Ethiopian diaspora with inheritance, property and family matters at home", "በውጭ የሚኖሩ ኢትዮጵያውያን ውርስ፣ ንብረት እና የቤተሰብ ጉዳዮች ሲኖሯቸው")}</li>
        <li>{T.tx("Small and medium businesses, from formation through to commercial disputes", "ትንንሽ እና መካከለኛ ንግዶች — ከመመስረት እስከ የንግድ ክርክር")}</li>
        <li>{T.tx("Foreign companies and investors establishing or operating in Ethiopia", "በኢትዮጵያ የሚቋቋሙ ወይም የሚሠሩ የውጭ ኩባንያዎች እና ባለሀብቶች")}</li>
      </ul>

      <h2>{T.tx("Confidentiality &amp; fees", "ሚስጥራዊነት እና ክፍያ")}</h2>
      <p class="i18n-en">Everything a client tells this office is confidential from the first conversation, whether or not that conversation leads to an instruction. Fees are discussed openly and early — fixed fees wherever the work allows it, agreed in writing before work begins.</p>
      <p class="i18n-am" lang="am">ደንበኛ ከመጀመሪያው ውይይት ጀምሮ ለዚህ ቢሮ የሚነግረው ሁሉ በሚስጥር ይያዛል — ውይይቱ ወደ ስራ ባይመራም። ክፍያ በግልጽ እና ቀድሞ ይነገራል — ስራው በሚፈቅድበት ጊዜ ቋሚ ክፍያ፣ ስራ ከመጀመሩ በፊት በጽሁፍ ይስማማል።</p>

      <h2>{T.tx("Visit the office", "ቢሮውን ይጎብኙ")}</h2>
      <p class="i18n-en">The office is at {C.STREET}, in {C.DISTRICT}, {C.CITY}. Consultations are by appointment — call or WhatsApp to arrange a time. Telephone and video consultations are available for clients outside Addis Ababa.</p>
      <p class="i18n-am" lang="am">ቢሮው በ{C.STREET}፣ {C.DISTRICT}፣ {C.CITY} ይገኛል። ምክክር በቀጠሮ ነው — ጊዜ ለመያዝ ይደውሉ ወይም WhatsApp ይላኩ። ከአዲስ አበባ ውጭ ለሚገኙ ደንበኞች በስልክ እና በቪዲዮ ምክክር ይገኛል።</p>
      {T.connect_buttons(gold=False)}
    </div>
  </div>
</section>

<section class="section section--warm section--tight">
  <div class="wrap photo-strip">
    <figure class="photo-frame reveal">
      <img src="/assets/img/consultation.png" alt="Client consultation at the office" width="1024" height="576">
    </figure>
    <figure class="photo-frame reveal">
      <img src="/assets/img/office-desk.png" alt="Desk at Elizabeth Tesfaye Law Office overlooking Addis Ababa" width="1024" height="576">
    </figure>
    <figure class="photo-frame reveal">
      <img src="/assets/img/signing.png" alt="Signing a legal services agreement" width="1024" height="576">
    </figure>
  </div>
</section>

{T.cta_band()}
"""
    html += T.footer()
    write(path, html)


def build_practice_index():
    path = "/practice-areas/"
    trail = [("Home", "/"), ("Practice Areas", None)]
    title = "Practice Areas | Lawyer in Addis Ababa, Ethiopia"
    desc = ("Family law, civil litigation, succession and inheritance, business and "
            "corporate law, criminal defense and legal consultation in Addis Ababa, "
            "Ethiopia.")

    html = T.head(title, desc, path, breadcrumbs=trail)
    html += T.header(path)
    html += T.page_header(
        "Practice areas",
        "Six areas of Ethiopian law, handled from the first consultation through to "
        "judgment and enforcement.", trail)

    html += f"""<section class="section section--paper">
  <div class="wrap">
    <div class="grid grid--3">
{practice_cards()}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">Not sure where your matter fits?</span>
    <h2>Most problems cross more than one category</h2>
    <hr class="rule">
    <p>A divorce raises questions about a family business. An inheritance dispute turns
    on a property transfer made years earlier. A commercial disagreement escalates into
    a criminal complaint. Legal problems rarely arrive in a single tidy category, which
    is one reason we handle a broad range of matters within one office — clients are
    not sent elsewhere at the point where continuity matters most.</p>
    <p>If you are not certain which area your situation falls under, that is not a
    problem. Describe what has happened and we will tell you.</p>
    <div class="btn-row">
      <a class="btn btn--navy" href="/contact/">{T.tx("Describe your matter", "ጉዳይዎን ይግለጹ")}</a>
      <a class="btn btn--ghost" href="/faq/">Read common questions</a>
    </div>
  </div>
</section>

{T.cta_band()}
"""
    html += T.footer()
    write(path, html)


def build_practice_pages():
    for area in C.PRACTICE_AREAS:
        slug = area["slug"]
        content = PRACTICE_CONTENT[slug]
        path = f"/{slug}/"
        trail = [("Home", "/"), ("Practice Areas", "/practice-areas/"),
                 (area["title"], None)]

        title = f'{area["title"]} in {C.CITY} | {C.FIRM_NAME}'
        if len(title) > 62:
            title = f'{area["title"]} Lawyer, {C.CITY} | {C.FIRM_SHORT}'
        desc = area["summary"] + f" Speak to a {area['keyword']}. Confidential consultation."
        if len(desc) > 155:
            desc = area["summary"][:120].rsplit(" ", 1)[0] + f" — {C.FIRM_NAME}, {C.CITY}."

        html = T.head(title, desc, path,
                      extra_schema=T.service_schema(area), breadcrumbs=trail)
        html += T.header(path)
        html += T.page_header(area["title"], content["lead"], trail)

        html += f"""<section class="section section--paper">
  <div class="wrap grid grid--split">
    <div class="article-body prose">
{content['body']}
      <div class="btn-row">
        <a class="btn btn--navy" href="tel:{C.PHONE}">{T.tx("Call the office", "ወደ ቢሮ ይደውሉ")}</a>
        <a class="btn btn--ghost" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
    <div>
{sidebar(slug)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Related</span>
      <h2>Other practice areas</h2>
      <hr class="rule">
    </div>
    <div class="grid grid--3">
{practice_cards(exclude=slug, limit=3)}
    </div>
  </div>
</section>

{T.cta_band()}
"""
        html += T.footer()
        write(path, html)


def build_faq():
    path = "/faq/"
    trail = [("Home", "/"), ("FAQ", None)]
    title = "Frequently Asked Questions | Lawyer in Addis Ababa, Ethiopia"
    desc = ("Answers to common questions about divorce, inheritance, court cases, "
            "bail and company registration in Ethiopia — from a law office in "
            "Addis Ababa.")

    html = T.head(title, desc, path,
                  extra_schema=T.faq_schema(all_faq_pairs()), breadcrumbs=trail)
    html += T.header(path)
    html += T.page_header(
        "Frequently asked questions",
        "General answers to the questions clients ask most often. They are not a "
        "substitute for advice on your own situation.", trail)

    sections = []
    for heading, pairs in FAQ_GROUPS:
        items = "\n".join(f"""      <details>
        <summary>{q}</summary>
        <div class="answer">{a}</div>
      </details>""" for q, a in pairs)
        anchor = heading.lower().replace(" ", "-").replace("&", "and")
        sections.append(f"""  <div class="wrap" style="margin-bottom:3.5rem">
    <h2 id="{anchor}" style="font-size:var(--step-2)">{heading}</h2>
    <div class="accordion">
{items}
    </div>
  </div>""")

    html += f"""<section class="section section--paper">
{"".join(sections)}
  <div class="wrap prose">
    <div class="callout">
      <p><strong>A note on these answers.</strong> They describe Ethiopian law in
      general terms for a lay reader. The law changes, and the outcome of any matter
      depends on its particular facts. Please do not rely on this page in place of
      advice about your own situation — <a href="/contact/">ask us directly</a>
      instead.</p>
    </div>
  </div>
</section>

{T.cta_band("Still have a question?",
            "If your question is not answered here, send it to us. "
            + C.RESPONSE_PROMISE)}
"""
    html += T.footer()
    write(path, html)


def build_contact():
    path = "/contact/"
    trail = [("Home", "/"), ("Contact", None)]
    title = "Contact | Law Office in Summit, Addis Ababa"
    desc = (f"Contact {C.FIRM_NAME} in {C.CITY}. {C.STREET}. "
            f"Telephone {C.PHONE_DISPLAY}.")

    hours_rows = "\n".join(
        f"<div style='display:flex;justify-content:space-between;gap:1rem;padding:.55rem 0;border-bottom:1px solid var(--line)'>"
        f"<span>{d}</span><span style='color:var(--muted)'>{h}</span></div>"
        for d, h in C.OPENING_HOURS)

    map_q = "Summit+Hewan+Building,+Addis+Ababa,+Ethiopia"

    html = T.head(title, desc, path, breadcrumbs=trail,
                  extra_schema={
                      "@context": "https://schema.org",
                      "@type": "ContactPage",
                      "url": C.SITE_URL + path,
                      "mainEntity": {"@id": C.SITE_URL + "/#organization"},
                  })
    html += T.header(path)
    html += T.page_header(
        T.tx("Contact the office", "ቢሮውን ያግኙ"),
        T.tx("No forms. Call, WhatsApp or email — every conversation is confidential.",
             "ቅጽ አይሞሉም። ይደውሉ፣ WhatsApp ይላኩ ወይም ኢሜይል — እያንዳንዱ ውይይት በሚስጥር ይያዛል።"), trail)

    html += f"""<section class="section section--paper">
  <div class="wrap">
    <div class="connect-grid">
      <a class="connect-card reveal" href="tel:{C.PHONE}">
        <span class="connect-icon">{T.ICONS['phone']}</span>
        <h2>{T.tx("Call", "ይደውሉ")}</h2>
        <p>{C.PHONE_DISPLAY}</p>
        <span class="card-link">{T.tx("Direct line", "ቀጥተኛ መስመር")}</span>
      </a>
      <a class="connect-card connect-card--wa reveal" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener">
        <span class="connect-icon">{T.ICONS['whatsapp']}</span>
        <h2>WhatsApp</h2>
        <p>{C.PHONE_DISPLAY}</p>
        <span class="card-link">{T.tx("Message now", "አሁን ይጻፉ")}</span>
      </a>
      <a class="connect-card reveal" href="mailto:{C.EMAIL}">
        <span class="connect-icon">{T.ICONS['mail']}</span>
        <h2>{T.tx("Email", "ኢሜይል")}</h2>
        <p>{C.EMAIL}</p>
        <span class="card-link">{T.tx("Write to the office", "ወደ ቢሮው ይጻፉ")}</span>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow">{T.tx("Office", "ቢሮ")}</span>
      <h2 style="font-size:var(--step-2)">Elizabeth Tesfaye Law Office</h2>
      <hr class="rule">
      <ul class="contact-list">
        <li>
          <span class="ci">{T.ICONS['pin']}</span>
          <div><span class="ci-label">{T.tx("Address", "አድራሻ")}</span>
          <p class="ci-value">{C.STREET}<br>{C.CITY}, {C.COUNTRY}</p></div>
        </li>
        <li>
          <span class="ci">{T.ICONS['clock']}</span>
          <div style="flex:1"><span class="ci-label">{T.tx("Office hours", "የቢሮ ሰዓት")}</span>
          <div class="ci-value" style="margin-top:.4rem">{hours_rows}</div></div>
        </li>
      </ul>
      <p class="form-note" style="margin-top:2rem">{T.tx("Consultations are by appointment. Telephone and video meetings are available for clients outside Addis Ababa and outside Ethiopia. Please do not send confidential documents until we have agreed in writing to act for you.",
        "ምክክር በቀጠሮ ነው። ከአዲስ አበባ እና ከኢትዮጵያ ውጭ ለሚገኙ ደንበኞች በስልክ እና በቪዲዮ ስብሰባ ይገኛል። በጽሁፍ እስክንስማማ ድረስ ሚስጥራዊ ሰነዶችን አይላኩ።")}</p>
    </div>
    <figure class="photo-frame">
      <img src="/assets/img/office-desk.png" alt="Elizabeth Tesfaye Law Office, Addis Ababa" width="1024" height="576">
    </figure>
  </div>
</section>

<section class="section section--warm section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{T.tx("Find us", "አድራሻችን")}</span>
      <h2 style="font-size:var(--step-2)">{C.DISTRICT}, {C.CITY}</h2>
      <hr class="rule">
      <p class="lead">{C.STREET}</p>
    </div>
    <div class="map-embed">
      <iframe
        title="Map showing the location of {C.FIRM_NAME} in {C.CITY}"
        src="https://www.google.com/maps?q={map_q}&amp;output=embed"
        loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        allowfullscreen></iframe>
    </div>
  </div>
</section>
"""
    html += T.footer()
    write(path, html)


def build_insights():
    path = "/insights/"
    trail = [("Home", "/"), ("Insights", None)]
    title = "Legal Insights on Ethiopian Law | Elizabeth Tesfaye Law Office"
    desc = ("Practical notes on Ethiopian family law, inheritance, litigation and "
            "company law from a law office in Addis Ababa.")

    posts = "\n".join(f"""      <article class="post-card reveal">
        <p class="post-meta">{p['category']} &middot; {p['date_display']}</p>
        <h3><a href="/insights/{p['slug']}/">{p['title']}</a></h3>
        <p>{p['description']}</p>
      </article>""" for p in INSIGHTS)

    html = T.head(title, desc, path, breadcrumbs=trail,
                  extra_schema={
                      "@context": "https://schema.org",
                      "@type": "Blog",
                      "url": C.SITE_URL + path,
                      "name": "Legal Insights",
                      "publisher": {"@id": C.SITE_URL + "/#organization"},
                  })
    html += T.header(path)
    html += T.page_header(
        "Legal insights",
        "Plain explanations of the Ethiopian law questions clients ask most often.",
        trail)
    html += f"""<section class="section section--paper">
  <div class="wrap">
    <div class="grid grid--3">
{posts}
    </div>
  </div>
</section>

{T.cta_band()}
"""
    html += T.footer()
    write(path, html)

    # Individual articles
    for i, post in enumerate(INSIGHTS):
        p_path = f"/insights/{post['slug']}/"
        p_trail = [("Home", "/"), ("Insights", "/insights/"), (post["title"], None)]
        related = next(a for a in C.PRACTICE_AREAS if a["slug"] == post["related"])

        others = [q for q in INSIGHTS if q["slug"] != post["slug"]]
        more = "\n".join(f"""      <article class="post-card reveal">
        <p class="post-meta">{q['category']} &middot; {q['date_display']}</p>
        <h3><a href="/insights/{q['slug']}/">{q['title']}</a></h3>
        <p>{q['description']}</p>
      </article>""" for q in others)

        h = T.head(post["seo_title"], post["description"], p_path,
                   og_type="article", extra_schema=T.article_schema(post),
                   breadcrumbs=p_trail)
        h += T.header("/insights/")
        h += T.page_header(post["title"], None, p_trail)
        h += f"""<section class="section section--paper">
  <div class="wrap grid grid--split">
    <div class="article-body prose">
      <p class="post-meta" style="margin-bottom:1.5rem">{post['category']} &middot;
      Published {post['date_display']}</p>
{post['body']}
      <hr>
      <p><em>This article describes Ethiopian law in general terms and is not legal
      advice. The outcome of any matter depends on its particular facts. For advice on
      your own situation, <a href="/contact/">contact the office</a>.</em></p>
      <div class="btn-row">
        <a class="btn btn--navy" href="tel:{C.PHONE}">{T.tx("Call the office", "ወደ ቢሮ ይደውሉ")}</a>
        <a class="btn btn--ghost" href="/{related['slug']}/">{related['title']}</a>
      </div>
    </div>
    <div>
{sidebar(post['related'])}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">More insights</span>
      <h2>Continue reading</h2>
      <hr class="rule">
    </div>
    <div class="grid grid--3">
{more}
    </div>
  </div>
</section>

{T.cta_band()}
"""
        h += T.footer()
        write(p_path, h)


def build_404():
    path = "/404.html"
    html = T.head("Page not found | " + C.FIRM_NAME,
                  "The page you were looking for could not be found.",
                  "/404.html", noindex=True)
    html += T.header("")
    html += f"""<section class="page-header">
  <div class="wrap">
    <h1>Page not found</h1>
    <p class="lead">The page you were looking for does not exist, or has moved.</p>
  </div>
</section>
<section class="section section--paper">
  <div class="wrap prose">
    <p>You may find what you need on one of these pages:</p>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/practice-areas/">Practice areas</a></li>
      <li><a href="/faq/">Frequently asked questions</a></li>
      <li><a href="/contact/">Contact the office</a></li>
    </ul>
    <div class="btn-row">
      <a class="btn btn--navy" href="/">Return home</a>
    </div>
  </div>
</section>
"""
    html += T.footer()
    write(path, html)


# ===========================================================================
# sitemap.xml / robots.txt
# ===========================================================================

def build_sitemap():
    urls = [("/", "1.0", "monthly"),
            ("/practice-areas/", "0.9", "monthly"),
            ("/about/", "0.8", "yearly"),
            ("/contact/", "0.8", "yearly"),
            ("/faq/", "0.8", "monthly"),
            ("/insights/", "0.7", "weekly")]
    urls += [(f'/{p["slug"]}/', "0.9", "monthly") for p in C.PRACTICE_AREAS]
    urls += [(f'/insights/{p["slug"]}/', "0.6", "yearly") for p in INSIGHTS]

    entries = "\n".join(f"""  <url>
    <loc>{C.SITE_URL}{u}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""" for u, prio, freq in urls)

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    WRITTEN.append(("sitemap.xml", "sitemap.xml"))

    robots = f"""User-agent: *
Allow: /

Sitemap: {C.SITE_URL}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)
    WRITTEN.append(("robots.txt", "robots.txt"))


# ===========================================================================

def main():
    build_home()
    build_about()
    build_practice_index()
    build_practice_pages()
    build_faq()
    build_contact()
    build_insights()
    build_404()
    build_sitemap()

    print(f"Built {len(WRITTEN)} files:")
    for site_path, rel in sorted(WRITTEN, key=lambda x: x[1]):
        print(f"  {rel}")


if __name__ == "__main__":
    main()
