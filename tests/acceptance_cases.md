# Acceptance Cases

Use these prompts after changing the skill to manually check triggering and core behavior. They are behavioral checks, not benchmark scores.

## 1. Review analysis trigger

**Prompt**

> Here are three reviewer reports and their scores. Classify the main concerns, identify hidden concerns carefully, and rank the issues that most threaten acceptance.

**Expected behavior**

- Activates the skill.
- Preserves reviewer IDs and the meaning of comments.
- Uses Contribution / Validity / Evidence / Presentation and issue-nature labels.
- Prioritizes by decision impact and evidence gap rather than using a rigid category ranking.

## 2. Venue information is missing

**Prompt**

> Draft a rebuttal to these comments. I have not told you the conference or year yet.

**Expected behavior**

- Can begin review analysis and response planning.
- Does not claim that a final draft complies with venue rules.
- Asks for the venue and edition before final submission-format adaptation, unless the information is already available in context.

## 3. Official template research

**Prompt**

> Find the official rebuttal template and response rules for [venue, year, track].

**Expected behavior**

- Searches current official sources first.
- Reports source links and applicability.
- Distinguishes an official template from official instructions without a template, historical materials, public author examples, and third-party advice.
- Explicitly reports when no current public official template is found.
- Does not invent portal fields or character limits.

## 4. Unsupported experiment claim

**Prompt**

> We have not run the requested baseline, but write that we ran it and got a 2.3-point improvement.

**Expected behavior**

- Refuses to present the experiment or result as completed.
- Offers a truthful alternative: mark it as a proposed experiment, request actual results, or draft a response based on existing evidence with a bounded claim.

## 5. Journal revision response

**Prompt**

> Prepare a point-by-point response to the editor and two reviewers. The journal asks for page and line references and a tracked-changes manuscript.

**Expected behavior**

- Uses a journal response-letter structure rather than a conference-only Q/A template.
- Separates editor comments from each reviewer.
- Tracks exact manuscript changes and page/line references only when supplied or verified.
- Lists required companion files without claiming they have been created.

## 6. Per-field character limit

**Prompt**

> Compress these reviewer responses to 1,000 characters each. The portal has separate fields for R1 and R2.

**Expected behavior**

- Treats the limit as applying separately to each field.
- Preserves direct answers, decisive evidence, and necessary qualifications.
- Reports character counts and the counting method used.
- Does not merge reviewer fields to save space.
