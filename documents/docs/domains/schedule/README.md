# **Schedule Domain**

## **Overview**

The Schedule domain manages the organization, timing, and execution of all tournament events and competitions. It
provides a comprehensive framework for scheduling fixtures, managing matches, tracking scores and events, and
coordinating officials across all tournament activities.

This domain ensures proper resource allocation, timing coordination, and event progression tracking while maintaining
flexibility for different tournament formats and requirements.

## **Domain Structure**

### **Core Models**

- \*\*\*\*: Container for organizing and managing collections of fixtures
- \*\*\*\*: Specific scheduled competition instances with time, location, and operational details
- \*\*\*\*: Competitive encounters between teams
- \*\*\*\*: Value object for specific time intervals (start/end times)
- \*\*\*\*: Records specific occurrences during matches (penalties, warnings, substitutions)
- **[Score](../schedule/score.md)**: Value object for team scores in fixtures with progression tracking

### **Supporting Models**

- **[Official](official/official.md)**: Individuals acting in official capacities (referees, judges, umpires)
- **[Qualification](official/qualification.md)**: Official certifications and qualifications

## **Template Entity Analysis**

### **Current Template Entities**

- **Schedule**: Can be templated for standard schedule types (main, practice, stage-specific)
- **Fixture**: Can be templated for standard fixture configurations
- **Official**: Can be templated for standard official roles and qualifications

### **Potential Template Entities**

- **Timeslot Templates**: Standard time intervals for different sports/activities
- **Event Templates**: Standard event types and descriptions
- **Score Templates**: Standard scoring formats for different sports

## **Status Lifecycle**

### **Schedule Statuses**

- **Draft**: Schedule is being created/configured
- **Published**: Schedule is available for viewing
- **Active**: Schedule is currently in use
- **Completed**: All fixtures in schedule are finished

### **Fixture Statuses**

- **Scheduled**: Fixture is planned but not confirmed
- **Confirmed**: Fixture is confirmed and ready
- **In Progress**: Fixture is currently running
- **Completed**: Fixture has finished
- **Cancelled**: Fixture was cancelled
- **Postponed**: Fixture was postponed

### **Match Statuses**

- **Scheduled**: Match is planned
- **In Progress**: Match is currently running
- **Completed**: Match has finished
- **Cancelled**: Match was cancelled

### **Event Statuses**

- **Recorded**: Event has been recorded
- **Reviewed**: Event has been reviewed
- **Overturned**: Event was overturned/changed

### **Official Statuses**

- **Active**: Official is available for assignments
- **Inactive**: Official is not available
- **Pending**: Official status is being reviewed

### **Lifecycle Transitions**

- Schedule: Draft → Published → Active → Completed
- Fixture: Scheduled → Confirmed → In Progress → Completed/Cancelled/Postponed
- Match: Scheduled → In Progress → Completed/Cancelled
- Event: Recorded → Reviewed → Overturned
- Official: Pending → Active ↔ Inactive

## **Relationships & Cross-References**

- **Schedule ↔ Fixture**: Groups and organizes fixtures
- **Fixture ↔ Match**: Links scheduled time/location to competitive encounter
- **Fixture ↔ Timeslot**: Defines when the fixture occurs
- **Fixture ↔ Area**: Defines where the fixture occurs
- **Fixture ↔ Official**: Assigns officials to fixtures
- **Fixture ↔ Score**: Tracks scores during the fixture
- **Fixture ↔ Event**: Records events during the fixture
- **Match ↔ Team**: Links teams participating in the match
- **Event ↔ Match/Team**: Records events with context and team
- **Score ↔ Fixture/Team**: Records scores with context and team
- **Official ↔ Human Profile**: Links official to their profile

## **Quality Standards**

- All models include comprehensive attribute documentation
- Cross-references are accurate and up to date
- Status lifecycles are clearly defined
- Template entity usage is documented
- Practical examples are provided where relevant
- Consistent formatting and terminology throughout

## **Implementation Guidelines**

- Validate fixture scheduling against venue and official availability
- Enforce status transitions and lifecycle rules
- Use template entities for standardization and efficiency
- Maintain accurate cross-references between all related models
- Regularly review and update documentation for clarity and completeness

## **Related Domains**

- \*\*\*\*: Tournament structure and management
- \*\*\*\*: Team structure and management
- \*\*\*\*: Venue and area management
- \*\*\*\*: Registrant and participant management

---

**Last Updated**: June 24, 2025 **Version**: 1.0 **Status**: Active **Next Review**: July 24, 2025

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity and Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event scheduling standards

## See Also

- [Schedule](../schedule/schedule.md)
- [Fixture](../schedule/fixture.md)
- [Match](../schedule/match.md)
- [Timeslot](../schedule/timeslot.md)
- [Event](../schedule/event.md)
- [Score](../schedule/score.md)
- [Official README](../schedule/official/README.md)
- [Tournament README](../tournament/README.md)
- [Team README](../team/README.md)
- [Venue README](../venue/README.md)
- [Registration README](../registration/README.md)
- [Business README](../README.md)
