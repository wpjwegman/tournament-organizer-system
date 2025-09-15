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

## Purpose

This value object enables comprehensive score tracking by:

- Recording quantitative performance metrics for teams during competitive fixtures
- Supporting diverse scoring formats from simple numeric values to complex structured data
- Maintaining chronological progression of scores throughout match duration
- Providing immutable score records for tournament integrity and historical analysis
- Enabling real-time score tracking and display for tournament stakeholders

## Structure

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Team** | Reference to the Team this score belongs to | UUID | Yes | References a team participating in the related Fixture. `team-uuid-A` |
| **Value** | Numerical or descriptive representation of the score | Text | Yes | Examples: `"15"`, `"3"` (goals), `"{\"sets\": 1, \"games\": 4, \"points\": \"AD\"}"` (tennis) |
| **Unit** | Specific metric used to quantify the performance | String | Optional | Example: "Points", "Goals", "Games", "Sets", "Rounds" |
| **Timestamp** | Date and time when the score was recorded | DateTime | Yes | `2024-10-27T10:30:00Z` |
| **Clock** | The time elapsed within the game/match when the score was recorded | String | Optional | `"15:32"`, `"Period 2, 08:15"`, `"Set 3, Game 5"` |
| **Notes** | Additional comments or context related to the score | Text | Optional | Example: "Final score of the match." |

## Considerations

- **Score Progression:** The order of Score objects within a Fixture helps maintain the chronological order of scores
- **Score Representation:** The Value field uses Text type to support various scoring formats:
  - Simple numeric scores (e.g., "15" for points)
  - Complex structured scores (e.g., tennis match with sets, games, points)  
  - Special states (e.g., "AD" for advantage in tennis)

## Example

### Basketball Championship Score Progression

```mermaid
graph TD
  S[Score: Team Eagles vs Team Hawks]
  S --> T[Team: eagles-uuid-123]
  S --> V[Value: "89"]
  S --> U[Unit: "Points"]
  S --> TS[Timestamp: 2024-11-15T21:45:00Z]
  S --> C[Clock: "Final"]
  S --> N[Notes: "Championship game final score"]
```

This example demonstrates a final basketball score for Team Eagles showing all score attributes: the team reference,  
numerical value representing total points, unit of measurement, precise timestamp of recording, game clock context,  
and additional notes providing match significance. This structure enables comprehensive score tracking throughout  
tournament progression while maintaining clear team attribution and temporal context.

## See Also

- [Fixture](./fixture.md) - Scheduled competition instances containing scores
- [Match](./match.md) - Competitive encounters between teams
- [Event](./event.md) - Specific occurrences that may affect scores
- [Team](../team/team.md) - Teams participating and achieving scores
- [Standing](../standing/standing.md) - Overall tournament standings derived from scores
