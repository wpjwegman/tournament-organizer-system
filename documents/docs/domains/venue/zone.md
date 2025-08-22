# **Zone** (Data Model - Template Entity)

## **Introduction**

A **Zone** Entity Template defines a blueprint for a logical grouping or section within a larger venue template. It
serves as an optional organizational layer to cluster references to related \*\*\*\* templates, making it easier to
manage and navigate complex venue layouts.

Examples include templates for an "Indoor Courts Section", "Outdoor Fields Area", or "Main Competition Zone".

When a `Venue` template is used, the definitions of its associated `Zone` templates (and their referenced `Area`
templates) are typically **copied** into the specific instance (e.g., within a `Tournament`), allowing for modification
without affecting the original template.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status` [e.g., Active, Deprecated], `CreatedAt`,
`LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute       | Description                                                                                                                                                       | Type       | Required | Notes / Example                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | ------------------------------------------------------------------------------------------ |
| **Name**        | A human-readable name identifying the zone template (e.g., a section name, area designation).                                                                     | String     | Yes      | E.g., "Indoor Courts", "Outdoor Fields", "Main Competition Zone"                           |
| **Description** | Optional detailed description of the zone template, its purpose, or general features.                                                                             | Text       | Optional | "Collection of standard indoor competition courts suitable for basketball and volleyball." |
| **Type**        | Categorizes the primary purpose or type of the zone template.                                                                                                     | String     | Yes      | E.g., "Indoor", "Outdoor", "Mixed", "Competition", "Training", "Spectator", "Service"      |
| **Areas**       | List of references (by ID) to \*\*\*\* templates within this zone template.                                                                                       | List[UUID] | Yes      | References Area template IDs. `["area-tmpl-field1", "area-tmpl-field2"]`                   |
| **Maps**        | Optional list of references (by ID) to **[Map](../venue/map.md)** entities specifically depicting this zone template or its immediate surroundings. | List[UUID] | Optional | `["map-uuid-zone-indoor-layout", "map-uuid-zone-indoor-detail"]`                           |
| **Notes**       | General notes about the configuration, access, or specific characteristics of this type of zone.                                                                  | Text       | Optional | "Access via North entrance only.", "Requires special security clearance."                  |

---

## **Relationships**

- A `Zone` Entity Template is referenced by a \*\*\*\* template to organize its areas.
- It references a list of one or more \*\*\*\* templates.
- It optionally references a list of specific **[Map](../venue/map.md)** entities.
- When the parent `Venue` template is copied into a `Tournament`, this `Zone` template definition is also copied as part

  of that structure.

---

## **Considerations**

- **Template Nature:** Defines a standard zone configuration. Instance-specific details (status changes during an event,

  temporary notes) belong on the copied instance within the `Tournament`.

- **Copy Mechanism:** Part of the larger `Venue` template copy process.
- **Optional Layer:** Zones are an optional organizational layer. Areas can belong directly to a Venue if zone

  organization is unnecessary.

- **Map Reference:** Allows associating specific visual layouts (e.g., zone boundaries, access points) with this zone

  template.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 20121:2012 - Event sustainability management systems](https://www.iso.org/standard/54552.html)
- [ISO 41001:2018 - Facility management — Management systems — Requirements with guidance for use](https://www.iso.org/standard/69426.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event venue management

  standards

## See Also

- [Venue README](README.md)
- [Venue](venue.md)
- [Area](area.md)
- [Map](map.md)
- [Tournament README](../tournament/README.md)
- [Schedule README](../schedule/README.md)
- [Business README](../README.md)

---
