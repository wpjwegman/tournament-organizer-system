---
tags:

  - identity
  - contact-information
  - template-entity
  - domain

---

# Contact Information (Template Entity)

## Overview

Contact Information is a template entity that centralizes all contact details for an individual or organization, including phone, email, address, and digital channels. It is used throughout the system to ensure consistent, up-to-date, and privacy-compliant contact management.

## Purpose

- Centralized management of contact details
- Support for multiple contact types (personal, business, emergency)
- Linking contact information to profiles, accounts, and organizations
- Privacy and validation of contact data

## Structure

This template entity includes all standard attributes from the [Base Entity](../foundation/base_entity.md) (ID, Status, CreatedAt, LastUpdatedAt).

| Attribute            | Description                                             | Type       | Required | Notes / Example                           |
|----------------------|---------------------------------------------------------|------------|----------|-------------------------------------------|
| **Type**             | The type of contact information                         | String     | Yes      | "Personal", "Business", "Emergency"        |
| **Phone**            | Primary phone number                                    | String     | Optional | "+1-555-123-4567"                         |
| **Email**            | Primary email address                                   | String     | Optional | "<john.doe@example.com>"                    |
| **Address**          | Reference to [Physical Address](attributes/address.md)  | UUID       | Optional | `address-uuid-123`                        |
| **Digital Channels** | List of [Digital Channel](../media/digital_channel.md)  | List[UUID] | Optional | References to digital channel entities     |
| **Preferred**        | Preferred method of contact                             | String     | Optional | "Email", "Phone", "SMS"                   |
| **Notes**            | Additional notes                                        | Text       | Optional | "Best time to call: 9 AM - 5 PM"          |

## Example

```mermaid
graph TD
    ContactInfo[Contact Information]
    ContactInfo --> Phone[Phone: +1-555-123-4567]
    ContactInfo --> Email[Email: <john.doe@example.com>]
    ContactInfo --> Address[Address: address-uuid-123]
    ContactInfo --> DigitalChannels[Digital Channels: [dc-001, dc-002]]
    ContactInfo --> Preferred[Preferred: Email]
    ContactInfo --> Notes[Notes: Best time to call: 9 AM - 5 PM]
```

This example shows a contact information entity with all attributes represented, including links to address and digital channels.

## See Also

- [Physical Address](attributes/address.md)
- [Digital Channel](../media/digital_channel.md)
- [Emergency Contact](../identity/attributes/emergency_contact.md)
- [Base Entity](../foundation/base_entity.md)
