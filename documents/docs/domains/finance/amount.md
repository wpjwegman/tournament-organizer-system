---
tags:
  - finance
  - amount
  - value-object
  - currency
  - money
  - monetary
---

# **Amount** (Data Model - Value Object)

## **Introduction**

An **Amount** Value Object represents a monetary value with its associated currency. It is an immutable value object
that encapsulates the concept of money in the system. This model follows the Value Object pattern, meaning it has no
identity and is defined by its attributes.

It is used throughout the system wherever monetary values need to be represented, such as in pricing, fees, payments,
and financial calculations.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

| Attribute    | Description                              | Type    | Required | Notes / Example            |
| ------------ | ---------------------------------------- | ------- | -------- | -------------------------- |
| **Value**    | The numerical value of the amount.       | Decimal | Yes      | `10.50`, `1000.00`, `0.99` |
| **Currency** | The three-letter ISO 4217 currency code. | String  | Yes      | `USD`, `EUR`, `GBP`, `JPY` |

---

## **Relationships**

- An `Amount` Value Object has no independent identity and holds no references to other entities.
- It is always embedded within an owning Entity (e.g., `Fee`, `Payment`, `Expense`).

---

## **Considerations**

- **Embedding:** This defines a monetary value and is embedded within the owning entity.
- **Immutability:** If the amount needs to change, the owning Entity should replace the entire embedded Amount object.
- **Precision:** All monetary calculations should maintain 2 decimal places of precision.
- **Currency Consistency:** All amounts in a single context (e.g., a single payment) must use the same currency.
- **Validation:** Amounts must be validated according to the rules above before being used.

---

## References

- [ISO 4217 — Currency codes (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_4217) - International

  standard for currency codes

- [IEEE 754-2008 - Standard for Floating-Point Arithmetic](https://standards.ieee.org/standard/754-2008.html) - Standard

  for decimal precision in financial calculations

- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object pattern reference

## See Also

- [Fee](../finance/fee.md)
- [Payment](../finance/payment.md)
- [Expense](../finance/expense.md)
- [Income](../finance/income.md)
- [Discount](../finance/discount.md)
- [Cart](../finance/cart.md)

---
