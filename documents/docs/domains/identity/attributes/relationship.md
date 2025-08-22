# **Relationship** (Data Model - Template Entity)

## **Description**

A **Relationship** Template Entity defines a reusable blueprint for relationship types and configurations that can be
used to create specific relationship instances. It provides a standardized framework for relationship categories,
types, and requirements that can be applied across different contexts and profiles.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute       | Type   | Description                                                                                                               | Required | Notes / Example                                                       |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------- |
| **Name**        | String | The name of the relationship template.                                                                                    | Yes      | `"Parent-Child"`, `"Owner-Pet"`, `"Coach-Athlete"`                    |
| **Type**        | String | Broad classification of the relationship template (e.g., Familial, Professional, Social, Ownership).                     | Yes      | Example: "Familial", "Ownership"                                      |
| **Sub Type**    | String | Specific nature of the relationship template from the perspective of the involved profile.                               | Yes      | Example: "Parent", "Child", "Owner", "Guardian", "Colleague", "Coach" |
| **Description** | String | Description of the relationship template and its characteristics.                                                         | No       | "Standard parent-child relationship template"                         |
| **Requirements** | List[String] | Standard requirements for this relationship template.                                                                   | Optional | `["Legal documentation", "Age verification", "Consent forms"]`        |
| **Permissions** | List[String] | Standard permissions granted by this relationship template.                                                             | Optional | `["Medical decisions", "Tournament registration", "Emergency contact"]` |
| **Validation Rules** | List[String] | Rules for validating this relationship template.                                                                       | Optional | `["Both parties must be registered", "Age requirements met"]`         |

---

## **Domain Rules**

### **Relationship Management Rules**

- **Directionality**: The `Sub Type` defines the relationship from the embedding profile's perspective towards the

  related profile

- **Reciprocal Relationships**: A reciprocal relationship might be represented by a separate `Relationship` instance or

  inferred by application logic

- **Status Management**: Use the `End Date` field to reflect the current validity of the relationship
- **Uniqueness**: The combination of profiles and `Sub Type` should be unique for active relationships

### **Legal and Regulatory Rules**

- **Guardianship Requirements**: Guardian relationships may have legal implications for tournament participation
- **Ownership Verification**: Ownership relationships may require documentation for animal participants
- **Professional Relationships**: Professional relationships may affect role assignments and permissions
- **Privacy Protection**: Relationship data can be sensitive and requires appropriate access controls

### **Tournament Participation Rules**

- **Guardian Consent**: Minor participants require guardian relationship verification
- **Animal Ownership**: Animal participants require owner relationship verification
- **Team Formation**: Relationships may influence team formation and assignment
- **Emergency Contacts**: Relationship data is crucial for emergency contact procedures

---

## **Relationships**

- A `Relationship` Template Entity may be referenced by relationship instance entities.
- A `Relationship` Template Entity may be referenced by profile entities.
- A `Relationship` Template Entity may be referenced by registration entities for verification.

### Parent Relationships

- Profile templates - The profile types this relationship template applies to

### Child Relationships

- Relationship instances - Specific relationships created from this template
- Profile instances - Profile connections using this relationship template

### Related Entities

- Registration templates - Registration types that require this relationship template
- Tournament templates - Tournament types that recognize this relationship template

---

## **Considerations**

- **Template Nature:** This template defines a standard relationship type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a specific organization's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a specific organization)

  needs to be handled by application logic.

- **Template Management:**
  - Templates should be curated and maintained by relationship administrators
  - New templates can be added based on relationship standards and organizational requirements
  - Templates should be reviewed periodically for privacy and compliance
- **Type vs. Sub Type:** The `Type` provides a broad category, while `Sub Type` offers specificity
- **Privacy:** Relationship template data can be sensitive. Ensure appropriate access controls and adherence to privacy policies
- **Profile Types:** The model supports relationships between any profile types, allowing for flexible associations

  like:

  - Human to Human (e.g., parent-child, coach-athlete)
  - Human to Animal (e.g., owner-pet, trainer-horse)
  - Human to Computer (e.g., owner-device, administrator-system)
  - Any other valid profile type combinations
- **Customization Balance:**
  - Templates provide structure while allowing personalization
  - Customizations should not break the fundamental relationship structure
  - System should support both template-based and fully custom relationships

---

## **Related Data Models**

-
-
-
<!-- TODO: Add links when profile types are implemented

- Plant Profile (not yet implemented)
- Resource Profile (not yet implemented)  
- Software Profile (not yet implemented)

-->

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event participant

  relationship standards

## See Also

- [Human Profile](../../identity/profile/human.md)
- [Animal Profile](../../identity/profile/base_profile.md)
- [Identity README](../../identity/README.md)
- [Registration](../../registration/registration.md)
- [Business README](../../README.md)
