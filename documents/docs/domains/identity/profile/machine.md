# **Machine Profile** (Data Model – Entity)

## **Introduction**

The **Machine Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a machine participant or resource within Tournament Organizer. It adds machine-specific attributes and
relationships, such as type, manufacturer, model, year, and operator.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute                     | Description                                       | Type                   | Required | Notes / Example                                                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                      | The type of machine                               | String                 | Yes      | `"Printer"`, `"Scoreboard"`, `"Camera"`                                                                                                                                                                      |
| **Manufacturer**              | The manufacturer of the machine                   | String                 | No       | `"Canon"`, `"Epson"`                                                                                                                                                                                         |
| **Model**                     | The model of the machine                          | String                 | No       | `"X1000"`, `"ProCam"`                                                                                                                                                                                        |
| **Year**                      | The year the machine was manufactured             | Integer                | No       | `2021`                                                                                                                                                                                                       |
| **Operator**                  | Reference to the human profile of the operator    | UUID                   | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                                                                         |
| **Firmware/Software Version** | The current firmware or software version          | String                 | No       | Example: "v1.0.3"                                                                                                                                                                                            |
| **Maintenance Schedule**      | Reference to maintenance schedule or log entity   | UUID                   | No       | Links to Maintenance Log <!-- TODO: Create maintenance log -->                                    |
| **Capabilities**              | List or reference to capabilities entity/template | List[String]/UUID      | No       | Example: ["Printing", "Scanning"] or link to Capabilities <!-- TODO: Create capabilities model --> |
| **Owner**                     | Reference to the human profile of the owner       | UUID                   | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                                                                         |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Machine Profile:
  - [Human Profile](../../identity/profile/human.md) (Operator)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Machine profiles may be linked to human operators, teams, or organizations.

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
