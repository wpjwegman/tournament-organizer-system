# **Sex** (Data Model - Value Object)

## **Introduction**

A **Sex** Value Object represents biological sex classification in a standardized format. It provides a consistent way
to handle sex information for medical, legal, and administrative purposes within the tournament system.

It describes biological characteristics and is typically embedded within other entities (like
[Human Profile](../profile/human.md) or [Medical History](medical_history/medical_history.md)) to specify biological details.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute       | Description                                                     | Type   | Required | Notes / Example                              |
| --------------- | --------------------------------------------------------------- | ------ | -------- | -------------------------------------------- |
| **Category**    | The biological sex category.                                    | String | Yes      | `"Male"`, `"Female"`, `"Intersex"`           |
| **Code**        | A standardized code for the sex category.                       | String | Optional | `"M"`, `"F"`, `"I"`                          |
| **Description** | Additional description or context about the sex classification. | String | Optional | `"Biological male"`, `"Intersex individual"` |

---

## **Relationships**

- A `Sex` Value Object is embedded within [Human Profile](../profile/human.md) entities.
- A `Sex` Value Object may be embedded within [Medical History](medical_history/medical_history.md) entities.
- A `Sex` Value Object may be referenced by [Registration](../../registration/README.md) entities for eligibility purposes.

---

## **Considerations**

- **Privacy:** Sex information should be handled according to privacy regulations.
- **Sensitivity:** This information is personal and should be treated with appropriate confidentiality.
- **Medical Context:** Sex information may be relevant for medical and safety considerations.
- **Legal Requirements:** Some jurisdictions have specific requirements for sex classification.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [WHO: Gender and health](https://www.who.int/health-topics/gender)

## See Also

- [Human Profile](../profile/human.md)
- [Medical History](medical_history/medical_history.md)
- [Identity README](../README.md)
- [Registration](../../registration/README.md)
- [Business README](../../README.md)
