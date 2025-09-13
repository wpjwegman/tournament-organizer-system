---
tags:
- identity
- attributes
- health-condition
- value-object
- medical
- diagnosis
---

# Health Condition (Value Object)

## Introduction

A **Health Condition** Value Object represents a specific medical condition or health issue in a standardized format. It
provides a consistent way to handle health condition information for medical monitoring, treatment planning, and safety
considerations within the tournament system.

It describes health characteristics and is typically embedded within other entities (like
[Medical History](../medical_history.md)) to specify condition details.

It inherits properties from the [Base Entity](../../../../foundation/base_entity.md).

---

## **Attributes**

| Attribute          | Description                                           | Type   | Required | Notes / Example                                                             |
| ------------------ | ----------------------------------------------------- | ------ | -------- | --------------------------------------------------------------------------- |
| **Name**           | The name of the health condition.                     | String | Yes      | `"Asthma"`, `"Diabetes"`, `"Hypertension"`                                  |
| **Type**           | The type of health condition.                         | String | Optional | `"Chronic"`, `"Acute"`, `"Genetic"`, `"Environmental"`                      |
| **Severity**       | The severity level of the condition.                  | String | Optional | `"Mild"`, `"Moderate"`, `"Severe"`                                          |
| **Diagnosis Date** | The date when the condition was diagnosed.            | Date   | Optional | `"2020-03-15"`, `"2018-11-22"`                                              |
| **Status**         | The current status of the condition.                  | String | Optional | `"Active"`, `"In Remission"`, `"Managed"`, `"Resolved"`                     |
| **Symptoms**       | List of symptoms associated with the condition.       | List   | Optional | `["Shortness of breath", "Chest tightness", "Wheezing"]`                    |
| **Treatments**     | List of treatments or medications for the condition.  | List   | Optional | `["Albuterol inhaler", "Daily controller medication"]`                      |
| **Notes**          | Additional notes or observations about the condition. | String | Optional | `"Triggered by exercise and cold air"`, `"Well-controlled with medication"` |

---

## **Relationships**

- A `Health Condition` Value Object is embedded within [Medical History](../medical_history.md) entities.
- A `Health Condition` Value Object may be referenced by [First Aid](../../../../first_aid/README.md) entities for
  emergency response.
- A `Health Condition` Value Object may be referenced by [Training](../../../../process/README.md) entities for safety considerations.

---

## **Considerations**

- **Privacy:** Health condition information is highly sensitive and should be handled with strict confidentiality.
- **Accuracy:** Health condition information should be accurate and up-to-date.
- **Emergency Planning:** Critical health conditions should be flagged for emergency response planning.
- **Activity Modifications:** Health conditions may require activity modifications or restrictions.
- **Medical Oversight:** Health condition management should be overseen by qualified medical professionals.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [WHO International Classification of Diseases (ICD)](https://www.who.int/standards/classifications/classification-of-diseases)

## See Also

- [Medical History](../medical_history.md)
- [First Aid](../../../../first_aid/README.md)
- [Training](../../../../process/README.md)
- [Identity README](../../../../identity/README.md)
- [Safety](../../../../safety/safety.md)
- [Business README](../../../../README.md)
