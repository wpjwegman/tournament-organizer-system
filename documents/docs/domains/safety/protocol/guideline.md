# **Safety Guideline** (Data Model - Template Entity)

## **Introduction**

A **Safety Guideline** Entity Template defines a reusable blueprint for a specific instruction, recommendation, or
requirement designed to prevent harm, injury, or loss and ensure well-being within a particular context (e.g., during an
activity, within a venue).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md). When used, its
definition is typically **copied** into the target context (like a specific `Safety Protocol` instance), allowing for
potential minor modifications or annotations without altering the original template.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute        | Description                                                            | Type   | Required | Notes / Example                                                 |
| ---------------- | ---------------------------------------------------------------------- | ------ | -------- | --------------------------------------------------------------- |
| **Name**         | A descriptive name for the safety guideline template.                  | String | Yes      | `"Wear Protective Equipment"`, `"Maintain Safe Distance"`       |
| **Description**  | Detailed description of the safety guideline template and its purpose. | Text   | Yes      | `"All participants must wear appropriate protective equipment"` |
| **Type**         | The type of safety guideline template.                                 | String | Yes      | `"Preventive"`, `"Response"`, `"Recovery"`, `"Emergency"`       |
| **Priority**     | The priority level of this guideline template.                         | String | Yes      | `"Low"`, `"Medium"`, `"High"`, `"Critical"`                     |
| **Requirements** | Specific requirements for implementing this guideline template.        | Text   | Optional | `"Must be followed at all times"`                               |
| **Notes**        | Additional notes about the guideline template.                         | Text   | Optional | `"Based on industry best practices"`                            |

---

## **Relationships**

- A `Safety Guideline` Entity Template is referenced by [Safety Protocol](protocol.md) entities.
- A `Safety Guideline` Entity Template may be associated with specific [Role](../../foundation/base_entity.md) entities.

### Parent Relationships

- 🚨 **BROKEN:** 🚨 **BROKEN:** 🚨 **BROKEN:** [Safety Protocol](../../safety/protocol/protocol.md) 🚨 🚨 🚨 - Safety

  protocols that include this guideline template

### Child Relationships

- None

### Related Entities

- [Role](../../foundation/base_entity.md) - Roles responsible for implementing this guideline

---

## **Considerations**

- **Template Nature:** This template defines a standard safety guideline. Instance-specific variations or customizations

  belong on the copied instance within its specific context.

- **Copy Mechanism:** The process of copying this template definition into a target context needs to be handled by

  application logic.

- **Priority Management:** Guideline templates should have clear priority levels for implementation.
- **Role Assignment:** Guideline templates should specify which roles are responsible for implementation.

---
