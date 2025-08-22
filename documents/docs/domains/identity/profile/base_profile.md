# **Base Profile** (Data Model – Abstract Entity)

## **Introduction**

The **Base Profile** Abstract Entity defines the core attributes and relationships shared by all profile types in the
system (e.g., Human, Animal, Plant, Vehicle, Robot, etc.). It provides a unified foundation for representing any
participant, resource, or asset within the Tournament Organizer, ensuring consistency and extensibility across all
profile subtypes.

All specific profile entities (such as Human Profile, Animal Profile, etc.) inherit from this base model and add their
domain-specific attributes.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This abstract entity inherits the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) from the
.

| Attribute               | Description                             | Type       | Required | Notes / Example                          |
| ----------------------- | --------------------------------------- | ---------- | -------- | ---------------------------------------- |
| **ProfileType**         | Discriminator for the profile subtype   | String     | Yes      | `"Human"`, `"Animal"`, `"Vehicle"`, etc. |
| **Name**                | Display name for the profile            | String     | Yes      | `"John Smith"`, `"Rover"`, `"Team Bus"`  |
| **Contact Information** | Reference to Contact Information entity | UUID       | No       |                                          |
| **Image**               | Embedded or referenced image            | [Image]    | No       |                                          |
| **Relationships**       | List of relationship references         | List[UUID] | No       | Links to Relationship entities           |
| **Media**               | List of media asset references          | List[UUID] | No       | Links to Media Asset entities            |

---

## **Relationships**

- All specific profile entities inherit from Base Profile.
- Relationships and media are managed consistently across all profile types.
- Contact Information is referenced for communication and notifications.

---

## **Considerations**

- **Extensibility:** New profile types can be added by inheriting from Base Profile and extending with domain-specific

  attributes.

- **Polymorphism:** APIs and UIs can treat all profiles generically using the `ProfileType` discriminator.
- **Consistency:** Shared attributes and relationships ensure uniform handling of all profiles.
- **Security:** Access control and audit logging should be applied at the base level for sensitive data.

---

## **Inheritance Diagram**

```text
Base Profile
 ├── Human Profile
 ├── Animal Profile
 ├── Plant Profile
 ├── Vehicle Profile
 ├── Robot Profile
 ├── Software Profile
 ├── Machine Profile
 ├── Digital Profile
 ├── Art Profile
 └── Computer Profile

```

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event participant

  management standards

## See Also

- [Human](../../identity/profile/human.md)
- [Animal](../../identity/profile/animal.md)
- [Contact Information](../../identity/contact_information.md)
- [Identity README](../../identity/README.md)
- [Registration](../../registration/registration.md)
- [Business README](../../README.md)
