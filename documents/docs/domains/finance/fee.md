---
tags:
  - finance
  - fee
  - template
  - pricing
  - billing
  - charge
---

# **Fee** (Data Model - Template Entity)

## **Introduction**

A **Fee** Entity represents a charge or fee that can be applied to participants, teams, or organizations within the
tournament system. It provides a consistent way to handle fee information for pricing, billing, and financial management
within the tournament system.

It describes financial characteristics and is typically managed by [Finance](../finance/finance.md)
entities to provide complete fee oversight.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

| Attribute       | Description                                     | Type     | Required | Notes / Example                                         |
| --------------- | ----------------------------------------------- | -------- | -------- | ------------------------------------------------------- |
| **ID**          | Unique identifier for the fee entity.           | UUID     | Yes      | `"f123e456-7890-1234-5678-901234567890"`                |
| **Name**        | The name of the fee.                            | String   | Yes      | `"Team Registration Fee"`, `"Late Registration Fee"`    |
| **Type**        | The type of fee.                                | String   | Yes      | `"Registration"`, `"Late"`, `"Equipment"`, `"Facility"` |
| **Amount**      | The amount of the fee.                          | Decimal  | Yes      | `50.00`, `25.00`, `100.00`                              |
| **Currency**    | The currency of the fee.                        | String   | Optional | `"USD"`, `"EUR"`, `"CAD"`                               |
| **Description** | Description of what the fee covers.             | String   | Optional | `"Covers tournament entry and basic equipment"`         |
| **Category**    | The category of the fee.                        | String   | Optional | `"Required"`, `"Optional"`, `"Penalty"`                 |
| **Due Date**    | The date when the fee is due.                   | Date     | Optional | `"2024-02-15"`, `"2024-03-01"`                          |
| **Status**      | The status of the fee.                          | String   | Optional | `"Active"`, `"Inactive"`, `"Suspended"`                 |
| **Created At**  | Timestamp when the fee entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                |
| **Updated At**  | Timestamp when the fee entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                |

---

## **Relationships**

- A `Fee` Entity is managed by a [Finance](../finance/finance.md) entity.
- A `Fee` Template Entity may be applied to [Registration](../registration/registration.md) entities.
- A `Fee` Template Entity may be associated with [Cart](../finance/cart.md) entities.

---

## **Considerations**

- **Transparency:** Fee structures should be clear and transparent to participants.
- **Fairness:** Fees should be reasonable and justified by the services provided.
- **Flexibility:** Fee structures should accommodate different participant categories.
- **Collection:** Fee collection processes should be efficient and secure.
- **Refunds:** Fee refund policies should be clearly defined.

---

## References

- [ISO 4217 — Currency codes (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_4217) - Standard for currency representation
- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html) - Standard for date and timestamp

  representations

- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity pattern reference

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event pricing and fee

  management standards

## See Also

- [Amount](../finance/amount.md)
- [Cart](../finance/cart.md)
- [Discount](../finance/discount.md)
- [Payment](../finance/payment.md)
- [Registration](../registration/registration.md)
- [Finance README](../finance/README.md)

---
