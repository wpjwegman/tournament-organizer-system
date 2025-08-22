# **Ranking** (Data Model - Template Entity)

## **Description**

An entity representing a calculated position for a team within a tournament's ranking list. Rankings are used to
evaluate performance, determine seeding, track progress, and provide a basis for awards. Standings
([Standing](../standing/standing.md)) typically represent positions within intermediate stages like groups
or poules.

---

## **Attributes**

| Attribute     | Type     | Description                                                           | Required | Notes / Example        |
| ------------- | -------- | --------------------------------------------------------------------- | -------- | ---------------------- |
| **Team**      | UUID     | Identifier of the [Team](../team/team.md) being ranked. | Yes      | `team-uuid-abc`        |
| **Position**  | Integer  | The numerical rank position (e.g., 1, 2, 3).                          | Yes      | `1`, `5`, `100`        |
| **Points**    | Decimal  | The points associated with this position, if applicable.              | No       | `1250.75`, `800.0`     |
| **Timestamp** | DateTime | When the ranking was calculated or published.                         | Yes      | `2024-07-26T10:00:00Z` |

---

## **Relationships**

- **Team:** The `Team` attribute links to a specific [Team](../team/team.md).
- Rankings are often derived from or final [Standings](../standing/standing.md) calculated via a .
- This Ranking is embedded within a [Tournament](../tournament/tournament.md), which provides the context

  and scope for the ranking list.

---

## **Considerations**

- **Seeding Usage:** Rankings are primarily used for tournament seeding and initial team placement.
- **Historical Tracking:** The system maintains historical ranking records to track team performance over time. The

  status field from the base entity model is used to indicate if a ranking is current or historical.

- **Discipline Context:** Rankings may be discipline-specific or cross-discipline depending on the tournament type.
- **Update Frequency:** Rankings are typically updated periodically, not in real-time.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event ranking and seeding

  standards

## See Also

- [Ranking README](../ranking/README.md)
- [Team](../team/team.md)
- [Standing](../standing/standing.md)
- [Tournament](../tournament/tournament.md)
- [Discipline README](../discipline/README.md)
- [Business README](../README.md)
