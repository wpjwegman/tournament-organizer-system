# **Position** (Data Model - Template Entity)

## **Introduction**

A **Position** Entity Template defines a reusable blueprint for a specific role or location occupied by a participant
within the context of a team-based activity (e.g., Goalkeeper, Point Guard, Setter).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../../foundation/base_entity.md). It serves as a standard
definition that can be referenced when configuring team formats, assigning roles, or describing player capabilities. The
specific sport or activity context is determined by how this template is used (e.g., referenced within a `Team Format`
linked to an [Activity Discipline](../../../../discipline/discipline.md)).

Using Field Position templates helps to:

- Standardize terminology for roles.
- Configure team formats by specifying required or allowed positions.
- Assign specific, standardized roles to players on a roster.
- Facilitate strategy discussions with clear role definitions.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status` [e.g., Active, Deprecated], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity](../../../foundation/base_entity.md).

| Attribute       | Description                                                                                                | Type    | Required | Notes / Example                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------------------------------------------------------------------------------------ |
| **Name**        | A human-readable name identifying the position template (e.g., a role name, position designation).         | String  | Yes      | E.g., "Goalkeeper", "Point Guard", "Setter", "Forward"                                     |
| **Description** | Optional detailed description of the position template, its purpose, or general responsibilities.          | Text    | Optional | "Defensive player responsible for preventing goals."                                       |
| **Type**        | Categorizes the primary purpose or type of the position template.                                          | String  | Yes      | E.g., "Offensive", "Defensive", "Specialist", "Utility"                                    |
| **Number**      | A numeric identifier used for ordering and sorting positions within their context.                         | Integer | Yes      | E.g., `1`, `2`, `3` for sequential ordering, or `10`, `20`, `30` for hierarchical ordering |
| **Notes**       | General notes about the configuration, requirements, or specific characteristics of this type of position. | Text    | Optional | "Requires specialized training.", "Must be physically fit."                                |

---

## **Relationships**

- A `Position` Entity Template is referenced by a \*\*\*\* to define available positions.
- It may be referenced by \*\*\*\* entities to indicate their assigned position.
- When the parent `Team Format` template is copied into a `Tournament`, this `Position` template definition is also

  copied as part of that structure.

---

## **Considerations**

- **Template Nature:** Defines a standard position configuration. Instance-specific details (player assignments,

  performance notes) belong on the copied instance within the `Tournament`.

- **Copy Mechanism:** Part of the larger team format template copy process.
- **Sport Context:** Position templates are typically used within specific sport or activity contexts.
- **Number Assignment:** Position numbers help with ordering and identification within team formats.

---
