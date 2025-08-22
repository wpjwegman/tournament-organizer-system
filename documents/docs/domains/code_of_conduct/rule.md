# **Rule** (Data Model - Template Entity)

## **Introduction**

A **Rule** Entity defines a mandatory, enforceable requirement or prohibition within the context of a tournament, event,
or organization. Rules are referenced by the [Code of Conduct](../code_of_conduct/code_of_conduct.md) and
are the basis for disciplinary action if violated. Each rule is specific, actionable, and includes clear consequences
for non-compliance.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute         | Description                           | Type   | Required | Notes / Example                               |
| ----------------- | ------------------------------------- | ------ | -------- | --------------------------------------------- |
| **Title**         | Short, descriptive name for the rule. | String | Yes      | `No Physical Contact with Officials`          |
| **Description**   | Detailed explanation of the rule.     | Text   | Yes      | `Participants must not physically contact...` |
| **Category**      | Classification of the rule.           | String | No       | `Safety`, `Fair Play`, `Anti-Discrimination`  |
| **Applicability** | Context where the rule applies.       | String | No       | `Tournament`, `Match`, `All Participants`     |
| **Consequence**   | Action taken if the rule is violated. | Text   | Yes      | `Immediate disqualification`                  |
| **Severity**      | Severity of violation.                | String | No       | `Minor`, `Major`, `Critical`                  |

---

## **Considerations**

- **Enforceability:** Rule templates must be clear, actionable, and have defined consequences.
- **Clarity:** Avoid ambiguity in rule template language.
- **Contextualization:** Specify where and to whom the rule template applies.

---

## References

- [ISO 26000:2010 - Guidance on social responsibility](https://www.iso.org/standard/42546.html) - Standard for

  organizational conduct and social responsibility

- [ISO 37301 — Compliance management systems (ISO official page)](https://www.iso.org/standard/75080.html) - Standard for compliance

  and rule enforcement

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event management standards

  including rule enforcement

## See Also

- [Code Of Conduct](../code_of_conduct/code_of_conduct.md)
- [Expected Behavior](../code_of_conduct/expected_behavior.md)
- [Tournament Rule](../tournament/rule.md)

---
