# **Roster** (Data Model - Template Entity)

## **Introduction**

A **Roster** Template Entity defines a reusable blueprint for roster structures and configurations that can be used to
create specific roster instances. It provides a standardized framework for roster types, player roles, and team
composition patterns that can be applied across different contexts and tournaments.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute       | Description                                                                 | Type   | Required | Notes / Example                                |
| --------------- | --------------------------------------------------------------------------- | ------ | -------- | ---------------------------------------------- |
| **Name**        | The name of the roster template.                                            | String | Yes      | `"Standard Roster"`, `"Tournament Roster"`     |
| **Type**        | The type of roster template.                                                | String | Yes      | `"Competitive"`, `"Recreational"`, `"Tournament"` |
| **Description** | Description of the roster template and its characteristics.                 | Text   | Optional | `"Standard competitive roster structure"`      |
| **Max Starters** | Maximum number of starters for this roster template.                       | Integer| Yes      | `5`, `11`, `15`                                |
| **Max Substitutes** | Maximum number of substitutes for this roster template.                   | Integer| Yes      | `3`, `5`, `7`                                  |
| **Max Reserves** | Maximum number of reserves for this roster template.                       | Integer| Optional | `2`, `3`, `5`                                  |
| **Player Roles** | Standard player roles for this roster template.                            | List[String] | Yes | `["Starter", "Substitute", "Reserve"]`         |
| **Requirements** | Standard requirements for this roster template.                            | List[String] | Optional | `["Minimum 8 players", "Maximum 15 players"]`  |

---

## **Relationships**

- A `Roster` Template Entity may be referenced by roster instance entities.
- A `Roster` Template Entity may be associated with team template entities.
- A `Roster` Template Entity may be associated with player template entities.
- A `Roster` Template Entity may be referenced by tournament template entities.

### Parent Relationships

- Team templates - The team template this roster template belongs to
- Tournament templates - The tournament template this roster template is used in

### Child Relationships

- Roster instances - Specific rosters created from this template
- Player instances - Player assignments using this roster template

### Related Entities

- Player templates - Player types that can be part of this roster template
- Match templates - Match types this roster template can be used in

---

## **Considerations**

- **Template Nature:** This template defines a standard roster type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a specific team's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a specific team)

  needs to be handled by application logic.

- **Template Management:**

  - Templates should be curated and maintained by team administrators
  - New templates can be added based on roster standards and organizational requirements
  - Templates should be reviewed periodically for effectiveness and fairness

- **Role Management:**

  - **STARTER:** Primary players who begin the match
  - **SUBSTITUTE:** Players who can replace starters during a match
  - **RESERVE:** Players who can replace starters/substitutes before a match begins

- **Role Transitions:**

  - Substitutes can be activated during a match
  - Reserves can only be activated before a match begins
  - Role changes must follow tournament rules

- **Status Tracking:**

  - Each player's status affects their availability
  - Status changes must be tracked and validated
  - Roster status affects its modifiability

- **Validation Rules:**

  - Must respect maximum numbers for each role type
  - Must follow tournament substitution rules
  - Must maintain proper team composition

- **Customization Balance:**

  - Templates provide structure while allowing personalization
  - Customizations should not break the fundamental roster structure
  - System should support both template-based and fully custom rosters

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event roster management

  standards

## See Also

- [Roster README](../../team/roster/README.md)
- [Team README](../../team/README.md)
- [Team](../../team/team.md)
- [Roster](../../team/roster.md)
- [Identity README](../../identity/README.md)
- [Discipline README](../../discipline/README.md)
- [Schedule README](../../schedule/README.md)
- [Business README](../../README.md)

---
