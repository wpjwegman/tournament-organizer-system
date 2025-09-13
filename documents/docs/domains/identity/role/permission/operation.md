---
tags:
- identity
- role
- permission
- operation
- template-entity
---

# Operation (Template Entity)

## Introduction

An **Operation** Entity Template defines a reusable blueprint for a specific action or activity that can be performed on
resources within the tournament system. It provides a standardized way to define what operations are available and how
they should be executed.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../../foundation/base_entity.md). When used, its definition is typically **copied** into the target
context, allowing for potential minor modifications or annotations without altering the original template.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## Attributes

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the [Base Entity](../../../foundation/base_entity.md).

| Attribute       | Description                                                      | Type         | Required | Notes / Example                                          |
| --------------- | ---------------------------------------------------------------- | ------------ | -------- | -------------------------------------------------------- |
| **Name**        | A descriptive name for the operation template.                   | String       | Yes      | `"Create"`, `"Read"`, `"Update"`, `"Delete"`, `"Manage"` |
| **Description** | Detailed description of the operation template and what it does. | Text         | Yes      | `"Allows creating new instances of a resource"`          |
| **Type**        | The type of operation template.                                  | String       | Yes      | `"CRUD"`, `"Custom"`, `"System"`                         |
| **Code**        | A unique code identifier for the operation template.             | String       | Yes      | `"CREATE"`, `"READ"`, `"UPDATE"`, `"DELETE"`             |
| **Parameters**  | List of parameters required for this operation template.         | List[String] | Optional | `["id", "data"]`                                         |
| **Notes**       | Additional notes about the operation template.                   | Text         | Optional | `"Requires validation before execution"`                 |

---

## Relationships

- An `Operation` Entity Template is referenced by entities.
- An `Operation` Entity Template may be applicable to multiple [Resource Type](resource_type.md) entities.

### Parent Relationships

- - Permissions that use this operation

### Child Relationships

- None

### Related Entities

- [Resource Type](resource_type.md) - Resource types this operation can be applied to

---

## **Considerations**

- **Template Nature:** This template defines a standard operation. Instance-specific variations or customizations belong

  on the copied instance within its specific context.

- **Copy Mechanism:** The process of copying this template definition into a target context needs to be handled by

  application logic.

- **Operation Clarity:** Operations should be clearly defined and well-documented.
- **Parameter Management:** Operation parameters should be clearly specified when required.

---
