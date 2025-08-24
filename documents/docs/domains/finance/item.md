---
tags:
  - finance
  - item
  - inventory
  - line-item
  - product
  - service
---

# **Item** (Data Model - Entity)

## **Introduction**

An **Item** Entity represents a product or service that can be purchased within the tournament system. It provides a
consistent way to handle item information for inventory management, pricing, and sales tracking within the tournament
system.

It describes product characteristics and is typically managed by [Finance](../finance/finance.md) entities
to provide complete item oversight.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

| Attribute       | Description                                      | Type     | Required | Notes / Example                                                    |
| --------------- | ------------------------------------------------ | -------- | -------- | ------------------------------------------------------------------ |
| **ID**          | Unique identifier for the item entity.           | UUID     | Yes      | `"i123e456-7890-1234-5678-901234567890"`                           |
| **Name**        | The name of the item.                            | String   | Yes      | `"Tournament Registration"`, `"Team Jersey"`, `"Equipment Rental"` |
| **Type**        | The type of item.                                | String   | Optional | `"Service"`, `"Product"`, `"Fee"`, `"Donation"`                    |
| **Description** | Description of the item.                         | String   | Optional | `"Registration fee for tournament participation"`                  |
| **Price**       | The price of the item.                           | Decimal  | Yes      | `50.00`, `25.00`, `100.00`                                         |
| **Currency**    | The currency of the item price.                  | String   | Optional | `"USD"`, `"EUR"`, `"CAD"`                                          |
| **Category**    | The category of the item.                        | String   | Optional | `"Registration"`, `"Merchandise"`, `"Equipment"`, `"Services"`     |
| **SKU**         | Stock keeping unit or product code.              | String   | Optional | `"REG-001"`, `"JER-001"`, `"EQU-001"`                              |
| **Inventory**   | Current inventory level (for physical items).    | Integer  | Optional | `100`, `50`, `0`                                                   |
| **Status**      | The status of the item.                          | String   | Optional | `"Active"`, `"Inactive"`, `"Out of Stock"`, `"Discontinued"`       |
| **Created At**  | Timestamp when the item entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                           |
| **Updated At**  | Timestamp when the item entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                           |

---

## **Relationships**

- An `Item` Entity is managed by a [Finance](../finance/finance.md) entity.
- An `Item` Entity may be contained in [Cart](../finance/cart.md) entities.
- An `Item` Entity may be associated with entities.

---

## **Considerations**

- **Pricing:** Item pricing should be accurate and competitive.
- **Inventory:** Inventory levels should be tracked for physical items.
- **Availability:** Item availability should be clearly communicated.
- **Categories:** Items should be properly categorized for easy discovery.
- **Pricing Updates:** Item pricing should be updated when costs change.

---
