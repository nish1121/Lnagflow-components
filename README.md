# Langflow Components - SOW Generation

A collection of custom Langflow components for Statement of Work (SOW) generation and management.

## Components

### SOW State Manager

A conversation state management component that systematically collects all necessary information for generating a Statement of Work for Cayenta utility implementations.

**Features:**
- Multi-turn conversation tracking
- Sequential question flow
- State persistence across interactions
- Multiple granular outputs for workflow integration

**Location:** `components/sow_state_manager.py`

[View detailed documentation](components/README.md)

## Installation

1. Clone this repository
2. Import the component files into your Langflow workspace
3. Use the components in your flows

## Usage

Import the SOW State Manager component into Langflow and connect it to your conversation flow. The component will guide users through a structured process to collect:

- Utility Type (GAS, Electric, Water, etc.)
- Deployment Model (Cloud/OnPrem)
- Cayenta Modules (CIS, Billing, WMS, etc.)
- Implementation Timeline
- Scope Preferences

## Requirements

- Langflow
- Python 3.8+

## Component Structure

```
components/
├── __init__.py
├── sow_state_manager.py
└── README.md
```
