# **Team Domain**

## **Overview**

The Team domain defines the structure, management, and lifecycle of teams as the fundamental units of competition in the
Tournament Organizer system. It covers all aspects of team composition, roster management, player roles, and team
participation in tournaments and matches.

This domain supports both individual and group competition formats, ensuring flexibility and consistency across all
sports and activities.

## **Domain Structure**

### **Core Models**

- \*\*\*\*: Central entity representing a competition unit (single or multiple participants)
- **[Roster](../team/roster.md)**: Official list of players (starters, substitutes, reserves) for a team
- **[Player](roster/player/player.md)**: Instance of a registrant as a player in a specific context
- **[Seed](seed.md)**: Team seeding for tournament placement

### **Supporting Templates**

- \*\*\*\*: Template for team structure rules (active players, substitutes, gender composition)
- **[Position](roster/player/position.md)**: Template for field positions (e.g., Goalkeeper, Point Guard)

## **Template Entity Analysis**

### **Current Template Entities**

- **Team Format**: Defines standard team structure rules, copied or referenced for tournaments/matches
- **Position**: Standardizes field roles, referenced by players and rosters

### **Potential Template Entities**

- **Team Templates**: Standard team archetypes (e.g., "Default 5v5 Soccer Team")
- **Staff Role Templates**: Standard roles for coaches, managers, etc.
- **Roster Configuration Templates**: Standard roster setups for different sports

## **Status Lifecycle**

### **Team Statuses**

- **Draft**: Team is being created/configured
- **Active**: Team is eligible and participating
- **Locked**: Team roster is locked for competition
- **Suspended**: Team is temporarily ineligible
- **Archived**: Team is preserved for historical reference

### **Roster Statuses**

- **Active**: Roster is current and modifiable
- **Locked**: Roster is fixed for a match or stage
- **Archived**: Roster is preserved for history

### **Player Statuses**

- **Active**: Player is available for selection
- **Benched**: Player is not starting but available
- **Injured**: Player is unavailable due to injury
- **Suspended**: Player is temporarily ineligible

### **Lifecycle Transitions**

- Team: Draft → Active → Locked/Suspended → Archived
- Roster: Active → Locked → Archived
- Player: Active ↔ Benched/Injured/Suspended

## **Relationships & Cross-References**

- **Team ↔ Organization**: Teams may be affiliated with or sponsored by organizations
- **Team ↔ Player**: Teams manage a roster of players
- **Team ↔ Activity Discipline**: Teams participate in specific disciplines
- **Team ↔ Match**: Teams compete in matches
- **Roster ↔ Player**: Rosters manage player roles and status
- **Roster ↔ Team Format**: Rosters are validated against team format rules
- **Player ↔ Registrant**: Players are instances of registrants in a competition context
- **Player ↔ Position**: Players are assigned field positions
- **Seed ↔ Team**: Seeds determine team placement in tournaments

## **Quality Standards**

- All models include comprehensive attribute documentation
- Cross-references are accurate and up to date
- Status lifecycles are clearly defined
- Template entity usage is documented
- Practical examples are provided where relevant
- Consistent formatting and terminology throughout

## **Implementation Guidelines**

- Validate team and roster composition against discipline and tournament rules
- Enforce status transitions and lifecycle rules
- Use template entities for standardization and efficiency
- Maintain accurate cross-references between all related models
- Regularly review and update documentation for clarity and completeness

## **Related Domains**

- \*\*\*\*: Tournament structure and management
- \*\*\*\*: Match and event scheduling
- \*\*\*\*: Financial management
- \*\*\*\*: Registrant and participant management

---

**Last Updated**: June 24, 2025 **Version**: 1.0 **Status**: Active **Next Review**: July 24, 2025

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity and Template patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event team management

  standards

## See Also

- [Team](../team/team.md)
- [Roster](../team/roster.md)
- [Seed](../team/seed.md)
- [Roster README](../team/roster/README.md)
- [Tournament README](../tournament/README.md)
- [Schedule README](../schedule/README.md)
- [Discipline README](../discipline/README.md)
- [Registration README](../registration/README.md)
- [Organization README](../organization/README.md)
- [Standing README](../standing/README.md)
- [Business README](../README.md)
