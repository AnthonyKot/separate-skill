# Match snapshots

Parsed match JSON from the OpenDota API, one file per registered case, committed
as a **snapshot**: the record as it stood when the chapter was written.

`verify.sh` re-fetches each match and diffs it against the snapshot. A difference
is reported loudly and is not automatically a failure — the API reparses matches
and adds fields between versions. What must never change is a registered claim.

Fetch with `tools/fetch-match.py <match_id>`. Do not hand-edit these files.
