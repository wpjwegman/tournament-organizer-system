# **Registrant** (Data Model - Template Entity)

## **Introduction**

A **Registrant** Entity represents an individual or entity that can participate in tournaments, activities, or events
within the system. It serves as the core identity record that links to specific profiles (human, animal, computer, etc.)
and manages participation across different contexts.

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute   | Description                                                               | Type   | Required | Notes / Example                                               |
| ----------- | ------------------------------------------------------------------------- | ------ | -------- | ------------------------------------------------------------- |
| **Profile** | Reference to the specific profile entity (Human, Animal, Computer, etc.). | UUID   | Yes      | `profile-uuid-human-123`                                      |
| **Type**    | The type of registrant (Human, Animal, Computer, etc.).                   | String | Yes      | `"Human"`, `"Animal"`, `"Computer"`                           |
| **Status**  | Current status of the registrant.                                         | String | Yes      | `"Active"`, `"Inactive"`, `"Suspended"`, `"Pending"`          |
| **Contact** | Reference to the for this registrant.                                     | UUID   | Optional | `contact-uuid-456`                                            |
| **Account** | Reference to the associated with this registrant.                         | UUID   | Optional | `account-uuid-789`                                            |
| **Notes**   | Additional notes about the registrant.                                    | Text   | Optional | `"Professional athlete"`, `"Requires special accommodations"` |

---

## **Relationships**

- A `Registrant` Entity has one profile entity (Human, Animal, Computer, etc.).
- A `Registrant` Entity may have one entity.
- A `Registrant` Entity may have one entity.
- A `Registrant` Entity may participate in multiple [Registration](../registration/registration.md)

  entities.

### Parent Relationships

- - The specific profile type

### Child Relationships

- [Registration](../registration/registration.md) - Registrations for this registrant

### Related Entities

- - Contact details for this registrant
- - Account associated with this registrant

---

## **Considerations**

- **Profile Linkage:** Each registrant must be linked to a specific profile type.
- **Status Management:** Registrant status should be managed to control participation eligibility.
- **Contact Information:** Contact details should be maintained for communication purposes.
- **Account Association:** Registrants may have associated accounts for system access.

---
