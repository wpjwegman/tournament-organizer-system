# **Standing** (Data Model - Entity)

## **Introduction**

A **Standing** Entity represents a team's position and performance within a specific scope of a tournament. A team can
have multiple standings instances as they progress through different stages and disciplines. The scope can be:

- A specific stage (e.g., group stage, quarter-finals)
- A specific discipline (e.g., tennis, chess)
- A combination of disciplines (e.g., overall tournament standing)

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status` [e.g., Active, Inactive], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute     | Description                                                                              | Type       | Required | Notes / Example                                            |
| ------------- | ---------------------------------------------------------------------------------------- | ---------- | -------- | ---------------------------------------------------------- |
| **Scope**     | The type of standing (Stage, Discipline, or Multi-Discipline).                           | String     | Yes      | `"STAGE"`, `"DISCIPLINE"`, `"MULTI_DISCIPLINE"`            |
| **Scope IDs** | References to the specific scopes (Stage ID, Discipline ID, or multiple Discipline IDs). | List[UUID] | Yes      | For multi-discipline, contains all relevant discipline IDs |
| **Position**  | The current ranking position in this scope.                                              | Integer    | Yes      | `1`, `2`, `3`                                              |
| **Team**      | Reference to the [Team](../team/team.md) this standing represents.         | UUID       | Yes      | Links to the team's profile and details.                   |
| **Points**    | Total points accumulated according to the scoring rules.                                 | Integer    | Yes      | `25`, `18`, `12`                                           |
| **Wins**      | Number of matches won by the team.                                                       | Integer    | Yes      | `8`, `5`, `3`                                              |
| **Draws**     | Number of matches drawn by the team.                                                     | Integer    | Yes      | `2`, `1`, `0`                                              |
| **Losses**    | Number of matches lost by the team.                                                      | Integer    | Yes      | `1`, `3`, `5`                                              |

## **Relationships**

- A `Standing` is linked to a specific [Team](../team/team.md)
- Based on Scope, a `Standing` is linked to:

  - A (for stage standings)
  - A [Discipline](../discipline/discipline.md) (for discipline standings)
  - Multiple disciplines (for multi-discipline standings)

- Can be used as a basis for in subsequent stages or tournaments

## **Considerations**

- **Scope-Specific Rules:**

  - Stage standings: Used for stage progression and seeding
  - Discipline standings: Track performance within a specific discipline
  - Multi-discipline standings: Aggregate performance across all referenced disciplines

- **Multiple Standings:**

  - A team can have multiple standings instances
  - Each instance represents performance in a specific scope
  - Standings are updated independently based on their scope
  - Changes in one scope may affect related standings

- **Validation Rules:**

  - Scope and Scope IDs must be consistent
  - Team must be eligible for all referenced scopes
  - For discipline standings, team must be registered in that discipline
  - For stage standings, team must be participating in that stage
  - For multi-discipline standings, team must be participating in all referenced disciplines

- **Position Updates:**

  - Recalculated whenever Points, Wins, Draws, or Losses change
  - Updates occur in real-time as match results are recorded
  - Different calculation rules may apply based on scope

- **Ranking Usage:**

  - Can be used to update team rankings
  - Can serve as a basis for seeding
  - May influence qualification for other tournaments

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event performance tracking

  standards

## See Also

- [Standing README](../standing/README.md)
- [Team README](../team/README.md)
- [Discipline README](../discipline/README.md)
- [Tournament README](../tournament/README.md)
- [Schedule README](../schedule/README.md)
- [Ranking README](../ranking/README.md)
- [Business README](../README.md)
