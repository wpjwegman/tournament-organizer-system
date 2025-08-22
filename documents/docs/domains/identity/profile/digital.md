# **Digital Profile** (Data Model – Entity)

## **Introduction**

The **Digital Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents a digital asset, identity, or resource within Tournament Organizer. It adds digital-specific attributes and
relationships, such as platform, handle, and owner.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute    | Description                                 | Type   | Required | Notes / Example                                                      |
| ------------ | ------------------------------------------- | ------ | -------- | -------------------------------------------------------------------- |
| **Platform** | The digital platform or service             | String | Yes      | `"Twitter"`, `"Discord"`, `"Website"`                                |
| **Handle**   | The digital handle, username, or URL        | String | Yes      | `"@tournamentorg"`, `"discord.gg/xyz"`                               |
| **Owner**    | Reference to the human profile of the owner | UUID   | No       | Links to [Human Profile](../../identity/profile/human.md) |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Digital Profile:
  - [Human Profile](../../identity/profile/human.md) (Owner)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Digital profiles may be linked to human owners, teams, or organizations.

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
