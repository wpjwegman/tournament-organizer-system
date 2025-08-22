# **Temperament** (Data Model - Template Entity)

## **Introduction**

A **Temperament** Template Entity defines a reusable blueprint for temperament categories and assessment criteria that
can be used to evaluate animal behavioral characteristics. It provides a standardized framework for categorizing
temperament types for care, handling, training, and activity suitability decisions.

It provides crucial insights for:

- Care and handling protocols
- Training approaches
- Housing decisions
- Owner matching
- Activity suitability

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute           | Description                                                                                        | Type         | Required | Notes / Example                                                                                                                                         |
| ------------------- | -------------------------------------------------------------------------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | A concise label summarizing the overall temperament template category.                             | String       | Yes      | E.g., "Calm and Friendly", "Shy but Gentle", "High Energy Playful", "Nervous Reactive"                                                                  |
| **Category**        | A classification based on a predefined scale or system.                                            | String       | Yes      | E.g., "Green - Excellent Pet Potential", "Amber - Needs Support", "Red - Experienced Handler Required"                                                  |
| **Key Traits**      | A list of specific observable behavioral characteristics for this template.                        | List<String> | Yes      | Example: `["Friendly towards strangers", "Tolerant of handling", "Playful with other dogs", "Anxious in new environments", "Resource Guarding (Food)"]` |
| **Description**     | A narrative summary providing context about the temperament template category.                      | Text         | Yes      | E.g., "Generally relaxed and seeks human attention. Shows some fear response to loud noises but recovers quickly. Good with gentle children."           |
| **Assessment Criteria** | Standard criteria for evaluating this temperament template.                                       | List<String> | Optional | `["Observe stranger interactions", "Test handling tolerance", "Assess energy levels"]` |
| **Handler Requirements** | Required handler experience level for this temperament template.                                 | String       | Optional | `"Beginner"`, `"Intermediate"`, `"Expert"` |
| **Activity Restrictions** | Activities that may be restricted for this temperament template.                                | List<String> | Optional | `["High-stress competitions", "Crowded environments"]` |

---

## **Domain Rules**

### **Assessment Rules**

- **Standardization**: Use consistent categories and assessment criteria across all evaluations
- **Context Consideration**: Consider environmental factors, health status, and recent experiences when applying

  assessments

- **Regular Updates**: Regular reassessment may be needed as temperament can change over time
- **Purpose Alignment**: Adjust assessment criteria based on intended use (e.g., adoption vs. working animal)

### **Safety and Handling Rules**

- **Handler Requirements**: Temperament assessment determines required handler experience level
- **Activity Restrictions**: Certain temperaments may restrict participation in specific activities
- **Safety Protocols**: Temperament influences safety protocols and handling procedures
- **Training Requirements**: Temperament assessment guides training approach and requirements

### **Tournament Participation Rules**

- **Eligibility Assessment**: Temperament may affect tournament participation eligibility
- **Category Placement**: Temperament can influence tournament category placement
- **Safety Considerations**: Temperament assessment is crucial for safety in competitive environments
- **Handler Matching**: Temperament influences handler assignment and supervision requirements

---

## **Examples by Category**

### Green Level Temperaments

| Name                   | Description                      | Key Traits                                                                     | Category                        |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------------------ | ------------------------------- |
| `Calm and Friendly`    | Ideal companion temperament      | Friendly with strangers, Tolerant of handling, Good with children              | Green - Excellent Pet Potential |
| `Confident and Social` | Well-adjusted social temperament | Confident in new situations, Good with other animals, Enjoys human interaction | Green - Excellent Pet Potential |

### Amber Level Temperaments

| Name             | Description               | Key Traits                                             | Category               |
| ---------------- | ------------------------- | ------------------------------------------------------ | ---------------------- |
| `Shy but Gentle` | Needs confidence building | Initially timid, Avoids eye contact, Never aggressive  | Amber - Needs Support  |
| `High Energy`    | Requires active lifestyle | Very playful, Needs lots of exercise, Can be excitable | Amber - Needs Activity |

### Red Level Temperaments

| Name                | Description                  | Key Traits                                                          | Category                           |
| ------------------- | ---------------------------- | ------------------------------------------------------------------- | ---------------------------------- |
| `Nervous Reactive`  | Requires experienced handler | Fearful of strangers, Reactive to stimuli, Needs careful management | Red - Experienced Handler Required |
| `Resource Guarding` | Needs behavior modification  | Guards food/toys, Can be territorial, Requires training             | Red - Specialized Care Required    |

---

## **Relationships**

- A `Temperament` Template Entity may be referenced by [Animal Profile](../../identity/profile/base_profile.md) entities.
- A `Temperament` Template Entity may be referenced by behavioral assessment entities.
- A `Temperament` Template Entity may be referenced by training entities for appropriate training approaches.
- A `Temperament` Template Entity may be referenced by safety entities for handling protocols.

---

## **Considerations**

- **Template Nature:** This template defines a standard temperament type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a specific organization's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a specific organization)

  needs to be handled by application logic.

- **Template Management:**
  - Templates should be curated and maintained by behavioral specialists
  - New templates can be added based on behavioral standards and organizational requirements
  - Templates should be reviewed periodically for accuracy and safety
- **Standardization:** Use consistent categories and assessment criteria across all evaluations
- **Context:** Consider environmental factors, health status, and recent experiences when applying assessments
- **Updates:** Regular reassessment may be needed as temperament can change over time
- **Purpose:** Adjust assessment criteria based on intended use (e.g., adoption vs. working animal)
- **Customization Balance:**
  - Templates provide structure while allowing personalization
  - Customizations should not break the fundamental temperament structure
  - System should support both template-based and fully custom temperaments

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 14001:2015 - Environmental management systems](https://www.iso.org/standard/60857.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [AVMA Animal Welfare Principles](https://www.avma.org/resources-tools/avma-policies/animal-welfare-principles) - AVMA animal

  behavior standards

## See Also

- [Animal Profile](../../identity/profile/base_profile.md)
- [Safety](../../safety/safety.md)
- [Identity README](../../identity/README.md)
- [Team](../../team/team.md)
- [Business README](../../README.md)
