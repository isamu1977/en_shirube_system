# Rename Database to en_shirube_system

## Summary

Rename the PostgreSQL database from `taro_de_raizes` to `en_shirube_system` to better reflect the current project identity.

## Motivation

The project has evolved and the name `taro_de_raizes` is no longer the primary identifier. `en_shirube_system` is the new standard name across the detailed design and configuration.

## Proposed Changes

- Update database name in `backend/app/database.py`.
- Update database name in `scripts/init_db.py`.
- Update any other references to `taro_de_raizes` in the codebase.
- Ensure local development environments are updated (requires manual intervention or script).

## Risks

- Existing local data might be effectively "lost" if developers don't migrate it (though it will still exist in the old DB).
- Deployment scripts/configs might need updates if they hardcode the DB name (checked, seems to be env var driven but defaults might need changing).

## Alternatives Considered

- Keep `taro_de_raizes` as legacy name (rejected: causes confusion).
