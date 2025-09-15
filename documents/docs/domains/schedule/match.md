---
tags:
  - match
  - template-entity
  - competition
  - team-encounter
---

# Match (Template Entity)

## Overview

A Match Entity represents a competitive encounter between teams. It is a simple entity that links the teams  
participating in the match.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

## Structure

This template entity includes standard attributes from the [Base Entity](../foundation/base_entity.md)  
and adds the following match-specific attributes:

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Teams** | List of teams participating in the match | List[UUID] | Yes | Example: `[550e8400-e29b-41d4-a716-446655440000, 6ba7b810-9dad-11d1-80b4-00c04fd430c8]` |

## Relationships

- A Match Entity references multiple Team entities via the Teams attribute

## Considerations

- **Team References:** The Teams list should contain valid references to existing Team entities
- **Minimum Teams:** A match should have at least two teams

## See Also

- [Schedule](./schedule.md) - Tournament scheduling and coordination
- [Fixture](./fixture.md) - Scheduled competition instances  
- [Event](./event.md) - Specific occurrences during matches
- [Score](./score.md) - Team scores and results
- [Team](../team/team.md) - Team structure and participation
- [Base Entity](../foundation/base_entity.md) - Common entity structure and lifecycle
