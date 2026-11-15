# L14 • From idea to product: WholesaleDesk prototype

**Author:** Kodirjon Khayitov · **Date:** 2026-11-15
**Reviewer:** `ihar_rubanovich@epam.com` 
**Brief:** the supplied wholesale supplier portal brief (`READY_PRODUCT_BRIEF_EN.txt`)
**Prototype:**
- **Link:** https://claude.ai/artifact/Lbrc6TwNVAwpCbcYb8VAfW. It is private until I share it from claude.ai.
- **Local copy:** `app/index.html`. Open it in any browser; it needs no installation.

**Built with:** Claude as the AI builder, as a single-page web app. Only fictional sample data is used.

## Who it is for
- **Buyer:** the purchasing person at a café or restaurant (sample: "Café Navruz LLC"). Today they order by phone or messenger in free text, such as "3 cases of oil, 25 kg rice…".
- **Sales manager at the wholesale supplier:** today they retype these messages into the system by hand, check case sizes and stock, and call back about anything unclear.

## What work it makes easier
- **The buyer** writes or dictates the order in their own words, as they already do. The portal turns that into a priced draft:
  - their own contract prices;
  - quantities rounded to full cases;
  - availability shown as a status only, never as a stock number.
- **The manager** gets a structured order next to the **original wording**. Unrecognised requests and stock problems are highlighted, so the manager decides instead of retyping.

## Value hypothesis to discuss with first users
> *If buyers can keep ordering in free text or voice, and the portal turns it into a priced, case-correct draft that they confirm in one step, then ordering takes less of the buyer's time, managers re-key far fewer orders, and fewer orders come back with case-size or price mistakes.*

**Questions for first users:**
1. **Buyers:** would you trust the draft enough to submit after a quick glance?
2. **Managers:** is "original text + prepared lines + flags" enough to approve without calling the buyer?
3. **Buyers:** is availability as a status (not a number) acceptable?

## The complete user journey (one scenario)
| # | Who | Step | Screen |
|---|---|---|---|
| 1 | Buyer | Types or dictates the order in free text (an example order is one click away). File upload (.txt/.csv) and "+ case" from the catalog also work. | `screens/01_buyer_input.png` |
| 2 | Buyer | **Prepare draft**: items, cases, quantities, contract prices, line totals and total. Rounding is explained ("Rounded from 40 to 42 bottles (full cases of 6)"). Out-of-stock items are marked. "Do you have olive oil?" is listed as *not recognised*, not invented. The delivery address is pre-selected from "Chilanzar branch". | `screens/02_buyer_draft.png` |
| 3 | Buyer | Adjusts by case if needed, selects the address and **submits**. The order appears in history as *Submitted*. | `screens/03_buyer_submitted_history.png` |
| 4 | Manager | Opens the incoming order. They see the **original buyer input**, which interpreter was used, the prepared lines with stock status, and the warning "2 point(s) need attention". They write a note (chickpeas out of stock, so offer lentils; olive oil is not in the assortment). | `screens/04_manager_review.png` |
| 5 | Manager | **Approve**, then **Send to fulfilment**. Status and history update ("Mark as shipped" comes next). | `screens/05_manager_fulfilment.png` |
| 6 | Buyer | Sees status *In fulfilment* and the manager's note in history. **Repeat order** refills the draft in one click. | `screens/06_buyer_history_repeat.png` |

## Model vs. ordinary code (as the brief requires)
- **The model only interprets.** On the published page, free text is sent to Claude (the page's `sample` capability). Claude returns `sku + amount + measure (case/unit/kg) + the buyer's words`, plus a list of unrecognised items. Voice input uses the page's `dictation` capability, which turns speech into text. The prompt forbids the model from calculating prices, and the buyer text is treated as untrusted data.
- **Code calculates everything with money in it:**
  - kg → packs;
  - rounding up to full cases;
  - contract price × quantity, and the order total;
  - availability labels;
  - order statuses.
- **If the model is not available** (for example in the local file), a simple rule-based parser is used. The page always says which interpreter produced the draft, and the manager sees this too.
- **Screens:** they were taken from the local file in headless Chrome, so they show the **rule-based parser** path. On the published link the AI model path is used after the viewer consents once.
- **Arithmetic check:** 36×21,500 + 8×96,000 + 42×4,200 + 12×27,900 + 10×17,400 = **2,227,200 UZS**. This matches the total on screen.

## Known limits of this prototype
- **Single-browser state.** Orders are kept in memory and the browser's local storage, and buyer and manager are two tabs of one page, not two accounts.
- **No real stock, ERP or delivery integration.** The status flow is manual.
- **Audio files are not supported.** The supplied `synthetic_order_en.wav` cannot be uploaded; only live dictation works. Interpreting an audio file would be the next feature, for example with Google AI Studio, which the lesson shows.
- **Repeat order copies an out-of-stock item again.** A real version should re-check availability and suggest the substitute the manager proposed.

## Conclusion: direction for development
The strongest part to validate is **"keep my habit, remove re-typing"**: free text or voice in, a priced case-correct draft out, and the original wording kept for the manager. Next steps, in order:
1. **Real accounts and shared storage**, so buyer and manager work on different devices.
2. **Substitutes for out-of-stock items** proposed in the draft itself, using manager rules.
3. **Audio file upload and messenger intake** (Telegram), because that is where buyers already write.
4. **Measure the hypothesis:**
   - share of drafts submitted without edits;
   - manager time per order;
   - number of orders corrected after submission.

## Files
`app/index.html` (prototype) · `screens/` (6 screens of the journey) · `READY_PRODUCT_BRIEF_EN.txt` (original brief) · `README.md`
