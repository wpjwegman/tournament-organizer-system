# **Unit** (Data Model - Entity)

## **Introduction**

A **Unit** is an **Entity** representing a distinct division within an (e.g., department, team, project group). It
includes relationships with other units and defines the people involved through memberships.

As an entity, it has its own identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md).

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute               | Description                                                                                                                                                                  | Type         | Required | Notes / Example                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                | Defines the role or category of the unit.                                                                                                                                    | String       | Yes      | Example: "Division", "Department", "Team", "Project Group", "Committee", "Working Group"                                                       |
| **Name**                | Clear and identifiable label for the unit.                                                                                                                                   | String       | Yes      | Should be unique within the organization. Example: "Marketing Department"                                                                      |
| **Description**         | Explanation of the unit's purpose, responsibilities, scope.                                                                                                                  | String       | Optional | Example: "Handles all marketing activities for the organization."                                                                              |
| **Contact Information** | Reference (by ID) to the unit's \*\*\*\*.                                                                                                                                    | UUID         | Optional | Example: `550e8400-e29b-41d4-a716-446655440000`                                                                                                |
| **Units**               | List of references to related **[Unit](unit.md)** entities with their relationship types.                  | List[Object] | No       | Example: `[{"id": "550e8400-e29b-41d4-a716-446655440000", "type": "parent"}, {"id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8", "type": "child"}]` |
| **Members**             | List of **[Member](member.md)** assigned to this unit, each with their role assignments. | List[Object] | No       | Example: `[{"id": "550e8400-e29b-41d4-a716-446655440000", "roles": ["6ba7b810-9dad-11d1-80b4-00c04fd430c8"]}]`                                 |

---

## **Relationships**

- A `Unit` **Entity** represents a specific division within an organization.
- It holds a reference to its `Contact Information`.
- It can reference other `Unit` entities to define hierarchical and collaborative relationships.
- It can have `Member` records assigned to it, each with their specific role assignments.

### Parent Relationships

- - The organization that contains this unit

### Child Relationships

- [Member](member.md) - Members

  assigned to this unit with their roles

### Related Entities

- [Unit](unit.md) - Related units (parent, child, or related)
- - Unit's contact information

---

## **Considerations**

- **Naming:** `Name` should uniquely identify this unit within its organization.
- **Unit Relationships:**

  - The `Units` attribute defines all relationships with other units
  - Each relationship includes the unit ID and relationship type (parent, child, related)
  - Circular references should be prevented
  - A unit can have multiple relationships of different types

- **Member Management:**

  - Members are assigned to the unit with specific roles
  - Members can have multiple roles within the unit
  - Member assignments can be updated as needed

---
