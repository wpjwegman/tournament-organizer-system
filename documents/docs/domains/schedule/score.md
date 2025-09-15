---
tags:
  - score
  - value-object
  - team-scoring
  - match-results
---

# Score (Value Object)

## Overview

A Score Value Object represents the score a team achieves in a fixture. It is embedded within a Fixture and does not  
have its own identity or lifecycle. The order of scores is determined by the Teams list in the fixture.

## Structure

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Team** | Reference to the Team this score belongs to | UUID | Yes | References a team participating in the related Fixture. `team-uuid-A` |
| **Value** | Numerical or descriptive representation of the score | Text | Yes | Examples: `"15"`, `"3"` (goals), `"{\"sets\": 1, \"games\": 4, \"points\": \"AD\"}"` (tennis) |
| **Unit** | Specific metric used to quantify the performance | String | Optional | Example: "Points", "Goals", "Games", "Sets", "Rounds" |
| **Timestamp** | Date and time when the score was recorded | DateTime | Yes | `2024-10-27T10:30:00Z` |
| **Clock** | The time elapsed within the game/match when the score was recorded | String | Optional | `"15:32"`, `"Period 2, 08:15"`, `"Set 3, Game 5"` |
| **Notes** | Additional comments or context related to the score | Text | Optional | Example: "Final score of the match." |

## Relationships

- A Score Value Object is always embedded within a Fixture and is not referenced by ID
- The sequence of Score objects within a Fixture describes the progression of the match

## Considerations

- **Score Progression:** The order of Score objects within a Fixture helps maintain the chronological order of scores
- **Score Representation:** The Value field uses Text type to support various scoring formats:
  - Simple numeric scores (e.g., "15" for points)
  - Complex structured scores (e.g., tennis match with sets, games, points)  
  - Special states (e.g., "AD" for advantage in tennis)

## See Also

- [Fixture](./fixture.md) - Scheduled competition instances containing scores
- [Match](./match.md) - Competitive encounters between teams
- [Event](./event.md) - Specific occurrences that may affect scores
- [Team](../team/team.md) - Teams participating and achieving scores
- [Standing](../standing/standing.md) - Overall tournament standings derived from scores
