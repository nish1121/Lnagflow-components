# SOW State Manager Component

A custom Langflow component that manages conversation state for collecting Statement of Work (SOW) requirements.

## Overview

The SOW State Manager component tracks multi-turn conversations to gather all necessary information for generating a Statement of Work. It systematically collects:

- Utility Type
- Deployment Model
- Modules Selected
- Implementation Timeline
- Scope Preferences

## Features

- **State Management**: Maintains conversation state across multiple interactions
- **Sequential Questions**: Asks questions in a predefined order
- **Multiple Outputs**: Provides individual outputs for each collected field
- **Status Tracking**: Indicates whether data collection is in progress or complete
- **Flexible Input Handling**: Accepts Message objects or plain text

## Inputs

### Last User Message
- **Name**: `last_message`
- **Type**: MessageTextInput
- **Description**: The latest user message (can be a Message object or plain text)

### Current State (JSON)
- **Name**: `current_state_json`
- **Type**: MessageTextInput
- **Description**: JSON string holding the current SOW state
- **Note**: Leave empty on first run; the component will initialize it

## Outputs

1. **Updated State (JSON)** - Serialized state object for next iteration
2. **Assistant Message** - The next question or completion message
3. **Status** - Either "collecting" or "ready"
4. **Pending Key** - The field currently being collected
5. **Utility Type** - The collected utility type value
6. **Deployment Model** - The collected deployment model value
7. **Modules Selected** - The collected modules value
8. **Implementation Timeline** - The collected timeline value
9. **Scope Preferences** - The collected scope preferences value
10. **All Slots Filled?** - Boolean indicating if all data is collected

## Usage in Langflow

1. Import the component into your Langflow workspace
2. Connect the user input to the `last_message` input
3. Loop the `state_json` output back to the `current_state_json` input for subsequent turns
4. Use the `assistant_message` output to display questions to the user
5. When `status` becomes "ready", all information is collected

## Example Flow

```
User Input → SOW State Manager → Assistant Message Display
                ↑           |
                |           ↓
                +--- state_json (loop back)
```

## Data Collection Sequence

1. **Utility Type**: GAS, Electric, Water, Multi-service, or Waste Management
2. **Deployment Model**: Cloud or OnPrem
3. **Modules Selected**: Cayenta modules (e.g., CIS, Billing, WMS, ERP, HCM)
4. **Implementation Timeline**: Expected timeline (e.g., 12 months + 3 months hypercare)
5. **Scope Preferences**: Key integrations, data migration, customizations, or constraints

## State Structure

```json
{
  "slots": {
    "utility_type": "",
    "deployment_model": "",
    "modules_selected": "",
    "implementation_timeline": "",
    "scope_preferences": ""
  },
  "pending_key": null,
  "status": "collecting"
}
```

## Error Handling

- Invalid JSON in `current_state_json` triggers automatic state reset
- Missing or null values are handled gracefully
- The component accepts flexible input types (Message objects, strings, or None)
