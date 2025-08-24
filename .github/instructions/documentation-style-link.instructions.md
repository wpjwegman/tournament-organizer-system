# Documentation, Style & Link Management Lessons

---
tags:
  - documentation
  - writing
  - style
  - formatting
  - markdown
  - links
---

## Purpose
This document provides clear, concise, and complete instructions for writing, formatting, and linking documentation. It is designed for both human and AI authors to ensure consistency and quality across all project documentation.

## Scope
Comprehensive guidelines for writing clear, professional, consistently formatted, and well-linked documentation for the project.

## MANDATORY: Titles and Tags

- Visible H1 titles: Every Markdown page MUST begin its content with a visible H1 heading (first body line after front matter): `# Page Title`.
  - Do NOT use `title:` in front matter. If present, remove it to avoid duplicate titles.
  - Only one H1 per page (MD025). Subsequent sections start at H2 (`##`).
- **Entity type indicators**: For data model entities, MUST include the entity type in the title:
  - **Template Entity**: `# Entity Name (Template Entity)` - for reusable templates that define structure for creating instances
  - **Entity**: `# Entity Name (Entity)` - for concrete entities with independent identity and lifecycle  
  - **Value Object**: `# Entity Name (Value Object)` - for objects embedded in other entities without independent identity
  - **Domain Overview**: `# Domain Name` - for domain README files (no entity type indicator)
- Required tags: Every page MUST include a `tags:` list in YAML front matter with relevant, specific tags (2–6 recommended).
  - **MANDATORY**: Use YAML front matter block format with `tags:` as an array, NOT inline comma-separated format
  - Prefer domain- and concept-specific tags (e.g., `team`, `roster`, `tournament`, `ranking`, `finance`, `payment`, `identity`, `profile`, `venue`, `schedule`).
  - Use lowercase, hyphenated tokens when multi-word (e.g., `first-aid`, `match-system`).

**REQUIRED Template (copy/paste exactly):**

```yaml
---
tags:
  - domain
  - subdomain
  - concept
---
```

**IMPORTANT**: Never use the old inline format like `tag: documentation, writing, style`. Always use the YAML array format shown above.

Template complete example:

```markdown
---
tags:
  - domain
  - subdomain
  - concept
---

# Entity Name (Template Entity)

Intro paragraph…
```

**Entity Type Examples:**
- Template Entity: `# Protocol (Template Entity)` - defines reusable first aid protocol templates
- Entity: `# Unit (Entity)` - concrete measurement unit with independent identity  
- Value Object: `# Measurement (Value Object)` - embedded quantitative value without independent identity
- Domain: `# First Aid Domain` - domain overview page (no entity type indicator)

Notes
- **CRITICAL**: The Tags plugin requires YAML front matter format. Always use `tags:` as an array in YAML front matter block, never inline comma-separated format.
- Tags power search and taxonomy pages through the MkDocs Material theme.
- Lint rules enforce a single H1 (MD025) and first-line H1 (MD041) when configured for visible titles.
- When converting existing pages: remove `title:` from front matter, add `# Page Title` as the first body line, convert any inline `tag:` to YAML `tags:` array format.

## Key Lessons

### Writing & Structure
- For all template entities, always reference standard attributes from the Base Entity (e.g., "This template entity includes standard attributes from the [Base Entity](../foundation/base_entity.md)") instead of listing them explicitly. This ensures documentation remains maintainable and up to date if the Base Entity changes.
- Use direct, active voice and concise sentences.
- Organize content with clear headings, lists, and sections.
- Adapt writing for the intended audience:
  - For technical readers, use precise terminology and provide detailed explanations (without code blocks).
  - For non-technical readers, avoid jargon, explain concepts simply, and use analogies or visuals where helpful.
- Begin each domain file with a brief summary or introduction.
- Use the following section order in domain files: Overview, Purpose, Structure, Example, See Also.
- In the Structure section, always reference the Base Entity for standard attributes (do not list them explicitly). This ensures maintainability if the Base Entity changes. Always include an attributes table for template entities to provide clarity and quick reference for users.
- Remove sections for Relationships, Key Concepts, and References unless absolutely necessary. Prioritize clarity and relevance. Ensure documentation supports both human and automated validation, emphasizing transparency, consistency, and adaptability for future use cases.
Add an Example section after Structure to illustrate domain concepts with real-world scenarios or visuals (e.g., mermaid diagrams). Follow these best practices:
  - Always provide contextual explanations for each example, immediately following the example.
  - MANDATORY: Ensure every example represents ALL attributes from the Structure section, both visually (in the diagram) and explicitly in the explanatory paragraph.
  - If a single diagram would become unreadable, use two small diagrams (Example A/B) to cover all attributes.
  - Do not add “Also shows” bullet lists. Prefer additional small diagrams or a second example to cover remaining attributes.
  - Use descriptive, domain-relevant values in examples (avoid technical identifiers or placeholders).
  - Provide multiple examples for different use cases or variations when possible.
  - Use readable diagram formats (e.g., `A --> B[Attribute: Value]`) for mermaid diagrams to improve comprehension.
  - Avoid repetitive or superficial explanations; provide expert-level context that clarifies the purpose, logic, and practical application of each template entity.
  - Avoid confusing or overly abstract examples unless specifically required for the domain.
  - Prefer Mermaid flowcharts using `graph TD` for clarity and left-to-right/top-down readability.
  - Immediately follow each diagram with a concise paragraph that explains the structure and its practical impact (why it matters for organizers, navigation, eligibility, reporting, etc.).

  ### Modeling Rules (Data, Embedding, Terminology)
  - Embedding within the same domain (document database model):
    - When one model references another model in the SAME domain (e.g., `discipline/*` → `discipline/stage/*`), embed the referenced model instead of using a UUID. Reflect this in docs:
      - Use types like `Stage Format`, `Match System`, `List[Stage Phase]`, `List[Stage Tiebreaker]`, `List[Match Unit]`, etc., not `UUID`/`List[UUID]`.
      - Examples must illustrate embedded/nested data, not identifiers.
    - If the referenced model is in a DIFFERENT domain (e.g., `discipline/*` → `ranking/*` or `classification/measurement/*`), keep it as a reference by UUID.
  - Terminology: Teams vs. Participants
    - Use "team"/"teams" for competitive units throughout docs. A single-player entry is a "team" of one.
    - Avoid using "player(s)" to describe competitors at the tournament/stage level; reserve "player" for team roster contexts when necessary.
    - Reserve "participant" for the broad set of people/entities involved in a tournament (teams, officials, staff, etc.), not just competitors.

Example diagram style (Graph TD) — intent and usage:
- Use `graph TD` flowcharts to show hierarchies and classifications in a way that mirrors how users think about grouping.
- Label nodes with meaningful, domain-focused names (e.g., "Activity: Basketball", "Domain: Sports").
- Show classification edges with descriptive text when helpful (e.g., `-. classified in .->`).
- For categories, show parent→child relationships to illustrate how top-level categories (e.g., Sports) contain subcategories (e.g., Darts → 501, 301) and why that helps grouping, scheduling, reporting, and eligibility.
- For geography, show continent→country→region→city→venue to demonstrate how location hierarchies enable filtering and selection during planning and reporting.
- Maintain a clear, professional, and neutral tone throughout. Focus on actionable guidance and practical examples. Avoid unnecessary jargon or informality.

### Formatting & Accessibility
- Use consistent Markdown syntax for headings and lists.
- Avoid code blocks for code samples in documentation. Use diagrams instead. Exception: Mermaid fenced blocks are encouraged for diagrams (prefer `graph TD`).
- Apply project-specific style rules. Most important MkDocs recommendations:
  - Use clear, descriptive headings and organize content hierarchically.
  - Keep navigation simple and intuitive.
  - Ensure all pages have a title and metadata for searchability.
- Use whitespace and line breaks to separate sections and improve readability.
- Follow style and formatting standards for consistency.
- Review for common Vale warnings (passive voice, wordiness, weasel words).
- Prefer short, clear sentences over long, complex ones.
- Follow accessibility best practices:
  - Add alt text to images.
  - Use clear, descriptive link text.
  - Ensure sufficient color contrast and readable font sizes.
- Format tables and diagrams for clarity:
  - Use simple tables with clear headers and consistent alignment.
  - Add captions or descriptions to diagrams.
- Keep formatting simple and intuitive, especially for non-technical users. Avoid complex layouts or excessive styling.
- Use tags and metadata for organization and searchability.

### Link Management
- Always check links for accuracy and relevance before publishing.
- Use relative links for internal documentation to avoid broken links when moving files.
- Prefer descriptive link text over raw URLs (e.g., "See the [Style Guide]" instead of "http://.../style-guide").
- Regularly audit documentation for broken or outdated links.
- Document link management practices in style guides and templates.

### Content Relevance & Maintenance
- Only add content that is relevant and necessary for users; avoid clutter and unnecessary documentation.
- Regularly review and update content to ensure accuracy and relevance.
- Use versioning to track changes and maintain historical records.
- Remove or revise outdated information promptly.
- Populate empty files and folders with meaningful content and cross-references.
- Organize domain documentation for clarity and discoverability:
  - Use a hierarchical folder structure to group documents by domain and subdomain.
  - Apply consistent naming conventions for files and folders.
  - Create and follow templates for domain documents to ensure uniformity.
  - Link related domain documents to support navigation and context.

## Link Management

### Internal Links
- Use relative paths for all internal documentation links (e.g., `[Base Entity](../foundation/base_entity.md)`)
- Test links locally before committing to ensure they resolve correctly
- Use descriptive link text that explains the destination or purpose
- Avoid generic phrases like "click here" or "read more"

### External Links
- Use full URLs for external resources
- Include link text that identifies the external source (e.g., `[MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)`)
- Verify external links are stable and likely to remain available
- Consider using archive links for important but potentially unstable resources

### Cross-References
- Link to related domain documents using clear, contextual anchor text
- Create bidirectional links where relationships exist between domains
- Use the `See Also` section for related links that don't fit naturally in the content
- Maintain a consistent linking strategy across all domain documentation

### Link Validation
- Run link checking tools during pre-commit hooks
- Regularly audit documentation for broken internal and external links
- Update or remove outdated links promptly
- Document any intentionally broken links (e.g., planned future content) with clear notes

## Quick Reference Checklist

### Before Publishing Any Documentation

**Structure & Content:**
- [ ] Starts with visible H1 title (no `title:` in front matter)
- [ ] Uses correct entity type indicator in title: (Template Entity), (Entity), (Value Object), or none for domain pages
- [ ] Includes 2-6 relevant tags in YAML front matter array format (`tags:` not inline `tag:`)
- [ ] References Base Entity for standard attributes (no explicit listing)
- [ ] Includes comprehensive examples covering ALL attributes
- [ ] Uses active voice and concise sentences
- [ ] Follows domain file structure: Overview → Purpose → Structure → Example → See Also

**Formatting & Style:**
- [ ] Uses consistent Markdown syntax
- [ ] Applies proper heading hierarchy (single H1, then H2+)
- [ ] Includes alt text for images
- [ ] Uses descriptive link text
- [ ] Follows terminology conventions (teams vs. participants)
- [ ] Uses Mermaid `graph TD` for diagrams when appropriate

**Technical Requirements:**
- [ ] Passes markdown linting (MD025, MD041 compliance)
- [ ] Uses relative links for internal references
- [ ] Validates all external links
- [ ] Includes proper YAML front matter with `tags:` array (never inline `tag:` format)
- [ ] Follows embedding rules (same domain = embed, different domain = UUID reference)

**Final Review:**
- [ ] Content is relevant and necessary
- [ ] Examples use domain-relevant, descriptive values
- [ ] Links are accurate and functional
- [ ] Accessible to intended audience
- [ ] Maintains professional, neutral tone

## How to Use
Use this file as a checklist when writing or reviewing documentation. For best results, follow this order:
1. Draft content using the writing and structure guidelines.
2. Apply formatting and accessibility rules.
3. Check and manage links.
4. Review for relevance and maintain content as needed.
These instructions are designed for both human and AI authors. Link to related lessons for deeper guidance.
