# **Medicine** (Data Model - Template Entity)

## **Introduction**

A **Medicine** Entity Template represents a standardized definition of a medication or medical treatment that can be
used across the tournament system. It serves as a reusable template for recording and managing medical interventions,
treatments, and medications administered to participants.

As an Entity Template, it inherits from the and provides a standardized definition that can be used across multiple
medical records.

_(Medicine management guide to be added as future enhancement)._

It inherits properties from the [Base Entity](../../../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status` [e.g., Active, Deprecated], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity](../../../../../foundation/base_entity.md).

| Attribute       | Description                                                                            | Type   | Required | Notes / Example                                                  |
| --------------- | -------------------------------------------------------------------------------------- | ------ | -------- | ---------------------------------------------------------------- |
| **Name**        | The official name of the medicine or treatment.                                        | String | Yes      | `"Paracetamol"`, `"Ibuprofen"`, `"First Aid Kit"`, `"Ice Pack"`  |
| **Type**        | Categorizes the medicine (e.g., Prescription, Over-the-counter, Controlled Substance). | String | Yes      | E.g., `Prescription`, `Over-the-counter`, `Controlled Substance` |
| **Description** | Detailed description of the medicine, its purpose, and usage guidelines.               | Text   | Yes      | `"Standard pain relief medication, maximum 4 doses per day"`     |

---

## **Relationships**

- A `Medicine` **Entity Template** is referenced by:
  - **[Treatment](treatment.md)** entities for specific treatment protocols
  - **[Medical History](../../medical_history.md)** records for current medications
  - **Medical Log** entries for administered medications (_future enhancement_)

---

## **Considerations**

- **Template Usage:** Defines standard medicine information, not individual prescriptions or administrations.
- **Safety:** Consider safety requirements and risk management in the template design.
- **Documentation:** Clear documentation of usage guidelines and warnings is essential.
- **Regulatory Compliance:** Ensure compliance with relevant medical regulations and guidelines.

---
