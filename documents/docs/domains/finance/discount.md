---
tags:
  - finance
  - discount
  - template
  - pricing
  - promotion
  - reduction
---

# **Discount** (Data Model - Template Entity)

## **Introduction**

A **Discount** Entity represents a reduction in fees or charges that can be applied to participants, teams, or
organizations within the tournament system. It provides a consistent way to handle discount information for pricing,
promotions, and financial management within the tournament system.

It describes financial characteristics and is typically managed by [Finance](../finance/finance.md)
entities to provide complete discount oversight.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

| Attribute       | Description                                          | Type     | Required | Notes / Example                                       |
| --------------- | ---------------------------------------------------- | -------- | -------- | ----------------------------------------------------- |
| **ID**          | Unique identifier for the discount entity.           | UUID     | Yes      | `"d123e456-7890-1234-5678-901234567890"`              |
| **Name**        | The name of the discount.                            | String   | Yes      | `"Early Bird Discount"`, `"Group Discount"`           |
| **Type**        | The type of discount.                                | String   | Yes      | `"Percentage"`, `"Fixed Amount"`, `"Free Entry"`      |
| **Value**       | The value of the discount.                           | Decimal  | Yes      | `10.00`, `25.00`, `50.00`                             |
| **Percentage**  | The percentage discount (if applicable).             | Decimal  | Optional | `10.0`, `25.0`, `50.0`                                |
| **Description** | Description of the discount offer.                   | String   | Optional | `"10% off for early registration"`                    |
| **Category**    | The category of the discount.                        | String   | Optional | `"Promotional"`, `"Loyalty"`, `"Group"`               |
| **Start Date**  | The date when the discount becomes available.        | Date     | Optional | `"2024-01-15"`, `"2024-02-01"`                        |
| **End Date**    | The date when the discount expires.                  | Date     | Optional | `"2024-03-15"`, `"2024-04-01"`                        |
| **Eligibility** | Criteria for discount eligibility.                   | String   | Optional | `"Early registration only"`, `"Groups of 5+ players"` |
| **Status**      | The status of the discount.                          | String   | Optional | `"Active"`, `"Inactive"`, `"Expired"`                 |
| **Created At**  | Timestamp when the discount entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                              |
| **Updated At**  | Timestamp when the discount entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                              |

---

## **Relationships**

- A `Discount` Entity is managed by a [Finance](../finance/finance.md) entity.
- A `Discount` Template Entity may be applied to [Registration](../registration/registration.md) entities.
- A `Discount` Template Entity may be associated with entities.

---

## **Considerations**

- **Clarity:** Discount terms and conditions should be clear and understandable.
- **Fairness:** Discounts should be applied consistently and fairly.
- **Timing:** Discount availability periods should be clearly communicated.
- **Eligibility:** Discount eligibility criteria should be well-defined.
- **Tracking:** Discount usage should be tracked for reporting purposes.

---
