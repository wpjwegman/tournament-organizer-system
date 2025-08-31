---
tags:

  - communication
  - notification
  - template-entity
  - messaging
  - alert

---

# Notification (Template Entity)

## Overview

A Notification is a template entity that represents a message or alert sent to tournament participants and organizers. It provides a standardized structure for capturing notification content, delivery information, and tracking status within the tournament system.

As a Template Entity, it includes standard lifecycle management from the [Base Entity](../foundation/base_entity.md), with additional attributes specific to notification handling and delivery tracking.

## Purpose

- Store notification content and delivery information
- Track notification lifecycle from creation to delivery
- Support different notification types and priority levels
- Provide standardized message structure across the tournament system
- Enable scheduled and immediate notification delivery

## Structure

This template entity includes standard attributes from the [Base Entity](../foundation/base_entity.md).

### Attributes

| Attribute        | Description                                               | Type      | Required | Example                                      |
| ---------------- | --------------------------------------------------------- | --------- | -------- | -------------------------------------------- |
| Type             | The delivery method for the notification                  | String    | Yes      | `"Email"`, `"SMS"`, `"Push"`, `"In-App"`     |
| Title            | The title or subject of the notification                  | String    | Yes      | `"Tournament Update"`, `"Match Cancelled"`   |
| Message          | The main content of the notification                      | String    | Yes      | `"Your match has been rescheduled"`         |
| Recipient        | Reference to the notification recipient                   | Reference | Yes      | Reference to participant or organizer       |
| Priority         | The urgency level of the notification                     | String    | Optional | `"Low"`, `"Normal"`, `"High"`, `"Critical"`  |
| Scheduled At     | When the notification should be sent                      | DateTime  | Optional | `"2025-08-25T14:30:00Z"`                     |
| Sent At          | When the notification was actually sent                   | DateTime  | Optional | `"2025-08-25T14:30:02Z"`                     |
| Read At          | When the recipient read the notification                  | DateTime  | Optional | `"2025-08-25T15:15:30Z"`                     |

## Example

### Basic Notification

{% raw %}

```json
{
  "notification_id": "not_001",
  "type": "Email",
  "title": "Match Schedule Update",
  "message": "Your semifinal match has been moved to Court 3 at 2:30 PM today.",
  "recipient_id": "participant_456",
  "priority": "High",
  "created_at": "2025-08-23T13:15:00Z",
  "scheduled_at": "2025-08-23T13:15:00Z",
  "sent_at": "2025-08-23T13:15:05Z",
  "read_at": null,
  "status": "Active"
}
```

{% endraw %}

This example shows a high-priority notification informing a participant about a match schedule change. The notification was sent immediately upon creation and is awaiting the recipient's acknowledgment.

## See Also

- [Communication Domain](README.md)
- [Base Entity](../foundation/base_entity.md)
- [Tournament Domain](../tournament/README.md)
