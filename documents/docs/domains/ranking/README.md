# Ranking Domain

## Overview

The Ranking Domain handles the pre-tournament ranking systems used for tournament seeding and initial team placement.
This domain focuses on calculating and maintaining team rankings that serve as the foundation for tournament seeding
decisions.

## Purpose

The primary purpose of the Ranking Domain is to provide a fair and accurate basis for tournament seeding by:

- Maintaining historical performance records
- Calculating team rankings across different time periods
- Supporting discipline-specific ranking systems
- Enabling cross-discipline ranking normalization
- Providing the foundation for tournament seeding decisions

## Current Models

### Ranking

The core model for storing team rankings. See [Ranking Model](../ranking/ranking.md) for detailed
documentation.

Key aspects:

- Stores team ranking positions
- Tracks ranking points
- Maintains ranking history
- Links to teams and disciplines
- Supports ranking period management
- Enables seeding system integration

## Domain Scope

### In Scope

- Ranking calculation and storage
- Historical ranking tracking
- Ranking period management
- Seeding system integration
- Discipline-specific rankings
- Cross-discipline ranking normalization
- Ranking validation and verification

### Out of Scope

- In-tournament performance tracking
- Stage-specific standings
- Match result processing
- Tournament progression
- Real-time performance updates
- Multi-discipline aggregation
- Tournament stage management

## Future Considerations

While not currently implemented, the following aspects may be considered for future development:

- Advanced ranking algorithms (ELO, Glicko, etc.)
- Ranking decay systems
- Qualification threshold management
- Ranking visualization and reporting
- Historical ranking analysis
- Custom ranking rule engines
- Ranking period automation

## Related Documentation

- - For tournament seeding and setup
- [Team Model](../team/team.md) - For team information
- [Discipline Model](../discipline/discipline.md) - For discipline-specific ranking rules
- - For core entity attributes

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event ranking and seeding

  standards

## See Also

- [Ranking](../ranking/ranking.md)
- [Team](../team/team.md)
- [Discipline](../discipline/discipline.md)
- [Tournament README](../tournament/README.md)
- [Business README](../README.md)
