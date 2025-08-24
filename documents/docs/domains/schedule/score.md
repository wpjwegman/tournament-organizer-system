# **Score** (Data Model - Value Object)

## **Introduction**

A **Score** Value Object represents the score a team achieves in a fixture. It is embedded within a and does not have
its own identity or lifecycle. The order of scores is determined by the list in the fixture.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

| Attribute     | Description                                                                                                  | Type     | Required | Notes / Example                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------ | -------- | -------- | --------------------------------------------------------------------------------------------- |
| **Team**      | Reference to the this score belongs to.                                                                      | UUID     | Yes      | References a team participating in the related Fixture. `team-uuid-A`                         |
| **Value**     | Numerical or descriptive representation of the score.                                                        | Text     | Yes      | Examples: `"15"`, `"3"` (goals), `"{\"sets\": 1, \"games\": 4, \"points\": \"AD\"}"` (tennis) |
| **Unit**      | Specific metric used to quantify the performance.                                                            | String   | Optional | Example: "Points", "Goals", "Games", "Sets", "Rounds"                                         |
| **Timestamp** | Date and time when the score was recorded.                                                                   | DateTime | Yes      | `2024-10-27T10:30:00Z`                                                                        |
| **Clock**     | (Optional) The time elapsed within the game/match when the score was recorded (e.g., period, minute:second). | String   | Optional | `"15:32"`, `"Period 2, 08:15"`, `"Set 3, Game 5"`                                             |
| **Notes**     | Additional comments or context related to the score.                                                         | Text     | Optional | Example: "Final score of the match."                                                          |

---

## **Relationships**

- A `Score` Value Object is always embedded within a and is not referenced by ID.
- The sequence of Score objects within a Fixture describes the progression of the match.

---

## **Considerations**

- **Score Progression:** The order of Score objects within a Fixture helps maintain the chronological order of scores.
- **Score Representation:** The `Value` field uses Text type to support various scoring formats:

  - Simple numeric scores (e.g., "15" for points)
  - Complex structured scores (e.g., tennis match with sets, games, points)
  - Special states (e.g., "AD" for advantage in tennis)

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event scoring standards

## See Also

- [Schedule README](../schedule/README.md)
- [Fixture](../schedule/fixture.md)
- [Match](../schedule/match.md)
- [Team README](../team/README.md)
- [Standing README](../standing/README.md)
- [Business README](../README.md)

---
