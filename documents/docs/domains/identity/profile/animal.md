# **Animal Profile** (Data Model – Entity)

## **Introduction**

The **Animal Profile** Entity inherits from the [Base Profile](base_profile.md) and
represents an animal participant or resource within Tournament Organizer. It includes only the most essential
animal-specific attributes and relationships, with all context-specific roles (handler, trainer, etc.) managed elsewhere
in the system.

It inherits properties from the [Base Entity](../../foundation/README.md).

---

## **Additional Attributes**

**Note:** This entity inherits all attributes from [Base Profile](base_profile.md).

| Attribute           | Description                                                                                                       | Type   | Required | Notes / Example                                                                  |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ------ | -------- | -------------------------------------------------------------------------------- |
| **Owner**           | Reference (by ID) to the human profile of the owner ([Human Profile](human.md)) | UUID   | Yes      | `"hum-1234-5678-90ab-cdef"`                                                      |
| **Species**         | The species of the animal                                                                                         | String | Yes      | `"Dog"`, `"Horse"`                                                               |
| **Breed**           | The breed of the animal                                                                                           | String | No       | `"Labrador Retriever"`                                                           |
| **Breed Standard**  | Reference (by ID) to breed standard or registry entity ()                                                         | UUID   | No       | `"breed-std-1234-5678-90ab-cdef"`, `"FCI Standard No. 122 (Labrador Retriever)"` |
| **Date of Birth**   | The animal's date of birth                                                                                        | Date   | No       | `"2018-05-01"`                                                                   |
| **Microchip ID**    | The animal's microchip identifier                                                                                 | String | No       | `"985112004879123"`                                                              |
| **Medical History** | Reference (by ID) to medical history entity (includes vaccination records) ()                                     | UUID   | No       | `"medhist-1234-5678-90ab-cdef"`, `"Annual Checkup 2023, Rabies Vaccination"`     |

---

## **Relationships**

- Inherits all relationships from [Base Profile](base_profile.md).
- Additional relationships specific to Animal Profile:

  - [Human Profile](human.md) (Owner)

---

## **Considerations**

- Inherits all considerations from [Base Profile](base_profile.md).
- Only the owner is tracked at the profile level; all other roles are managed in team/event/assignment contexts.
- Vaccination records are included as part of the referenced Medical History entity.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 14001:2015 - Environmental management systems](https://www.iso.org/standard/60857.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

<!-- Removed broken external link: AVMA Animal Welfare Principles (404) -->

  standards

## See Also

- [Base Profile](base_profile.md)
- [Human](human.md)
- [Medical History](../attributes/medical_history/medical_history.md)
- [Identity README](../README.md)
- [Safety](../../safety/README.md)
- [Business README](../../README.md)

---
