"""Site-wide configuration.

Everything a non-developer is likely to need to change lives in this file.
After editing, re-run:  python3 tools/build.py
"""

# --- Domain -----------------------------------------------------------------
# Used for canonical URLs, Open Graph tags and sitemap.xml.
# Change this if you host on a different domain.
SITE_URL = "https://etlawoffice.com"

# --- Firm identity ----------------------------------------------------------
FIRM_NAME = "Elizabeth Tesfaye Law Office"
FIRM_SHORT = "ET Law Office"
ATTORNEY_NAME = "Elizabeth Tesfaye"
TAGLINE = "Attorneys & Legal Consultants"

# --- Contact ----------------------------------------------------------------
EMAIL = "elizabeth@etlawoffice.com"
PHONE = "+251912614966"           # E.164 format — used in tel: links and schema
PHONE_DISPLAY = "+251 91 261 4966"  # human-readable format shown on the page
WHATSAPP = "251912614966"           # digits only, no plus

STREET = "Summit Hewan Building, 2nd Floor, Office No. 210"
DISTRICT = "Summit"
CITY = "Addis Ababa"
COUNTRY = "Ethiopia"
COUNTRY_CODE = "ET"
FULL_ADDRESS = f"{STREET}, {CITY}, {COUNTRY}"

# Approximate coordinates for Summit, Addis Ababa.
# Refine these to your exact doorway: open Google Maps, right-click your
# building, and copy the latitude/longitude pair it shows.
LATITUDE = "9.0227"
LONGITUDE = "38.8331"

OPENING_HOURS = [
    ("Monday – Friday", "8:30 AM – 5:30 PM"),
    ("Saturday", "By appointment"),
    ("Sunday", "Closed"),
]
# Machine-readable version for schema.org (24-hour, Mo-Fr etc.)
OPENING_HOURS_SCHEMA = [
    {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
     "opens": "08:30", "closes": "17:30"},
]

RESPONSE_PROMISE = "We respond to every enquiry within one business day."

# --- Language ---------------------------------------------------------------
LANG = "en"
# Set to True once /am/ Amharic pages exist; this switches on hreflang tags
# and activates the language toggle in the header.
AMHARIC_READY = False

# --- Navigation -------------------------------------------------------------
NAV = [
    ("Home", "መነሻ", "/"),
    ("About", "ስለ እኛ", "/about/"),
    ("Practice Areas", "የስራ መስኮች", "/practice-areas/"),
    ("Insights", "ጽሑፎች", "/insights/"),
    ("FAQ", "ጥያቄዎች", "/faq/"),
    ("Contact", "ያግኙን", "/contact/"),
]

# --- Practice areas ---------------------------------------------------------
# Order here controls the order everywhere on the site.
PRACTICE_AREAS = [
    {
        "slug": "family-law-addis-ababa",
        "nav_title": "Family Law",
        "nav_title_am": "የቤተሰብ ህግ",
        "title": "Family Law",
        "title_am": "የቤተሰብ ህግ",
        "keyword": "family lawyer in Addis Ababa",
        "summary": "Marriage, divorce, child-related matters, maintenance, custody, "
                   "and other family disputes.",
        "icon": "family",
    },
    {
        "slug": "civil-litigation-ethiopia",
        "nav_title": "Civil Litigation",
        "nav_title_am": "የፍትሐ ብሔር ክስ",
        "title": "Civil Litigation",
        "title_am": "የፍትሐ ብሔር ክስ",
        "keyword": "civil litigation lawyer in Ethiopia",
        "summary": "Representation in civil disputes and proceedings before the "
                   "federal and regional courts.",
        "icon": "scales",
    },
    {
        "slug": "succession-inheritance-ethiopia",
        "nav_title": "Succession & Inheritance",
        "nav_title_am": "ውርስና ተከታይነት",
        "title": "Succession & Inheritance",
        "title_am": "ውርስና ተከታይነት",
        "keyword": "inheritance lawyer in Addis Ababa",
        "summary": "Legal advice and representation concerning inheritance and "
                   "succession matters.",
        "icon": "scroll",
    },
    {
        "slug": "business-corporate-law-addis-ababa",
        "nav_title": "Business & Corporate",
        "nav_title_am": "የንግድና የኮርፖሬት ህግ",
        "title": "Business & Corporate Law",
        "title_am": "የንግድና የኮርፖሬት ህግ",
        "keyword": "business lawyer in Addis Ababa",
        "summary": "Legal consultation and support for businesses and corporate "
                   "matters, from formation to contracts.",
        "icon": "building",
    },
    {
        "slug": "criminal-defense-lawyer-addis-ababa",
        "nav_title": "Criminal Law",
        "nav_title_am": "የወንጀል ህግ",
        "title": "Criminal Law",
        "title_am": "የወንጀል ህግ",
        "keyword": "criminal defense lawyer in Addis Ababa",
        "summary": "Legal representation and defense in criminal proceedings at "
                   "every stage.",
        "icon": "shield",
    },
    {
        "slug": "legal-consultation-ethiopia",
        "nav_title": "Legal Consultation",
        "nav_title_am": "የህግ ምክክር",
        "title": "Legal Consultation",
        "title_am": "የህግ ምክክር",
        "keyword": "legal consultation in Ethiopia",
        "summary": "Professional legal advice, legal opinions, document review, "
                   "and strategic guidance.",
        "icon": "consult",
    },
]
