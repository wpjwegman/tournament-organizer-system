---
tags:
- identity
- attributes
- medical-history
- value-object
- health
- emergency
---

# Medical History (Value Object)

## Introduction

A **Medical History** Value Object represents a comprehensive record of medical information in a standardized format. It
provides a consistent way to handle medical history information for health monitoring, emergency response, and safety
planning within the tournament system.

It describes health characteristics and is typically embedded within other entities (like
[Human Profile](../../profile/human.md) or [Animal Profile](../../profile/animal.md)) to specify medical details.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## **Attributes**

| Attribute             | Description                                 | Type   | Required | Notes / Example                                      |
| --------------------- | ------------------------------------------- | ------ | -------- | ---------------------------------------------------- |
| **Allergies**         | List of known allergies and sensitivities.  | List   | Optional | `["Peanuts", "Latex", "Penicillin"]`                 |
| **Conditions**        | List of current or past medical conditions. | List   | Optional | `["Asthma", "Diabetes", "Hypertension"]`             |
| **Medications**       | List of current medications and dosages.    | List   | Optional | `["Insulin", "Albuterol", "Lisinopril"]`             |
| **Surgeries**         | List of past surgeries and procedures.      | List   | Optional | `["Appendectomy 2020", "Knee surgery 2018"]`         |
| **Vaccinations**      | List of vaccinations and dates.             | List   | Optional | `["COVID-19 2021", "Flu 2023", "Tetanus 2022"]`      |
| **Emergency Contact** | Emergency contact information.              | Object | Optional | Name, phone, relationship                            |
| **Blood Type**        | Blood type information.                     | String | Optional | `"A+"`, `"O-"`, `"B+"`                               |
| **Notes**             | Additional medical notes or observations.   | String | Optional | `"Allergic to bee stings"`, `"Requires epinephrine"` |

---

## **Relationships**

- A `Medical History` Value Object is embedded within [Human Profile](../../profile/human.md) entities.
- A `Medical History` Value Object is embedded within [Animal Profile](../../profile/animal.md) entities.
- A `Medical History` Value Object may be referenced by [First Aid](../../../first_aid/README.md) entities for
  emergency response.

---

## **Considerations**

- **Privacy:** Medical history information is highly sensitive and should be handled with strict confidentiality.
- **Access Control:** Access to medical history should be restricted to authorized personnel only.
- **Emergency Access:** Emergency responders should have appropriate access to critical medical information.
- **Updates:** Medical history should be kept current and accurate.
- **Compliance:** Medical information handling should comply with relevant privacy regulations.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [WHO Data: About and tools](https://www.who.int/data)

## See Also

- [Human Profile](../../profile/human.md)
- [Animal Profile](../../profile/animal.md)
- [First Aid](../../../first_aid/README.md)
- [Identity README](../../../identity/README.md)
- [Safety](../../../safety/safety.md)
- [Business README](../../../README.md)
