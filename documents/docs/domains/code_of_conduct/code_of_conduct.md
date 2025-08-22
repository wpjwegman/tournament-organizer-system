# **Code of Conduct** (Data Model - Template Entity)

## **Introduction**

A **Code of Conduct** Entity Template defines the enforceable standards and positive expectations for conduct within a
given context (e.g., Tournament, Organization). It is composed of references to 🚨 **BROKEN:** 🚨 **BROKEN:**
[Rule](../discipline/activity/variation/rule.md) entities (mandatory, enforceable requirements) and
[Expected Behavior](../code_of_conduct/expected_behavior.md) entities (positive standards), ensuring a
safe, respectful, and fair environment.

Guidelines, which are non-binding recommendations, are not referenced directly in the Code of Conduct but may be
provided separately.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

| Attribute              | Description                                                                                                                                               | Type       | Required | Notes / Example                                                                |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | ------------------------------------------------------------------------------ |
| **Title**              | The official name or title of the Code of Conduct template.                                                                                               | String     | Yes      | Example: `Fair Play and Respect Policy`, `Standard Tournament Code of Conduct` |
| **Version**            | A version identifier (e.g., date or number) for this specific template revision.                                                                          | String     | Optional | Example: `v2.1`, `2024-07-28`                                                  |
| **Introduction**       | Optional introductory text (Markdown) to set the context, purpose, or spirit of the Code of Conduct.                                                      | Text       | Optional | Example: "This document outlines the behavior expected of all participants..." |
| **Applicability**      | Describes the intended scope or context (e.g., Tournament, Organization, Event).                                                                          | String     | Optional | Example: `"Tournament - General"`, `"Youth Events"`                            |
| **Expected Behaviors** | List of references (by ID) to the **[Expected Behavior](../code_of_conduct/expected_behavior.md)** Entities included in this template.      | List[UUID] | Optional | Example: `["eb-a1b2c3d4-e5f6-4890-1234-567890abc111"]`                         |
| **Rules**              | List of references (by ID) to the **[Rule](../code_of_conduct/rule.md)** Entities included in this template.  | List[UUID] | Optional | Example: `["rule-a1b2c3d4-e5f6-4890-1234-567890abc222"]`                       |

---

## **Considerations**

- **Enforceability:** Only Rules and Expected Behaviors are referenced to ensure all standards are actionable and

  enforceable.

- **Clarity:** Guidelines are kept separate to avoid confusion between mandatory requirements and recommendations.
- **Template vs. Instance:** This model defines the _template_. The actual Code of Conduct applied to a specific context

  is created by copying this template's definition into the target context.

- **Versioning:** The `Version` attribute tracks changes to the template composition itself.

---

## References

- [ISO 26000:2010 - Guidance on social responsibility](https://www.iso.org/standard/42546.html) - Standard for

  organizational conduct and social responsibility

- [ISO 37301 — Compliance management systems (ISO official page)](https://www.iso.org/standard/75080.html) - Standard for compliance

  and conduct management

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event management standards

  including conduct guidelines

## See Also

- [Expected Behavior](../code_of_conduct/expected_behavior.md)
- [Rule](../code_of_conduct/rule.md)

---
