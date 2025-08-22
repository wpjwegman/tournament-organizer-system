# **Physical** (Data Model - Template Entity)

## **Introduction**

A **Physical** Template Entity defines a reusable blueprint for physical measurement categories and standards that can
be applied to profiles (human, animal, or plant). It provides a standardized framework for defining what physical
measurements are relevant for different profile types and contexts.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

\_(For a guide on managing physical characteristics, see the

<!-- 🚨 **BROKEN:** 🚨 **BROKEN:** [User Guide: Physical Characteristics](../# ../user_guide/ (TODO: Create user guide) 🚨 🚨 -->))._

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute        | Description                                              | Type       | Required | Notes / Example                           |
| ---------------- | -------------------------------------------------------- | ---------- | -------- | ----------------------------------------- |
| **Name**         | The name of the physical measurement template.            | String     | Yes      | `"Human Adult Measurements"`, `"Dog Breed Standards"` |
| **Description**  | Description of the physical measurement template.         | Text       | Yes      | `"Standard measurements for adult human participants"` |
| **Type**         | The type of profile this template applies to.             | String     | Yes      | `"Human"`, `"Animal"`, `"Plant"` |
| **Measurement Categories** | List of measurement categories for this template.        | List[String] | Yes    | `["Height", "Weight", "Build"]`, `["Length", "Height", "Weight"]` |
| **Required Measurements** | List of required measurements for this template.         | List[String] | Optional | `["Height", "Weight"]` |
| **Optional Measurements** | List of optional measurements for this template.         | List[String] | Optional | `["Build", "Wingspan"]` |
| **Validation Rules** | Rules for validating measurements in this template.      | List[String] | Optional | `["Height must be positive", "Weight must be reasonable"]` |

---

## **Domain Rules**

### **Measurement Rules**

- **Profile Type Specificity**: Different profile types may have different sets of relevant physical measurements
- **Measurement Flexibility**: The model allows for any type of physical measurement to be associated with a profile
- **Update Frequency**: Physical characteristics may change over time, so regular updates should be encouraged
- **Data Validation**: Measurements should be validated against reasonable ranges for the specific profile type

### **Tournament Eligibility Rules**

- **Size Requirements**: Some tournaments may have size or weight requirements for participants
- **Physical Standards**: Certain events may require specific physical characteristics for fair competition
- **Safety Considerations**: Physical measurements may be used for safety equipment sizing
- **Category Classification**: Physical measurements may determine tournament category placement

### **Health and Safety Rules**

- **Growth Tracking**: Physical measurements can track growth and development over time
- **Health Monitoring**: Changes in physical measurements may indicate health issues
- **Equipment Sizing**: Physical measurements are used for proper equipment and safety gear sizing
- **Medical Context**: Physical measurements may be relevant for medical assessments

---

## **Relationships**

- A `Physical` Template Entity may be referenced by [Human Profile](../../identity/profile/human.md) entities.
- A `Physical` Template Entity may be referenced by [Animal Profile](../../identity/profile/base_profile.md) entities.
- A `Physical` Template Entity may be referenced by measurement entities for validation.
- A `Physical` Template Entity may be referenced by tournament entities for eligibility requirements.

---

## **Considerations**

- **Template Nature:** This template defines a standard physical measurement type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a specific organization's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a specific organization)

  needs to be handled by application logic.

- **Template Management:**
  - Templates should be curated and maintained by measurement specialists
  - New templates can be added based on measurement standards and organizational requirements
  - Templates should be reviewed periodically for accuracy and relevance
- **Profile Type Specificity:** Different profile types may have different sets of relevant physical measurements
- **Measurement Flexibility:** The model allows for any type of physical measurement to be associated with a profile
- **Update Frequency:** Physical characteristics may change over time, so regular updates should be encouraged
- **Data Validation:** Measurements should be validated against reasonable ranges for the specific profile type
- **Customization Balance:**
  - Templates provide structure while allowing personalization
  - Customizations should not break the fundamental physical structure
  - System should support both template-based and fully custom physical measurements

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 31:1992 - Quantities and units](https://www.iso.org/standard/3621.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [ACSM Books: Exercise Testing and Prescription](https://acsm.org/education-resources/books/)

## See Also

- [Human Profile](../../identity/profile/human.md)
- [Animal Profile](../../identity/profile/base_profile.md)
- [Identity README](../../identity/README.md)
- [Safety](../../safety/safety.md)
- [Business README](../../README.md)

---
