# **Cart** (Data Model - Template Entity)

## **Introduction**

A **Cart** Entity represents a shopping cart within the tournament system. It provides a consistent way to handle cart
information for fee collection, payment processing, and transaction management within the tournament system.

It describes financial characteristics and is typically managed by [Finance](../finance/finance.md)
entities to provide complete cart oversight.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

| Attribute           | Description                                      | Type      | Required | Notes / Example                                             |
| ------------------- | ------------------------------------------------ | --------- | -------- | ----------------------------------------------------------- |
| **ID**              | Unique identifier for the cart entity.           | UUID      | Yes      | `"c123e456-7890-1234-5678-901234567890"`                    |
| **User**            | Reference to the user who owns the cart.         | Reference | Yes      | Reference to entity                                         |
| **Items**           | List of items in the cart.                       | List      | Optional | List of [Item](../inventory/item.md) entities |
| **Subtotal**        | The subtotal amount before taxes and fees.       | Decimal   | Optional | `150.00`, `250.50`, `75.25`                                 |
| **Tax Amount**      | The tax amount applied to the cart.              | Decimal   | Optional | `15.00`, `25.05`, `7.53`                                    |
| **Discount Amount** | The discount amount applied to the cart.         | Decimal   | Optional | `10.00`, `20.00`, `5.00`                                    |
| **Total Amount**    | The total amount including taxes and discounts.  | Decimal   | Optional | `155.00`, `255.55`, `77.78`                                 |
| **Currency**        | The currency of the cart.                        | String    | Optional | `"USD"`, `"EUR"`, `"CAD"`                                   |
| **Status**          | The status of the cart.                          | String    | Optional | `"Active"`, `"Abandoned"`, `"Converted"`, `"Expired"`       |
| **Expires At**      | The timestamp when the cart expires.             | DateTime  | Optional | `"2024-01-15T23:59:59Z"`                                    |
| **Created At**      | Timestamp when the cart entity was created.      | DateTime  | Yes      | `"2024-01-15T10:30:00Z"`                                    |
| **Updated At**      | Timestamp when the cart entity was last updated. | DateTime  | Yes      | `"2024-01-20T14:45:00Z"`                                    |

---

## **Relationships**

- A `Cart` Entity belongs to a entity.
- A `Cart` Entity contains multiple [Item](../inventory/item.md) entities.
- A `Cart` Entity is managed by a [Finance](../finance/finance.md) entity.

---

## **Considerations**

- **Expiration:** Carts should have appropriate expiration times to prevent abandoned carts.
- **Pricing:** Cart pricing should be accurate and up-to-date.
- **Taxes:** Tax calculations should be handled correctly based on location.
- **Discounts:** Discounts should be applied correctly and transparently.
- **Security:** Cart data should be secure and protected.

---

## References

- [ISO 4217 — Currency codes (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_4217) - Standard for currency representation
- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html) - Standard for timestamp

  representations

- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity pattern reference

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event e-commerce and

  financial standards

## See Also

- [Amount](../finance/amount.md)
- [Fee](../finance/fee.md)
- [Payment](../finance/payment.md)
- [Discount](../finance/discount.md)
- [Item](../inventory/item.md)
- [Account](../identity/account/account.md)
- [Finance README](../finance/README.md)

---
