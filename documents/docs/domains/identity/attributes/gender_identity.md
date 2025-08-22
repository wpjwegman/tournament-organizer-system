# **Gender Identity** (Data Model - Value Object)

## **Introduction**

A **Gender Identity** Value Object represents an individual's personal sense of their gender in a standardized format.
It provides a consistent way to handle gender identity information for respectful and inclusive interactions within the
tournament system.

It describes personal characteristics and is typically embedded within other entities (like
[Human Profile](../profile/human.md)) to specify gender identity details.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute       | Description                                                  | Type   | Required | Notes / Example                                     |
| --------------- | ------------------------------------------------------------ | ------ | -------- | --------------------------------------------------- |
| **Identity**    | The gender identity category.                                | String | Yes      | `"Man"`, `"Woman"`, `"Non-binary"`, `"Genderfluid"` |
| **Code**        | A standardized code for the gender identity.                 | String | Optional | `"M"`, `"W"`, `"NB"`, `"GF"`                        |
| **Pronouns**    | Preferred pronouns for the individual.                       | String | Optional | `"he/him"`, `"she/her"`, `"they/them"`              |
| **Description** | Additional description or context about the gender identity. | String | Optional | `"Identifies as a transgender woman"`               |

---

## **Relationships**

- A `Gender Identity` Value Object is embedded within [Human Profile](../profile/human.md) entities.
- A `Gender Identity` Value Object may be referenced by [Registration](../../registration/README.md) entities for inclusive

  practices.

---

## **Considerations**

- **Respect:** Gender identity should always be respected and used appropriately.
- **Privacy:** This information is personal and should be handled with confidentiality.
- **Inclusivity:** The system should support diverse gender identities.
- **Optional:** Gender identity should be optional and not required for participation.

---

## References

- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [ISO 26000:2010 - Guidance on social responsibility](https://www.iso.org/standard/42546.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [GLAAD Media Reference Guide](https://www.glaad.org/reference) - Gender identity and LGBTQ+ terminology

## See Also

- [Human Profile](../profile/human.md)
- [Registration](../../registration/README.md)
- [Identity README](../../identity/README.md)
- [Team Format](../../discipline/stage/team_format.md)
- [Business README](../../README.md)
