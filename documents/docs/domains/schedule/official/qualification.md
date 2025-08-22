# **Qualification** (Data Model - Value Object)

## **Introduction**

A **Qualification** Value Object represents a certification or qualification held by an official. It is embedded within
an entity and does not have its own identity or lifecycle.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute        | Description                                                  | Type   | Required | Notes / Example                                                         |
| ---------------- | ------------------------------------------------------------ | ------ | -------- | ----------------------------------------------------------------------- |
| **Type**         | The category of qualification.                               | String | Yes      | E.g., `Referee`, `Umpire`, `Judge`, `Scorekeeper`                       |
| **Level**        | The level or grade of the qualification.                     | String | Yes      | E.g., `National`, `Regional`, `Local`, `International`                  |
| **Issued Date**  | The date when the qualification was issued.                  | Date   | Yes      | `2020-05-15`                                                            |
| **Expiry Date**  | The date when the qualification expires.                     | Date   | Yes      | `2025-12-31`                                                            |
| **Issuing Body** | The organization or authority that issued the qualification. | UUID   | Yes      | Reference to an entity                                                  |
| **Notes**        | Additional information about the qualification.              | Text   | No       | E.g., `"Specialized in youth competitions"`, `"Advanced certification"` |

---

## **Relationships**

- A `Qualification` Value Object is always embedded within an entity.
- It does not have its own identity or lifecycle.

---

## **Considerations**

- **Validation:** Ensure expiry dates are in the future when creating new qualifications.
- **Renewal:** Track qualification status and handle renewal processes.
- **Compliance:** Ensure qualifications meet tournament or event requirements.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 17024:2012 - Conformity assessment - General requirements for bodies operating certification of persons](https://www.iso.org/standard/52994.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event official

  qualification standards

## See Also

- [Official README](../../schedule/official/README.md)
- [Official](../../schedule/official/official.md)
- [Organization README](../../organization/README.md)
- [Identity README](../../identity/README.md)
- [Business README](../../README.md)

---
