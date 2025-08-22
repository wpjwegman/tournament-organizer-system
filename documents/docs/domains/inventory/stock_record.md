# Stock Record Model (Inventory)

This model (formerly located in Docs/models/inventory/stock_record.md) has been recreated as a placeholder. It is
intended to represent inventory stock records (for example, quantities, reorder thresholds, etc.) and is now embedded
within the Item model.

## Attributes

- **ID** (UUID, Required) – Unique identifier for the stock record.
- **Quantity** (Integer, Required) – Current quantity on hand.
- **Reorder Threshold** (Integer, Optional) – Threshold below which reordering is triggered.
- **Last Updated** (DateTime, Required) – Timestamp of the last update.

## Notes

- This model is now embedded (or merged) into the Item model. (See [Item Model](../inventory/item.md) for

  details.)

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 28000:2007 - Specification for security management systems for the supply chain](https://www.iso.org/standard/44651.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event inventory control

  standards

## See Also

- [Item](../inventory/item.md)
- [Inventory](../inventory/inventory.md)
- [Business README](../README.md)
