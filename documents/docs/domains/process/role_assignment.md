# **Role Assignment** (Data Model - Template Entity)

## **Introduction**

A **Role Assignment** Entity represents the assignment of a specific within a particular context, such as a tournament,
team, or organization. It manages the relationship between roles and participants, including assignment details and
status.

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute      | Description                                                                           | Type   | Required | Notes / Example                                       |
| -------------- | ------------------------------------------------------------------------------------- | ------ | -------- | ----------------------------------------------------- |
| **Registrant** | Reference to the being assigned the role.                                             | UUID   | Yes      | `registrant-uuid-123`                                 |
| **Role**       | Reference to the [Role](../foundation/base_entity.md) being assigned.                                             | UUID   | Yes      | `role-uuid-referee`                                   |
| **Context**    | The context in which this role assignment applies.                                    | String | Yes      | `"Tournament"`, `"Team"`, `"Organization"`            |
| **Context ID** | Reference to the specific entity (Tournament, Team, etc.) this assignment applies to. | UUID   | Yes      | `tournament-uuid-456`                                 |
| **Start Date** | When this role assignment becomes effective.                                          | Date   | Yes      | `2024-06-01`                                          |
| **End Date**   | When this role assignment expires (optional for ongoing assignments).                 | Date   | Optional | `2024-06-30`                                          |
| **Status**     | Current status of the role assignment.                                                | String | Yes      | `"Active"`, `"Inactive"`, `"Pending"`, `"Terminated"` |
| **Notes**      | Additional notes about the role assignment.                                           | Text   | Optional | `"Temporary assignment due to staff shortage"`        |

---

## **Relationships**

- A `Role Assignment` Entity assigns one .
- A `Role Assignment` Entity applies to a specific context entity (Tournament, Team, Organization, etc.).

### Parent Relationships

- - The person/entity being assigned the role
- [Role](../foundation/base_entity.md) - The role being assigned

### Child Relationships

- None

### Related Entities

- - Context for tournament-specific role assignments
- - Context for team-specific role assignments
- - Context for organization-specific role assignments

---

## **Considerations**

- **Role Assignment Lifecycle:** Role assignments should have clear start and end dates.
- **Context Management:** Each role assignment must be associated with a specific context.
- **Status Tracking:** Role assignment status should be updated as assignments change.
- **Conflict Resolution:** The system should prevent conflicting role assignments.

---
