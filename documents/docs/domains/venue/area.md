# **Area** (Data Model - Template Entity)

## **Introduction**

An **Area** Entity Template defines a blueprint for a *single, specific, playable space* within a larger venue context
(e.g., a template or a [Zone](../venue/zone.md) template). It represents the fundamental unit where a
single competition event (like a ) takes place at any given time.

Examples include templates for a *single* standard competition court (e.g., "Court 1"), a specific field ("Field A"), a
particular table ("Table 3"), or a designated rink ("Rink 2"). It does **not** represent a collection of courts or a
general spectator zone.

When a `Venue` or `Zone` template is used, the definitions of its associated `Area` templates are typically **copied**
into the specific instance (e.g., within a `Tournament`), allowing for modification (e.g., setting status to 'Under
Maintenance') without affecting the original template. This template serves as the fundamental unit for fixture
scheduling.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status` [e.g., Active, Deprecated, Under
Maintenance], `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute       | Description                                                                                                                                                                | Type       | Required | Notes / Example                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Name**        | A human-readable name identifying the specific area template (e.g., a court number, field name). Should be unique within a relevant context.                               | String     | Yes      | E.g., "Court 1", "Field A", "Table 3", "Rink 2", "Lane 4"                                                                        |
| **Number**      | A numeric identifier used for ordering and sorting areas within their context (e.g., within a Zone or Venue).                                                              | Integer    | Yes      | E.g., `1`, `2`, `3` for sequential ordering, or `101`, `102`, `103` for hierarchical ordering                                    |
| **Type**        | Categorizes the primary purpose or type of the specific playable area template.                                                                                            | String     | Yes      | E.g., "CompetitionCourt", "PlayingField", "CompetitionTable", "SwimmingLane", "RunningTrackLane", "BowlingLane", "Rink", "Board" |
| **Description** | Optional detailed description of the specific area template, its standard features (relevant to play), or typical use.                                                     | Text       | Optional | "Standard competition court, suitable for basketball/volleyball."                                                                |
| **Surface**     | The standard type of ground or floor surface for this specific playable area, if applicable.                                                                               | String     | Optional | E.g., "Hardwood", "Artificial Turf", "Grass", "Clay", "Concrete", "Ice", "Synthetic"                                             |
| **Dimensions**  | Textual description or structured data representing the typical playable size/dimensions of this area type.                                                                | String     | Optional | E.g., "Regulation Basketball Court (94x50 ft)", "400m Lane", "10m x 5m"                                                          |
| **Maps**        | Optional list of references (by ID) to detailed **[Map](../venue/map.md)** entities specifically depicting this area template or its immediate surroundings. | List[UUID] | Optional | `["map-uuid-area-court1-layout", "map-uuid-area-court1-detail"]`                                                                 |
| **Notes**       | General notes about the configuration, access, or specific characteristics of this type of playable area.                                                                  | Text       | Optional | "North end goal needs pre-game check.", "Requires key card access via West door."                                                |

---

## **Relationships**

- An `Area` Entity Template is typically referenced by a \***\* template (directly) or a

  **[Zone](../venue/zone.md)\*\* template to define the specific playable spaces within them.

- It may reference a \*\*\*\* entity if dimensions are provided with units.
- It optionally references a list of specific **[Map](../venue/map.md)** entities.
- When the parent `Venue`/`Zone` template is copied into a `Tournament`, this `Area` template definition is also copied

  as part of that structure, becoming the specific instance used by entities.

---

## **Considerations**

- **Template Nature:** Defines a standard configuration for a *single* playable area. Instance-specific details (e.g.,

  current availability status during an event, temporary setup notes for a specific fixture) are handled on the copied
  instance within the `Tournament` data or potentially on the `Fixture` itself.

- **Copy Mechanism:** Part of the larger `Venue`/`Zone` template copy process.
- **Specificity:** Represents the most granular level of *schedulable, playable space* within the `Venue` hierarchy

  (Venue -> [Zone] -> Area). It is the target location for a `Fixture`.

- **No Capacity:** This model does **not** track spectator capacity or general occupancy; that would belong to a

  different model, perhaps related to the parent `Venue` or `Zone` if needed.

- **Dimensions:** Useful for planning layouts and confirming suitability for specific activities.
- **Map Reference:** Allows associating specific visual layouts (e.g., boundary lines, equipment placement) with this

  area template.

---
