# **Reservation** (Data Model - Template Entity)

## **Introduction**

A **Reservation** Entity represents a booking of a service or amenity for a specific time period. In this system,
services and amenities are unified under a single model since they share common characteristics - both provide specific
offerings that can be reserved, though they may differ in their physical presence and operational characteristics.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute        | Description                                                                         | Type       | Required | Notes / Example                                               |
| ---------------- | ----------------------------------------------------------------------------------- | ---------- | -------- | ------------------------------------------------------------- |
| **Service**      | Reference to the [Service](../reservation/service.md) being reserved. | UUID       | Yes      | `service-uuid-tennis-court`                                   |
| **Timeslot**     | The time period for the reservation, embedded as a Value Object.                    | Timeslot   | Yes      | Start: 14:00, End: 15:00, Duration: 60 minutes                |
| **Registrant**   | Reference to the making the reservation.                                            | UUID       | Yes      | `registrant-uuid-123`                                         |
| **Status**       | Current status of the reservation.                                                  | String     | Yes      | `"Confirmed"`, `"Pending"`, `"Cancelled"`, `"Completed"`      |
| **Requirements** | List of additional resources needed                                                 | List[UUID] | Optional | References to other resources needed (equipment, staff, etc.) |
| **Notes**        | Additional information about the reservation                                        | Text       | Optional | `"Setup required 30 mins prior", "Special access needed"`     |

## **Relationships**

- A `Reservation` Entity references one [Service](../reservation/service.md) entity.
- A `Reservation` Entity is made by one entity.
- A `Reservation` Entity may be associated with a or entity.

### Parent Relationships

- [Service](../reservation/service.md) - The service being reserved
- - The person making the reservation

### Child Relationships

- None

### Related Entities

- - The tournament context for this reservation
- - The event context for this reservation

## **Considerations**

- **Booking Management:** Reservations provide a structured way to manage service bookings and resource allocation.
- **Time Conflicts:** The system should prevent double-booking of services during overlapping time periods.
- **Status Tracking:** Reservation status should be updated as the booking progresses.
- **Validation:** Must ensure the service is actually reservable (check IsReservable flag)
- **Area Requirements:** Physical amenities must have a valid Venue Area reference
