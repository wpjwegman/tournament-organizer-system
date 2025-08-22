# **Service** (Data Model: Entity Template)

## **Introduction**

A **Service** template defines a distinct offering, facility, or support function that can be provided during a
tournament. This unified model handles both traditional services (like massage therapy or equipment rental) and
amenities (like VIP lounges or food vendors), recognizing that they share common characteristics while potentially
differing in their physical presence and operational aspects.

As an Entity Template, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md). When used, its
definition is typically **copied** into the target context (like a specific tournament), allowing for potential minor
modifications or annotations without altering the original template.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute         | Description                                                        | Type       | Required | Notes / Example                                                     |
| ----------------- | ------------------------------------------------------------------ | ---------- | -------- | ------------------------------------------------------------------- |
| **Name**          | A descriptive name for the service template.                       | String     | Yes      | `"Tennis Court Rental"`, `"VIP Lounge Access"`, `"Massage Therapy"` |
| **Description**   | Detailed description of the service template and what it provides. | Text       | Yes      | `"Professional tennis court with equipment provided"`               |
| **Type**          | The type of service template.                                      | String     | Yes      | `"Facility"`, `"Amenity"`, `"Support"`, `"Equipment"`               |
| **Is Reservable** | Whether this service can be reserved in advance.                   | Boolean    | Yes      | `true` for bookable services, `false` for walk-in services          |
| **Capacity**      | Maximum number of people or items this service can accommodate.    | Integer    | Optional | `4` for a tennis court, `50` for a lounge                           |
| **Duration**      | Standard duration for this service in minutes.                     | Integer    | Optional | `60` for a massage session, `120` for a court rental                |
| **Requirements**  | List of additional resources needed for this service.              | List[UUID] | Optional | References to equipment, staff, or other resources needed           |
| **Notes**         | Additional notes about the service template.                       | Text       | Optional | `"Requires advance booking"`                                        |

---

## **Relationships**

- A `Service` Entity Template is referenced by [Reservation](../reservation/reservation.md) entities.
- A `Service` Entity Template may be associated with specific or entities.

### Parent Relationships

- - The venue where this service is provided
- - The specific area where this service is provided

### Child Relationships

- [Reservation](../reservation/reservation.md) - Reservations for this service

### Related Entities

- - Unit responsible for providing this service
- / - Location where this service is provided

---

## **Considerations**

- **Template Nature:** This template defines a standard service. Instance-specific variations or customizations belong

  on the copied instance within its specific context.

- **Copy Mechanism:** The process of copying this template definition into a target context needs to be handled by

  application logic.

- **Reservation Management:** Services that are reservable should have clear booking procedures.
- **Capacity Planning:** Service capacity should be managed to prevent overbooking.

---
