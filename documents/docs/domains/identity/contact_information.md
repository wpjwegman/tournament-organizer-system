# **Contact Information** (Data Model - Template Entity)

## **Introduction**

A **Contact Information** Entity represents a collection of contact details for an individual or organization. It
provides a centralized way to manage various types of contact information such as phone numbers, email addresses,
physical addresses, and digital channels.

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute            | Description                                                                                                                                                                   | Type       | Required | Notes / Example                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | ----------------------------------------- |
| **Type**             | The type of contact information.                                                                                                                                              | String     | Yes      | `"Personal"`, `"Business"`, `"Emergency"` |
| **Phone**            | Primary phone number.                                                                                                                                                         | String     | Optional | `"+1-555-123-4567"`                       |
| **Email**            | Primary email address.                                                                                                                                                        | String     | Optional | `"john.doe@example.com"`                  |
| **Address**          | Reference to the [Physical Address](attributes/address.md) for this contact. | UUID       | Optional | `address-uuid-123`                        |
| **Digital Channels** | List of [Digital Channel](../media/digital_channel.md) entities for online contact.                                                                             | List[UUID] | Optional | References to digital channel entities    |
| **Preferred**        | The preferred method of contact.                                                                                                                                              | String     | Optional | `"Email"`, `"Phone"`, `"SMS"`             |
| **Notes**            | Additional notes about the contact information.                                                                                                                               | Text       | Optional | `"Best time to call: 9 AM - 5 PM"`        |

---

## **Relationships**

- A `Contact Information` Entity may be associated with a entity.
- A `Contact Information` Entity may be associated with an entity.
- A `Contact Information` Entity may have one 🚨 **BROKEN:** 🚨 **BROKEN:** 🚨 **BROKEN:** 🚨 **BROKEN:**

  [Physical Address](attributes/address.md) entity.

- A `Contact Information` Entity may have multiple [Digital Channel](../media/digital_channel.md)

  entities.

### Parent Relationships

- - The person/entity this contact information belongs to
- - The organization this contact information belongs to

### Child Relationships

- 🚨 **BROKEN:** 🚨 **BROKEN:** 🚨 **BROKEN:** 🚨 **BROKEN:**

  [Physical Address](attributes/address.md) - The physical address for this contact

- [Digital Channel](../media/digital_channel.md) - Digital channels for this contact

### Related Entities

- [Emergency Contact](../identity/attributes/emergency_contact.md) - Emergency contact information

---

## **Considerations**

- **Contact Management:** Contact information should be kept up-to-date and validated.
- **Privacy:** Contact information should be handled according to privacy regulations.
- **Preferred Method:** The preferred contact method should be clearly indicated.
- **Validation:** Contact information should be validated for format and accuracy.

---
