# **Breed Standard** (Data Model - Template Entity)

## **Introduction**

A **Breed Standard** Entity Template represents a standardized breed standard or registry entry for a recognized animal
breed. It provides a reference for breed characteristics, registry authority, and documentation that can be selected and
customized by users.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity Model](../../foundation/base_entity.md). When used, its definition is typically **copied** into the target
context (like a specific animal profile), allowing for potential minor modifications or annotations without altering the
original template.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the [Base Entity Model](../../foundation/base_entity.md).

| Attribute         | Description                                                                    | Type         | Required | Notes / Example                                                    |
| ----------------- | ------------------------------------------------------------------------------ | ------------ | -------- | ------------------------------------------------------------------ |
| **Name**          | The official name of the breed standard template                               | String       | Yes      | `"Labrador Retriever"`, `"Shetland Pony"`                          |
| **Registry**      | The registry or authority that maintains the standard                          | String       | Yes      | `"FCI"`, `"AKC"`, `"The Kennel Club"`                              |
| **Description**   | Description of the breed standard template                                     | Text         | Yes      | `"Medium-sized, athletic, friendly temperament"`                   |
| **Reference URL** | Link to the official standard or documentation                                 | String       | No       | `"https://www.akc.org/dog-breeds/labrador-retriever/"` |
| **Category**      | Animal category for this breed standard                                        | String       | Yes      | `"Dog"`, `"Horse"`, `"Cat"`, `"Bird"`                              |
| **Icon**          | (Optional) Icon or visual representation                                       | String       | No       | `"labrador"`, `"pony"`, `"retriever"`                              |
| **Tags**          | (Optional) Additional tags for categorization                                  | List[String] | No       | `["sporting", "retriever", "family"]`                              |
| **Last Updated**  | When the breed standard was last updated                                       | Date         | No       | `2024-01-15`                                                       |
| **Is Active**     | Flag indicating if the breed standard template is currently available for use. | Boolean      | Yes      | `true` / `false`                                                   |
| **Version**       | Version number for tracking changes to the breed standard template.            | Integer      | Yes      | System-managed. Starts at 1.                                       |

---

## **Domain Rules**

### **Template Management Rules**

- **Standardization**: Templates provide consistent breed categorization across the system
- **Registry Compliance**: Templates should align with official registry standards
- **Updates**: Templates should be updated when registry standards change
- **Validation**: Templates should be validated against official registry documentation

### **Registry Validation Rules**

- **Authority Recognition**: Only recognized and reputable registries should be used
- **Standard Verification**: Breed standard templates should be verified against official registry documentation
- **International Standards**: Some breeds have different standards in different countries or registries
- **Version Control**: Breed standard templates may be updated; consider versioning for future extensions

### **Tournament Classification Rules**

- **Breed Categories**: Breed standard templates may determine tournament category placement
- **Competition Eligibility**: Some competitions may have breed-specific eligibility requirements
- **Performance Standards**: Breed standard templates may influence performance expectations
- **Judging Criteria**: Breed standard templates may be used in judging and evaluation criteria

### **Documentation Rules**

- **Official References**: Always use official registry documentation when available
- **Standard Compliance**: Animal profiles should comply with recognized breed standard templates
- **Documentation Updates**: Keep breed standard template documentation current with registry updates
- **Cross-Reference**: Maintain cross-references between different registry standards for the same breed

---

## **Relationships**

- **Template Relationships:**

- Breed Standard Templates can be grouped by Category for easier discovery
- Breed Standard Templates can be referenced by tournament categories or competition rules
- Breed Standard Templates can be linked to Registry <!-- TODO: Create registry model --> entities for authority validation

- **Instantiation Relationships:**

- When instantiated, Breed Standard Templates create Breed Standard instances embedded within

    [Animal Profile](../profile/animal.md) entities

- Multiple animal profiles may instantiate the same Breed Standard Template with different customizations
- Breed Standard Templates can be referenced by [Competition Category](../../classification/category.md) entities

---

## **Considerations**

- **Template Nature:** This template defines a standard breed standard. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., an Animal Profile's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like an Animal Profile)

  needs to be handled by application logic.

- **Template Management:**

- Templates should be curated and maintained by system administrators
- New templates can be added based on official registry updates
- Templates should be reviewed periodically for accuracy and compliance

- **Registry Compliance:**

- Templates should strictly follow official registry standards
- Changes to registry standards should trigger template updates
- Versioning may be needed to track standard evolution

- **Customization Balance:**

- Templates provide structure while allowing personalization
- Customizations should not break the fundamental breed classification
- System should support both template-based and fully custom breed standards

- **Internationalization:**

- Some breeds have different standards in different countries
- Templates should support multiple registry authorities
- Localization may be needed for breed names and descriptions

- **Performance:**

- Template lookups should be optimized for quick selection
- Popular templates should be cached for better performance
- Search and filtering should work efficiently across templates

- **Data Consistency:**

- Template changes should not affect existing instantiations
- Customizations should be preserved when templates are updated
- Versioning may be needed for template evolution

- **Validation Requirements:**

- `Name` must be unique within its context
- `Registry` should be from a recognized authority
- `Description` should be accurate and up-to-date

---

## References

- [FCI Breed Standards](https://www.fci.be/en/nomenclature/) - International breed standards
- [AKC Breed Standards](https://www.akc.org/dog-breeds/) - American Kennel Club standards
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Template Entity patterns

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)

## See Also

- [Base Entity](../../foundation/base_entity.md)
- [Animal Profile](../../identity/profile/base_profile.md)
- [Category](../../classification/category.md)
- [Identity README](../../identity/README.md)
- [Business README](../../README.md)
