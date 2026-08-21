# -*- coding: utf-8 -*-
"""Copy for the FAQ, About page and the Insights articles."""

# ---------------------------------------------------------------------------
# FAQ — grouped. Each group is (heading, [(question, answer_html), ...])
# ---------------------------------------------------------------------------
FAQ_GROUPS = [
("Working with the firm", [

("Is my first conversation with you confidential?",
 "<p>Yes. Everything you tell us is confidential from the first conversation, "
 "whether or not you go on to instruct us. That is a professional obligation "
 "rather than a courtesy. Please note, though, that confidentiality is not the "
 "same as an attorney–client relationship — the latter begins only once we have "
 "agreed in writing to act for you.</p>"),

("How much do you charge?",
 "<p>Fees depend on the nature and complexity of the matter. For consultations, "
 "document review and written legal opinions we can usually quote a fixed fee in "
 "advance, so you know the cost before the work begins. For litigation we discuss "
 "the fee basis at the outset and confirm it in writing. We would rather have a "
 "frank conversation about cost early than surprise a client later.</p>"),

("I live outside Ethiopia. Can you handle my matter without me travelling?",
 "<p>In most cases, yes. We act regularly for clients in the diaspora. Documents "
 "can be exchanged by email and consultations held by telephone or video call. "
 "Where steps must be taken here in Ethiopia — filing a case, obtaining a "
 "certificate of heir, transferring property — this can generally be done under a "
 "properly executed and authenticated power of attorney. We will tell you exactly "
 "what needs to be signed, and where it needs to be authenticated, before you "
 "incur any expense.</p>"),

("What should I bring to a first consultation?",
 "<p>Bring whatever documents relate to the matter: contracts, title deeds, "
 "correspondence, court papers you have received, a marriage or death certificate, "
 "business registration documents. If you are not sure whether something is "
 "relevant, bring it. A consultation with the documents in front of us is far more "
 "productive than one without them, and it lets us give you a concrete assessment "
 "rather than a general one.</p>"),
]),

("Family law", [

("How do I start a divorce in Ethiopia?",
 "<p>A divorce is commenced by presenting a petition to the competent court. The "
 "court has authority not only to dissolve the marriage but to determine the "
 "consequences: how common property is divided, arrangements for any children, and "
 "any maintenance payable. Which court is competent depends on where the parties "
 "reside and where the marriage was concluded. Family matters are governed "
 "principally by the Revised Family Code, Proclamation No. 213/2000, although "
 "several regional states have their own family codes that follow it closely.</p>"),

("How is property divided when a marriage ends?",
 "<p>The Revised Family Code distinguishes between each spouse's <em>personal</em> "
 "property and the <em>common</em> property of the marriage. Property acquired "
 "during the marriage is generally presumed to be common unless a spouse proves "
 "otherwise — for example, that it was owned before the marriage or received by "
 "inheritance or donation. That presumption is significant in practice, because it "
 "places the burden of proof on the spouse claiming an asset is personal. "
 "Documentary evidence of when and how an asset was acquired is usually what "
 "decides these disputes.</p>"),

("Who gets custody of the children?",
 "<p>The governing standard in every decision concerning a child is the best "
 "interests of the child. Courts consider the child's age and circumstances, the "
 "practical capacity of each parent to provide care and, depending on the child's "
 "maturity, the child's own wishes. It is worth understanding that custody and "
 "parental responsibility are distinct: the parent with whom a child does not live "
 "retains rights and duties toward that child.</p>"),

("Can a maintenance order be changed later?",
 "<p>Yes. Maintenance is a continuing obligation and can be revisited if "
 "circumstances change materially — a significant change in either parent's "
 "income, a change in the child's needs, or relocation. An order made at the time "
 "of divorce is not necessarily permanent. Equally, if an order is being ignored, "
 "it can be enforced.</p>"),

("Is a religious or customary marriage legally recognised?",
 "<p>Yes. The Revised Family Code recognises marriage concluded before an officer "
 "of civil status, marriage concluded according to religion, and marriage "
 "concluded according to custom. Once validly formed, all three produce the same "
 "legal effects between the spouses. In a dispute, however, the existence of a "
 "religious or customary marriage may need to be proved before any other claim can "
 "proceed — which is why we often begin such matters with an application "
 "concerning proof of the marriage itself.</p>"),
]),

("Inheritance and succession", [

("What happens to a person's property if they die without a will?",
 "<p>The estate passes according to the rules of intestate succession in the Civil "
 "Code of 1960. The Code distributes the estate among defined classes of relatives, "
 "beginning with the deceased's children and their descendants. Where there are no "
 "descendants, the estate passes to the parents and their descendants, and failing "
 "them to more remote ascendants and their lines. The order is prescribed by the "
 "Code; it is not a matter of the court's discretion.</p>"),

("How do I obtain a certificate of heir?",
 "<p>Application is made to the competent court, which is generally determined by "
 "the deceased's place of principal residence at the time of death. You will need "
 "the death certificate and evidence of your relationship to the deceased. The "
 "certificate matters practically as well as legally: banks, land administration "
 "offices, share registries and transport authorities will normally require it "
 "before releasing or transferring any asset of the estate.</p>"),

("What makes a will valid in Ethiopia?",
 "<p>The Civil Code recognises three forms: a public will, made and signed in the "
 "presence of the required witnesses; a holograph will, written entirely by the "
 "testator personally and clearly stating that it is intended as a will; and an "
 "oral will, which is permitted only in narrowly defined circumstances and is valid "
 "for a limited purpose and period. Formal requirements are strictly applied. A "
 "will that expresses the testator's wishes perfectly but fails a formal "
 "requirement can be set aside entirely, which is why having a will properly drawn "
 "is worth the modest cost.</p>"),

("The other heirs are holding estate property and will not account for it. What can I do?",
 "<p>This is one of the most common inheritance disputes we see. Before the estate "
 "can be partitioned it must be liquidated — the assets identified, the debts "
 "settled, and the remainder divided. Where an heir in possession will not account, "
 "the court can be asked to order the production of estate property and, where the "
 "heirs cannot agree on division, to order partition, including by sale and "
 "division of the proceeds. Acting promptly matters, because assets become harder "
 "to trace over time.</p>"),
]),

("Civil and criminal matters", [

("How long does a civil case take?",
 "<p>It varies considerably with the complexity of the matter, the court, and "
 "whether the other side contests every step. It is realistic to plan in terms of "
 "months rather than weeks, and a contested matter that goes through appeal can run "
 "considerably longer. We give clients a realistic estimate at the outset, and we "
 "will tell you when settling is likely to serve you better than litigating — "
 "recovering part of a claim now is often worth more than a judgment for the full "
 "amount years from now against a debtor who may no longer be able to pay.</p>"),

("Is there a time limit for bringing a claim?",
 "<p>Yes. Civil claims are subject to limitation periods, and the applicable period "
 "depends on the type of claim. Some are shorter than clients expect. If you think "
 "you may have a claim, take advice promptly — a claim that has expired cannot be "
 "revived, and finding this out before filing fees are paid is considerably better "
 "than finding it out after.</p>"),

("A family member has been arrested. What should I do?",
 "<p>Contact a lawyer immediately — what happens in the first days of a criminal "
 "matter often shapes everything that follows. Note where the person is being held "
 "and which police station is handling the file, and avoid discussing the substance "
 "of the allegation over the telephone. Under the Constitution an arrested person "
 "has the right to be informed of the reason for arrest, the right to legal "
 "representation, the right not to be compelled to incriminate themselves, and the "
 "right to be brought before a court within a short and defined period.</p>"),

("Is bail available?",
 "<p>Release pending trial is available for many but not all offences, and it is "
 "not automatic. The court considers the nature of the allegation, the risk of "
 "flight, the risk of interference with witnesses and the accused's ties to the "
 "community. A bail application should be prepared as an evidential exercise, with "
 "guarantors and supporting documentation, rather than treated as a formality. "
 "Where bail is refused, the refusal may be appealed.</p>"),
]),

("Business and corporate", [

("What type of company should I register?",
 "<p>It depends on how many owners there are, how much personal liability you are "
 "willing to carry, whether you intend to raise outside capital, and what your "
 "sector requires. The Commercial Code, Proclamation No. 1243/2021, introduced the "
 "One Person Private Limited Company, which is often the right answer for a sole "
 "proprietor who previously had to trade personally or recruit a nominal second "
 "shareholder. The Private Limited Company remains the standard form for small and "
 "medium businesses, and the Share Company is used for larger ventures. We advise "
 "on the choice before registration rather than after, because changing form later "
 "is more expensive than choosing correctly at the start.</p>"),

("Can a foreigner own a business in Ethiopia?",
 "<p>In many sectors, yes, but not all. The Investment Proclamation No. 1180/2020 "
 "and the regulations under it set out which areas are open to foreign investment, "
 "which are reserved for domestic investors, and which are open only on a joint "
 "venture basis, along with minimum capital requirements and the process for "
 "obtaining an investment permit. Because these rules are revised from time to "
 "time, the position should be confirmed for your specific activity before you "
 "commit funds to a structure.</p>"),

("Do I really need a shareholders' agreement?",
 "<p>If you have business partners, yes. The most common avoidable dispute we see "
 "involves two or three people who start a business on the strength of a "
 "friendship, register a company with a standard-form memorandum, and never agree "
 "in writing how profits are shared, how decisions are made, or what happens if one "
 "of them wants to leave. A short shareholders' agreement at the beginning is "
 "inexpensive. The litigation that follows its absence is not.</p>"),
]),
]


def all_faq_pairs():
    """Flatten to [(q, a)] for FAQPage schema."""
    return [qa for _, group in FAQ_GROUPS for qa in group]


# ---------------------------------------------------------------------------
# Insights / blog
# ---------------------------------------------------------------------------
INSIGHTS = [
{
  "slug": "common-property-ethiopian-divorce",
  "title": "Dividing property in an Ethiopian divorce: what counts as common property",
  "seo_title": "Dividing Property in an Ethiopian Divorce | ET Law Office",
  "description": "How the Revised Family Code divides property on divorce in "
                 "Ethiopia, and what evidence actually decides these disputes.",
  "date": "2026-05-14",
  "date_display": "14 May 2026",
  "category": "Family Law",
  "related": "family-law-addis-ababa",
  "body": """
<p>In most divorces we handle, the dissolution of the marriage is straightforward.
The dispute is about property — and specifically about a single question: which
assets belong to the marriage, and which belong to one spouse alone.</p>

<h2>Two categories, one presumption</h2>

<p>The Revised Family Code, Proclamation No. 213/2000, divides matrimonial assets
into the <strong>personal property</strong> of each spouse and the
<strong>common property</strong> of the marriage. Common property is divided
between the spouses on dissolution. Personal property is not.</p>

<p>The decisive feature of this scheme is the presumption that attaches to it:
property acquired during the marriage is generally treated as common
<em>unless the spouse claiming it is personal proves otherwise</em>. That single
allocation of the burden of proof determines the outcome of a great many cases.
It means the spouse asserting sole ownership must come forward with evidence, and
that a plausible account unsupported by documents will usually fail.</p>

<h2>What normally counts as personal property</h2>

<p>Broadly, property a spouse owned before the marriage remains personal, as does
property received during the marriage by inheritance or by donation made
personally to that spouse. Certain items of a strictly personal character are also
treated as personal.</p>

<p>The difficulty is rarely the principle. It is proof, and it is what has
happened to the asset since.</p>

<h2>Three situations that cause most of the argument</h2>

<h3>1. The asset that changed form</h3>

<p>A spouse owned a house before the marriage, sold it during the marriage, and
used the proceeds toward a different property purchased in joint names. Is the new
property personal, common, or partly each? Tracing an asset through a change of
form is evidentially demanding, and it requires the sale documents, the bank
records showing the movement of funds, and the purchase documents to line up. Where
that chain is intact the argument is strong. Where a spouse can only say
"I paid for it from my own money," it usually is not.</p>

<h3>2. The asset improved during the marriage</h3>

<p>A spouse brings a plot of land into the marriage, and during the marriage the
couple builds on it using their joint income. The land may remain personal while
the value contributed by the marriage is treated differently. Disputes of this kind
turn on construction receipts, permits, loan records and bank statements — the
documents nobody keeps, and which are very difficult to reconstruct years
afterwards.</p>

<h3>3. The business interest</h3>

<p>Where one spouse holds shares in a private limited company, the questions
multiply: when were the shares acquired, what was contributed for them, and what
has happened to the company's value since. Where the company was formed during the
marriage, the presumption applies to those shares as it does to any other asset.
Company records and the memorandum of association become central evidence.</p>

<div class="callout">
  <p><strong>The practical lesson:</strong> in property disputes on divorce, the
  side with the documents usually wins. If you own property you regard as
  personal, keep the acquisition records — title documents, the inheritance or
  donation paperwork, bank records showing the source of funds — organised and
  separate. This is worth doing while the marriage is healthy, not once it is
  in difficulty.</p>
</div>

<h2>Where a spouse is moving assets</h2>

<p>Occasionally a client discovers that a spouse has begun transferring property,
emptying accounts or restructuring a business in anticipation of divorce
proceedings. Where this is happening, speed matters. Protective measures may be
available to preserve assets pending the determination of the case, but they
require prompt action and evidence — not merely suspicion.</p>

<h2>If you are facing this</h2>

<p>The first consultation in a matrimonial property matter should be about
documents. Bring the title deeds, the bank statements, the business registration
papers and the marriage certificate, and we will tell you how the presumption is
likely to apply to each asset and what evidence you will need. That assessment is
usually more useful — and more sobering — than any general statement of the law.</p>
""",
},
{
  "slug": "valid-will-ethiopia-three-forms",
  "title": "Making a valid will in Ethiopia: the three forms, and where they go wrong",
  "seo_title": "How to Make a Valid Will in Ethiopia | Inheritance Lawyer",
  "description": "The Civil Code recognises three forms of will in Ethiopia. How "
                 "each works, and the formal defects that most often invalidate them.",
  "date": "2026-06-25",
  "date_display": "25 June 2026",
  "category": "Succession & Inheritance",
  "related": "succession-inheritance-ethiopia",
  "body": """
<p>A will is one of the few legal documents where getting the form wrong destroys
the substance completely. A document that records a person's intentions with
perfect clarity can be set aside in its entirety because of a defect that would be
trivial anywhere else. Ethiopian succession law is strict about this, and it is
worth understanding why before you write one.</p>

<h2>Why the formalities are so rigid</h2>

<p>A will takes effect only when the person who made it is no longer available to
explain it. There is no opportunity to ask the testator what they meant, or whether
the document truly represents their wishes. The Civil Code of 1960 compensates for
that by insisting on forms that are hard to fabricate and hard to alter. The
strictness is the protection.</p>

<h2>The three forms</h2>

<h3>The public will</h3>

<p>Made and signed in the presence of the required witnesses, with the document
read out so that its contents are confirmed in their presence. This is the most
robust form and the hardest to challenge successfully, because the circumstances of
its making are independently attested. For any estate of significance, or any
family situation where a dispute is foreseeable, this is the form we recommend.</p>

<h3>The holograph will</h3>

<p>Written entirely by the testator personally, and clearly expressing that the
document is intended to be a will. The requirement that it be written by the
testator's own hand throughout is not a technicality to be worked around — it is
the feature that makes the document verifiable. Two problems recur: documents
partly typed or partly written by someone else, and documents that read as a letter
or a note of intentions without stating clearly that they are meant to operate as a
will.</p>

<h3>The oral will</h3>

<p>Permitted only in narrowly defined circumstances — essentially where a person
is unable to make a will in another form — declared before witnesses, and valid
only for a limited purpose and a limited period. Oral wills are contested more
often than they succeed. They should be regarded as an emergency provision, not a
planning option.</p>

<h2>The defects we see most often</h2>

<ul>
  <li><strong>Mixed authorship in a holograph will.</strong> A relative helps by
      typing part of it, or writes in a detail the testator dictated. This can be
      fatal to the whole document.</li>
  <li><strong>Witness problems.</strong> Witnesses who do not meet the
      requirements, or who have an interest in the estate.</li>
  <li><strong>Unclear testamentary intention.</strong> A document that describes
      what the writer would like to happen without stating that it is a will.</li>
  <li><strong>Later alterations.</strong> Amendments added afterwards without
      observing the same formalities as the original.</li>
  <li><strong>Multiple undated documents.</strong> Where several versions exist and
      none can be reliably placed in sequence, establishing which one governs
      becomes a dispute in itself.</li>
  <li><strong>Disposing of property that is not the testator's to dispose of</strong>
      — most commonly, treating common matrimonial property as though it were
      personal.</li>
</ul>

<div class="callout">
  <p><strong>If you have already written a will:</strong> it is worth having it
  reviewed. A defect found now can be corrected by making a fresh will. A defect
  found after death cannot be corrected at all — it can only be litigated, at
  your family's expense.</p>
</div>

<h2>Challenging a will</h2>

<p>Where a will is being challenged, the formal requirements are the first place we
look, because a formal defect can dispose of the matter without any inquiry into
the testator's state of mind. Beyond form, a will may be attacked on the basis that
the testator lacked capacity when it was made, or that it was procured by undue
influence — both of which are considerably harder to prove and require evidence
about circumstances that may be years in the past.</p>

<h2>A note on estates spanning several countries</h2>

<p>Many Ethiopian families now hold assets in more than one country. A will drawn
in Ethiopia may not deal effectively with property abroad, and a foreign will may
not satisfy Ethiopian requirements for property here. If your assets are spread
across jurisdictions, take advice on whether one will or several is the better
arrangement — this is a question worth resolving deliberately rather than by
accident.</p>
""",
},
{
  "slug": "choosing-business-form-commercial-code-2021",
  "title": "Choosing a business form under Ethiopia's 2021 Commercial Code",
  "seo_title": "Choosing a Business Form in Ethiopia | 2021 Commercial Code",
  "description": "The Commercial Code of 2021 replaced a code from 1960 and introduced "
                 "the One Person PLC. A practical guide to choosing between business "
                 "forms in Ethiopia.",
  "date": "2026-07-30",
  "date_display": "30 July 2026",
  "category": "Business & Corporate",
  "related": "business-corporate-law-addis-ababa",
  "body": """
<p>For sixty years, Ethiopian businesses were organised under a Commercial Code
enacted in 1960. The <strong>Commercial Code, Proclamation No. 1243/2021</strong>
replaced it. If your company was formed under the old Code, or if you are working
from advice given before 2021, some of what you believe about your obligations may
no longer be accurate.</p>

<h2>The change that matters most to small businesses</h2>

<p>The 2021 Code introduced the <strong>One Person Private Limited Company</strong>
— a limited liability company with a single member.</p>

<p>Under the previous regime, a sole proprietor who wanted limited liability faced
an awkward choice: trade personally and accept unlimited exposure of personal
assets to business debts, or recruit a second shareholder who held a nominal
stake purely to satisfy the minimum. That second arrangement was extremely common
and caused a steady stream of disputes, because the nominal shareholder was, in
law, a real shareholder — with rights that could be asserted when relations
soured, or when they died and their heirs inherited the holding.</p>

<p>The One Person PLC removes the need for that arrangement. For a genuine sole
proprietor, it is now usually the correct form.</p>

<h2>Choosing between the forms</h2>

<h3>One Person Private Limited Company</h3>
<p>One owner, limited liability, relatively light governance. Suitable for
consultants, professionals, small traders and single-founder ventures. If you are
currently trading personally, this is the form to look at first.</p>

<h3>Private Limited Company (PLC)</h3>
<p>The standard form for small and medium businesses with more than one owner.
Limited liability, restrictions on the transfer of shares to outsiders, and
governance obligations that are manageable. Most Ethiopian businesses with
partners should be a PLC.</p>

<h3>Share Company</h3>
<p>For larger ventures, businesses intending to raise capital from a wider group
of investors, and regulated sectors that require it. Higher minimum capital,
a board, and materially heavier governance and reporting obligations. Do not
choose this form because it sounds more substantial — the compliance burden is
real and ongoing.</p>

<h3>Partnerships</h3>
<p>General, limited and joint venture forms remain available. They are appropriate
in specific circumstances, particularly for professional practices and defined
single-project ventures, but a general partnership exposes partners personally.
Choose it deliberately, not by default.</p>

<h3>Branch or representative office</h3>
<p>For a foreign company establishing a presence in Ethiopia. The choice between a
branch and a locally incorporated subsidiary has liability, tax and regulatory
consequences that should be examined before registration rather than after.</p>

<h2>The question people skip</h2>

<p>Choosing the form is the easy part. The part clients skip — and the source of
most of the corporate disputes we see — is agreeing in writing what happens
between the owners.</p>

<p>A standard-form memorandum of association does not tell you how profits will be
distributed, how a deadlock between two equal shareholders is broken, whether a
shareholder may compete with the company, what happens when a founder wants to
leave, or what happens to a shareholding on death. A short
<strong>shareholders' agreement</strong> settles all of this while everyone is
still on good terms and has no reason to argue about it. Drafted at formation, it
is inexpensive. Its absence, three years later, is not.</p>

<div class="callout">
  <p><strong>If your company was formed before 2021:</strong> it is worth a review.
  The governance provisions, directors' duties and the rules on business
  organisations changed with the new Code, and constitutive documents drafted
  against the 1960 Code may contain provisions that no longer reflect the law.</p>
</div>

<h2>Beyond registration</h2>

<p>Registration is one step among several. A business in Ethiopia will generally
also need a trade name registration, commercial registration, a business licence
matching its specific activity, tax registration and a TIN, and — once it engages
employees — payroll and pension registrations along with employment documentation
compliant with the Labour Proclamation No. 1156/2019. Regulated sectors carry
additional licensing. Foreign investors should confirm the position under the
Investment Proclamation No. 1180/2020 for their specific activity before
committing capital.</p>
""",
},
]
