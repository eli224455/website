# Before you publish

A short list of things the site cannot know about you, plus the launch steps.

---

## 1. Fill in the highlighted placeholders

Four facts on the **About** page are marked with a yellow highlight. They appear
on the live page until you replace them, so they're hard to miss. Open
`tools/build.py`, search for `todo(`, and replace the text inside each one — then
run `python3 tools/build.py`.

| Placeholder | What to put |
|---|---|
| `[courts before which you are licensed…]` | e.g. "Federal Courts of Ethiopia", or whichever courts your licence covers |
| `[LL.B. / LL.M., institution, year]` | Your degree(s), the university, and the year |
| `[number]` years of experience | Years in practice |
| `[languages…]` | The languages you advise in |

Consider also adding, if you're comfortable doing so:

- Your **licence or bar registration number** — a strong trust signal on a law
  firm site, and clients do look for it
- A **professional photograph** — the About page has a clear place for one, and
  a real photo materially increases enquiries on solo-practice sites

---

## 2. Confirm the details that are already filled in

These were taken from what you provided. Please check each one:

- **Firm name:** Elizabeth Tesfaye Law Office
- **Address:** Summit Hewan Building, 2nd Floor, Office No. 210, Addis Ababa,
  Ethiopia
- **Phone:** +251 91 261 4966
- **Email:** elizabeth@etlawoffice.com
- **Domain:** etlawoffice.com — change `SITE_URL` in `tools/config.py` if this
  isn't right
- **Office hours:** Monday–Friday 8:30 AM – 5:30 PM, Saturday by appointment,
  Sunday closed — edit `OPENING_HOURS` and `OPENING_HOURS_SCHEMA` in
  `tools/config.py` if these differ

---

## 3. Have the legal content reviewed

**This matters more than anything else on this list.**

The practice-area pages, the FAQ and the three articles describe Ethiopian law in
general terms for a lay reader. They cite the Revised Family Code
(Proc. No. 213/2000), the Civil Code (1960), the Civil Procedure Code (1965), the
Commercial Code (Proc. No. 1243/2021), the Criminal Code (Proc. No. 414/2004),
the Criminal Procedure Code (1961), the Federal Courts Proclamation
(No. 1234/2021), the Labour Proclamation (No. 1156/2019), the Investment
Proclamation (No. 1180/2020) and the Arbitration and Conciliation Working
Procedure Proclamation (No. 1237/2021).

Those citations were checked against public sources, and the descriptions were
deliberately kept general rather than procedural. But you are the practitioner —
**read every page and correct anything that doesn't match current practice**
before this goes on the public internet under your name. Legislation is amended,
procedure varies between courts, and the content should reflect how these matters
actually run in Addis Ababa.

The disclaimer in the footer of every page states that the site is general
information, not legal advice, and that no attorney–client relationship arises
from visiting or sending an enquiry. Confirm it's worded the way you want it.

---

## 4. Make the contact form deliver

Out of the box, the form opens the visitor's email program. That loses some
enquiries. See "Making the contact form actually send email" in `README.md` —
Formspree takes about five minutes to set up and is free at low volume.

**Then send yourself a test enquiry and confirm it arrives.**

---

## 5. Launch steps

- [ ] Placeholders filled in and the site rebuilt
- [ ] Every page read and legally reviewed
- [ ] Contact form tested end to end
- [ ] Phone link tested from a mobile phone
- [ ] Deployed to Cloudflare Pages or GitHub Pages
- [ ] Domain connected, HTTPS confirmed working
- [ ] Exact map coordinates set in `tools/config.py`
- [ ] Google Business Profile created and verified
- [ ] Sitemap submitted in Google Search Console
- [ ] Firm listed in Ethiopian legal directories with identical name/address/phone

---

## 6. Optional, worth considering

- **Client testimonials** — a commented-out section is ready on the home page.
  Use real quotes from clients who've given written permission.
- **Photographs** — of you and of the office. The design is built to look good
  without photography, but real images of a real office build trust.
- **Amharic version** — the site is structured for it; see `README.md`.
- **Privacy notice** — if you connect an analytics tool or a form service that
  stores submissions, add a short privacy page explaining what's collected. The
  site currently sets no cookies and loads no trackers.
