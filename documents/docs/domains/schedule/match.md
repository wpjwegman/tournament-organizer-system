# **Match** (Data Model - Template Entity)

## **Introduction**

A **Match** Entity represents a competitive encounter between teams. It is a simple entity that links the teams
participating in the match.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute | Description                               | Type                                                                                                   | Required | Notes / Example |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------- | --------------- |
| **Teams** | List of teams participating in the match. | List entities. Example: `[550e8400-e29b-41d4-a716-446655440000, 6ba7b810-9dad-11d1-80b4-00c04fd430c8]` | | |

---

## **Relationships**

- A `Match` Entity references multiple entities via the `Teams` attribute.

---

## **Considerations**

- **Team References:** The `Teams` list should contain valid references to existing Team entities.
- **Minimum Teams:** A match should have at least two teams.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event competition standards

## See Also

- [Schedule README](../schedule/README.md)
- [Fixture](../schedule/fixture.md)
- [Event](../schedule/event.md)
- [Score](../schedule/score.md)
- [Team README](../team/README.md)
- [Business README](../README.md)
