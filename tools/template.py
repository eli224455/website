"""HTML shell: <head>, header, footer, CTA band, JSON-LD."""

import json
import config as C

# --- Monogram: serif E + Ionic column T (matches official lockup) ---
MARK_SVG = """<svg viewBox="0 0 200 160" aria-hidden="true" focusable="false">
<g fill="#1B3654"><path d="M24 16h16v128H24z"/><path d="M16 16h96v18H16z"/><path d="M24 71h72v16H24z"/><path d="M16 126h96v18H16z"/><path d="M16 12h24v10H16z"/><path d="M16 138h24v10H16z"/></g>
<g fill="#C4A35A"><rect x="102" y="58" width="86" height="8"/><path d="M110 66c-12 0-18 7-18 16 0 8 7 13 14 9l3-7V66h78v18l3 7c7 4 14-1 14-9 0-9-6-16-18-16H110z"/><rect x="128" y="86" width="5.2" height="50"/><rect x="136.4" y="86" width="5.2" height="50"/><rect x="144.8" y="86" width="5.2" height="50"/><rect x="153.2" y="86" width="5.2" height="50"/><rect x="124" y="136" width="38" height="7"/><rect x="116" y="143" width="54" height="9"/></g>
</svg>"""

MARK_SVG_LIGHT = MARK_SVG.replace('fill="#1B3654"', 'fill="#F7F3EA"')


def tx(en, am, block=False):
    """Bilingual phrase. JS toggles html[lang] to show one language."""
    cls = "i18n-block" if block else ""
    return (f'<span class="i18n-en {cls}">{en}</span>'
            f'<span class="i18n-am {cls}" lang="am">{am}</span>')

ICONS = {
    "family": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z"/><path d="M16.5 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z"/><path d="M3 21v-4a5 5 0 0 1 5-5 5 5 0 0 1 3.2 1.2"/><path d="M13 21v-3.5a4 4 0 0 1 4-4 4 4 0 0 1 4 4V21"/><path d="M12.2 21H3"/></svg>',
    "scales": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"/><path d="M7 21h10"/><path d="M4 6h16"/><path d="m7 6-3.5 7a3.5 3.5 0 0 0 7 0Z"/><path d="m17 6-3.5 7a3.5 3.5 0 0 0 7 0Z"/></svg>',
    "scroll": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h11a2 2 0 0 1 2 2v13a3 3 0 0 0 3 3H8a3 3 0 0 1-3-3Z"/><path d="M5 3a2 2 0 0 0-2 2v2h2"/><path d="M9 8h5"/><path d="M9 12h5"/><path d="M9 16h3"/></svg>',
    "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V6a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v15"/><path d="M14 10h5a1 1 0 0 1 1 1v10"/><path d="M2 21h20"/><path d="M7 9h3"/><path d="M7 13h3"/><path d="M7 17h3"/><path d="M17 14h1"/><path d="M17 17h1"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5.5l-8-3-8 3V12c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
    "consult": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H8l-4 4V5a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2Z"/><path d="M9.5 9a2.5 2.5 0 1 1 3.3 2.4c-.5.2-.8.6-.8 1.1v.3"/><path d="M12 15.5h.01"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.05 4.91A9.82 9.82 0 0 0 12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.87 9.87 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.91-7.02Zm-7.01 15.24h-.01a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.83c0 4.55-3.7 8.25-8.24 8.25Zm4.52-6.16c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.39-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.35-.76-1.84-.2-.48-.4-.42-.56-.42h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74 1.75.76 2.11.67 2.49.63.38-.04 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.23-.17-.48-.29Z"/></svg>',
}


def connect_buttons(gold=True):
    primary = "btn--gold" if gold else "btn--navy"
    email_cls = "btn--light" if gold else "btn--ghost"
    return f"""<div class="btn-row connect-row">
      <a class="btn {primary}" href="tel:{C.PHONE}">{ICONS['phone']}<span>{tx("Call " + C.PHONE_DISPLAY, "ይደውሉ " + C.PHONE_DISPLAY)}</span></a>
      <a class="btn btn--whatsapp" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener">{ICONS['whatsapp']}<span>WhatsApp</span></a>
      <a class="btn {email_cls}" href="mailto:{C.EMAIL}">{ICONS['mail']}<span>{C.EMAIL}</span></a>
    </div>"""


def head(title, description, path, og_type="website", extra_schema=None,
         breadcrumbs=None, noindex=False):
    """Build the <head> block for one page."""
    canonical = C.SITE_URL + path
    depth_prefix = ""  # all URLs are absolute from root, so no depth juggling

    schema_blocks = [legal_service_schema()]
    if breadcrumbs:
        schema_blocks.append(breadcrumb_schema(breadcrumbs))
    if extra_schema:
        if isinstance(extra_schema, list):
            schema_blocks.extend(extra_schema)
        else:
            schema_blocks.append(extra_schema)

    ld = "\n".join(
        '<script type="application/ld+json">%s</script>'
        % json.dumps(block, ensure_ascii=False, separators=(",", ":"))
        for block in schema_blocks
    )

    hreflang = ""
    if C.AMHARIC_READY:
        hreflang = (
            f'<link rel="alternate" hreflang="en" href="{canonical}">\n'
            f'<link rel="alternate" hreflang="am" href="{C.SITE_URL}/am{path}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{canonical}">'
        )

    robots = '<meta name="robots" content="noindex,follow">' if noindex else \
             '<meta name="robots" content="index,follow,max-image-preview:large">'

    return f"""<!DOCTYPE html>
<html lang="{C.LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{canonical}">
{hreflang}
<meta name="author" content="{C.FIRM_NAME}">
<meta name="geo.region" content="{C.COUNTRY_CODE}-AA">
<meta name="geo.placename" content="{C.CITY}">
<meta name="geo.position" content="{C.LATITUDE};{C.LONGITUDE}">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{C.FIRM_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_ET">
<meta property="og:image" content="{C.SITE_URL}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{C.FIRM_NAME} — {C.CITY}, {C.COUNTRY}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{C.SITE_URL}/assets/img/og-image.png">

<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#1B3654">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&amp;family=Inter:wght@300;400;500;600&amp;family=Noto+Sans+Ethiopic:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&amp;family=Inter:wght@300;400;500;600&amp;family=Noto+Sans+Ethiopic:wght@400;500;600&amp;display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&amp;family=Inter:wght@300;400;500;600&amp;family=Noto+Sans+Ethiopic:wght@400;500;600&amp;display=swap"></noscript>
<link rel="stylesheet" href="/assets/css/style.css">
{ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""


def header(current_path):
    """Sticky site header with logo, bilingual nav and direct-call CTA."""
    links = []
    for en, am, href in C.NAV:
        aria = ' aria-current="page"' if href == current_path else ""
        links.append(f'<a href="{href}"{aria}>{tx(en, am)}</a>')
    nav_links = "\n      ".join(links)

    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="{C.FIRM_NAME} — home">
      <img class="brand-lockup" src="/assets/img/logo.png" width="640" height="640" alt="Elizabeth Tesfaye Law Office — Addis Ababa, Ethiopia">
    </a>

    <nav class="nav" id="primary-nav" aria-label="Primary">
      {nav_links}
      <a class="btn btn--gold" href="tel:{C.PHONE}">{tx("Call the Office", "ወደ ቢሮ ይደውሉ")}</a>
    </nav>

    <div class="header-actions">
      <div class="lang-switch" role="group" aria-label="Language">
        <button type="button" class="lang-toggle is-active" data-lang="en" lang="en">EN</button>
        <button type="button" class="lang-toggle" data-lang="am" lang="am">አማ</button>
      </div>
      <a class="btn btn--gold header-cta" href="tel:{C.PHONE}">{tx("Call Now", "አሁን ይደውሉ")}</a>
      <button class="nav-toggle" type="button" aria-expanded="false"
              aria-controls="primary-nav" aria-label="Open navigation menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<main id="main">
"""


def breadcrumb_html(trail):
    """trail = [(label, href_or_None), ...] — last item is the current page."""
    items = []
    for label, href in trail:
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
    return ('<nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
            + "".join(items) + "</ol></nav>")


def page_header(title, lead, trail=None):
    crumbs = breadcrumb_html(trail) if trail else ""
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="page-header">
  <div class="wrap">
    {crumbs}
    <h1>{title}</h1>
    {lead_html}
  </div>
</section>
"""


def cta_band(heading=None, body=None, heading_am=None, body_am=None):
    heading = heading or "Speak with the office directly"
    heading_am = heading_am or "ከቢሮው ጋር በቀጥታ ይነጋገሩ"
    body = body or ("No forms. Call, WhatsApp or email — every conversation is confidential.")
    body_am = body_am or "ቅጽ አይሞሉም። ይደውሉ፣ WhatsApp ይላኩ ወይም ኢሜይል — እያንዳንዱ ውይይት በሚስጥር ይያዛል።"
    return f"""<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow">{tx("Private consultation", "የግል ምክክር")}</span>
    <h2>{tx(heading, heading_am, block=True)}</h2>
    <p>{tx(body, body_am, block=True)}</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--gold" href="tel:{C.PHONE}">{ICONS['phone']}<span>{tx("Call " + C.PHONE_DISPLAY, "ይደውሉ " + C.PHONE_DISPLAY)}</span></a>
      <a class="btn btn--whatsapp" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener">{ICONS['whatsapp']}<span>WhatsApp</span></a>
      <a class="btn btn--light" href="mailto:{C.EMAIL}">{C.EMAIL}</a>
    </div>
  </div>
</section>
"""


def footer():
    practice_links = "\n        ".join(
        f'<li><a href="/{p["slug"]}/">{tx(p["nav_title"], p.get("nav_title_am", p["nav_title"]))}</a></li>'
        for p in C.PRACTICE_AREAS
    )
    hours = "\n        ".join(
        f"<li><strong>{d}</strong><br>{h}</li>" for d, h in C.OPENING_HOURS
    )
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img class="footer-logo" src="/assets/img/logo.png" width="640" height="640" alt="Elizabeth Tesfaye Law Office">
        <p>{tx("Private practice in Addis Ababa. Former public prosecutor in criminal and civil matters. 13 years advising families, businesses and individuals — in English and Amharic.",
              "በአዲስ አበባ የግል ልምምድ። በወንጀል እና በፍትሐ ብሔር ጉዳዮች የቀድሞ ዐቃቤ ሕግ። 13 ዓመት ለቤተሰቦች፣ ለንግድ ድርጅቶች እና ለግለሰቦች — በእንግሊዝኛ እና በአማርኛ።", True)}</p>
      </div>

      <nav aria-label="Practice areas">
        <h4>{tx("Practice Areas", "የስራ መስኮች")}</h4>
        <ul>
        {practice_links}
        </ul>
      </nav>

      <nav aria-label="Footer">
        <h4>{tx("Firm", "ቢሮ")}</h4>
        <ul>
          <li><a href="/about/">{tx("About the Firm", "ስለ ቢሮው")}</a></li>
          <li><a href="/practice-areas/">{tx("Practice Areas", "የስራ መስኮች")}</a></li>
          <li><a href="/insights/">{tx("Legal Insights", "የህግ ጽሑፎች")}</a></li>
          <li><a href="/faq/">{tx("Frequently Asked Questions", "ተደጋጋሚ ጥያቄዎች")}</a></li>
          <li><a href="/contact/">{tx("Contact", "ያግኙን")}</a></li>
        </ul>
      </nav>

      <div class="footer-nap">
        <h4>{tx("Contact", "ያግኙን")}</h4>
        <address>
          <strong style="color:#fff">{C.FIRM_NAME}</strong><br>
          {C.STREET}<br>
          {C.CITY}, {C.COUNTRY}<br><br>
          <a href="tel:{C.PHONE}">{C.PHONE_DISPLAY}</a><br>
          <a href="mailto:{C.EMAIL}">{C.EMAIL}</a>
        </address>
        <h4 style="margin-top:1.75rem">{tx("Office Hours", "የቢሮ ሰዓት")}</h4>
        <ul>
        {hours}
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {C.FIRM_NAME}. All rights reserved.</span>
      <span>{C.CITY}, {C.COUNTRY}</span>
    </div>
  </div>

  <div class="disclaimer">
    <div class="wrap">
      <p class="i18n-en" style="margin:0"><strong style="color:#9FB0C4">Disclaimer:</strong>
      The content of this website is provided for general information only and does
      not constitute legal advice. Ethiopian law changes, and the outcome of any
      matter depends on its particular facts. Visiting this website, or contacting
      the office, does not create an attorney–client relationship between
      you and {C.FIRM_NAME}. An attorney–client relationship arises only once we
      have agreed to act for you in writing. Please do not send confidential
      information until that agreement is in place.</p>
      <p class="i18n-am" lang="am" style="margin:0"><strong style="color:#9FB0C4">ማሳሰቢያ፦</strong>
      የዚህ ድህረ ገጽ ይዘት ለአጠቃላይ መረጃ ብቻ ነው፣ የህግ ምክር አይደለም። የኢትዮጵያ ህግ ይለወጣል፣ የማንኛውም ጉዳይ ውጤት ደግሞ በእውነታዎቹ ላይ የተመሰረተ ነው። ይህን ድህረ ገጽ መጎብኘት ወይም ቢሮውን ማግኘት በእርስዎ እና በ{C.FIRM_NAME} መካከል የጠበቃ-ደንበኛ ግንኙነት አይፈጥርም። ግንኙነቱ በጽሁፍ ከተስማማን በኋላ ብቻ ይጀምራል።</p>
    </div>
  </div>
</footer>
<a class="float-bar" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp">
  {ICONS['whatsapp']}
  <span>{tx("Message on WhatsApp", "በWhatsApp ይጻፉ")}</span>
</a>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


# --- Structured data --------------------------------------------------------

def legal_service_schema():
    return {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": C.SITE_URL + "/#organization",
        "name": C.FIRM_NAME,
        "description": ("Law office in Addis Ababa, Ethiopia advising on family law, "
                        "civil litigation, succession and inheritance, business and "
                        "corporate law, criminal defense and legal consultation."),
        "url": C.SITE_URL + "/",
        "logo": C.SITE_URL + "/assets/img/logo.png",
        "image": C.SITE_URL + "/assets/img/og-image.png",
        "email": C.EMAIL,
        "telephone": C.PHONE,
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": C.STREET,
            "addressLocality": C.CITY,
            "addressRegion": C.CITY,
            "addressCountry": C.COUNTRY_CODE,
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": C.LATITUDE,
            "longitude": C.LONGITUDE,
        },
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": spec["days"],
                "opens": spec["opens"],
                "closes": spec["closes"],
            }
            for spec in C.OPENING_HOURS_SCHEMA
        ],
        "areaServed": [
            {"@type": "City", "name": C.CITY},
            {"@type": "Country", "name": C.COUNTRY},
        ],
        "availableLanguage": [
            {"@type": "Language", "name": "English"},
            {"@type": "Language", "name": "Amharic"},
        ],
        "knowsAbout": [p["title"] for p in C.PRACTICE_AREAS],
        "founder": {
            "@type": "Person",
            "@id": C.SITE_URL + "/about/#attorney",
            "name": C.ATTORNEY_NAME,
            "jobTitle": "Attorney-at-Law, former public prosecutor",
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Legal services",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": p["title"],
                        "description": p["summary"],
                        "url": f'{C.SITE_URL}/{p["slug"]}/',
                    },
                }
                for p in C.PRACTICE_AREAS
            ],
        },
    }


def attorney_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Attorney",
        "@id": C.SITE_URL + "/about/#attorney",
        "name": C.ATTORNEY_NAME,
        "jobTitle": "Attorney-at-Law and Legal Consultant. Former public prosecutor in criminal and civil matters. 13 years in Ethiopian law.",
        "url": C.SITE_URL + "/about/",
        "email": C.EMAIL,
        "telephone": C.PHONE,
        "worksFor": {"@id": C.SITE_URL + "/#organization"},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": C.STREET,
            "addressLocality": C.CITY,
            "addressCountry": C.COUNTRY_CODE,
        },
        "knowsLanguage": ["English", "Amharic"],
        "knowsAbout": [p["title"] for p in C.PRACTICE_AREAS],
    }


def breadcrumb_schema(trail):
    items = []
    for i, (label, href) in enumerate(trail, start=1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = C.SITE_URL + href
        items.append(entry)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def faq_schema(qa_pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
            }
            for q, a in qa_pairs
        ],
    }


def service_schema(area):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": area["title"],
        "description": area["summary"],
        "url": f'{C.SITE_URL}/{area["slug"]}/',
        "serviceType": area["title"],
        "provider": {"@id": C.SITE_URL + "/#organization"},
        "areaServed": [
            {"@type": "City", "name": C.CITY},
            {"@type": "Country", "name": C.COUNTRY},
        ],
    }


def article_schema(post):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["description"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "url": f'{C.SITE_URL}/insights/{post["slug"]}/',
        "mainEntityOfPage": f'{C.SITE_URL}/insights/{post["slug"]}/',
        "author": {"@id": C.SITE_URL + "/about/#attorney"},
        "publisher": {"@id": C.SITE_URL + "/#organization"},
        "image": C.SITE_URL + "/assets/img/og-image.png",
        "inLanguage": "en",
    }


import re

def strip_tags(html):
    """Plain-text version of an answer, for JSON-LD."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = text.replace("&amp;", "&").replace("&nbsp;", " ")
    text = re.sub(r"&[a-z]+;", "", text)
    return re.sub(r"\s+", " ", text).strip()
