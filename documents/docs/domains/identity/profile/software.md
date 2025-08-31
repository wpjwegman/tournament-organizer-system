# **Software Profile** (Data Model – Entity)

## **Introduction**

The **Software Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a software participant or resource within Tournament Organizer. It adds software-specific attributes and
relationships, such as type, vendor, version, license, and administrator.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute          | Description                                      | Type         | Required | Notes / Example                                                                                                                   |
| ------------------ | ------------------------------------------------ | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**           | The type of software                             | String       | Yes      | `"Scoring System"`, `"Registration App"`                                                                                          |
| **Vendor**         | The vendor or developer of the software          | String       | No       | `"Microsoft"`, `"Custom Dev"`                                                                                                     |
| **Version**        | The version of the software                      | String       | No       | `"1.0.0"`, `"2023.2"`                                                                                                             |
| **License**        | The license or registration key                  | String       | No       | `"GPLv3"`, `"ABC-123-XYZ"`                                                                                                        |
| **Administrator**  | Reference to the human profile of the admin      | UUID         | No       | Links to [Human Profile](../../identity/profile/human.md)                                                              |
| **Dependencies**   | List of dependencies or compatible systems       | List[String] | No       | Example: ["Windows 10", ".NET 6"]                                                                                                 |
| **Support Status** | The support status or end-of-life date           | String/Date  | No       | Example: "Supported", "End-of-Life: 2025-12-31"                                                                                   |
| **Security Audit** | Reference to security audit or vulnerability log | UUID         | No       | Links to Security Audit <!-- TODO: Create security audit --> |
| **Owner**          | Reference to the human profile of the owner      | UUID         | No       | Links to [Human Profile](../../identity/profile/human.md)                                                              |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Software Profile:

- [Human Profile](../../identity/profile/human.md) (Administrator)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Software profiles may be linked to human administrators, teams, or organizations.

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
