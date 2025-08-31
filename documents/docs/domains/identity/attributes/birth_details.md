# **Birth Details** (Data Model - Value Object)

## **Introduction**

A **Birth Details** Value Object aggregates information related to an individual's birth, primarily the date, used for
age calculation and eligibility checks.

As a Value Object, it is defined entirely by its attributes and does not have its own identity or lifecycle. It is
intended to be **embedded** within an owning Entity like .

*(For details on usage, see the <!-- TODO: Create User Guide: Birth Details -->User Guide).*

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute               | Description                                                                                                | Type   | Required | Notes / Example                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- | ------ | -------- | --------------------------------------------------------------------------------- |
| **Date**                | The date of birth.                                                                                         | Date   | Yes      | Example: `1990-10-25`                                                             |
| **Place**               | The city, town, or locality of birth.                                                                      | String | Optional | Example: "Metropolis"                                                             |
| **Country**             | Optional reference (by ID) to the **[Country](../../identity/attributes/country.md)** of birth. | UUID   | Optional | Example: `c0a1b2c3-d4e5-4f67-8901-234567abcdef`                                   |
| **Verification Status** | Optional status indicating if the Date has been verified (e.g., against documentation).                    | String | Optional | `Verified`, `Unverified`, `Requires Verification`. Default might be `Unverified`. |

---

## **Relationships**

- A `Birth Details` **Value Object** holds an optional reference (by ID) to a `Country` Entity.
- It is always **embedded within** an owning Entity (e.g., `Human Profile`).

---

## **Considerations**

- **Embedding:** This defines birth details and is embedded within the owning profile.
- **Privacy:** Date of birth is sensitive information requiring appropriate access controls.
- **Verification:** The `Verification Status` is important for confirming age eligibility based on verified data.
- **Immutability:** If details need correction, the owning Entity should replace the entire embedded `Birth Details`

  object.

---

## References

- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [GDPR Article 9 - Processing of special categories of personal data](https://gdpr-info.eu/art-9-gdpr/)

## See Also

- [Country](../../identity/attributes/country.md)
- [Date Of Birth](../../identity/attributes/date_of_birth.md)
- [Identity README](../../identity/README.md)
- [Registration](../../registration/registration.md)
- [Business README](../../README.md)

---
