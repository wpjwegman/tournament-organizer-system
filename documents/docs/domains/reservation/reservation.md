---
tags:
  - service-reservation
  - entity
  - booking-instance
  - amenity-booking
  - resource-allocation
  - tournament-management
---

# Service Reservation (Entity)

## Overview

A Service Reservation represents a concrete booking instance for a specific service or amenity within a tournament
context. As an entity with independent identity and lifecycle, it provides comprehensive tracking of booking
details, service allocation, usage monitoring, and financial accounting for all types of tournament-related
services and amenities.

## Purpose

This entity enables comprehensive service booking management by:

- Managing concrete booking instances for facilities, equipment, amenities, and support services
- Tracking comprehensive reservation details including timing, participants, and service requirements
- Supporting diverse booking types from facilities and equipment to hospitality and support services
- Enabling detailed usage monitoring, billing integration, and service delivery coordination
- Facilitating conflict prevention, capacity management, and service optimization

## Structure

This entity includes standard attributes from the [Base Entity](../foundation/base_entity.md)
and adds the following service reservation-specific attributes:

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Reservation System** | Reference to the booking process methodology | UUID | Yes | Links to [Reservation System](system.md) template |
| **Reservation Period** | Reference to the availability window configuration | UUID | Yes | Links to [Reservation Period](period.md) template |
| **Service Type** | Category of service being reserved | Enum | Yes | `FACILITY`, `EQUIPMENT`, `HOSPITALITY`, `SUPPORT_SERVICE`, `AMENITY` |
| **Service Reference** | Reference to the specific service being booked | UUID | Yes | Links to Venue Area, Equipment, or Service Provider |
| **Reservation Holder** | Reference to the participant making the booking | UUID | Yes | Links to [Identity](../identity/README.md) participant |
| **Start Time** | Beginning time of the reservation | DateTime | Yes | `"2024-07-15T14:00:00Z"`, `"2024-08-20T09:30:00Z"` |
| **End Time** | Ending time of the reservation | DateTime | Yes | `"2024-07-15T16:00:00Z"`, `"2024-08-20T11:30:00Z"` |
| **Duration** | Length of the reservation in minutes | Integer | Yes | `120` (2 hours), `60` (1 hour), `480` (8 hours) |
| **Participants** | Number of people included in the reservation | Integer | Optional | `4` (court booking), `1` (massage), `20` (meeting room) |
| **Requirements** | Embedded booking criteria and special needs | Reservation Requirements | Yes | Access requirements, equipment needs, setup specifications |
| **Terms** | Embedded booking conditions and pricing | Reservation Terms | Yes | Payment terms, cancellation policy, usage conditions |
| **Special Requests** | Additional services or accommodations requested | List[String] | Optional | `["Setup 30 min early", "Equipment delivery", "Catering service"]` |
| **Access Credentials** | Authentication details for service access | String | Optional | `"Keycard #1234"`, `"Access code: TOUR2024"`, `"VIP wristband required"` |
| **Setup Requirements** | Preparation needed before service delivery | String | Optional | `"Standard court setup"`, `"AV equipment installation"`, `"Catering setup required"` |
| **Usage Tracking** | Monitoring information for service utilization | String | Optional | `"Check-in required"`, `"Usage logged automatically"`, `"Manual verification"` |
| **Billing Reference** | Financial tracking for payment processing | UUID | Optional | Links to [Finance](../finance/README.md) payment record |
| **Emergency Contact** | Contact information for reservation issues | String | Optional | `"Tournament desk: +1-555-0199"`, `"Facility manager: ext 101"` |
| **Service Notes** | Additional information about the reservation | Text | Optional | `"VIP guest preference noted"`, `"Maintenance scheduled before use"` |

## Example

### Example: VIP Lounge Reservation

```mermaid
graph TD
  SR[Service Reservation: VIP Lounge Access]
  SR --> RS[Reservation System: VIP Amenity Booking]
  SR --> RP[Reservation Period: Tournament VIP Window]
  SR --> ST[Service Type: HOSPITALITY]
  SR --> SRef[Service Reference: VIP Lounge Area A]
  SR --> RH[Reservation Holder: Sarah Johnson - Sponsor]
  SR --> StartT[Start Time: 2024-07-15T11:00:00Z]
  SR --> EndT[End Time: 2024-07-15T18:00:00Z]
  SR --> Dur[Duration: 420 minutes (7 hours)]
  SR --> Part[Participants: 8 guests maximum]
  SR --> REQ[Requirements: VIP status verified, Catering included]
  SR --> TERMS[Terms: Premium rate, 24h cancellation notice]
  SR --> SpecReq[Special Requests: Welcome refreshments, Privacy setup]
  SR --> AC[Access Credentials: VIP keycard #V789]
  SR --> SetupReq[Setup Requirements: Premium catering, Privacy screens]
  SR --> UT[Usage Tracking: Check-in at VIP desk required]
  SR --> BR[Billing Reference: Payment processed - Premium VIP rate]
  SR --> EC[Emergency Contact: VIP coordinator: +1-555-0156]
  SR --> SN[Service Notes: High-value sponsor - exceptional service required]
```

This example demonstrates a comprehensive VIP lounge reservation with premium service requirements.
The booking includes extended access, catering services, and privacy setup with dedicated VIP
support coordination. Detailed tracking ensures exceptional service delivery for high-value sponsors.

### Example: Practice Court Equipment Package

```mermaid
graph TD
  SR[Service Reservation: Practice Court with Equipment]
  SR --> RS[Reservation System: Practice Court Allocation]
  SR --> RP[Reservation Period: Daily Equipment Rental]
  SR --> ST[Service Type: FACILITY]
  SR --> SRef[Service Reference: Practice Court 3 + Equipment Set B]
  SR --> RH[Reservation Holder: Michael Chen - Player]
  SR --> StartT[Start Time: 2024-07-16T08:00:00Z]
  SR --> EndT[End Time: 2024-07-16T10:00:00Z]
  SR --> Dur[Duration: 120 minutes (2 hours)]
  SR --> Part[Participants: 1 player + 1 coach]
  SR --> REQ[Requirements: Valid tournament registration, Equipment waiver]
  SR --> TERMS[Terms: Complimentary for participants, 2h cancellation notice]
  SR --> SpecReq[Special Requests: Ball machine setup, Video recording allowed]
  SR --> AC[Access Credentials: Court access via tournament badge]
  SR --> SetupReq[Setup Requirements: Ball machine positioned, Net height checked]
  SR --> UT[Usage Tracking: Self-service check-in/out]
  SR --> BR[Billing Reference: Complimentary - No charge]
  SR --> EC[Emergency Contact: Equipment desk: ext 201]
  SR --> SN[Service Notes: Player preparation for quarterfinal match]
```

This second example shows a practice court reservation with equipment package for tournament
preparation. The booking includes specialized equipment setup, video recording permission,
and self-service tracking suitable for competitive player preparation needs.

## See Also

- [Reservation System](./system.md) - Booking process and service configuration templates
- [Reservation Period](./period.md) - Time-based availability window configuration
- [Reservation Requirements](./requirements.md) - Embedded booking criteria and eligibility rules
- [Reservation Terms](./terms.md) - Embedded booking conditions and policies
- [Venue](../venue/README.md) - Facility and area management for location-based bookings
- [Identity](../identity/README.md) - Participant identity and profile management
- [Finance](../finance/README.md) - Payment processing and billing integration
- [Tournament](../tournament/tournament.md) - Tournament context for service reservations
