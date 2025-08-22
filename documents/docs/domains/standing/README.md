# Standing Domain

## Overview

The Standing Domain manages the in-tournament performance tracking and position calculation for teams across different
contexts (stages, disciplines, or combinations of disciplines). This domain focuses on calculating and maintaining
current standings that reflect team performance within specific tournament contexts.

## Purpose

The primary purpose of the Standing Domain is to track and display team performance during tournaments by:

- Tracking team performance in stages, disciplines, or multi-discipline combinations
- Supporting multiple standings per team as they progress through the tournament
- Calculating current positions within each context (stage, discipline, or multi-discipline)
- Providing real-time position updates
- Enabling tournament progression decisions
- Supporting seeding and ranking calculations

## Current Models

### Standing

The core model for tracking team standings. See for detailed documentation.

Key aspects:

- Supports standings for stages, disciplines, and multi-discipline combinations
- Tracks team positions in each context
- Manages performance statistics (wins, draws, losses)
- Calculates points based on context-specific rules
- Enables multiple standings per team
- Provides basis for tournament progression and rankings

## Domain Scope

### In Scope

- In-tournament performance tracking
- Stage-specific standing calculations
- Discipline-specific standing calculations
- Multi-discipline standing aggregation
- Real-time standing updates
- Performance statistics tracking
- Tournament progression support
- Multiple standings per team
- Context-specific validation rules

### Out of Scope

- Pre-tournament ranking systems
- Tournament seeding
- Historical performance tracking
- Ranking period management
- Qualification systems
- Long-term performance analysis
- Tournament setup and configuration

## Future Considerations

While not currently implemented, the following aspects may be considered for future development:

- Advanced standing calculation methods
- Complex multi-discipline scoring systems
- Real-time standing visualization
- Performance trend analysis
- Custom standing rule engines
- Advanced statistics and analytics
- Automated standing updates
- Context-specific standing rules (stage, discipline, multi-discipline)

## Related Documentation

- - For tournament stage management
- [Team Model](../team/team.md) - For team information
- [Discipline Model](../discipline/discipline.md) - For discipline-specific rules
- - For stage-specific standing calculations
- - For ranking and seeding
- - For core entity attributes

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event performance tracking

  standards

## See Also

- [Standing](../standing/standing.md)
- [Tournament README](../tournament/README.md)
- [Team README](../team/README.md)
- [Discipline README](../discipline/README.md)
- [Schedule README](../schedule/README.md)
- [Ranking README](../ranking/README.md)
- [Foundation README](../foundation/README.md)
- [Business README](../README.md)
