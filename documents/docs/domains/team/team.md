# **Team** (Data Model - Entity)

## **Introduction**

A **Team** Entity represents the fundamental unit of competition in tournaments, regardless of its size. Whether
consisting of a single player or multiple participants, all competitive entities are treated as teams within the system.
This unified approach simplifies tournament management, match scheduling, and result tracking while maintaining
consistency across different competition formats.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute        | Description                                                                         | Type       | Required | Notes / Example                                                                          |
| ---------------- | ----------------------------------------------------------------------------------- | ---------- | -------- | ---------------------------------------------------------------------------------------- |
| **Name**         | Official title or designation of the team.                                          | String     | Yes      | `"Alpha Eagles"`, `"Thunder Strikers"`                                                   |
| **Organization** | Reference to the this team belongs to or is sponsored by.                           | UUID       | No       | `org-uuid-123` (Company) or `org-uuid-456` (Sponsor)                                     |
| **Roster**       | [List of players](../team/roster.md)                                  | List[UUID] | Yes      | References to Player entities. `[player-uuid-abc, player-uuid-def]`                      |
| **Disciplines**  |                                                                                     | List[UUID] | Yes      | References to Activity Discipline entities. `[discipline-uuid-123, discipline-uuid-456]` |
| **Staff**        | Coaches, managers, and supporting personnel.                                        | List[UUID] | No       | References to User entities with staff roles. `[user-uuid-789, user-uuid-012]`           |
| **Seed**         | [Team's initial placement](seed.md)     | UUID       | No       | Reference to Seed entity. `seed-uuid-abc`                                                |
| **Media**        | Optional list of references (by ID) to \*\*\*\* entities associated with this team. | List[UUID] | Optional | Example: `[media-a1b2c3d4-e5f6-4890-1234-567890abc099]`                                  |

---

## **Relationships**

- A `Team` Entity optionally references an \*\*\*\* (via `Organization`) for company affiliation or sponsorship.
- It references multiple \*\*\*\* entities via the `Roster` attribute.
- It references multiple \*\*\*\* entities via the `Disciplines` attribute.
- It optionally references multiple \*\*\*\* entities via the `Staff` attribute.
- It optionally references a [Seed](seed.md) entity

  via the `Seed` attribute.

- It may be referenced by \*\*\*\* entities as a participant.
- It may be referenced by \*\*\*\* entities for performance tracking.

---

## **Considerations**

- **Organization Types:** The `Organization` reference can represent either a company affiliation or a sponsorship

  relationship.

- **Roster Management:** The `Roster` list must be validated against the team's active disciplines and format

  requirements.

- **Staff Roles:** Staff members must have appropriate roles and permissions assigned.
- **Lifecycle:** The team's status affects its participation eligibility and visibility.
- **Seed Management:** The `Seed` is typically assigned during tournament registration or qualification.
- **Single Player Teams:** Even teams with only one player in their roster are treated as full teams for all tournament

  operations.

---
