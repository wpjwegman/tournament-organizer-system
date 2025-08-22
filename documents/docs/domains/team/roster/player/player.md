# **Player** (Data Model - Entity)

## **Introduction**

A **Player** Entity represents a specific instance of a participating in a defined context, such as competing in an .

It captures context-specific attributes (e.g., jersey number, role, position) and links back to the core `Registrant`
entity, which contains the fundamental identity and profile information.

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../../foundation/base_entity.md).

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status` [e.g., Active, Inactive, Suspended], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity](../../../foundation/base_entity.md).

| Attribute         | Description                                                                                                                                                               | Type    | Required | Notes / Example                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------------------------------------------------------ |
| **Registrant**    | Reference to the core entity containing identity and profile information.                                                                                                 | UUID    | Yes      | `550e8400-e29b-41d4-a716-446655440000`                       |
| **Jersey Number** | The player's jersey or uniform number for this specific context.                                                                                                          | Integer | Optional | `10`, `23`, `99`                                             |
| **Position**      | Reference to the player's assigned [Position](position.md) in this context. | UUID    | Optional | `position-uuid-goalkeeper`                                   |
| **Role**          | The player's role or responsibility within the team or competition.                                                                                                       | String  | Optional | `"Captain"`, `"Vice Captain"`, `"Starter"`, `"Substitute"`   |
| **Status**        | Current participation status of the player in this context.                                                                                                               | String  | Yes      | `"Active"`, `"Injured"`, `"Suspended"`, `"Inactive"`         |
| **Notes**         | Additional context-specific notes about the player's participation.                                                                                                       | Text    | Optional | `"Team captain for 2024 season"`, `"Recovering from injury"` |

---

## **Relationships**

- A `Player` Entity is linked to one entity.
- A `Player` Entity may be assigned to one [Position](position.md) within a team context.
- A `Player` Entity may participate in multiple entities.
- A `Player` Entity belongs to one entity.

### Parent Relationships

- - The core identity and profile information
- - The team this player belongs to

### Child Relationships

- None

### Related Entities

- [Position](position.md) - The player's assigned position
- - Matches the player participates in
- - The context of participation

---

## **Considerations**

- **Context-Specific:** Player entities are created for specific contexts (e.g., a tournament, season, or team).
- **Registrant Link:** Always links back to a Registrant entity for core identity information.
- **Position Assignment:** Players may be assigned to specific positions within their team context.
- **Status Management:** Player status can change throughout their participation period.
- **Jersey Numbers:** Jersey numbers should be unique within a team context.

---
