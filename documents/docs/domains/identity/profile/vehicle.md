# **Vehicle Profile** (Data Model – Entity)

## **Introduction**

The **Vehicle Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a vehicle participant or resource within Tournament Organizer. It adds vehicle-specific attributes and
relationships, such as type, make, model, year, registration, and owner.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute                    | Description                                     | Type    | Required | Notes / Example                                                                                                                                 |
| ---------------------------- | ----------------------------------------------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                     | The type of vehicle                             | String  | Yes      | `"Car"`, `"Bus"`, `"Truck"`, `"Boat"`                                                                                                           |
| **Make**                     | The manufacturer of the vehicle                 | String  | No       | `"Toyota"`, `"Mercedes"`                                                                                                                        |
| **Model**                    | The model of the vehicle                        | String  | No       | `"Corolla"`, `"Sprinter"`                                                                                                                       |
| **Year**                     | The year the vehicle was manufactured           | Integer | No       | `2020`                                                                                                                                          |
| **Registration**             | Vehicle registration number or ID               | String  | No       | `"ABC-1234"`                                                                                                                                    |
| **Owner**                    | Reference to the human profile of the owner     | UUID    | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                            |
| **Inspection/Certification** | Reference to inspection or certification record | UUID    | No       | Links to Inspection Record <!-- TODO: Create inspection record --> |
| **Insurance**                | Reference to insurance policy entity            | UUID    | No       | Links to Insurance Policy <!-- TODO: Create insurance policy -->   |
| **Usage Log**                | Reference to usage or maintenance log entity    | UUID    | No       | Links to Usage Log <!-- TODO: Create usage log -->                 |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Vehicle Profile:

- [Human Profile](../../identity/profile/human.md) (Owner)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Vehicle profiles may be linked to human owners, teams, or organizations.

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
