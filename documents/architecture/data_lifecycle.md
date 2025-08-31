# Data Lifecycle Architecture

## Overview

The Tournament Organizer implements a **status-based data lifecycle** approach where data is never hard-deleted from the
system. Instead, entities transition through various status states that control their visibility, accessibility, and
operational behavior. This approach ensures data integrity, supports compliance requirements, and provides a
professional user experience.

## Core Principles

### 1. No Hard Deletion

- **Data Preservation**: All data remains in the system indefinitely
- **Audit Trail**: Complete history is maintained for compliance and debugging
- **Recovery Capability**: Accidental deletions can be reversed
- **Legal Compliance**: Supports data retention requirements

### 2. Status-Based Lifecycle

- **State Management**: Entities transition through predefined status states
- **Behavioral Control**: Status determines system behavior and user access
- **Professional Communication**: Users are notified of data status changes professionally

### 3. Equal Profile Treatment

- **No Hierarchy**: All profiles (human, animal, organization, etc.) are treated equally
- **Consistent Rules**: Same lifecycle rules apply across all entity types
- **Unified Management**: Centralized status management across domains

## Data Lifecycle States

### 1. **Active** (Default State)

- **Description**: Entity is fully operational and visible
- **Behavior**:
  - Normal system operations
  - Full user access and interaction
  - Visible in searches and listings
  - Can participate in tournaments and activities
- **Transitions**: Can be moved to any other state

### 2. **Archived**

- **Description**: Entity is preserved but not actively used
- **Behavior**:
  - Hidden from normal operations
  - Read-only access for historical reference
  - Not visible in active searches
  - Maintains relationships and references
- **Use Cases**:
  - Completed tournaments
  - Inactive participants
  - Historical data preservation
  - Compliance requirements

### 3. **Deleted** (Soft Delete)

- **Description**: Entity is marked for deletion but preserved
- **Behavior**:
  - Hidden from all normal operations
  - Maintains referential integrity
  - Professional notification to users
  - Recoverable within retention period
- **User Experience**:
  - Professional communication about data status
  - Clear explanation of what "deleted" means
  - Information about recovery options
  - Respectful handling of user concerns

### 4. **Purged** (System-Only)

- **Description**: Data marked for eventual physical removal
- **Behavior**:
  - Completely hidden from all operations
  - Maintained for legal/compliance reasons
  - Scheduled for eventual physical deletion
  - Requires administrative override for recovery
- **Use Cases**:
  - Legal compliance requirements
  - Data retention policies
  - System cleanup operations

## Implementation Strategy

### 1. Base Entity Model Integration

```python
class BaseEntity:
    id: str
    status: DataStatus  # Active, Archived, Deleted, Purged
    created_at: datetime
    last_updated_at: datetime
    deleted_at: Optional[datetime]  # When soft-deleted
    archived_at: Optional[datetime]  # When archived
    purged_at: Optional[datetime]    # When marked for purge
```

### 2. Status Enum Definition

```python
class DataStatus(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    PURGED = "purged"
```

### 3. Status Transition Rules

- **Active → Archived**: Manual or automatic (e.g., tournament completion)
- **Active → Deleted**: User-initiated deletion
- **Archived → Active**: Manual restoration
- **Deleted → Active**: Recovery within retention period
- **Deleted → Purged**: Automatic after retention period
- **Purged → Active**: Administrative override only

## Cross-Domain Impact

### 1. **Identity Domain**

- Profile status affects user access and visibility
- Contact information remains accessible for active relationships
- Role assignments respect profile status
- Professional communication about status changes

### 2. **Tournament Domain**

- Active participants only in active tournaments
- Historical data preserved for completed events
- Archive completed tournaments automatically
- Maintain tournament history for analysis

### 3. **Finance Domain**

- Financial records preserved for compliance
- Active accounts only for active entities
- Archive completed transactions
- Maintain audit trail for all financial activities

### 4. **Schedule Domain**

- Active events only for active entities
- Preserve historical scheduling data
- Archive completed events
- Maintain relationship integrity

## Technical Implementation

### 1. **Database Schema**

```javascript
// MongoDB document structure
{
  "_id": ObjectId,
  "status": "active|archived|deleted|purged",
  "created_at": ISODate,
  "last_updated_at": ISODate,
  "deleted_at": ISODate,  // Optional
  "archived_at": ISODate, // Optional
  "purged_at": ISODate,   // Optional
  // ... entity-specific fields
}
```

### 2. **Query Filtering**

```python

# Default queries filter by status

def get_active_entities():
    return collection.find({"status": "active"})

def get_all_entities(include_deleted=False):
    query = {}
    if not include_deleted:
        query["status"] = {"$ne": "deleted"}
    return collection.find(query)
```

### 3. **Status Transition Logic**

```python
def transition_status(entity_id: str, new_status: DataStatus, reason: str = None):
    # Validate transition rules
    validate_status_transition(current_status, new_status)

    # Update status and timestamps
    update_data = {
        "status": new_status,
        "last_updated_at": datetime.utcnow()
    }

    if new_status == DataStatus.DELETED:
        update_data["deleted_at"] = datetime.utcnow()
    elif new_status == DataStatus.ARCHIVED:
        update_data["archived_at"] = datetime.utcnow()
    elif new_status == DataStatus.PURGED:
        update_data["purged_at"] = datetime.utcnow()

    # Update entity
    collection.update_one({"_id": entity_id}, {"$set": update_data})

    # Notify users professionally
    notify_status_change(entity_id, new_status, reason)
```

## User Experience Guidelines

### 1. **Professional Communication**

- **Clear Messaging**: Explain what "deleted" means in the system
- **Respectful Language**: Use professional, non-technical language
- **Recovery Information**: Provide clear recovery options
- **Timeline Expectations**: Set appropriate expectations for data retention

### 2. **Status Visibility**

- **Clear Indicators**: Show current status in UI
- **Status History**: Provide status change history
- **Recovery Options**: Easy access to restoration features
- **Professional Notifications**: Respectful status change notifications

### 3. **Data Access Patterns**

- **Default Views**: Show only active entities by default
- **Archive Access**: Easy access to archived data
- **Search Options**: Include/exclude deleted data in searches
- **Bulk Operations**: Support for bulk status changes

## Compliance Considerations

### 1. **Data Retention**

- **Legal Requirements**: Comply with data retention laws
- **Audit Trails**: Maintain complete change history
- **Recovery Capability**: Support legal discovery requests
- **Documentation**: Clear documentation of data handling

### 2. **Privacy Protection**

- **GDPR Compliance**: Support right to be forgotten
- **Data Minimization**: Only retain necessary data
- **Consent Management**: Respect user consent preferences
- **Access Controls**: Proper access restrictions based on status

### 3. **Security Measures**

- **Access Logging**: Log all status change operations
- **Authorization**: Proper authorization for status changes
- **Data Encryption**: Encrypt sensitive data at rest
- **Audit Compliance**: Support for security audits

## Best Practices

### 1. **Status Management**

- **Consistent Application**: Apply status rules consistently across all domains
- **Validation**: Validate status transitions before applying
- **Notifications**: Always notify users of status changes
- **Documentation**: Document status change reasons

### 2. **Performance Optimization**

- **Indexing**: Index status fields for efficient queries
- **Caching**: Cache active entity lists
- **Cleanup**: Regular cleanup of purged data
- **Monitoring**: Monitor status distribution and trends

### 3. **Data Integrity**

- **Referential Integrity**: Maintain relationships across status changes
- **Consistency Checks**: Regular consistency validation
- **Backup Strategy**: Include status information in backups
- **Recovery Procedures**: Clear procedures for data recovery

## Migration Strategy

### 1. **Existing Data**

- **Default Status**: Set all existing entities to "active"
- **Timestamps**: Set created_at and last_updated_at appropriately
- **Validation**: Validate data integrity after migration
- **Testing**: Test status transitions with existing data

### 2. **Application Updates**

- **Query Updates**: Update all queries to respect status
- **UI Updates**: Add status indicators and controls
- **API Updates**: Include status in API responses
- **Documentation**: Update all relevant documentation

### 3. **User Communication**

- **Announcement**: Communicate the new approach to users
- **Training**: Provide training on new status features
- **Support**: Enhanced support for status-related questions
- **Feedback**: Collect user feedback on the approach

## Monitoring and Maintenance

### 1. **Status Distribution Monitoring**

- Track distribution of entities across statuses
- Monitor status transition patterns
- Alert on unusual status distributions
- Report on data lifecycle metrics

### 2. **Performance Monitoring**

- Monitor query performance with status filters
- Track storage usage by status
- Monitor status transition operation performance
- Alert on performance degradation

### 3. **Compliance Monitoring**

- Track data retention compliance
- Monitor audit trail completeness
- Validate privacy compliance
- Report on compliance metrics

## Related Documentation

- [Base Entity Model](../models/business/foundation/base_entity.md)
- [Identity Domain](../models/business/identity/README.md)
- [Tournament Domain](../models/business/tournament/tournament.md)
- [Security Architecture](../security/overview.md)
- [Database Architecture](../database/README.md)
