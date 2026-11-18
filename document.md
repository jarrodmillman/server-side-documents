# Document-side contract: cell execution state

The REST endpoint only requests execution.
Its results are delivered by the server writing to the cell in the shared (CRDT) document, and clients see them through normal document synchronization.

## Fields written by the server

For each executed code cell the server writes:

- `execution_state`: whether the cell is running.
- `execution_count`: from the kernel.
- `outputs`: nbformat outputs built from IOPub messages.

## Current behavior

| Aspect                       | Jupyverse                                           | jupyter-server-documents                                             |
| ---------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- |
| Running value                | `busy`                                              | `running`                                                            |
| Set to running               | When `execute_request` is sent                      | When the cell is enqueued, so queued cells also show running         |
| Outputs cleared              | When the request is handled                         | At enqueue                                                           |
| `execution_count` and `idle` | From `execute_reply`, same transaction              | Written together at completion                                       |
| Output messages handled      | `stream`, `display_data`, `execute_result`, `error` | Those plus `update_display_data` and `clear_output` including `wait` |

> > > > > > > 9e57655 (Add basic document contract)
