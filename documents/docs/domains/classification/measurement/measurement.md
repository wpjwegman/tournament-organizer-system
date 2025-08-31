---
tags:

  - measurement
  - value-object
  - classification
  - quantitative

---

# Measurement (Value Object)

## Overview

A Measurement represents a precise quantitative value paired with its unit. It is embedded in other entities (such as [Score](../../schedule/score.md), performance records, or configuration parameters) to provide context and scale. Measurements do not have independent identity or lifecycle.

## Purpose

To provide a consistent, precise way to represent and communicate numerical values with their units across all domains. This supports clarity, validation, and interoperability.

## Structure

The Measurement value object defines the following attributes:

| Attribute | Type    | Required | Description                                                                 | Example(s)                                                      |
|-----------|---------|----------|-----------------------------------------------------------------------------|-----------------------------------------------------------------|
| Value     | Decimal | Yes      | The numerical value, stored as Decimal for precision.                       | `Decimal('10.500')`, `Decimal('75')`                            |
| Unit      | Unit    | Yes      | Embedded [Unit](../../classification/measurement/unit.md).  | `seconds`, `kg`  |

## Example

**Example 1: Time Measurement in a Score**

Suppose a tournament system records the time taken by a registrant to complete a race. The score entity embeds a Measurement value object to represent this time. In this case, the value is `180.000` and the unit is 'seconds'.

```mermaid
graph TD
    A[Score] --> B[Measurement]
    B --> C[Value: Decimal('180.000')]
    B --> D[Unit: 'seconds' (ID: 550e8400-e29b-41d4-a716-446655440000)]
```

This diagram shows how a score references a measurement, which in turn specifies both the value and the unit. This makes it clear that the score represents a time duration of 180 seconds.

**Example 2: Weight Measurement in a Performance Record**

Imagine a performance record for a weightlifting event. The system uses a Measurement value object to record the weight lifted. Here, the value is `75.00` and the unit is 'kg'.

```mermaid
graph TD
    X[Performance Record] --> Y[Measurement]
    Y --> Z[Value: Decimal('75.00')]
    Y --> W[Unit: 'kg' (ID: 123e4567-e89b-12d3-a456-426614174000)]
```

This diagram illustrates how a performance record embeds a measurement, making it explicit that the athlete lifted 75 kilograms. The unit reference ensures clarity and consistency across records.

## See Also

- [Unit](../../classification/measurement/unit.md): Defines measurement units and scales.
- [System](../../classification/measurement/system.md): Describes systems of measurement.
- [Dimension](../../classification/dimension.md): Explains measurement dimensions.
- [Score](../../schedule/score.md): Example of Measurement usage.
