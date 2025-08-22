# **Permission** (Data Model - Template Entity)

## **Introduction**

A **Permission** Entity Template defines a reusable blueprint for a specific authorization or access right within the
tournament system. It provides a standardized way to define what actions or resources an entity can access or modify.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../../foundation/base_entity.md). When used, its
definition is typically **copied** into the target context, allowing for potential minor modifications or annotations
without altering the original template.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute       | Description                                                                                                                                                                                   | Type   | Required | Notes / Example                                        |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ------------------------------------------------------ |
| **Name**        | A descriptive name for the permission template.                                                                                                                                               | String | Yes      | `"View Matches"`, `"Edit Scores"`, `"Manage Users"`    |
| **Description** | Detailed description of the permission template and its scope.                                                                                                                                | Text   | Yes      | `"Allows viewing match details and results"`           |
| **Type**        | The type of permission template.                                                                                                                                                              | String | Yes      | `"Read"`, `"Write"`, `"Delete"`, `"Admin"`             |
| **Resource**    | Reference to the [Resource Type](resource_type.md) this permission applies to. | UUID   | Yes      | `resource-type-uuid-matches`                           |
| **Operation**   | Reference to the [Operation](operation.md) this permission allows.             | UUID   | Yes      | `operation-uuid-view`                                  |
| **Scope**       | The scope of this permission template.                                                                                                                                                        | String | Yes      | `"Global"`, `"Organization"`, `"Tournament"`, `"Team"` |
| **Notes**       | Additional notes about the permission template.                                                                                                                                               | Text   | Optional | `"Requires special approval"`                          |

---

## **Relationships**

- A `Permission` Entity Template is referenced by [Role](../../../foundation/base_entity.md) entities.
- A `Permission` Entity Template applies to one [Resource Type](resource_type.md) entity.
- A `Permission` Entity Template allows one [Operation](operation.md) entity.

### Parent Relationships

- [Role](../../../foundation/base_entity.md) - Roles that have this permission

### Child Relationships

- None

### Related Entities

- [Resource Type](resource_type.md) - The resource this permission applies to
- [Operation](operation.md) - The operation this permission allows

---

## **Considerations**

- **Template Nature:** This template defines a standard permission. Instance-specific variations or customizations

  belong on the copied instance within its specific context.

- **Copy Mechanism:** The process of copying this template definition into a target context needs to be handled by

  application logic.

- **Resource Mapping:** Permissions should be clearly mapped to specific resource types.
- **Operation Clarity:** Operations should be specific and well-defined.

---
