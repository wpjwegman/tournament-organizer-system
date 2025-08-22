# **Art Profile** (Data Model – Entity)

## **Introduction**

The **Art Profile** Entity inherits from the [Base Profile](../../identity/profile/base_profile.md) and
represents an art asset, identity, or resource within Tournament Organizer. It adds art-specific attributes and
relationships, such as type, artist, year, and owner.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](../../identity/profile/base_profile.md).

| Attribute               | Description                                         | Type            | Required | Notes / Example                                                                                                                 |
| ----------------------- | --------------------------------------------------- | --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                | The type of art                                     | String          | Yes      | `"Painting"`, `"Sculpture"`, `"Poster"`                                                                                         |
| **Artist**              | The artist or creator of the art                    | String          | No       | `"Van Gogh"`, `"Banksy"`                                                                                                        |
| **Year**                | The year the art was created                        | Integer         | No       | `2021`                                                                                                                          |
| **Owner**               | Reference to the human profile of the owner         | UUID            | No       | Links to [Human Profile](../../identity/profile/human.md)                                                            |
| **Provenance**          | Reference to provenance or ownership history entity | UUID            | No       | Links to Provenance <!-- TODO: Create provenance model --> |
| **Exhibition History**  | List of exhibitions or competitions entered         | List[UUID]      | No       | Links to Exhibition <!-- TODO: Create exhibition model -->   |
| **Appraisal/Valuation** | Reference to appraisal or valuation entity          | UUID            | No       | Links to Appraisal <!-- TODO: Create appraisal model -->     |

---

## **Relationships**

- Inherits all relationships from [Base Profile](../../identity/profile/base_profile.md).
- Additional relationships specific to Art Profile:
  - [Human Profile](../../identity/profile/human.md) (Owner)

---

## **Considerations**

- Inherits all considerations from [Base Profile](../../identity/profile/base_profile.md).
- Art profiles may be linked to human owners, teams, or organizations.

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
