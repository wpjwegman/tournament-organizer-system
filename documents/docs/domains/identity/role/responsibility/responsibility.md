# **Responsibility** (Data Model - Template Entity)

## **Introduction**

A **Responsibility** Entity Template defines a reusable blueprint for a specific duty, task, or obligation that can be
assigned to roles within the tournament system. It provides a standardized way to define what individuals or entities
are expected to do in their assigned roles.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../../foundation/base_entity.md). When used, its
definition is typically **copied** into the target context, allowing for potential minor modifications or annotations
without altering the original template.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute        | Description                                                                                                                                                                       | Type       | Required | Notes / Example                                                            |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | -------------------------------------------------------------------------- |
| **Name**         | A descriptive name for the responsibility template.                                                                                                                               | String     | Yes      | `"Match Officiating"`, `"Team Management"`, `"Safety Oversight"`           |
| **Description**  | Detailed description of the responsibility template and its scope.                                                                                                                | Text       | Yes      | `"Responsible for ensuring fair play and rule enforcement during matches"` |
| **Type**         | The type of responsibility template.                                                                                                                                              | String     | Yes      | `"Operational"`, `"Administrative"`, `"Safety"`, `"Technical"`             |
| **Priority**     | The priority level of this responsibility template.                                                                                                                               | String     | Yes      | `"Low"`, `"Medium"`, `"High"`, `"Critical"`                                |
| **Tasks**        | List of [Task](task.md) entities that make up this responsibility. | List[UUID] | Optional | References to task entities                                                |
| **Requirements** | Specific requirements for fulfilling this responsibility template.                                                                                                                | Text       | Optional | `"Must be certified in relevant area"`                                     |
| **Notes**        | Additional notes about the responsibility template.                                                                                                                               | Text       | Optional | `"Requires regular training updates"`                                      |

---

## **Relationships**

- A `Responsibility` Entity Template is referenced by [Role](../role.md) entities.
- A `Responsibility` Entity Template may contain multiple [Task](task.md) entities.

### Parent Relationships

- [Role](../role.md) - Roles that have this responsibility

### Child Relationships

- [Task](task.md) - Tasks that make up this responsibility

### Related Entities

- - Role assignments that include this responsibility

---

## **Considerations**

- **Template Nature:** This template defines a standard responsibility. Instance-specific variations or customizations

  belong on the copied instance within its specific context.

- **Copy Mechanism:** The process of copying this template definition into a target context needs to be handled by

  application logic.

- **Task Breakdown:** Responsibilities should be broken down into specific, actionable tasks.
- **Priority Management:** Responsibility priorities should be clearly defined for effective resource allocation.

---
