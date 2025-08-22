# **Computer Profile** (Data Model – Entity)

## **Introduction**

The **Computer Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a computer participant or resource within Tournament Organizer. It adds computer-specific attributes and
relationships, such as type, manufacturer, model, year, and user.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute              | Description                                      | Type       | Required | Notes / Example                                                                                                                                       |
| ---------------------- | ------------------------------------------------ | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**               | The type of computer                             | String     | Yes      | `"Laptop"`, `"Desktop"`, `"Tablet"`                                                                                                                   |
| **Manufacturer**       | The manufacturer of the computer                 | String     | No       | `"Apple"`, `"Dell"`                                                                                                                                   |
| **Model**              | The model of the computer                        | String     | No       | `"MacBook Pro"`, `"XPS 13"`                                                                                                                           |
| **Year**               | The year the computer was manufactured           | Integer    | No       | `2023`                                                                                                                                                |
| **User**               | Reference to the human profile of the user       | UUID       | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                  |
| **Installed Software** | List or reference to installed software profiles | List[UUID] | No       | Links to [Software Profile](../../identity/profile/software.md)                                                                            |
| **Network/Location**   | Reference to network or physical location entity | UUID       | No       | Links to Location <!-- TODO: Create location model --> |
| **Owner**              | Reference to the human profile of the owner      | UUID       | No       | Links to [Human Profile](../../identity/profile/human.md)                                                                                  |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Computer Profile:
  - [Human Profile](../../identity/profile/human.md) (User)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Computer profiles may be linked to human users, teams, or organizations.

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
- [Software](../../identity/profile/software.md)
- [Identity README](../../identity/README.md)
- [Business README](../../README.md)

---
