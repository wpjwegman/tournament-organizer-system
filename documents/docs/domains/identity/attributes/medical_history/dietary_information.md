---
tags:
- identity
- attributes
- dietary-information
- template-entity
- medical
- nutrition
---

# Dietary Information (Template Entity)

## Introduction

A **Dietary Information** Entity Template serves as a blueprint for creating specific dietary requirement instances that
can be referenced by various profiles (Human, Animal, Plant, Resource). It represents standardized dietary needs,
restrictions, or preferences that can be reused across the system.

It possesses a unique identity and lifecycle, managed according to the [Base Entity Model](../../../foundation/base_entity.md).

\_(For a guide on managing dietary information, see the

<!-- [User Guide: Dietary Information](# ../user_guide/ (TODO: Create user guide) -->))._

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status` [e.g., Active, Deprecated], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity Model](../../../foundation/base_entity.md).

| Attribute               | Description                                                                                         | Type   | Required | Notes / Example                                                          |
| ----------------------- | --------------------------------------------------------------------------------------------------- | ------ | -------- | ------------------------------------------------------------------------ |
| **Name**                | The name used to identify this dietary requirement in Tournament Organizer.                         | String | Yes      | `Vegetarian`, `Gluten-Free`, `High Protein`, `Organic`                   |
| **Description**         | Detailed explanation of the dietary requirement, including any specific guidelines or restrictions. | Text   | Yes      | `"No meat or fish products. Includes dairy and eggs."`                   |
| **Restriction Type**    | Categorizes the nature of the dietary restriction.                                                  | String | Yes      | `Allergy`, `Preference`, `Medical Requirement`, `Religious`, `Lifestyle` |
| **Item**                | Specifies the food item, ingredient, or general category.                                           | String | Yes      | `"Peanuts"`, `"Gluten"`, `"Vegetarian"`, `"Halal"`                       |
| **Severity**            | Indicates the severity level, particularly for allergies or medical requirements.                   | String | Optional | `Mild`, `Moderate`, `Severe`, `Life-threatening`                         |
| **Verification Status** | Status indicating if the information has been verified.                                             | String | Optional | `Verified`, `Unverified`, `Requires Documentation`                       |

---

## **Relationships**

- A `Dietary Information` Template can be referenced by multiple profile entities:

- [Human Profile](../../profile/human.md)
- [Animal Profile](../../profile/animal.md)
- [Plant Profile](../../profile/plant.md)

---

## **Considerations**

- **Template Usage:** This template serves as a standardized way to define common dietary requirements.
- **Reusability:** The same dietary requirement can be referenced by multiple profiles.
- **Clarity:** The description should be clear and detailed enough to ensure proper implementation.
- **Standardization:** Helps maintain consistency in how dietary requirements are defined and referenced.
- **Verification:** The `Verification Status` is crucial for managing risk associated with allergies or medical

  requirements.

- **Severity Levels:** The `Severity` field helps in prioritizing and managing dietary requirements appropriately.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 22000:2018 - Food safety management systems](https://www.iso.org/standard/65464.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [WHO Guidelines for Food Safety](https://www.who.int/news-room/fact-sheets/detail/food-safety)

## See Also

- [Human Profile](../../../identity/profile/human.md)
- [Animal Profile](../../../identity/profile/base_profile.md)
- [Medical History](../../../identity/attributes/medical_history/medical_history.md)
- [Identity README](../../../identity/README.md)
- [Safety](../../../safety/safety.md)
- [Business README](../../../README.md)

---
