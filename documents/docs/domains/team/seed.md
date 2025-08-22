# **Seed** (Data Model - Entity)

## **Introduction**

A **Seed** Entity represents a ranked position assigned to a participant (individual or team) within a specific \***\*.
This assignment is typically based on performance, rankings, or other criteria defined by a \*\***, aiming to create
balanced and fair tournament structures like brackets or groups.

As an Entity, it has its own identity and lifecycle, inheriting from the .

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status` [e.g., Active, Inactive], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute       | Description                                                                    | Type    | Required | Notes / Example                                    |
| --------------- | ------------------------------------------------------------------------------ | ------- | -------- | -------------------------------------------------- |
| **Ranking**     | The numerical rank associated with this seed (e.g., 1st, 2nd, 3rd).            | Integer | Yes      | `1`, `8`                                           |
| **Name**        | Optional display name for the seed, often combining discipline/group and rank. | String  | Optional | `"Group A Seed 1"`, `"Main Bracket Seed #4"`       |
| **Description** | Optional text providing additional context about the seed assignment.          | String  | Optional | `"Top seed based on international ranking points"` |

---

## **Relationships**

- Seeds are used to populate structures like \***\* or \*\*** within a tournament.

---

## **Considerations**

- **Uniqueness:** The `Ranking` number should be unique within its context (e.g., within a group or bracket).
- **Lifecycle:** Seeds should be managed throughout the tournament lifecycle, with status updates reflecting their

  current state.

- **Validation:** The `Ranking` should be a positive integer and should not exceed the total number of participants in

  the context.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event seeding standards

## See Also

- [Team README](../team/README.md)
- [Team](../team/team.md)
- [Tournament README](../tournament/README.md)
- [Discipline README](../discipline/README.md)
- [Ranking README](../ranking/README.md)
- [Standing README](../standing/README.md)
- [Business README](../README.md)

---
