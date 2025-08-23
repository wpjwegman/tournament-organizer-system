---
tags:
  - communication
  - notification
  - template-entity
  - messaging
  - alert
---

# Notification (Data Model - Template Entity)

# Notification (Data Model - Template Entity)

## Overview

A **Notification** Entity represents a message or alert that can be sent to participants, organizers, or other stakeholders within the tournament system. It provides a consistent way to handle notification information for communication, updates, and event management within the tournament system.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

## Purpose

- Standardize notification format and structure across the tournament system
- Provide template-based notification creation for consistency
- Support multiple delivery types (Email, SMS, Push, In-App)
- Enable priority-based notification processing
- Track notification lifecycle from creation to delivery to reading
- Support scheduled and immediate notification delivery

## Structure

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute        | Description                                               | Type      | Required | Notes / Example                                      |
| ---------------- | --------------------------------------------------------- | --------- | -------- | ---------------------------------------------------- |
| **Type**         | The type of notification.                                 | String    | Yes      | `"Email"`, `"SMS"`, `"Push"`, `"In-App"`             |
| **Title**        | The title or subject of the notification.                 | String    | Yes      | `"Tournament Update"`, `"Registration Confirmation"` |
| **Message**      | The content of the notification message.                  | String    | Yes      | `"Your team has been registered successfully"`       |
| **Recipient**    | The intended recipient of the notification.               | Reference | Yes      | Reference to participant, organizer, or stakeholder  |
| **Priority**     | The priority level of the notification.                   | String    | Optional | `"Low"`, `"Normal"`, `"High"`, `"Urgent"`            |
| **Scheduled At** | The scheduled time for sending the notification.          | DateTime  | Optional | `"2024-01-15T10:30:00Z"`                             |
| **Sent At**      | The time when the notification was sent.                  | DateTime  | Optional | `"2024-01-15T10:30:00Z"`                             |
| **Read At**      | The time when the notification was read by the recipient. | DateTime  | Optional | `"2024-01-15T11:00:00Z"`                             |

## Example

{% raw %}
```json
{
  "notification_id": "n48e9c2-5733-48d6-9851-88142f78ab5e",
  "type": "Email",
  "title": "Registration Confirmation",
  "message": "Your team has been successfully registered for the City Chess Championship. Tournament begins on September 1st at 9:00 AM.",
  "recipient_id": "p98e7d6-2394-4857-9183-7642abcdef12",
  "priority": "Normal",
  "created_at": "2025-08-25T14:30:00Z",
  "scheduled_at": "2025-08-25T14:30:00Z",
  "sent_at": "2025-08-25T14:30:02Z",
  "read_at": null,
  "status": "Active"
}
```
{% endraw %}

## See Also

- **Communication Models**: [Communication Domain](README.md), [Digital Channel](../media/digital_channel.md)
- **Related Domains**: [Identity](../identity/README.md), [Schedule](../schedule/README.md), [Tournament](../tournament/README.md)
- **Base Entity**: [Foundation Base Entity](../foundation/base_entity.md)
