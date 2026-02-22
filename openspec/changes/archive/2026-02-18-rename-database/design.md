# Design: Rename Database

## Overview

Straightforward string replacement of the database name constant.

## Impact

- **Backend**: `backend/app/database.py` contains the connection string logic.
- **Scripts**: `scripts/init_db.py` creates the database if it doesn't exist.

## Migration Strategy

For local development:

1. Developers can run `scripts/init_db.py` to create the new database.
2. Alembic migrations should be run against the new database.

We will not provide an automated migration script to move data from `taro_de_raizes` to `en_shirube_system` for local dev as it is assumed to be disposable. Production environments should handle this via infra-as-code or manual rename if preserving data is critical (though this seems to be pre-production).
