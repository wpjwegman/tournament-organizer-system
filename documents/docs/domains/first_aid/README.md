# First Aid Domain (Business Model Documentation)

## Introduction

The First Aid domain provides a structured way to define, manage, and implement standardized first aid protocols across
tournaments. This includes medical emergency procedures, injury response protocols, and safety guidelines that can be
consistently applied while allowing for tournament-specific customization.

## Key Concepts

- **Protocol:** A template defining a complete set of procedures for a specific medical situation or injury.
- **Symptom:** Observable indicators that help identify a medical situation.
- **Instruction:** An actionable instruction in the first aid procedure.
- **Escalation:** Conditions that require professional medical intervention.
- **Media:** Visual or audio aids that support the instruction.

## Relationships

- A **Protocol** contains multiple **Symptoms**, **Instructions**, and **Escalation** criteria.
- **Protocols** can be referenced by:
  - Tournaments (for event-specific protocols)
  - Venues (for location-specific requirements)
  - Training programs (for staff certification)
- **Media** resources can be shared across multiple protocols.

## Extensibility

The model is designed to be flexible, supporting:

- Different types of medical situations
- Various tournament environments
- Multiple languages and formats
- Integration with training and certification systems
- Venue-specific requirements
- Emergency response coordination

## References

- [American Red Cross: Performing First Aid](https://www.redcross.org/take-a-class/first-aid/performing-first-aid)
- [ISO 22320 — Emergency management (overview)](https://en.wikipedia.org/wiki/ISO_22320)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Domain modeling patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event safety and emergency

  standards

## See Also

- [Protocol](../first_aid/protocol.md)
- [Instruction](../first_aid/instruction.md)
- [Escalation](../first_aid/escalation.md)
- [Training](../first_aid/protocol.md)
- [Venue](../venue/venue.md)
- [Business README](../README.md)
