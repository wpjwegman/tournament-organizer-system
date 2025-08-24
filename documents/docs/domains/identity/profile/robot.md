# **Robot Profile** (Data Model – Entity)

## **Introduction**

The **Robot Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a robot participant or resource within Tournament Organizer. It adds robot-specific attributes and
relationships, such as type, manufacturer, model, year, and operator.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute                     | Description                                       | Type                   | Required | Notes / Example                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------- | ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                      | The type of robot                                 | String                 | Yes      | `"Humanoid"`, `"Industrial"`, `"Drone"`                                                                                                                                                                                |
| **Manufacturer**              | The manufacturer of the robot                     | String                 | No       | `"Boston Dynamics"`, `"KUKA"`                                                                                                                                                                                          |
| **Model**                     | The model of the robot                            | String                 | No       | `"Atlas"`, `"KR 10"`                                                                                                                                                                                                   |
| **Year**                      | The year the robot was manufactured               | Integer                | No       | `2022`                                                                                                                                                                                                                 |
| **Operator**                  | Reference to the human profile of the operator    | UUID                   | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                                                                                   |
| **Firmware/Software Version** | The current firmware or software version          | String                 | No       | Example: "v2.1.0"                                                                                                                                                                                                      |
| **Maintenance Schedule**      | Reference to maintenance schedule or log entity   | UUID                   | No       | Links to Maintenance Log <!-- TODO: Create maintenance log -->                                              |
| **Capabilities**              | List or reference to capabilities entity/template | List[String]/UUID      | No       | Example: ["Navigation", "Object Detection"] or link to Capabilities <!-- TODO: Create capabilities model --> |
| **Owner**                     | Reference to the human profile of the owner       | UUID                   | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                                                                                   |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Robot Profile:

  - [Human Profile](../../identity/profile/human.md) (Operator)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Robot profiles may be linked to human operators, teams, or organizations.

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
