---
tags:
  - standing
  - domain
  - tournament-performance
  - team-positioning
---

# Standing Domain

## Overview

The Standing Domain manages tournament performance tracking and position calculation for teams across different  
contexts (stages, disciplines, or combinations of disciplines). This domain focuses on calculating and maintaining  
current standings that reflect team performance within specific tournament contexts.

## Purpose

The primary purpose of the Standing Domain is to track and display team performance during tournaments by:

- Tracking team performance in stages, disciplines, or multi-discipline combinations
- Supporting multiple standings per team as they progress through the tournament
- Calculating current positions within each context (stage, discipline, or multi-discipline)
- Providing real-time position updates based on match results
- Enabling tournament progression decisions and seeding calculations
- Supporting qualification determinations and ranking system inputs

## Domain Models

### Standing (Entity)

The core model for tracking team standings within tournament contexts. See [Standing](./standing.md) for detailed documentation.

**Key Capabilities:**

- Supports standings for stages, disciplines, and multi-discipline combinations
- Tracks team positions and performance statistics (wins, draws, losses, points)
- Manages multiple concurrent standings per team across different scopes
- Provides real-time position updates as match results are recorded
- Enables context-specific validation rules and progression decisions

## Architecture Patterns

### Entity Structure

- **Standing**: Primary entity managing team position and performance within specific tournament contexts
- References external entities (Team, Discipline) via UUID
- Maintains performance statistics as embedded attributes
- Supports multiple scope types for flexible tournament structure

### Data Flow

1. **Match Results** → Performance statistics updated (wins, draws, losses, points)
2. **Statistics Update** → Position recalculation within scope context
3. **Position Changes** → Real-time standing updates across tournament systems
4. **Standing Data** → Tournament progression and seeding decision support

## Domain Scope

### In Scope

- In-tournament performance tracking and position calculation
- Stage-specific, discipline-specific, and multi-discipline standing calculations
- Real-time standing updates based on match results
- Performance statistics tracking (wins, draws, losses, points)
- Tournament progression support and qualification determinations
- Multiple concurrent standings per team across different contexts

### Out of Scope

- Pre-tournament ranking systems and historical performance analysis
- Tournament setup, configuration, and seeding algorithms
- Long-term performance tracking across multiple tournaments
- Complex analytics and performance trend analysis

## Integration Points

### Upstream Dependencies

- **Team Domain**: Team entity references for standing ownership
- **Discipline Domain**: Discipline context for scope-specific standings
- **Tournament Domain**: Tournament structure and stage context
- **Schedule Domain**: Match results triggering standing updates

### Downstream Consumers

- **Ranking Domain**: Standing data input for long-term ranking calculations
- **Tournament Domain**: Standing information for progression decisions
- **Reporting Systems**: Performance statistics and position data
- **User Interfaces**: Real-time standing displays and leaderboards

## Usage Patterns

### Standing Creation

```markdown
1. Team registers for tournament/stage/discipline
2. Initial standing created with zero statistics
3. Position calculated based on existing standings
```

### Standing Updates

```markdown
1. Match result recorded in Schedule domain
2. Standing statistics updated (wins/draws/losses/points)
3. Position recalculated within scope context
4. Real-time updates propagated to dependent systems
```

### Multi-Scope Management

```markdown
1. Team participates in multiple disciplines/stages
2. Separate standing instances maintained per scope
3. Multi-discipline standings aggregate across scope IDs
4. Independent updates based on scope-specific results
```

## See Also

- [Standing](./standing.md) - Core standing entity documentation
- [Team Domain](../team/README.md) - Team entity and management
- [Discipline Domain](../discipline/README.md) - Discipline-specific contexts
- [Tournament Domain](../tournament/README.md) - Tournament structure and stages
- [Schedule Domain](../schedule/README.md) - Match results and scheduling
- [Ranking Domain](../ranking/README.md) - Long-term ranking calculations
- [Foundation](../foundation/README.md) - Base entity patterns and standards
