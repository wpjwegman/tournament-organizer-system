# **Plant Profile** (Data Model – Entity)

## **Introduction**

The **Plant Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a plant participant or resource within Tournament Organizer. It adds plant-specific attributes and
relationships, such as species, variety, date of planting, and caretaker.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute            | Description                                     | Type   | Required | Notes / Example                                                                                                                                       |
| -------------------- | ----------------------------------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Species**          | The species of the plant                        | String | Yes      | `"Oak"`, `"Rose"`, `"Tomato"`                                                                                                                         |
| **Variety**          | The variety or cultivar of the plant            | String | No       | `"Red Delicious"`, `"Cherry Tomato"`                                                                                                                  |
| **Date of Planting** | The date the plant was planted                  | Date   | No       | `"2022-03-15"`                                                                                                                                        |
| **Caretaker**        | Reference to the human profile of the caretaker | UUID   | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                  |
| **Registration**     | Reference to registration entity                | UUID   | No       | Links to                                                                                                                                              |
| **Growth Stage**     | The current growth stage of the plant           | String | No       | Example: "Seedling", "Mature", "Flowering"                                                                                                            |
| **Health Status**    | Reference to health or inspection entity        | UUID   | No       | Links to Health Status <!-- TODO: Create plant health status -->         |
| **Location**         | Reference to location or plot entity            | UUID   | No       | Links to Location <!-- TODO: Create location model -->                   |
| **Owner**            | Reference to the human profile of the owner     | UUID   | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                  |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Plant Profile:

  - [Human Profile](../../identity/profile/human.md) (Caretaker)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Plant profiles may be linked to human caretakers, teams, or organizations.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 55000:2014 - Asset management](https://www.iso.org/standard/55088.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event asset management

  standards

## See Also

- [Base Profile](../../identity/profile/base_profile.md)
- [Human](../../identity/profile/human.md)
- [Identity README](../../identity/README.md)
- [Business README](../../README.md)

---
