# **Vaccination Record** (Data Model – Template Entity)

## **Introduction**

A **Vaccination Record** Template Entity defines a reusable blueprint for vaccination record types and configurations
that can be used to create specific vaccination record instances. It provides a standardized framework for vaccine
types, administration requirements, and record keeping that can be applied across different contexts and organizations.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute           | Description                                                           | Type        | Required | Notes / Example                           |
| ------------------- | --------------------------------------------------------------------- | ----------- | -------- | ----------------------------------------- |
| **Name**            | The name of the vaccination record template.                          | String      | Yes      | `"Rabies Vaccine"`, `"Tetanus Vaccine"`, `"COVID-19 Vaccine"` |
| **Vaccine Type**    | The type of vaccine for this template                                 | String      | Yes      | `"Rabies"`, `"Tetanus"`, `"COVID-19"`     |
| **Description**     | Description of the vaccination record template.                       | Text        | Optional | `"Standard rabies vaccination record"`    |
| **Target Species**  | The species this vaccine template applies to                          | String      | Yes      | `"Human"`, `"Dog"`, `"Cat"`, `"Horse"`    |
| **Administration Requirements** | Requirements for administering this vaccine template              | List[String] | Optional | `["Licensed veterinarian", "Age 12+ weeks"]` |
| **Booster Schedule** | Standard booster schedule for this vaccine template                 | String      | Optional | `"Annual"`, `"Every 3 years"`, `"One-time"` |
| **Documentation Requirements** | Required documentation for this vaccine template                   | List[String] | Optional | `["Vaccination certificate", "Health certificate"]` |
| **Validity Period** | Standard validity period for this vaccine template                  | Integer     | Optional | `365` (days), `1095` (3 years)            |

---

## **Domain Rules**

### **Health and Safety Rules**

- **Verification Requirements**: Vaccination records should be verified by healthcare providers when possible
- **Privacy Protection**: Handle vaccination data in compliance with relevant privacy regulations
- **Status Tracking**: Monitor vaccination status for overdue boosters or required follow-ups
- **Emergency Access**: Vaccination records must be accessible for emergency medical situations

### **Tournament Participation Rules**

- **Eligibility Requirements**: Some tournaments may require specific vaccinations for participation
- **Documentation Verification**: Vaccination records may need to be verified for tournament registration
- **Health Screening**: Vaccination status may be part of health screening processes
- **Safety Protocols**: Vaccination records inform safety protocols for events

### **Record Management Rules**

- **Accuracy Standards**: Ensure vaccination records are accurate and up-to-date
- **Update Procedures**: Establish procedures for updating vaccination status
- **Retention Policies**: Define how long vaccination records should be retained
- **Access Controls**: Implement appropriate access controls for sensitive health data

---

## **Relationships**

- A `Vaccination Record` Template Entity may be referenced by vaccination record instance entities.
- A `Vaccination Record` Template Entity may be referenced by medical history template entities.
- A `Vaccination Record` Template Entity may be referenced by tournament eligibility rules.

### Parent Relationships

- Medical history templates - The medical history template this vaccination record template belongs to

### Child Relationships

- Vaccination record instances - Specific vaccination records created from this template
- Medical history instances - Medical history entries using this vaccination record template

### Related Entities

- Tournament templates - Tournament types that require this vaccination record template
- Safety templates - Safety protocols that reference this vaccination record template

---

## **Considerations**

- **Template Nature:** This template defines a standard vaccination record type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a specific organization's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a specific organization)

  needs to be handled by application logic.

- **Template Management:**

- Templates should be curated and maintained by healthcare administrators
- New templates can be added based on vaccination standards and regulatory requirements
- Templates should be reviewed periodically for compliance and effectiveness

- **Verification:** Ensure vaccination record templates are accurate and, if possible, verified by healthcare providers
- **Privacy:** Handle personal and health data in compliance with relevant privacy regulations
- **Updates:** Vaccination status may change (e.g., booster required, overdue); keep templates up to date
- **Customization Balance:**

- Templates provide structure while allowing personalization
- Customizations should not break the fundamental vaccination record structure
- System should support both template-based and fully custom vaccination records

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [WHO Guidelines for Vaccination](https://www.who.int/news-room/questions-and-answers/item/vaccines-and-immunization-what-is-vaccination)

## See Also

- [Medical History](../../identity/attributes/medical_history/medical_history.md)
- [Safety](../../safety/safety.md)
- [Identity README](../../identity/README.md)
- [Registration](../../registration/registration.md)
- [Business README](../../README.md)

---
