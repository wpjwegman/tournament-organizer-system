# **Human Profile** (Data Model - Entity)

## **Introduction**

A **Human Profile** Entity represents a person within the tournament system. It provides a comprehensive way to handle
human profile information for participant management, personal identification, and user experience within the tournament
system.

It describes personal characteristics and coordinates with other entities (like [Name](../attributes/name.md),
[Contact Information](../contact_information.md), and [Medical History](../attributes/medical_history/medical_history.md)) to provide complete human
profile oversight.

It inherits properties from the [Base Entity](../../foundation/README.md).

---

## **Attributes**

| Attribute               | Description                                               | Type     | Required | Notes / Example                                                     |
| ----------------------- | --------------------------------------------------------- | -------- | -------- | ------------------------------------------------------------------- |
| **ID**                  | Unique identifier for the human profile entity.           | UUID     | Yes      | `"h123e456-7890-1234-5678-901234567890"`                            |
| **Name**                | The person's name information.                            | Object   | Yes      | Embedded [Name](../attributes/name.md) Value Object                               |
| **Contact Information** | The person's contact information.                         | Object   | Optional | Embedded [Contact Information](../contact_information.md) Value Object |
| **Date of Birth**       | The person's date of birth.                               | Object   | Optional | Embedded [Date of Birth](../attributes/date_of_birth.md) Value Object             |
| **Sex**                 | The person's biological sex.                              | Object   | Optional | Embedded [Sex](../attributes/sex.md) Value Object                                 |
| **Gender Identity**     | The person's gender identity.                             | Object   | Optional | Embedded [Gender Identity](../attributes/gender_identity.md) Value Object         |
| **Medical History**     | The person's medical history.                             | Object   | Optional | Embedded [Medical History](../attributes/medical_history/medical_history.md) Value Object         |
| **Interests**           | List of the person's interests.                           | List     | Optional | List of [Interest](../attributes/interest.md) Value Objects                       |
| **Preferences**         | List of the person's preferences.                         | List     | Optional | List of [Preference](../attributes/preference.md) Value Objects                   |
| **Status**              | The status of the human profile.                          | String   | Optional | `"Active"`, `"Inactive"`, `"Suspended"`                             |
| **Created At**          | Timestamp when the human profile entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                            |
| **Updated At**          | Timestamp when the human profile entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                            |

---

## **Relationships**

- A `Human Profile` Entity is associated with a [User](../account/account.md) entity.
- A `Human Profile` Entity may be associated with [Team](../../team/README.md) entities.
- A `Human Profile` Entity may be associated with [Registration](../../registration/README.md) entities.

---

## **Considerations**

- **Privacy:** Human profile information should be handled with appropriate privacy controls.
- **Accuracy:** Profile information should be accurate and up-to-date.
- **Consent:** Profile information should be collected with appropriate consent.
- **Access Control:** Profile access should be controlled based on permissions.
- **Data Retention:** Profile data retention should follow relevant regulations.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event participant

  management standards

## See Also

- [Base Profile](base_profile.md)
- [Contact Information](../contact_information.md)
- [Medical History](../attributes/medical_history/medical_history.md)
- [Identity README](../README.md)
- [Team](../../team/README.md)
- [Registration](../../registration/README.md)
- [Business README](../../README.md)
